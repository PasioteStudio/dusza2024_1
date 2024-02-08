dictionary={
    "elmebajom":{
        "béla":10
    }
}
dictionary2={
    "lajos":10
}
print(dictionary["elmebajom"].update(dictionary2))
print(dictionary)

a=256
b=256
print(a is b)
xd=257**25
c=xd
d=xd

print(c is d)
print(id(c),id(d))

while True:
    num=input("Baszd meg!")
    print(num.isnumeric())