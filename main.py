# files = ["memories.mp4","moneyheist.mp4","joker.mp4"]
# for x in files:
#
#     print(x[0:-4])

# ------------------
# multiplication table
# for i in range(1,11):
#     for j in range(1,11):
#         print(i, "X", j, "=", i * j)


# ------------------------------
# greatest of 2 numbers
# a=int(input())
# b=int(input())
# if a>b:
#     print(a,"is greater")
# else:
#     print(b,"is greater")


# ---------------------------
# greatest of 3 numbers
# a=int(input())
# b=int(input())
# c=int(input())
# if a>b:
#     if a>c:
#         print(a,"is greater")
#     else:
#         print(c,"is greater")
# else:
#     if b>c:
#         print(b,"is greater")
#     else:
#         print(c,'is greater')

# ----------------------------------

# simple calculator
# a=int(input("enter 2 numbers"))
# b=int(input())
# print("1.addition\n2.nsubtraction\n3.multiplication\n4.division")
# choice=int(input("enter your choice"))
# if 1<=choice<=4:
#     if choice==1:
#         result=a+b
#         print("result is", result)
#     elif choice==2:
#         result=a-b
#         print("result is", result)
#     elif choice==3:
#         result=a*b
#         print("result is", result)
#     elif choice==4:
#         result=a/b
#         print("result is", result)
# else:
#     print("you are a fool")

# ----------------------------------------

'''
write a program to solve a classic ancient chinese puzzle:
we count 35 heads and 94 legs among the chickens and rabbits in a farm.
how many rabbits and how many chickens do we have?
'''

for i in range(1,35):
        j=35-i
        if i*2+j*4 == 94:
                print("chicken",i)
                print("rabbit",j)

























