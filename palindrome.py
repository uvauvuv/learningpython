#write a program to find a palindrome
#get input from user palindome means yes if no not a palindrome
#Madam

#Scanner sc = new Scanner(System.in)

message = input("Please enter a string : ").lower()
print (message)

if message == message[::-1]:
    
    print ("It is a palindrome")
else:
    print("Not a palindrome")
