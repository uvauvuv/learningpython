#Given a list of name print the names with first letter of capital

Names = ["yuvarani", "bharath", "Hari"]
#op Yuvarani
#Bharath
#already in caps Hari
#Okay 


#for i in Names [0]: #Iterator.
 # print (i)

for i in Names:
    
    first = i[0].upper()
    second = i[1:].lower()

    print (first+second)