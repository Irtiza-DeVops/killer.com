# print("Hello, World!")
# print("irtiza_hassan")
# print("1,2,3,4,5")
# print("Hello \nWorld")
# print("Hello \tWorld")
# print("apple" "banana" "pickle",sep=",")
# print(1,2,3,sep="-")
# print("Hello" , "World")
# print(1,end="")
# print(2)
# print('He said,"Hello!"')
# print("Its name is backslash:\\")
# print("I am 15 years old")
# print("The number is 0.21")
# for i in range(1,6):
#     print(i)

    
# print("lalalala")
import os;
base_path =r'C:\Users\Master Tech\Desktop\a'
num_folder=100
for i in range(1,num_folder+1):
    folder_name =f'Folder_{i}'
    folder_path = os.path.join (base_path,folder_name)
    os.makedirs(folder_path,exist_ok = True)
    print(f'Folder_{i} created')
