def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

print("เลือกการดำเนินการ: ")
print("1.บวก")
print("2.ลบ")
print("3.คูณ")
print("4.หาร")

choice = input("ใส่ตัวเลือก(1/2/3/4): ")

num1 = float(input("ใส่ตัวเลขที่ 1: "))
num2 = float(input("ใส่ตัวเลขที่ 2: "))

if choice == '1':
    print(num1, "+", num2, "=", add(num1, num2))

elif choice == '2':
    print(num1, "-", num2, "=", subtract(num1, num2))

elif choice == '3':
    print(num1, "*", num2, "=", multiply(num1, num2))

elif choice == '4':
    print(num1, "/", num2, "=", divide(num1, num2))
else:
    print("ใส่ตัวเลือกที่ถูกต้อง")
#การสร้างเครื่องคิดเลขจะช่วยส่งเสริมความเข้าใจในพื้นฐานและการทำงานวนซ้ำ อย่างต่อเนื่อง จนกระทั่งโปรแกรมทำงานอย่างถูกต้อง

#### 2. โปรแกรมทายคำ (Hangman)

#โปรเจกต์ทายคำนี้เป็นโปรเจกต์ที่ง่ายขึ้นหน่อยแต่มีความท้าทาย เพราะต้องคำนวณทางตรรกะและทำการจัดการกับสตริงส์และข้อมูล


import random

words_list = ['python', 'java', 'kotlin', 'javascript']
word = random.choice(words_list)
guessed = "_" * len(word)
tries = 8

print("H A N G M A N\n")

while tries > 0 and "_" in guessed:
    print(guessed)
    guess = input("Guess a letter: ").lower()

    if guess in word and guess not in guessed:
        guessed = "".join([guess if word[i] == guess else guessed[i] for i in range(len(word))])
    else:
        print("That letter doesn't appear in the word")
        tries -= 1

    print()

if "_" not in guessed:
    print(f"You guessed the word {guessed}!\nYou survived!")
else:
    print("You lost!")
