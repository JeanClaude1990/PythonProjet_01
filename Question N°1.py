pre = 2000
dem = 3200
for i in range(pre,dem):
    if not i%5 == 0 and i%7 == 0:
        print(i)