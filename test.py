# import pprint
# from termcolor import colored,cprint
# vowel_count = 0
# vowels = ['a','e','i','o','u']
# word = "sanjanaiuo".lower()


# for each in word:
#     if each in vowels:
#         vowel_count+=1
# print(vowel_count)

# def factorial(n):
#     if n==1:
#         return 1
#     else:
#         return n * factorial(n-1)
# # f = 
# print(factorial(5))

# cprint("Sisan","red")

# lst = [1,3,4]
# def subby1(a):
#     a.append(2)
# subby1(lst)
# print(lst)



# ml = list(range(1,31))
# print(ml[:25])

# ml = [4,4,3,2,1,2]
# print(list(set(ml)))
# print(ml[:0])

# myset = {1,2,3,4,2,1}
# while len(myset):
#     print(myset.pop(), end= "\n")
# print()
# print(len(myset))

# myset.discard(1)
# print(myset)

# def ann():
#     return [1,2]
# print(type(ann()))

# dictionaries = {'a': 'an instrument', 'b' : 'baby elephant'}
# a = dictionaries['a']
# print(a) 

# print(dictionaries.keys())
# print(dictionaries.values())
# print(dictionaries.get('c'))  # while we try to get any keys firstly it checks whether the key exists and returns the respective value otherwise you can just insert an extra arguenmt for getting key.

# di = {'a':'home', 'b': 'school', 'c': 'college'}
# for key,value in di.items():
#     print(key+': '+value)

# li = [1,5,3,6,3,7,"append"]
# li.insert(0,'lame')
# print(li)


# list comprehensions. 
# list = [1,2,3,4,5]
# print([2*item for item in list])

# die = {('a', 'is a guitar'), ('b', 'is a doctor'), ('c', 'is a carpenter')}
# # overall = {item[0]: item[1] for item in die}  # prints the dictionary item from front wards
# overall = {keys: value for keys,value in die} # prints the dictionary items in random order.
# # print(die)
# print(overall)

# print(locals())

# text = '''I am a good man
# this is awesome
# I am going to ithahari International College
# Rajamati kumati'''
# ftext = text.replace('\n', " ")
# print(ftext)
    
# x = (lambda x: x + 2) (3) 
# print(x)

# f = open('HelloWorld.java', 'r')
# for line in f.readlines():
#     print(line.strip())  # strip for reduction of space of the next line

# f = open('myworld.txt', 'w')
# f.write('I am a good boi')
# f.close()

# f = 2
# print("hello " + str(f))

# dic = {'a': 'aeroplane'}
# for i,j in dic.items():
#     print(i , j)
    

# l=[1,2,3,4,5,6,7,8,9]
# nl=[]
# for i in l:
#     if i%2==0:
#         nl.append(i)

# print(nl)
        
# nl=[ i for i in l if i%2==0]
# print(nl)

# import json

# a Python object (dict):
# x = {
#   "name": "John",
#   "age": 30,
#   "city": "New York"
# }

# # convert into JSON:
# y = json.dumps(x)

# # the result is a JSON string:
# print(y)

# x = {'man': ' woman', 'uncle' : 'aunt', 'mother': 'father', 'cars': [{'brand': 'bmw'}, {'model': 'mercedes'}]}
# # for i,j in x.items():
# print(json.dumps(x , indent= 2))

# def mob(sam, man):
#     for i in sam:
#         for j in man:
#             print(i , j)
#     return
# mob(['a','b','c'], [1,2,3])

# some JSON:
# x =  '{ "name":"John", "age":30, "city":"New York"}'

# # parse x:


# # the result is a Python dictionary:
# print(json.loads(x)["age"])

# forjson = '{"name": "Season", "units" : 250}'

# a = json.loads(forjson)
# print(a['units'])

# fj = '{"car": "[{"brand": "pyron"}, {"brand": "adidas"}]"}'  
# m = json.loads(fj["car"])


# jsonData = '{"name": "Frank", "age": 39}'
# jsonToPython = json.loads(jsonData)
# print(jsonToPython)

# import csv
# with open('C:\Users\Eastpoint Computer\Desktop\hmm.csv','rt')as file:
#     csv_rows = csv.reader(file)
#     for row in csv_rows:
#         print(row)

#  code for finding vowels in a word or any sentence.

a = input("a word\n")
word = a.lower()
vowels = ['a','e','i','o','u']
count = 0
for each in word:
    if each in vowels:
        count += 1
if count==1:
    print(f"The word {a} has {count} vowel")
else:
    print(f"The word {a} has {count} vowels")