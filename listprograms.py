#for loop 

#while lo

listofchocolates = [" Bounty " , " Dairy Milk ","Fivestar","KitKat","Mumch","Milky bar","Eclairs","Ferrore"]

listofjuiceflavour  = ["Mango","Pineapple","apple","Orange","Kiwi","Leechi","Avacado"]
listofchocolates.remove("Ferrore")
listofchocolates.append("Uva")


both = listofchocolates+listofjuiceflavour
joinvar = "**".join(both)
splitvar = joinvar.split("**")
#print ("@".join(listofchocolates+listofjuiceflavour))
print (both)
print (joinvar)
print (splitvar)
print (both==splitvar)

