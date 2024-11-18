"""1.	Write a program to print all the Non-Prime numbers between A and B? Sample Input: A = 12 B = 19
Sample Output:          
14, 15, 16, 18

a = int(input())
b = int(input())
for x in range (a, b+1):
    if x > 1:
        for i in range (2, x):
            if (x%i)== 0:
                print("Non-Prime:",x)
                break
        else:
            print ("Prime:",x)
            
"""

"""
date = input("Enter the date to be checked: ")
c=date.split("/")
b = list(map(int,c))
input_year=(b[2])

if(input_year%4 == 0):
    if(input_year%100 == 0):
        if(input_year%400 == 0):
            print("%d is Leap Year" %input_year)
        else:
            print("%d is not the Leap Year" %input_year)
    else:
        print("%d is the Leap Year" %input_year)
else:
    print("%d is not the Leap Year" %input_year)

x=input_year%4
if x!=0:
    print("Previous Leap year:", input_year-x)
else:
    print("Next leap year:", input_year+4)
"""
"""
3.	Write a program to print the given number is Perfect number or not? 
Sample Input: Given Number: 6 
Sample Output: Its a Perfect Number """

Number = int(input(" Please Enter any Number: "))
Sum = 0
for i in range(1, Number):
    if(Number % i == 0):
        Sum = Sum + i
if (Sum == Number):
    print(" %d is a Perfect Number" %Number)
else:
    print(" %d is not a Perfect Number" %Number)
    
#4.	Write a program to generate Pythagorean Triplets for the given limit.
#Enter upper limit: 10
#3 4 5
#8 6 10

A=input("Enter upper limit:")
c=0
m=2
if A.isnumeric():
    x=int(A)
    while(c<x):
        for n in range(1,m+1):
            a=m*m-n*n
            b=2*m*n
            c=m*m+n*n
            if(c>x):
                break
            if(a==0 or b==0 or c==0):
                break
            print(a,b,c)
        m=m+1
else:
    print("invalid input")
    
    
#5.	Write a program to find the sum of digits of N digit number (sum should be single digit)
#Sample Input: Enter N value : 3 Enter 3 digit number: 143 
#Sample Output: Sum of 3 digit number: 8

num=int(input("Enter the number:"))
Sum=0
temp=num
while temp>0:
    digit=temp%10
    Sum+=digit
    temp=temp//10
print("Sum of Digits:", Sum)

#6.	Program to find whether the given number is Armstrong number or not 
#Sample Input: Enter number: 153 
#Sample Output: Given number is Armstrong number

num=int(input("Enter the number:"))
Sum=0
temp=num
while temp>0:
    digit=temp%10
    Sum+=digit**3
    temp=temp//10
if Sum==num:
    print("Armstrong Number")
else:
    print("Not a Armstrong Number")

#7.	Program to find whether the given number is Harshad number or not 
#Sample Input: Enter number: 21
#Sample Output: Given number is Harshad number

num=int(input("Enter the number:"))
Sum=0
temp=num
while temp>0:
    digit=temp%10
    Sum+=digit
    temp=temp//10
if num%Sum==0:
    print("Harshad Number")
else:
    print("Not a Harshad Number")

#8.	Program to find whether the given number is Happy number or not 
#Sample Input: Enter number: 19
#Sample Output: Given number is happy number

def happy(n):
    temp=n
    sum=0
    while temp>0:
        digit=temp%10
        sum=digit**2+sum
        temp=temp//10
    return sum
    
# Main Program

num=int(input("Enter the number:"))
result=num
while result!=1 and result!=4:
    result=(happy(result))
if result==1:
    print("True")
elif result==4:
    print("False")

#9.	Program to find whether the given number is Tech number or not 
#Sample Input: Enter number: 3025
#Sample Output: Given number is Tech number

n = 3025
m = str(n)
a = m[:len(m)//2]
b = m[len(m)//2:]
c = int(a)+int(b)
d = c**2

if(d==n):
    print("Tech number")
else:
    print("Not a Tech number")

#10.	Write a program using function to calculate the simple interest. Suppose the customer is a senior citizen. She is being offered 15 percent rate of interest; he is being offered 12 percent rate of interest for all other customers, the ROI is 10 percent.
#Sample Input:
#Enter the principal amount: 200000 Enter the no of years: 3
#Gender (m/f): m
#Is customer senior citizen (y/n): n Sample Output:
#Interest: 60000

p=int(input("Enter the Principle amount:"))
n=int(input("Enter the number of years:"))
SC=input("Senior Citizen Yes/No:")
G=input("Male/Female:")
if SC=='Y' and G=='M':
    print("SI=",(p*n*12)/100)
elif SC=='Y' and G=='F':
    print("SI=",(p*n*15)/100)
else:
    print("SI=",(p*n*10)/100)




