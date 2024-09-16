import math

# Function to calculate the future value of an investment based on interest type
def investment_calculator():
> main
    # Input: Get the deposit amount, interest rate, and number of years from the user
    deposit = float(input("Enter the amount of money you are depositing: "))
    rate = float(input("Enter the interest rate (as a percentage): "))
    years = int(input("Enter the number of years you plan on investing: "))
    
    # Convert the interest rate from percentage to decimal for calculation
    rate /= 100
    
    # Ask the user if they want simple or compound interest
    interest_type = input("Do you want simple or compound interest? ").lower()
    
    # Calculate total amount based on the interest type selected
    if interest_type == "simple":
        # Simple interest formula: A = P(1 + rt)
        total_amount = deposit * (1 + rate * years)
    elif interest_type == "compound":
        # Compound interest formula: A = P(1 + r)^t
        total_amount = deposit * math.pow((1 + rate), years)
    else:
        # If the user enters an invalid option, exit the function
        print("Invalid interest type entered.")
        return
    
    # Output: Display the total amount after the investment period
    print("Total amount after {} years: {:.2f}".format(years, total_amount))


# Function to calculate monthly bond repayments (mortgage)
def bond_calculator():


    # Input: Get the present value of the house, interest rate, and repayment period (in months)
    present_value = float(input("Enter the present value of the house: "))
    rate = float(input("Enter the interest rate (as a percentage): "))
    months = int(input("Enter the number of months for repayment: "))
    
    # Convert the annual interest rate to a monthly rate (as a decimal)
    rate /= 100
    monthly_rate = rate / 12
    
    # Bond repayment formula: 
    # Monthly repayment = [r * P] / [1 - (1 + r)^(-n)]
    # where P is the present value, r is the monthly interest rate, and n is the number of months
    repayment = (monthly_rate * present_value) / (1 - math.pow((1 + monthly_rate), -months))
    
    # Output: Display the monthly repayment amount
    print("Monthly repayment amount: {:.2f}".format(repayment))


# Main function to drive the financial calculator
def main():

    
    # Display the menu to the user
    print("Welcome to the financial calculator!")
    print("Menu:")
    print("1. Investment - to calculate the amount of interest you'll earn on your investment")
    print("2. Bond - to calculate the amount you'll have to pay on a home loan")
    
    # Get the user's option and convert to lowercase for easier matching
    option = input("Enter either 'investment' or 'bond' from the menu above to proceed: ").lower()
    
    # Call the appropriate function based on the user's choice
    if option == "investment":
        investment_calculator()  # Calls the investment calculator
    elif option == "bond":
        bond_calculator()  # Calls the bond calculator
    else:
        # If an invalid option is selected, display an error message
        print("Invalid option selected.")

# Ensure the main function runs when the script is executed
if __name__ == "__main__":
    main()

