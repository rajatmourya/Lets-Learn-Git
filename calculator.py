def cal(n):
    if n == 1:
        print(f"Addition of {a} and {b} is =",(a+b))
    elif n == 2:
        print(f"Subtraction of {a} and {b} is =",(a-b))
    elif n == 3:
        print(f"Divition of {a} and {b} is =",(a/b))
    elif n == 4:
        print(f"Multiplication of {a} and {b} is =",(a*b))
    else:
        print("Invalid Choice ! Please choose correct one ")
        
        
x = True
while x:
    a = int(input("Enter the First Number: "))
    b = int(input("Enter the Second Number: "))
    print("1). Addition \n 2). Subtraction \n 3). Divition \n 4).Multiplication")
    n = int(input())    
    cal(n)
    print("Do tou want to continue type Y or y otherwise any other key")
    z = input()
    if z == "Y" or z == "y":
        x = True
    else:
        x = False
