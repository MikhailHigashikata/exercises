values = []

for i in range(1000, 3000 + 1):
    i = str(i)
    if int(i[0]) % 2 == 0 and int(i[1]) == 0 % 2 and int(i[2]) % 2 == 0 and int(i[3]) % 2 == 0:
        values.append(i)
        
print(', '.join(values))