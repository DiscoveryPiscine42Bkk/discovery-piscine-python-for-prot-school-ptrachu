num1 = int(input("Enter the first Number: "))
num2 = int(input("Enter the second Number: "))
sum = num1*num2
print(num1,"x",num2,"=",sum)
if sum > 0:
    print("The result is positive.")
if sum < 0:
    print("The result is negative.")
if sum == 0:
    print("The result is positive and negative.")