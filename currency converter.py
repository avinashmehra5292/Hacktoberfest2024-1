# Simple Currency Converter

# Predefined exchange rates (just for example purposes)
exchange_rates = {
    "USD": {"INR": 83.10, "EUR": 0.95, "GBP": 0.81},
    "INR": {"USD": 0.012, "EUR": 0.011, "GBP": 0.0097},
    "EUR": {"USD": 1.05, "INR": 87.50, "GBP": 0.85},
    "GBP": {"USD": 1.24, "INR": 102.0, "EUR": 1.17},
}

def currency_converter(amount, from_currency, to_currency):
    try:
        rate = exchange_rates[from_currency][to_currency]
        converted_amount = amount * rate
        return converted_amount
    except KeyError:
        return None

def main():
    print("Welcome to the Simple Currency Converter!")
    
    from_currency = input("Enter the currency you want to convert from (USD, INR, EUR, GBP): ").upper()
    to_currency = input("Enter the currency you want to convert to (USD, INR, EUR, GBP): ").upper()
    
    try:
        amount = float(input(f"Enter the amount in {from_currency}: "))
    except ValueError:
        print("Invalid amount. Please enter a valid number.")
        return
    
    if from_currency in exchange_rates and to_currency in exchange_rates[from_currency]:
        converted_amount = currency_converter(amount, from_currency, to_currency)
        print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")
    else:
        print("Sorry, we don't support that currency conversion.")
        
if __name__ == "__main__":
    main()
