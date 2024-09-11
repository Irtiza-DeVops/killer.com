friend_name:str =str(input('enter your respected name : '))
num_list =[]
print(f"\n~~Hello !\n ~~ {friend_name}! lets explore your favourite number.Lets gooo!!")

for i in range(1,4):
    num:int=int(input(f"Enter your {i} favourite number:"))
    num_list.append(num)
fav_num=(f'\nThe list of your favourite number is {num_list}')
print(fav_num)
print('\n~~Lets,explore whether your favourite numbers is even or odd.Lets gooooooo!!')
for y in num_list:
    if y % 2 ==0 :
        print(f"your favourite number {y} is even.Thats great")
    else:
                print(f"your favourite number {y} is odd.Thats great")


print('\n~~Now,lets explore the square of your favourite numbers.Lets gooooooo!!' )

for x in num_list:
      print(f"Your  favourite number is {x} and its square is : ({x},{x ** 2})")
print('\n~~Its time to check the sum of your favourite number.Lets gooo!')
sum:int=sum(num_list)
print(f'~~WOW, the total sum of your favourite number is "{sum}",which is your lucky number')
print(f"\n~~Now,Lets check whether your number ia prime number or not ")
prime=True
if sum <=1:
      prime=False
      for x in range (2,sum):
            
            if sum % 2 ==0:
              prime =False
if prime:
      print(f"\nAmazing!!.The sum of your favourite number is {sum},which is a prime number")
else:
            print(f'''\nOh noo!!.The sum of your favourite number is {sum},which is not a prime number.
                  ~~~Better Luck next time :)''')           
print('''\n~~I hope that you had fun while exploring my programme.
# ~~Have a nice day
# ~~Good Bye      ''')






      
      


