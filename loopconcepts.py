#Two loops we have for and while


listofchocolates = ["Bounty", "Dairy Milk","Fivestar","KitKat","Munch","Milky bar","Eclairs","Ferrore"]
buychocolateslist= []

'''
buychocolateslist.append("Kitkat")
buychocolateslist.append("Bounty")
listofchocolates.remove("KitKat")
listofchocolates.remove("Bounty")
print  (buychocolateslist)
print (listofchocolates)
'''

for i in listofchocolates:
    if i.lower() in ["bounty" ,"kitkat"]:
        #Either i = Bounty or KitKat
        buychocolateslist.append(i)
        listofchocolates.remove (i)

        print  (buychocolateslist)
        print (listofchocolates)



#Kitkat and bounty got over , in empty these two chocs need to move 
#listofchocolates -  should remove this


listofjuiceflavour  = ["Mango","Pineapple","apple","Orange","Kiwi","Leechi","Avacado"]

#for i in listofchocolates:
   # print (i)

#for i in listofjuiceflavour[0:5]:

    #if (i.lower()  in  ["leechi" ,"orange"]): 
    #
       # print ("My favourite juice  is :" , i)
   