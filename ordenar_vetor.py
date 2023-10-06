lst = [11,18,9,12,23,4,17]
lost = []

for idx in range(len(lst)):
    val = lst[idx]
    if val > 15:
        lost.append(val)
        lst[idx] = 15
        
print('modif: ', lst, "- lost: ",lost)

b = [6, 3, 8, 2, 7, 3, 9]
b.sort()
print(b)

d = ["aaa", "bb", "c","ab", "a"]
d.sort(key=len)
print(d)

def fct(x,y,z):
    res = x,y,z
    return res

def fct1(x,y,z,*args,a=3,b=5,**kwargs):
    return x,y,z

resultado1 = fct(2,3,4)
print(resultado1)

resultado2 = fct1(2,3,4)
print(resultado2)
