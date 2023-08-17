def monthly_mortage(loan,years,rate):
    months = years * 12
    monthly_rate = rate / 12 / 100
    top = loan * (monthly_rate * (1 + monthly_rate)**months)
    mortage = top / ((1 + monthly_rate)**months - 1)
    return mortage

def main():
    loan = int(input("Enter your mortage loan: "))
    years = int(input("Enter the number of years: "))
    rate = int(input("Enter the yearly mortage rate: "))
    result = monthly_mortage(loan,years,rate)
    print("The monthly mortage will be " + str(result))

main()