items = input().split()
values = []

for i in items:  
    if not int(i,2) % 5:
        values.append(i)
        
print(','.join(values))