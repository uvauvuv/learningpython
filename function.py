'''
Q.Write a function to take two numbers , add, sub , mul, div send 
both num should be as input 
'''

getnum = input ("Please enter two numbers: ")
splitnumbers = getnum.split(" ")
#print (splitnumbers) #still strings 
#print (type (getnum))
'''
#convert to int
num = int (getnum)

print (num)
print (type (num))

'''
num1 = int (splitnumbers[0])

num2 =int (splitnumbers[1])

def calci (a,b):
    
    sum = a+b
    sub= a-b
    mul = a*b
    div = a/b
    return mul,sum,sub,div
#print (num1,num2)
#print (type (num1),type (num2))

result = calci(num1,num2) #4
functions = ["mul" ,"sum","sub" ,"div"] #4 ok
for i in range(len(functions)) : 
    print (functions[i] ," of two numbers is" , result[i])
    #oh ok ok 
   #sure 

   # know square [], list, 0

    '''  0 
print ("Sum of two numbers is : " , result[1] ) #indexing
print ("mul of two numbers is : ", result [0] )
print ("Div of two numbers is : " , result [3] )
print ("Sub of two numbers is : ", result[2] )
'''