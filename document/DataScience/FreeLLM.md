# Mendapatkan Akses gratis ke LLM secara gratis

Disini kita akan menggunakan https://docs.puter.com/Objects/fsitem/ 
Mereka menyediakan API gratis untuk developer, sedangkan client kita(Developer) yang akan menangung beban pemakaian nantinya. 

Intinya disini kita diberikan opsi mengunakan model LLM secara gratis, dengan cara membuat aplikasi.

Demo puter ada disini: https://docs.puter.com/playground/?example=ai-chatgpt

Model yang tersedia: https://puter.com/puterai/chat/models

## Tahapan
1. Buat aplikasi replit
2. tempel code dibawah
3. Jalankan file HTML tersebut

## Code

```
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI Chat App</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background-color: #f0f0f0;
            flex-direction: column;
        }

        #chat-container {
            width: 80%;
            max-width: 600px;
            margin: auto;
            background: white;
            border: 1px solid #ddd;
            border-radius: 4px;
            padding: 20px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }

        #messages {
            height: 300px;
            overflow-y: auto;
            border-bottom: 1px solid #ddd;
            margin-bottom: 20px;
            padding: 10px;
        }

        .message {
            padding: 5px;
            margin: 5px 0;
            border-radius: 4px;
            background: #2c7aef;
            color: white;
        }

        .user-message {
            text-align: right;
            background: #f9f9f9;
            color: black;
        }

        .user-message .message {
            background: #e0f7fa;
        }

        #chat-input {
            display: flex;
            gap: 10px;
        }

        #chat-input input[type="text"] {
            flex-grow: 1;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 4px;
        }

        #chat-input button {
            padding: 10px 20px;
            background: #007bff;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }

        #chat-input button:hover {
            background: #0056b3;
        }

        #file-input {
            display: none;
        }

        .file-upload-btn {
            padding: 10px 20px;
            background: #28a745;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }

        .file-upload-btn:hover {
            background: #218838;
        }

        .file-selected {
            padding: 5px 10px;
            background: #d4edda;
            border: 1px solid #c3e6cb;
            border-radius: 4px;
            font-size: 12px;
            color: #155724;
            margin-bottom: 10px;
        }
    </style>
    <script src="https://js.puter.com/v2/"></script>

</head>

<body>
    <div id="chat-container">
        <div id="messages"></div>
        <div id="file-selected-info"></div>
        <div id="chat-input">
            <input type="file" id="file-input" accept=".pdf" />
            <button class="file-upload-btn" onclick="selectFile()">Upload PDF</button>
            <input type="text" id="input-message" placeholder="Type a message or upload a PDF...">
            <button onclick="sendMessage()">Send</button>
        </div>
    </div>
    <p>Created using Puter.JS</p>

    <script>
        const messages = [];
        let uploadedFilePath = null;

        function addMessage(msg, isUser) {
            const messagesDiv = document.getElementById("messages");
            const messageDiv = document.createElement("div");
            messageDiv.classList.add("message");
            if (isUser) {
                messageDiv.classList.add("user-message");
            }
            messageDiv.textContent = msg;
            messagesDiv.appendChild(messageDiv);
            messagesDiv.scrollTop = messagesDiv.scrollHeight;
        }

        function selectFile() {
            document.getElementById("file-input").click();
        }

        document.getElementById("file-input").addEventListener("change", async (event) => {
            const fileInput = event.target;
            const fileInfoDiv = document.getElementById("file-selected-info");
            
            if (fileInput.files.length === 0) return;

            const file = fileInput.files[0];
            fileInfoDiv.innerHTML = `<div class="file-selected">📄 Uploading ${file.name}...</div>`;

            try {
                const uploadedFiles = await puter.fs.upload(fileInput.files);
                uploadedFilePath = uploadedFiles[0].path;
                fileInfoDiv.innerHTML = `<div class="file-selected">✅ ${file.name} uploaded! Click Send to analyze.</div>`;
            } catch (error) {
                console.error("Upload error:", error);
                fileInfoDiv.innerHTML = `<div class="file-selected" style="background: #f8d7da; border-color: #f5c6cb; color: #721c24;">❌ Upload failed. Please try again.</div>`;
                uploadedFilePath = null;
            }
        });

        async function sendMessage() {
            const input = document.getElementById("input-message");
            const message = input.value.trim();
            const fileInfoDiv = document.getElementById("file-selected-info");

            if (uploadedFilePath) {
                const fileName = fileInfoDiv.textContent.match(/✅ (.*) uploaded/)?.[1] || 'PDF';
                const userPrompt = message || 'Please analyze this PDF document and provide a summary.';
                
                addMessage(`📄 ${fileName}: ${userPrompt}`, true);
                input.value = '';
                fileInfoDiv.innerHTML = '<div class="file-selected">🤖 Analyzing PDF...</div>';

                try {
                    const response = await puter.ai.chat({
                        messages: [
                            ...messages,
                            {
                                role: 'user',
                                content: [
                                    { type: 'file', puter_path: uploadedFilePath },
                                    { type: 'text', text: userPrompt }
                                ]
                            }
                        ],
                        model: 'gpt-5-nano'
                    });

                    addMessage(response.message.content, false);
                    messages.push({ 
                        role: 'user', 
                        content: `[PDF Analysis] ${userPrompt}` 
                    });
                    messages.push(response.message);
                    
                    fileInfoDiv.innerHTML = '';
                    uploadedFilePath = null;
                    document.getElementById("file-input").value = '';
                } catch (error) {
                    console.error("AI response error:", error);
                    addMessage("Sorry, there was an error analyzing the PDF. Please try again.", false);
                    fileInfoDiv.innerHTML = '';
                    uploadedFilePath = null;
                    document.getElementById("file-input").value = '';
                }
            } else if (message) {
                addMessage(message, true);
                input.value = '';
                messages.push({ content: message, role: 'user' });

                try {
                    const response = await puter.ai.chat(messages, {model: 'claude-sonnet-4-5-20250929'});
                    addMessage(response.message.content, false);
                    messages.push(response.message);
                } catch (error) {
                    console.error("AI response error:", error);
                    addMessage("Sorry, there was an error. Please try again.", false);
                }
            }
        }

        document.getElementById("input-message").addEventListener("keypress", (event) => {
            if (event.key === "Enter") {
                sendMessage();
            }
        });
    </script>
</body>

</html>
```
