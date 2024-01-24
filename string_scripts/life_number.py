date = input("Input date of birth (in any format): ")
date = date.strip('/').strip()

inter_number = 0
life_number = 0

for char in date:
    inter_number += int(char)

life_number = inter_number

while life_number > 9:
    life_number = 0
    for number in str(inter_number):
        life_number += int(number)

print(life_number)