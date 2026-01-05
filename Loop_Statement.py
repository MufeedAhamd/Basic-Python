''' In this file we use Loop statement 
    1 . For Loop
    2 . While Loop
'''

#  Write the table of given number 
a = int(input("Enter the Number :"))
i=0
while(i<=10):

    print(f"{a} x {i} = ",i*a)
    i+=1


#  Calculates the sum of all numbers from 1 to a user-defined
num = int(input("Enter the Number :"))
i=1
total =0
while(i<=num):
    total = total +i
    
    i +=1
print(total)


#  Count the total digit in given number
num = int(input("Enter the Number :"))
count =0
n = abs(num)

if n==0:
    count =1
else:
    while(n>0):
        n //= 10
        count +=1
print(f"Total number of digits :", count)


# Identifies all Prime numbers in range(1-100)
a =[]
for i in range(1,100):
    if i %2 ==0:
        a .append(i)

print ( "All Prime Numbers Are:",a)


# Fibonacci Sequence
num = int(input("Enter the Number :"))
a = 0
b=1
for i in range(num):
    print(a,end=" ")
    a =b
    b= a+b
print()


# Print 1 - 10 table unsig nested loop
i = 1
while i <= 10:
    j = 1
    while j <= 10:
        # Calculate product
        result = i * j
        
        print(f"{result}", end="\t")
        j += 1
    print() 

    i += 1
