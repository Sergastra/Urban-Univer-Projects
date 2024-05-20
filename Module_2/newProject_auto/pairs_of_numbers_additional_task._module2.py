def password(num_):
    pas_ = ""
    for i in range(1, int(num_)):
        for j in range(i + 1, int(num_)):
            if int(num_) % (i + j) == 0:
                pas_ += str(i) + str(j)
    return pas_


num = input("Введите число от 3 до 20:")
if 3 <= int(num) <= 20:
    print(f'Код для чиcла {num}:', password(num))
else:
    print('Введите число от 3 до 20 !!!')
