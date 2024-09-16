import math

# Function to calculate investment
def investment_calculator():
    
    # Input deposit amount, interest rate, and years
    deposit = float(input("Enter the amount of money you are depositing: "))
    rate = float(input("Enter the interest rate (as a percentage): "))
    years = int(input("Enter the number of years you plan on investing: "))
    
    # Convert interest rate to decimal
    rate /= 100
    
    # Ask for interest type: simple or compound
    interest_type = input("Do you want simple or compound interest? ").lower()
    
    # Calculate total amount based on interest type
    if interest_type == "simple":
        total_amount = deposit * (1 + rate * years)
    elif interest_type == "compound":
        total_amount = deposit * math.pow((1 + rate), years)
    else:
        print("Invalid interest type entered.")
        return
    
    # Print the total amount after the given period
    print("Total amount after {} years: {:.2f}".format(years, total_amount))

# Function to calculate bond repayment
def bond_calculator():

    
    # Input present value, interest rate, and months
    present_value = float(input("Enter the present value of the house: "))
    rate = float(input("Enter the interest rate (as a percentage): "))
    months = int(input("Enter the number of months for repayment: "))
    
    # Convert interest rate to decimal and calculate monthly rate
    rate /= 100
    monthly_rate = rate / 12
    
    # Calculate bond repayment amount
    repayment = (monthly_rate * present_value) / (1 - math.pow((1 + monthly_rate), -months))
    
    # Print the monthly repayment amount
    print("Monthly repayment amount: {:.2f}".format(repayment))

# Main function
def main():
    
    # Display menu
    print("Welcome to the financial calculator!")
    print("Menu:")
    print("1. Investment - to calculate the amount of interest you'll earn on your investment")
    print("2. Bond - to calculate the amount you'll have to pay on a home loan")
    
    # Get user choice and convert to lowercase
    option = input("Enter either 'investment' or 'bond' from the menu above to proceed: ").lower()
    
    # Execute based on user choice
    if option == "investment":
        investment_calculator()
    elif option == "bond":
        bond_calculator()
    else:
        print("Invalid option selected.")

# Execute the main function
if __name__ == "__main__":
    main()
