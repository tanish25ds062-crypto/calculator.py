choice=int(input("\n 1.add \n 2.substract \n 3.divide \n 4.multiply \n"))
a=int(input("Enter a number value : "))
b=int(input("Enter a number value : "))
if choice==1:
    print(a+b) 
elif choice==2:
    print(a-b)
elif choice==3:
    print(a/b)
elif choice==4:
    print(a*b)
else:
    print("you Enter wrong input")


