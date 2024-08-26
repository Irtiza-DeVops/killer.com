# asking friend name
name =str(input('enter your respected name : '))
# Asking friend ror their three favourite number
fav_1 =int(input('enter your first favourite number :'))
fav_2=int(input('enter your second favourite number :'))
fav_3 =int(input('enter your third favourite number :'))


print(f"~~Hello {name}! lets explore your favourite numbers")

# if fav_1 % 2== 0:
#     print("your number is even")
# elif fav_2 % 2== 0:
#     print("your number is even")
# elif fav_3 % 2== 0:
#     print("your number is even")
# else :
#      print("your number is odd")
print('~~Lets,explore whether your favourite numbers is even or odd.Lets gooooooo!!')
print(f"your first favourite number is {fav_1} which is an  {'even number' if fav_1 % 2 == 0 else 'odd number' }")
print(f"your second favourite number is {fav_2} which is an {'even number' if fav_2 % 2 == 0 else 'odd number' } ")
print(f"your third favourite number is {fav_3} which is an {'even number' if fav_3 % 2 == 0 else 'odd number' } ")
print('~~Now,lets explore the square of your favourite numbers.Lets gooooooo!!' )
print(f"your first favourite number is {fav_1} and its square is : ({fav_1},{fav_1 ** 2})")
print(f"your second favourite number is {fav_2} and its square is : ({fav_2},{fav_2 ** 2})")
print(f"your third favourite number is {fav_3} and its square is : ({fav_3},{fav_3 ** 2})")
print('~~Its time to check the sum of your favourite number.Lets gooo!')
sum= fav_1 + fav_2 + fav_3
# message='''Wow! the total sum of your favourite numbers is {sum} which is a whole number
#  Thats Amazing '''
# print(message)
print(f'~~WOW, the total sum of your favourite number is "{sum}" which is your lucky number')
print('''~~I hope that you had fun while exploring my programme.
~~Have a nice day
~~Good Bye      ''')






