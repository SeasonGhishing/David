# def func():
#     try:
#         l = {1,2,5,3,2,4}
#         l.pop(2)
#         print(l)
#         return 1
#     except:
#         print("mistake chha")
#         return 0
#     finally:
#         print("malai kasle rok chha?")
    
# a = func()
# print(a)


# raise IndexError("eror")

# alist = [-1,-2,-3,-7,0,1,2,3,94,50]
# total_sum = 0
# count = 0
# for i in alist:
#     if i<0:
#         count += 1
#     elif i>0:
#         total_sum += i
# print(f"The total numbers in the list are {len(alist)}")
# print("There are {} negative numbers".format(count))
# print("Sum of the positive numbers are {}".format(total_sum))

# i = input("Enter a number greater than 5 and less than nine: ")

# if i=="quit".lower():
#     print("lets quit together")
# else:    
#     try:
#         enw = int(i)
#         if (enw>5 and enw<9):
#             print(enw)
#         else:
#             raise ValueError("Should be greater than 5 and less than 9")
#     except:
#         print("no way")


# def multiply(a=5):
#     i = 1
#     while i<=10:
#         print(f"{a} X {i} = {a*i}")
#         i+=1
#     print()
# multiply(6)

# print( lis[5][1][1][0])
        
# lis = [2,6,8,"sisan","chuck",("bro",("hyper",["psych"]))]


# roll,rick,age,name,tutor,pack = lis
# bro, (hyper, [psych]) = pack
# print(psych)

# dic = {"fish" : {["Redmi", "adidas",True] , ["earson", False, "dawson"]}, "gun" : "ak47"}

# dic = {"fish": ([ "Redmi", "adidas", True], ["earson", False, "dawson"]), "gun": "ak47"}




# lis = {1 : {"game", "name", ["bhai", "behen"]},  2 : "mst"}
# # print(lis[1])
# # lis.pop(2)
# for key, values in lis.items():
#     for i in values:
#         for j in i:
#             print(key, j)


# p = {"Redmi", "adidas"}

# redmi, adidas = p
# print("Redmi is: ",redmi)
# print("Adidas is: ", adidas)
    
# Redmi

pw = "Adidas1312"
a = len(pw[0:-5])
b = "*" * a
print(b + pw[a:]) 
# print(pw[-5:])






    
    