#взаимные циклы
max_len = 0
answer = 0
for d in range(2, 1000):
    remainder = 1
    remainders = []

    while remainder != 0:
        remainder = (remainder * 10) % d
        if remainder in remainders:
            length = len(remainders) - remainders.index(remainder)
            if length > max_len:
                max_len = length
                answer = d
            break
        remainders.append(remainder)
print(answer)
