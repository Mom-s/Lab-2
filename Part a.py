#Part a of lab 2
total=0    # take variable
y=int(input("enter the year- "))    #taking input from user
for i in range (1,y+1):      # Using loop for years entered by user
 print("year-",i)            # Print output of 1st loop
 for j in range(1,13):       # Taking another loop for entaring data of rainfall
    a=float(input("Enter the amount of monthly rainfall- "))        # taking input of rainfall from the user 
    total=total+a           


print("For 12 month")

print("Total Rainfall=",total)                  # printing the total
print("Average Rainfall",total/j*y)             # printing the average 

