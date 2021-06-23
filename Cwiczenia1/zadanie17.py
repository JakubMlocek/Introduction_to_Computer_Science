a = 2
b = a

dokladnosc = 100
cel = b/a

while(a < dokladnosc):
    #print(b/a)
    a, b = b, a + b
    cel = b/a

print(cel)




