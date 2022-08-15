#learning operators 
#building a simple calculator 

#available mathematical operations
print("Please select an operation: \n" \
        "1. Add\n" \
        "2. Subtract\n" \
        "3. Multiply\n" \
        "4. Divide\n" \
        "5. Power\n"
        "6. Remainder\n"
        )
 
# Take input from the user
select = int(input("Select operations form 1, 2, 3, 4, 5, 6 : "))
if select not in range(1,7) : print("invalid operation") 

else: num_1 = int(input("Enter first number: ")); num_2 = int(input("Enter second number: "))

#performing operations required by user and showing the output
if select == 1: print(num_1, "+", num_2, "=", num_1+num_2)
if select == 2: print(num_1, "-", num_2, "=", num_1-num_2)
if select == 3: print(num_1, "*", num_2, "=", num_1*num_2)
if select == 4: print(num_1, "/", num_2, "=", num_1/num_2)
if select == 5: print(num_1, "^", num_2, "=", num_1**num_2)
if select == 6: print(num_1, "%", num_2, "=", num_1%num_2)

#order of operations from left to right 
#PEMDAS
#Parenthesis, Exponent, Multiplication, Division, Addition, Subtraction
print(1+(2-1)) #should be 2
print(2**2+(2-1)) #should be 5
print(2**2*(2-1)/2) #should be 2.0