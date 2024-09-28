import random

print('''\n🌟 Welcome to the High-Low Game! 🌟
=========================================
🎮 Rules:
1️⃣ Guess the secret number between 1 and 100.
2️⃣ You will receive hints if your guess is too high or too low.
3️⃣ Type 'h' for higher and 'l' for lower.
4️⃣ Type 'no' to quit or 'yes' to play again. 
-----------------------------------------''')
print('🚀 Let\'s get started!')

def high_low():
    score = 0
    total_rounds = 3

    while True:
        for round in range(1, total_rounds + 1):
            print(f'\n🔄 Round {round}:')                     
            player_number = random.randint(1, 100)
            computer_num = random.randint(1, 100)
            print(f'🤖 Your number is: **{player_number}**')
            print('✨ Now, guess if your number is higher or lower than the computer number!')
            
            x = input('Type "h" for higher or "l" for lower: ').lower()
            if x not in ('h', 'l'):
                print('❌ Invalid input! Please enter "h" or "l" only.')
                x = input('Type "h" for higher or "l" for lower: ').lower()

            elif (x == 'h' and player_number > computer_num) or (x == 'l' and player_number < computer_num):
                print('🎉 Congratulations! You guessed correctly! 🎉')
                score += 1
            else:
                print(f'😢 Oops! You guessed wrong. The computer number was **{computer_num}**.')
        
        print('🌈 Your total score is: **', score, '**')

        again = input('🔄 Do you want to play again? (yes/no): ').lower()
        if  again =='no':
            print('🌟 Thanks you for playing! 🌟')
            print(f'📊 Your final score is: **{score}**.')
            break

high_low()
