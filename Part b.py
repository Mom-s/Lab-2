# Part b of lab 2
number=int(input("Starting number of organisms:"))                                # Taking input from user     
percentage=int(input("Average daily percentage increase:"))                        # Taking input from user
Total=int(input("Enter the number of the days to display the finaly data:"))        # Taking input from user
c=number
print("Day approximate\t\t\tpopulation")                       
print("---------------------------------")
print(c,"\n")                                                  
for i in range(1,Total):
    c=number+(number*(percentage/100))                           # Printing average
    print(f"{i}\t\t\t\t\t\t",c,"\n")                            # Printing output
    number=c
