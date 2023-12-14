money_owed = float(input('How much do you owe?\n'))
apr = float(input('What is the APR%?\n'))
monthly_payment = float(input('How much are you paying off per month?\n'))
months_to_see = int(input('How many months would you like to see?\n'))

monthly_interest_rate = apr/100/12 # to decimal, then to monthly rate

for i in range(months_to_see):

    interest_generated = money_owed * monthly_interest_rate
    money_owed = money_owed + interest_generated

    if money_owed - monthly_payment < 0:
        print(f'The last payment is {money_owed:.2f}. You paid off the load in {i + 1} months')
        break

    money_owed = money_owed - monthly_payment
    
    print(f'Paid {monthly_payment:.2f}, of which {interest_generated:.2f} was interest. Now you owe {money_owed:.2f}')