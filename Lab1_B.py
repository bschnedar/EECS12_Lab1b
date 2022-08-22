#Brandon Schnedar 
#25821724
#1/7/2016
#This program multiples a number input by 3 10 times
#and prints as man times as you want.

def main():
    Y = eval(input("Enter an integer number less than 15: "))
   ## X = 10
    Z = eval(input("Enter the # of times to print Y: "))
    for i in range (Z):
        Y = Y * 3
        print("The value of Y is: ", Y)

   ## for f in range(Z):
     ##   print("The value of Y is: ", Y)
main()
