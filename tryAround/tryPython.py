### string
kobe = "kobe bean bryant"
print(kobe.title()) #### 每项首字母大写

#print(kobe.upper()) ##每项全部字母大写
#print(kobe.lower()) ##全部小写
first_kobe = "kobe"
middle_kobe = "bean"
last_kobe = "bryant"
full_kobe = first_kobe+" "+middle_kobe +" "+last_kobe ## str 相加
print(full_kobe)
## 换行 /n 
## 删除空白
lebron = "  LeBron James   "
print(lebron.strip()) ## 清除两端空格
##lebron.lstrip() kill 左空格
##lebron.rstrip() kill 右空格

##list
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