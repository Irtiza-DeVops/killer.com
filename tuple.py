# tuple is defined as ;"A tuple looks just like a list, except you use parentheses instead of square brackets"
# it is not changeable means immutable
# we can do indexing
# name:tuple=("irtiza","uzair_bhai","amir_bhai")
# print(name{0})
# we cant use in built functions
# assigning multiple datatype
num :tuple[int|str,...]=(1,2,3,"irtiza","hassan")
# finding type
print(type(num))
print(num)
num1:tuple[int|str|float,...]=(1,2,3.6,"irtiza","hassan")
print(num1)
# making one item tuple
num2 :tuple=("irtiza",)
print(num2)
print(type(num2))
# not a tuple without ,
# num3 :str=("irtiza")
# Type constructor:
# ~it uses as function when we use it to convert list to tuple
# list1:list =[1,2,3,4]
# type_constructor=list1(tuple)
# print(type_constructor)
# ~else it use as variable



