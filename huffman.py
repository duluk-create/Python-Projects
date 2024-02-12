eingabe = "wir lieben erdbeeren"
values = {}
combined = {}

for x in eingabe:
    if(values.__contains__(x)):
       values[x] = values[x] + 1
    else:
        values[x] = 1
        combined[x] = ""


min1 = 99
key1 = "-1"
min2 = 99
key2 = "-1"

size = 0;

while(size < len(eingabe)):
    for c in values:
        if(values[c] < min1):
            min1 = values[c]
            key1 = c

    for d in values:
        if values[d] < min2  and d != key1:
            min2 = values[d]
            key2 = d

    size = min2 + min1
    values.pop(key1)
    values.pop(key2)
    values[key1 + key2] = size;



    for k in key1 + key2:
        if(key1.__contains__(k)):
            combined[k] = combined[k] + "0"
        else:
            combined[k] = combined[k] + "1"

    min1 = 99
    min2 = 99


for k in combined:
    print(k + " hat den Code: " + combined[k])
