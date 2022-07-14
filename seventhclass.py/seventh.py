# d = {"name": "grace",
#      "course": "backend",
#      "score": [10,2,50,56],
#     "address": {"str_num": 2,
#               "str_name": "montegomerty road",
#               "city": "yaba"}
# }





# print(d["name"][0])
# print(max(d["score"]))

# # print()
# # print(d["girl"])
# print(d.get("girl"))
# print(d.get("girl", "not found"))


# d["new_name"]= d.pop("name")
# print(d)

# d["george"]= d.pop("new_name")
# print(d)

# print(d.keys())
# print(d.values())
# print(d.copy())



from audioop import reverse


# data = {'5': 8,
# "3": 10,
# "4": 2,
# "9": 3,
# "2": 7,
# "0": 5}

# sorted_x = sorted(data.item(),
# key = lambda x: x[1], reverse= True)


# print(dict(sorted_x))
# # grade

# grade= [100, 50, 60, 70, 80,20]
# remark=("accept","no accept")

# new_map= (zip(grade,remark))
# print(dict(new_map))

# data= {"v":"S001","vi":"S002", "vii":"S003","viii":'S004',"viv":"S005","w":"S009","wi":"S007"}


# print(data.values())

# print(set(data.values()))
# # print(data.items())




while True:
    data = int(input(">>"))
    print(data)
    if data == 5:
       break



a =10
while a > 10:
   print(a)
   a-=1


a = 100
count = 0
while a > 0:
    print(a)
    a-=1
    count += 1
    if count == 3:
      break

