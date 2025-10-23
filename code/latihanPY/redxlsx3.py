import pandas as pd
import sys

def analyze_column(df, column_name):
    """
    Calculates skewness and kurtosis for a specific column.

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
    numeric_data = pd.to_numeric(data, errors='coerce')
    
    # 3. Drop all NaN values to get a clean series for calculation
    cleaned_data = numeric_data.dropna()

    # Check if we have any data left after cleaning
    if cleaned_data.empty:
        print(f"\n--- ERROR ---")
        print(f"The column '{column_name}' contains no valid numeric data.")
        sys.exit(1)
    
    # Check if we have enough data for these calculations
    # Skewness requires at least 3 data points, Kurtosis requires at least 4
    if len(cleaned_data) < 4:
        print(f"\n--- NOTICE ---")
        print(f"The column '{column_name}' only has {len(cleaned_data)} numeric entries.")
        print("Cannot calculate skewness or kurtosis (requires at least 4 data points).")
        sys.exit(0)

    # --- Calculate Statistics ---
    
    # 1. Skewness
    #    Measures the asymmetry of the data
    skew_val = cleaned_data.skew()
    
    # 2. Kurtosis
    #    Measures "tailedness". Pandas uses Fisher's definition (excess kurtosis),
    #    where 0 is the kurtosis of a normal distribution.
    kurt_val = cleaned_data.kurt()

    # --- Print the Results ---
    print("\n--- Statistics Report ---")
    print(f"Column:        {column_name}")
    print(f"Total numeric entries: {len(cleaned_data)}")
    print("---------------------------")
    print(f"Skewness:      {skew_val:.4f}")
    print(f"Kurtosis:      {kurt_val:.4f}")

    # --- Add Interpretation ---
    print("\n--- Interpretation ---")
    
    # Skewness Interpretation
    print("Skewness (Symmetry):")
    if skew_val > 1.0:
        print(f"  - Highly Right-Skewed (Positively Skewed). The tail is on the right.")
    elif skew_val > 0.5:
        print(f"  - Moderately Right-Skewed (Positively Skewed).")
    elif skew_val < -1.0:
        print(f"  - Highly Left-Skewed (Negatively Skewed). The tail is on the left.")
    elif skew_val < -0.5:
        print(f"  - Moderately Left-Skewed (Negatively Skewed).")
    else:
        print(f"  - Fairly Symmetrical (value is close to 0).")

    # Kurtosis Interpretation
    print("\nKurtosis (Peakedness):")
    print("  (Note: This is 'excess' kurtosis, where a normal distribution = 0)")
    if kurt_val > 1.0:
        print(f"  - Leptokurtic: Distribution is sharp, peaked, and has heavy tails.")
        print("    (More outliers than a normal distribution)")
    elif kurt_val < -1.0:
        print(f"  - Platykurtic: Distribution is flat and has light tails.")
        print("    (Fewer outliers than a normal distribution)")
    else:
        print(f"  - Mesokurtic: Distribution is similar to a normal distribution.")


def main():
    """
    Main function to run the script.
    """
    # 1. Get user input for the file
    file_path = input("Enter the path to your .xlsx file: ")

    try:
        # 2. Read the Excel file
        df = pd.read_excel(file_path)
    
    except FileNotFoundError:
        print(f"\n--- ERROR ---")
        print(f"File not found: '{file_path}'")
        print("Please check the file path and try again.")
        sys.exit(1) # Exit the script
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
    print("-" * 20) # Separator

    # 4. Get user input for the column
    col_name = input("Enter the column name to analyze: ")

    # 5. Run the analysis function
    analyze_column(df, col_name)

# This part runs the script when you execute it from the command line
if __name__ == "__main__":
    main()
