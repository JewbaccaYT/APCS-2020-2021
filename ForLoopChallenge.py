num_list = [1, 2, 3, 4, 5]
not_10 = True
# Challenge 1
starting_num = 0
while not_10:
    print(starting_num)
    starting_num += 1
    if starting_num == 11:
        not_10 = False

# Challenge 2
# .join converts list into string with separator
for x in range(5):
  print(" ".join(
      [str(x+1) for x in list(range(x+1))]))

# Challenge 3
user_num = int(input("Choose a number?: "))
loop_running = True
sum_of_all_fears = 0
for x in range(1, user_num + 1):
    sum_of_all_fears += x
print(sum_of_all_fears)
print("   ")

# Challenge 4
for y in range(1, 11):
    print(y * user_num)

# Challenge 5
number_species = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]
for selective_breeding in number_species:
    if selective_breeding > 150:
        break
    if selective_breeding % 5 == 0:
        print(selective_breeding)