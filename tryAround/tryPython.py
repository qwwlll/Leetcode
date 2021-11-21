from typing import List
# ### string
# kobe = "kobe bean bryant"
# print(kobe.title()) #### 每项首字母大写

# #print(kobe.upper()) ##每项全部字母大写
# #print(kobe.lower()) ##全部小写
# first_kobe = "kobe"
# middle_kobe = "bean"
# last_kobe = "bryant"
# full_kobe = first_kobe+" "+middle_kobe +" "+last_kobe ## str 相加
# print(full_kobe)
# ## 换行 /n 
# ## 删除空白
# lebron = "  LeBron James   "
# print(lebron.strip()) ## 清除两端空格
# ##lebron.lstrip() kill 左空格
# ##lebron.rstrip() kill 右空格

# ##list
# names = ['Westbrook', 'AD','Lebron','Kuzma','DHoward']
# #print(names)
# #for i in names:
# #    print("Hello, "+ i.title()+ " welcome to the laker show!!")
# #print("so sorry that " +names[3]+ " has been traded to DC!!")



# ###remove
# ##names.pop(0)  ##del the final one / any place
# ##del names[2]   ##del anyplace
# names.remove("Kuzma")
# print(names)



# ### adding
# names.append("Zo2") #### added at end
# #for i in names:
# #    print("Hello, "+ i.title()+ " welcome to the laker show!!")
# names.insert(0, "Melo")### added at anyplace mentioned as parameter
# print(names)


# ##sorting
# #names.sort() ## change the list forever
# sorted(names) ## change the list temp for showing but not forever
# print(names)
# names.reverse()## change the list forever
# print(names)




# #### -----------------------------------------condition line if condition
# #### if-elif-else line
# logging_names = []
# logging_names.append("David")
# logging_names.append("Lisa")
# logging_names.append("lizz")
# logging_names.append("Jason")
# logging_names.append("Raymond")
# logging_names.append("Clay")
# logging_names.append("Admin")
# if logging_names:
#     for i in logging_names:
#         if i == "Admin":
#             print("Hello, " + i + ", would you like to see the status report?")
#         else:
#             print("Hello, Brove"+ str(logging_names.index(i)) + i + " , welcome to the devgru")
# else: 
#     print("Hi, nobody is here! find somebody!")

######________________________________________________输入

# mesg = input(" Good morning, Mr.J "+"\n tell about it more : ")
# age = input("Sir, how old are you: ")
# if int(age) >= 18: ## what we got in the input box was str type using int() to trans to int
#     print(mesg)





######________________________________________________while condition
# num = input("enter the start num: ")
# nums = int(num) 
# while nums < 10:
#     nums  += 1
#     if nums % 2 == 0:
#         continue
#     else:
#         print(nums)

# age = input("Hi, welcome, Can I know your age: ")
# while int(age) < 3:
#     print('you are free!! young bud!')
#     break
# while int(age)>=3 and int(age)<= 12:
#     print("Nah boy, your price of the ticket is 10 dollars!")
#     break

# while int(age) > 12:
#     print('Nah boy, your price of the ticket is 15 dollars!') 
#     break

# #### while in lists:
# on_court = ['Bron','Kuz','AD','AC','DH']
# off_court = ['Melo','JR','Andre','Danny','KD']
# for player in on_court:
#     print(" these players are on the court now: ")
#     print(player)
#     off_court.pop()

# while off_court == []:
#     print(" nobody on the court! do something, coach!!")
#     print("you got:")
#     print(on_court)
#     break





# #### ----------------------------------------dictionary type
# nba_dic = {}
# nba_dic['names'] = 'lebron'
# nba_dic['teams'] = 'laker'
# nba_dic['pos'] = 'sf'
# print(nba_dic)
# laker_dic = {}
# laker_dic = {
#     "AD": 'PF',
#     'LBJ':'SF',
#     'Russ':'PG',
#     'Melo':'PF',
#     'DHoward':'C'
# }
# print(laker_dic)
# ### 遍历 整个字典
# for name, pos in laker_dic.items():
#     print(name.title() + "'s postion on court is  "+ pos)
# ### dic == {key: value,key: value,key: value,key: value,.....} 遍历所有的key 键
# for names in laker_dic.keys():
#     print(names)
# ### dic == {key: value,key: value,key: value,key: value,.....} 遍历所有的value 值
# for pos in laker_dic.values():
#     print(pos)



# bulls_dic = {
#     "DD": 'PF',
#     'Lavein':'SF',
#     'Zo':'PG',
#     'Vuicnic':'PF',
#     'AndreD':'C'
# }
# phlly_dic = {
#     "Ben": 'PF',
#     'Harris':'SF',
#     'S.Curry':'PG',
#     'Danny':'PF',
#     'Embiid':'C'
# }



# ### dic 删除
# del phlly_dic['S.Curry']
# print(phlly_dic)

# ### 嵌套dic 创建list 中有dic
# final_dic =[
#     laker_dic,
#     bulls_dic,
#     phlly_dic
# ]
# for team in final_dic:
#     print(team)

# ### 在dic 中创建list
# lal_dic = {
#     "AD": ['PF','C'],
#     'LBJ':['PF','SF'],
#     'Russ':['PG','SG'],
#     'Melo':['SF','PF'],
#     'DHoward':['C']
# }
# for name, pos in lal_dic.items():
#     print("this is "+ name + " and here are his pos:" )
#     for po in pos:
#         print(po)

# # ######________________________________________________ Function
def magicians(mags): #### 打印字典
    for mag_f, mag_l in mags.items():
        print("Hello, " + mag_f.title() +" "+ mag_l.title() + " welcome to the bar")

def edit_mags(mag, mags): #### 编辑字典
    for mag_f, mag_l in mag.items():
        mags[mag_f] = mag_l
    while "magic" in mags.keys():
        del mags["magic"]
            

maglk = {
    "magic":"Daron",
    "bryant":"kobe",
    "james":"harden"
}
mag = {
    "Anthoy":"Davis"
}
print("the older dict is: ")
magicians(maglk)
edit_mags(mag,maglk)
print("Now the new edited dict is :")    
magicians(maglk)
     
#### cars dict builder:
def builder(cars, names, colors):
    for i in range(len(names)):
        cars[names[i]] = colors[i]
    return print(cars)

cars ={}
names = ['Volvo',"BMW","Mercides","AMG","Audi","Lamborghini"]
colors = ["gray","black","Sliver","Green","blue","yellow"]

builder(cars, names,colors)