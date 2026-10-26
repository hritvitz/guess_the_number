import random
secret = (random.randint(1,100))
attempt=1

n=int(input("guess the number:"))

while n!=secret:
    
    if n > secret:
        print("TOO Hight")
        
    elif n < secret:
        print("TOO Low")

    n=int(input("guess the number:"))
    attempt+=1

print("correct answer buddy")
print("no of attempts:",attempt)
