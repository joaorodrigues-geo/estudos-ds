for number in range(1,101):
    output = number
    if number % 3 == 0 and number % 5 == 0:
        output = "FizzBuzz"
    elif number % 3 == 0:
        output = "Fizz"
    elif number % 5 == 0:
        output = "Buzz"
    print(output)
