# # # # # #Exception handling
# # # # # #try exception else finally
# # # # # a=int(input("Enter value for a:"))
# # # # # b=int(input("Enter value for b:"))
# # # # # try:
# # # # #     c=a/b
# # # # #     print(c)
# # # # # except:
# # # # #     print('Exception raised..')
# # # # # else:
# # # # #     print("No exception..")
# # # # # finally:
# # # # #     print("Program ends...")

# # # # #handle single exception
# # # # a=int(input("Enter the value for a:"))
# # # # b=int(input("Enter the value for b:"))
# # # # list=[1,2,3,4]
# # # # try:
# # # #     c=a/b
# # # #     print(c)
# # # #     print(list[5])
# # # # except IndexError:
# # # #     print("Error raised")


# # # #Multiple exception handling
# # # #using mulriple exception block
# # # a=int(input("Enter value for a:"))
# # # b=int(input("enter value for b:"))
# # # list=[1,2,3,4,5]
# # # try:

# # #     c=a/b
# # #     print(c)
# # #     print(list[4])
# # #     str='hello'+20
# # # except ZeroDivisionError:
# # #     print("Zero division error raised")
# # # except IndexError:
# # #     print('index error raised')
# # # except:
# # #     print("Error raised")

# # #single exception block
# # a=int(input("Enter value for a:"))
# # b=int(input("enter value for b:"))
# # list=[1,2,3,4,5]
# # try:
# #     c=a/b
# #     print(c)
# #     print(list[5])
# # except (ZeroDivisionError,IndexError):
# #     print('Error raised..')


# #Exception raised
# a=int(input("enter the value for a:"))
# b=int(input("Enter the value for b:"))
# try:
#     if b==0:
#         raise Exception("Exception raised..")
#     c=a/b
#     print(c)
# except Exception as e:
#     print(e)

#user defined exception
class InvalidData(Exception):
    pass
marks=int(input("enter your mark:"))
try:
    if marks<0 or marks>100:
        raise InvalidData
    print("marks=",marks)
except InvalidData:
    print("marks should be in between 0 and 100")
