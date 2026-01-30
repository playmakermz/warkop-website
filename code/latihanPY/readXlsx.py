import pandas as pd
import sys


def analyze_column(df, column_name):
    """
    Calculates the mean, median, and mode for a specific column in a DataFrame.

    Args:
        df (pd.DataFrame): The DataFrame containing the data.
        column_name (str): The exact name of the column to analyze.
    """
    # Check if the specified column exists in the DataFrame
    if column_name not in df.columns:
        print(f"\n--- ERROR ---")
        print(f"Column not found: '{column_name}'")
        print("\nPlease choose from the available columns:")
        for col in df.columns:
            print(f"- {col}")
        sys.exit(1)

    # --- Data Cleaning and Calculation ---

    # 1. Select the column
    data = df[column_name]

    # 2. Convert to numeric, forcing errors (like text) to NaN (Not a Number)
    numeric_data = pd.to_numeric(data, errors="coerce")

    # 3. Drop all NaN values to get a clean series for calculation
    cleaned_data = numeric_data.dropna()

    # Check if we have any data left after cleaning
    if cleaned_data.empty:
        print(f"\n--- ERROR ---")
        print(f"The column '{column_name}' contains no valid numeric data.")
        sys.exit(1)

    # --- Calculate Statistics ---

    # 1. Mean (Average)
    mean_val = cleaned_data.mean()

    # 2. Median (Middle value)
    median_val = cleaned_data.median()

    # 3. Mode (Most frequent value)
    # .mode() returns a pandas Series because there can be multiple modes
    mode_val = cleaned_data.mode().tolist()

    # --- Print the Results ---
    print("\n--- Statistics Report ---")
    print(f"Column:        {column_name}")
    print(f"Total numeric entries: {len(cleaned_data)}")
    print("---------------------------")
    print(f"Mean:          {mean_val:.4f}")
    print(f"Median:        {median_val}")

    # Nicely format the mode(s)
    if len(mode_val) == 1:
        print(f"Mode:          {mode_val[0]}")
    else:
        # Convert list of numbers to a string, e.g., [10, 20] -> "10, 20"
        mode_str = ", ".join(map(str, mode_val))
        print(f"Mode (Multi):  {mode_str}")


def main():
    """
    Main function to run the script.
    """
    # 1. Get user input for the file
    file_path = input("Enter the path to your .xlsx file: ")
    file_path = f"{file_path}.xlsx"

    try:
        # 2. Read the Excel file
        df = pd.read_excel(file_path)

    except FileNotFoundError:
        print(f"\n--- ERROR ---")
        print(f"File not found: '{file_path}'")
        print("Please check the file path and try again.")
        sys.exit(1)  # Exit the script
    except Exception as e:
        print(f"\n--- ERROR ---")
        print(f"An error occurred while reading the file: {e}")
        sys.exit(1)

    # 3. Show available columns
    print("\nFile loaded successfully.")
    print("Available columns:")
    # Print columns in a nice list
    for col in df.columns:
        print(f"- {col}")
    print("-" * 20)  # Separator

    # 4. Get user input for the column
    col_name = input("Enter the column name to analyze: ")

    # 5. Run the analysis function
    analyze_column(df, col_name)


# This part runs the script when you execute it from the command line
if __name__ == "__main__":
    main()
