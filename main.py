My_list = [42, 69, 322, 13, 0, 99, -5, 8, 7, -6, 5]
index = -1
while len(My_list) > index:
    index += 1
    if My_list[index] == 0:
        continue
    elif My_list[index] < 0:
        break
    else:
        print(My_list[index])
        i =+ 1


