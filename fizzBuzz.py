# Mini Project: A program to print numbers from 1 to 100, replacing multiples of 3 with 'Fizz' and multiples of 5 with 'Buzz'. If 3 and 5 both multiplies than show 'FizzBuzz'.

# A num is a multiply of 3 if that num is divided by 3 and the remainder of the division = 0

# FizzBuzz program

for num in range(1, 101): # This will works or iterate 1 to 100
    if num % 3 == 0 and num % 5 == 0:
        print('FizzBuzz')
    elif num % 3 == 0:
        print('Fizz')
    elif num % 5 == 0:
        print('Buzz')
    else:
        print(num)





