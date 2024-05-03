'''Bubble sort'''
# def sort(nums):
#     for i in range(len(nums)-1,0,-1):
#         for j in range(i):
#             if nums[j]>nums[j+1]:
#                 temp=nums[j]
#                 nums[j]=nums[j+1]
#                 nums[j+1]=temp
#
#
#
# nums=[9,4,5,7,1,8,3,6]
# sort(nums)
# print(nums)
#
#
# def sort(nums):
#     for i in range(len(nums)-1):
#         minpos=-1
#         for j in range(i,len(nums)):
#             if nums[j]<nums[minpos]:
#                 minpos=j
#
#         temp=nums[i]
#         nums[i]=nums[minpos]
#         nums[minpos]=temp
#
#         print(nums)
#
# nums=[9,4,5,7,1,8,3,6]
# sort(nums)
# print(nums)

# import pyodbc
# cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
#                       "Server=server_name;"
#                       "Database=db_name;"
#                       "Trusted_Connection=yes;")
#
#
# cursor = cnxn.cursor()
# cursor.execute('SELECT * FROM Table')
#
# for row in cursor:
#     print('row = %r' % (row,))


import pyodbc
cnxn = pyodbc.connect("Driver={SQL Server};"
                      "Server=DESKTOP-RKTKKQC;"
                      "Database=AuthApiDb;"
                      "Trusted_Connection=yes;")


cursor = cnxn.cursor()
cursor.execute('SELECT * FROM Users')

for row in cursor:
    print('row = %r' % (row,))