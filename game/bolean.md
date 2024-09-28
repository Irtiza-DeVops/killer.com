Here is the `.md` (Markdown) file that explains the steps and code:

# 🌟 High-Low Game: Step-by-Step Explanation 🌟

This Python code implements a simple "High-Low Game" where the player guesses whether their randomly generated number is higher or lower than the computer's number. Let's break down the code step by step!




## 🧩 Step-by-Step Explanation:

### 1️⃣ **Import the `random` module**:
```python
import random
```
- The game needs to generate random numbers, and the `random` module helps us generate a number between 1 and 100 for both the player and the computer.

---

### 2️⃣ **Introduction and Game Rules**:
```python
print('''\n🌟 Welcome to the High-Low Game! 🌟
=========================================
🎮 Rules:
1️⃣ Guess the secret number between 1 and 100.
2️⃣ You will receive hints if your guess is too high or too low.
3️⃣ Type 'h' for higher and 'l' for lower.
4️⃣ Type 'no' to quit or 'yes' to play again. 
-----------------------------------------''')
```
- This part prints a welcome message and explains the rules of the game to the user in a simple and engaging format.

---

### 3️⃣ **Define the Game Logic**:
```python
def high_low():
    score = 0
    total_rounds = 3
```
- **`high_low()`**: The main function of the game.
- **`score`**: Keeps track of the player's correct guesses.
- **`total_rounds`**: Sets the number of rounds in the game.

---

### 4️⃣ **Game Loop: For Each Round**:
```python
while True:
    for round in range(1, total_rounds + 1):
        print(f'\n🔄 Round {round}:')
```
- The game runs in an infinite loop, allowing the player to play multiple rounds. 
- For each round, the number of the round is displayed, and the loop continues until the player chooses to quit.

---

### 5️⃣ **Generate Random Numbers**:
```python
player_number = random.randint(1, 100)
computer_num = random.randint(1, 100)
```
- The game generates two random numbers: one for the player and one for the computer.
- **`random.randint(1, 100)`** gives a random number between 1 and 100.

---

### 6️⃣ **Player Makes a Guess**:
```python
x = input('Type "h" for higher or "l" for lower: ').lower()
```
- The player is asked to guess whether their number is higher or lower than the computer’s.
- **`input()`** takes the user's guess, and **`.lower()`** ensures the input is case-insensitive.

---

### 7️⃣ **Check Guess Validity**:
```python
if x not in ('h', 'l'):
    print('❌ Invalid input! Please enter "h" or "l" only.')
```
- If the user enters anything other than 'h' or 'l', the program prompts for valid input again.

---

### 8️⃣ **Check If the Guess is Correct**:
```python
elif (x == 'h' and player_number > computer_num) or (x == 'l' and player_number < computer_num):
    print('🎉 Congratulations! You guessed correctly! 🎉')
    score += 1
```
- If the player guessed correctly (e.g., guessed higher and the player's number is indeed higher), a congratulatory message is shown, and the score is increased.

---

### 9️⃣ **Wrong Guess**:
```python
else:
    print(f'😢 Oops! You guessed wrong. The computer number was **{computer_num}**.')
```
- If the player's guess is incorrect, the correct computer number is shown, and the round ends.

---

### 🔟 **Display Total Score and Replay Option**:
```python
again = input('🔄 Do you want to play again? (yes/no): ').lower()
if again != 'yes':
    print('🌟 Thank you for playing! 🌟')
    print(f'📊 Your final score is: **{score}**.')
    break
```
- After 3 rounds, the player's total score is displayed.
- The player can choose to play again or exit the game.

---

## 🏆 Summary:
The game provides a fun and engaging way for the player to guess whether a random number is higher or lower than the computer's number, with scoring and the option to replay.


