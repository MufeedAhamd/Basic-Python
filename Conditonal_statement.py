''' In this file we use Conditional Statement to solve our problems
    1 . if else statement
    2 . Nested if else statement
    3 . Switch (Match) statement
'''


# Checking the given number is Even or Odd
x = int(input("Enter the Number :"))
if x %2 ==0:
    print(f"The given {x}  is Even Number .")
else:
    print(f"The given {x} is Odd Number")


# Checking the Student result (Pass or Fail) 
a= int(input("Enter the subject 1 number (Out of Hunderd):"))
b= int(input("Enter the subject 2 number (Out of Hunderd):"))
c= int(input("Enter the subject 3 number (Out of Hunderd):"))

Total = a+b+c
per = (Total/300) *100

if per >=40 :
    print("Pass")
else:
    print("Fail")



# Given Number
a = int(input("Enter the Number :"))
if a <0 :
    print("Given Number is Negative")
elif a==0:
    print("Given Number is Zero")
else:
    print("Given Number is Positive")


# Eligibility for Voting
age = int(input("Enter Your Age :"))
if age <18:
    print("You are not Eligibile for Vote")
else:
    print("You can Vote")


# Checking the Student Result with grade
English= int(input("Enter  English number (Out of Hunderd):"))
Hindi= int(input("Entert Hindi number (Out of Hunderd):"))
Math= int(input("Enter  Math number (Out of Hunderd):"))
Science= int(input("Enter Science number (Out of Hunderd):"))
SST= int(input("Enter SST number (Out of Hunderd):"))

Total = English+Hindi+Math+Science+SST
per = (Total/500)*100

if per >=90:
    print("You got A+ Grade in your Exam")
elif per >80 and per<90:
    print("You got A Grade in your Exam")
elif per >70 and per<80:
    print("You got B Grade in your Exam")
elif per >60 and per<70:
    print("You got C Grade in your Exam")
elif per >50 and per<60:
    print("You got D Grade in your Exam")
else:
    print("your are Fail")

print(f"Your got {per} %")


# Find the Largest Number 
a=int(input("Enter the Number of a :"))
b=int(input("Enter the Number of b :"))
c=int(input("Enter the Number of c :"))

# Nested if Statement
if a>b:
    if a>c:
        print(f"{a} is Largest Number")
    else:
        print(f"{c} is Largest Number")

elif b>c:
    print(f"{b} is Largest Number")
else:
    print(f"{c} is Largest Number")



# Crate a Calculater (Using a Switch )
num1 = int(input("Enter the number 1 :"))
num2 = int(input("Enter the number 2 :"))
oper= input("Enter the symbole that operation you want (+,- ,* ,/) :")

match oper:
    case "+":
        print(f" The Addition of : {num1} + {num2} =", num1+num2)
    
    case "-":
        print(f" The Subtraction of : {num1} - {num2} =", num1-num2)
    
    case "*":
        print(f" The Multipliction of : {num1} * {num2} =", num1*num2)
    case "/":
        print(f" The Division of : {num1} / {num2} =", num1/num2)


   
# Calclulate the  Water Bill
unit  = int(input("Enter your Water unit (in KL):"))

if unit <8000 :
    print(f"Your Bill is :{unit *8.5} Rupees")
elif unit >8000 and unit <25000:
    print(f"Your Bill is :{unit *14} Rupees")
elif unit >25000 and unit <50000:
    print(f"Your Bill is :{unit *34} Rupees")
else:
    print(f"Your Bill is :{unit *55} Rupees")
