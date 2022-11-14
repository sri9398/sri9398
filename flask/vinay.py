# a=int(input('enter a value'))
# b=int(input('enter b value'))
# c=int(input('enter c value'))
# if a>b and a>c:
#     print('a is maximum')
# elif b>c:
#     print('b is maximum')
# # else:
# #     print('c is maximum')
# for i in range (1,6):
#     for j in range(1,6):
#         print(i,j)
#         if j==3:
# #             break
# for i in range (1,6):
#     for j in range (1,6):
#         print(i,j)
#         if i==3:
#             break
# for i in range (1,6):
#     for j in range (1,6):
#         print(i,j)
#     if i==3:
#         break
#         for i in range (1,6):
#             if i==3:
#                 break
#             for j in range (1,6):
# #                 print(i,j)
# for i in range (1,6):
#     if j==3:
#         break
#     for j in range (1,6):
# #         print(i,j)
# for i in range (1,6):
#     for j in range (1,6):
#         print(i,j)
#     if j==3:
#         break
#Read user inp
# #Read user input
# min = int(input("Enter the min : "))
# max = int(input("Enter the max : "))
#
# for n in range(min,max + 1):
#    if n > 1:
#        for i in range(2,n):
#            if (n % i) == 0:
#                break
#        else:
#            print(n)
#
# for i in range(1001,1021):
#     for j in range(2, i):
#         if i % j == 0:
#             break
#         else:
#             print(i)
# #             break
# start = int(input("Enter the starting number of the range"))
# end = int(input("Enter the ending number of the range"))
#
# for n in range(start, end + 1):
#     sum = 0
#
#     for i in range(1, n):
#         if n % i == 0:
#             sum += i
#     # print(n, sum)
#
#     if n == sum:
#         print(n)
#
n=int (input('Enter number:'))
s=''
for i in range(0,10):
    if i>1:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            s+=str(i)
            print(s[n:n+8])




