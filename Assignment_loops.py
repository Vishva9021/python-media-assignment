# 1. Print number from 1 to 5 ing a while loop
count = 1
while count <=5:
    print(count)
    count +=1

# 2. Calculate the sum of number from 1 to 10 ing a while loop
num = 15
sum = 0
while num > 0:
    sum += num
    num -= 1
print("The sum is", sum)

# 3. Calculate the factorial of a number using a for loop

n = int(input("Enter a number: "))
factorial = 1
if n >= 1:
    for i in range (1, n+1):
        factorial=factorial *i
print("Factorial of the given number is: ", factorial)

# 4. Count the number of vowel in a string using a for loop
def vowel_count(str):
    count = 0
    vowel = set("ASW")
    for alphabet in str:
        if alphabet in vowel:
            count = count + 1
    print("No. of vowels :", count)
str = "Assingment"
vowel_count(str)

# 5.Print a pattern ing nested loop.
for i in range(1,6):
  for j in range(i):
    print('*',end='')
  print('')

# 6. Generate a multiplication table using nested loop.
table_size = 10
print(" ", end="")
for i in range(1, table_size + 1):
    print(f"{i:4}", end="")
print("\n" + "-" * (table_size * 4 + 4))
for i in range(1, table_size + 1):
    print(f"{i:2} |", end="")
    for j in range(1, table_size + 1):
        print(f"{i * j:4}", end="")
    print()