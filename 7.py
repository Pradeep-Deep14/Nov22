def add_one(x):
    return x+1

d={'a':1,'b':2,'c':3}
result = map(add_one,d.values())
print(list(result))

#[2, 3, 4]