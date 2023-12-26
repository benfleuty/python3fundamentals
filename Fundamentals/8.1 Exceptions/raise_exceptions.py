def remainder_division(a, b):
    if b == 0:
        raise ZeroDivisionError

    # if b == 0:
    #     raise Excetpion("Divisor cannot be 0")

    result = a//b
    remainder = a%b
    print(f'a / b = {result}r{remainder}')

try:
    remainder_division(10,0)
except:
    print("Exception was thrown")