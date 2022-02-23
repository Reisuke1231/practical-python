# bounce.py
#
# Exercise 1.5
count = 0
DROP_HEIGHT = 100

bounce_height = DROP_HEIGHT
while count < 10:
    bounce_height = bounce_height * (3/5)
    print(f'{count+1}: {round(bounce_height, 4)}')

    count += 1
