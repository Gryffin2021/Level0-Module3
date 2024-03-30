"""
 TODO: Fizz Buzz
   In this project, we're going to build FizzBuzz. It's a children's game where
   you count from 1 to 20. Easy, right? Here's the catch:
   -
   Instead of saying a number that is divisible by 3, say "Fizz".
   And instead of saying a number that is divisible by 5, say "Buzz".
   For numbers divisible by both 3 and 5, say "FizzBuzz".
   -
   Print your results to the console.
   -
   If your code is correct, the output will be:
   -
   1 2 fizz 4 buzz fizz 7 8 fizz buzz 11 fizz 13 14 fizzbuzz 16 17 fizz 19 buzz
"""
if __name__ == '__main__':
    for i in range(20):
        j = i + 1
        if(j % 3 == 0 and j % 5 == 0):
            print("fizzbuzz")
        elif(j % 3 == 0):
            print("fizz")
        elif(j % 5 == 0):
            print("buzz")
        else:
            print(str(j))
