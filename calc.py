def add(a,b):
	return a+b
def subtract(a,b):
	return a-b
def multiply(a,b):
	return a*b
def divide(a,b):
	return x/y
def exponent(a,b):
	return a**b
def remainder(a,b):
	return a%b
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Exponent")
print("6.Remainder")
choice=input("Enter choice(1/2/3/4/5/6):")
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
if choice=='1':
	print(num1,"+",num2,"=",add(num1,num2))
elif choice=='2':
	print(num1,"-",num2,"=",subtract(num1,num2))
elif choice=='3':
	print(num1,"*",num2,"=",multiply(num1,num2))
elif choice=='4':
	print(num1,"/",num2,"=",divide(num1,num2))
elif choice=='5':
	print(num1,"**",num2,"=",exponent(num1,num2))
elif choice=='6':
	print(num1,"%",num2,"=",remainder(num1,num2))
else:
	print("Invalid Input")
