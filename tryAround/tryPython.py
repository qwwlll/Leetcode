names = ['Westbrook', 'AD','Lebron','Kuzma','DHoward']
#print(names)
#for i in names:
#    print("Hello, "+ i.title()+ " welcome to the laker show!!")
#print("so sorry that " +names[3]+ " has been traded to DC!!")



###remove
##names.pop(0)  ##del the final one / any place
##del names[2]   ##del anyplace
names.remove("Kuzma")
print(names)



### adding
names.append("Zo2") #### added at end
#for i in names:
#    print("Hello, "+ i.title()+ " welcome to the laker show!!")
names.insert(0, "Melo")### added at anyplace mentioned as parameter
print(names)


##sorting
#names.sort() ## change the list forever
sorted(names) ## change the list temp for showing but not forever
print(names)
names.reverse()## change the list forever
print(names)