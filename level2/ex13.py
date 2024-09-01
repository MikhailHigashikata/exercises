s = input()
values = {"alfa":0,"num":0}

for c in s:
    if c.isdigit():
        values['num'] += 1
        
    elif c.isalpha():
        values['alfa'] += 1
        
print(values)