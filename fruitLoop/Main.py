# For loops with a list:
# fruits = ["Apple", "Banana", "Mango", "Papaya"]
# for fruit in fruits:
#     print(fruit)
#     print(f"{fruit} Pie")

# For loops with range: default increase is one
# for number in range(1, 10):
#     print(number)


# For loops with range: default increase is number provided third argument
# for number in range(1, 10, 2):
#     print(number)

# adding numbers using for loop:
# total_sum = 0
# for number in range(1, 101):
#     total_sum += number
# print(f"Sum is : {total_sum}")

# Sum of all the even numbers from 1 - 100:
even_sum = 0
for num in range(1, 101):
    if num % 2 == 0:
        even_sum += num
print(f"Sum of all even numbers is : {even_sum}")
