import math

def exercise3():
    radius = 2
    height = 3

    cylinder_volume = math.pi * pow(radius,2) * height

    print(cylinder_volume)


def exercise4():
    
    score = input("Enter Score: ")
    score = int(score)
    
    if(score <= 9 and score >= 0):
       print("Insufficient")
    elif(score <= 13):       
        print("Average")
    elif(score <= 16):
        print("Good")
    elif(score <= 20):
        print("Excellent")
    else:
        print("Invalid score")
        
def exercise5():
    
    def ex5_a():
        sum = 0
        n = int(input("Enter a number for N:"))
        
        for i in range(0,n+1):
            sum += i
            
        print(sum)
        
    def ex5_b():
        sum = 0
        n = int(input("Enter a number for N:"))
        x = int(input("Enter a number for X:"))
        
        for i in range(0,n+1):
            sum += pow(x,i)
            
        print(sum)
        
    def ex5_c():
        sum = 0
        n = int(input("Enter a number for N:"))
        x = int(input("Enter a number for X:"))
        
        for i in range(0,n+1):
            sum += (pow(x,i)/math.factorial(i))
            
        print(sum)
        
    def ex5_d():
        sum = 0
        n = int(input("Enter a number for N:"))
        x = int(input("Enter a number for X:"))
        
        for i in range(0,n+1):
            sum += (pow(-1,i)) * (pow(x,2*i+1)/math.factorial(2*i+1))
            
        print(sum)
        
  
def exercise6():
    n = int(input("Enter a number for N:"))
    multiples = []
    
    for i in range(0,100+1):
        if(i%n == 0):
            multiples.append(i)
    
    print(multiples)
        
def exercise7(n):
    
    if(n == 0):
        return 0
    elif(n == 1):
        return 1
    elif(n >= 2):
        res = exercise7(n-1) + exercise7(n-2)
        return res
    else:
        return res

def exercise8():
    n = int(input("Enter a number for N:"))
    m = int(input("Enter a number for M:"))
    sum = 0
    
    for i in range(n,m+1):
        if(i%2 != 0):
            sum += i

    print(sum)
    
def exercise9():
    set = []
        
    for _ in range(0,3):
        set.append(int(input("Enter a number:")))
    
    print("Maximun number is: ", max(set))
    print("Minimum number is: ", min(set))
    print("Average is: ", sum(set)/len(set))
    print("Sum is: ", sum(set))


def exercise10():
    n = int(input("Enter a number for N:"))

    isAscending = False 
    isDescending = False
    
    # Finds the ascending or descending order of the number
    while(n > 10):
        
        # n%10 gives the last digit and the (n//10)%10 gives the second digit of the number
        if(n%10 > (n//10)%10):
            isAscending = True
        elif(n%10 < (n//10)%10):
            isDescending = True
        # If the digits are equal, then the number is not in any order
        else:
            pass
        
        n = n//10
        
    if(isAscending and isDescending):
        print("The number doesnt have an order")
    elif(isAscending):
        print("The number is in ascending order")
    elif(isDescending):
        print("The number is in descending order")


def exercise11():
    
    # Represents all the possible money that can be given
    existing_money = [50, 20, 10, 5, 2, 1, 0.5, 0.2, 0.1, 0.05, 0.01]
    # Represents the money that is retreived, each index represents the amount of each note/coin that is retreived
    retreived_money = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    
    while(True):
        to_be_paid = float(input("Enter the amount to be paid: "))
        received_money = float(input("Enter the amount received: "))
        
        # If the received money is less than the amount to be paid, then the loop continues
        if(received_money < to_be_paid):
            print("Not enough money")
            continue
          
        change = received_money - to_be_paid

        # If the change is 0, then the customer has paid the exact amount and loop ends
        while(change > 0):
            # Goes through the existing money and checks if the change is greater than the money than it adds the money to the retreived money
            for money in existing_money:
                if(change >= money):
                    retreived_money[existing_money.index(money)] += 1
                    change -= money
                    change = round(change, 2)
        
        # Prints the change that is returned
        print(f"\nChange returned: {received_money - to_be_paid:.2f}€")
        # With the enumerate function we can get both the index and value of the current index
        for index, count in enumerate(retreived_money):
            if count != 0:
                # <note/coin value> : number of
                print(f"{existing_money[index]}€ -> {count}")
                
        break
    

def exercise12():
    n = int(input("Enter a number bigger than 1: "))
    sum = 0
    last_number = 1
    
    while(sum + last_number <= n):
        sum += last_number
        last_number += 1
    
    last_number -= 1
    print(last_number)
    


