def find_pairs(n):
    pairs = []
    for i in range(1, 20):
        for j in range(i+1, 21):
            if (i + j) % n == 0:
                pairs.append((i, j))
    return pairs
def get_password(n):
    pairs = find_pairs(n)
    password = ''.join(f'{x}{y}' for x, y in pairs)
    return password
n = int(input("Введите число от 3 до 20: "))
result = get_password(n)
print(result)
