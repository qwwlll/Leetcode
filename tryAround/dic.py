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

#######   notes= collections.defaultdict(int) 用来聚类计数
#######   dic_map = collections.Counter(nums)

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





sorted(dic.iteritems(), key=lambda d:d[1], reverse = False )  


def dictionairy():  
 
    # 声明字典
    key_value ={}     
 
    # 初始化
    key_value[2] = 56       
    key_value[1] = 2 
    key_value[5] = 12 
    key_value[4] = 24
    key_value[6] = 18      
    key_value[3] = 323 
 
 
    print ("按值(value)排序:")   
    print(sorted(key_value.items(), key = lambda kv:(kv[1], kv[0]))) 



def dictionairy():  
  
    # 声明字典
    key_value ={}     
 
    # 初始化
    key_value[2] = 56       
    key_value[1] = 2 
    key_value[5] = 12 
    key_value[4] = 24
    key_value[6] = 18      
    key_value[3] = 323 
 
    print ("按键(key)排序:")   
 
    # sorted(key_value) 返回重新排序的列表
    # 字典按键排序
    for i in sorted (key_value) : 
        print ((i, key_value[i]), end =" ") 



lis = [{ "name" : "Taobao", "age" : 100},  
{ "name" : "Runoob", "age" : 7 }, 
{ "name" : "Google", "age" : 100 }, 
{ "name" : "Wiki" , "age" : 200 }] 
  
# 通过 age 升序排序
print ("列表通过 age 升序排序: ")
print (sorted(lis, key = lambda i: i['age']) )
  
print ("\r") 
  
# 先按 age 排序，再按 name 排序
print ("列表通过 age 和 name 排序: ")
print (sorted(lis, key = lambda i: (i['age'], i['name'])) )
  
print ("\r") 
  
# 按 age 降序排序
print ("列表通过 age 降序排序: ")
print (sorted(lis, key = lambda i: i['age'],reverse=True) )