money_owed = float(input('How much do you owe?\n'))
apr = float(input('What is the APR%?\n'))
monthly_payment = float(input('How much are you paying off per month?\n'))
months_to_see = float(input('How many months would you like to see?\n'))

monthly_interest_rate = apr/100/12 # to decimal, then to monthly

interest_generated = money_owed * monthly_interest_rate

money_owed = money_owed + interest_generated

money_owed = money_owed - monthly_payment

print(f'Paid {monthly_payment}, of which {interest_generated} was interest. Now you owe {money_owed}')