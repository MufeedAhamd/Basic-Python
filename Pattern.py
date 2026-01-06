''' Print all patterns using the  Loop Statement'''

# Print the Line of star
i=1
while(i<=5):
    print("*" ,end="") # for h
    # print("*" ) # for b
    i +=1

# Print Matrix formet of  star
for i in range(5):
    for j in range(5):
        print("*" , end="")
    print()

# # Print Left Side Triangle 
for i in range(5):
    for i in range(i+1):
        print(" * ",end="")
    print()

# Print Left (UP to Down) Side Triangle 
i= 5
while(i>=1):
    j=i
    while(j>=1):
        print(" * ",end="")
        j-=1
    print()
    i -=1


# Print Right Side Triangle  
# i=1
while(i<=5):
    j= i+1
    while(j<=5):
        print("   ", end="")
        j+=1

    k =i
    while(k>=1):
        print(" * ", end="")
        k-=1
    print()
    i+=1


#  Print Pyramid Pattern
i=1
while(i<=5):
    j= i+1
    while(j<=5):
        print("   ", end="")
        j+=1

    k =i
    while(k>=1):
        print(" * ", end="")
        k-=1


    m= i-1
    while(m>=1):
        print(" * ", end="")
        m-=1
    print()
    i+=1


# Print Revers Pyramid
# i=1
while(i<=5):
    j= i-1
    while(j>=1):
        print("   ", end="")
        j-=1

    k =i
    while(k<=5):
        print(" * ", end="")
        k+=1

    l = i+1
    while(l<=5):
        print(" * ", end="")
        l+=1

    print()
    i +=1



# Print A Pattern 
i =1 
while(i<=5):

    j=1
    while(j<=5):
        if (i>=2 )and( i!=3)and(j==2 or j==3 or j==4 ):
            print(" ",end="")
        else:
            
            print("*",end ="")
        j+=1

    print()
    i+=1


# Print M Pattern
i =1 
while(i<=5):

    j=1
    while(j<=5):
        if (i==1 and j==3):
            print(" ",end="")
        elif (i==2)and(j==2 or j==4):
            print(" ",end="")
        elif (i>=3)and(j==2 or j==3 or j==4):
            print(" ",end="")
        else:
            
            print("*",end ="")
        j+=1

    print()
    i+=1

# Print Z Pattern
i =1 
while(i<=5):

    j=1
    while(j<=5):
        if (i==2 ) and (j!=4):
            print(" ",end="")
        elif (i==3 ) and (j!=3):
            print(" ",end="")
        elif (i==4 ) and (j!=2):
            print(" ",end="")
        else:
            
            print("*",end ="")
        j+=1

    print()
    i+=1