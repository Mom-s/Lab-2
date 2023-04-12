#Part d of lab 2
a=[]       # taking list

num=int(input("Enter the value "))                     # Taking input from user
greater=int(input("Enter the value from where you want to print the greater number "))                 # Taking input from user
print("List of the number")                            # Taking input from user
for i in range(1,num+1):                               
  a.append(i)                                          # using append comand to add at the back

print(a)                                            # Printing the first list
b=[]        # taking list
print("List of number that larger then the entered value")       
for i in range(0,num):
  if (a[i]>greater):                  # Using loop for display the greater number
    b.append(a[i])
  else:
   pass

print(b)                                            # Printing the second list
