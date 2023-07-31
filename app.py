import csv
import sys
import questionary

# Placeholder for the list of qualifying loans
qualifying_loans = []

# Function to save qualifying loans to a CSV file
def save_qualifying_loans(qualifying_loans):
    # Prompt the user with a confirmation dialog using Questionary
    save_confirmation = questionary.confirm("Do you want to save your qualifying loans to a CSV file?").ask()

    if save_confirmation:
        # If the user wants to save the qualifying loans, prompt for the output file path
        output_file_path = questionary.text("Enter the output file path for saving the CSV file:").ask()
        
        # Write the qualifying loans to the CSV file
        with open(output_file_path, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(['Lender', 'Max Loan Amount', 'Max LTV', 'Max DTI', 'Min Credit Score', 'Interest Rate'])
            csv_writer.writerows(qualifying_loans)

        print(f"Qualifying loans saved to '{output_file_path}' successfully.")
    else:
        print("Qualifying loans were not saved.")

# Your existing code for the main function and loan qualification goes here...

if __name__ == "__main__":
    # Your existing code for the main function and loan qualification goes here...

    # Call the save_qualifying_loans function with the list of qualifying loans
    save_qualifying_loans(qualifying_loans)

