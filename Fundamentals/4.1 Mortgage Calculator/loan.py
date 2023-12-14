money_owed = float(input('How much do you owe?\n'))
apr = float(input('What is the APR%?\n'))
monthly_payment = float(input('How much are you paying off per month?\n'))
months_to_see = int(input('How many months would you like to see?\n'))

monthly_interest_rate = apr/100/12 # to decimal, then to monthly rate

for i in range(months_to_see):

    interest_generated = money_owed * monthly_interest_rate
    money_owed = money_owed + interest_generated
    money_owed = money_owed - monthly_payment

    if money_owed-monthly_payment < 0:
        print(f'The last payment is {money_owed}. You paid off the load in {i + 1} months')
        break

    print(f'Paid {monthly_payment}, of which {interest_generated} was interest. Now you owe {money_owed}')