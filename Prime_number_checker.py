#Write your code below this line 👇

def prime_checker(number):
    no = 0 
    for num in range(2,number):
        if number % num == 0 :
            no +=1
    if no > 1:
        print("It's not a prime number.")
            
    if no == 0:
        print("It's a prime number.")

#Write your code above this line 👆
    
#Do NOT change any of the code below👇

n = int(input("Check this number: "))
prime_checker(number=n)



