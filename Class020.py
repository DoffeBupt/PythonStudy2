def funX():
    x = 5
    def funY():
        nonlocal x
        x += 1
        return x
    return funY

print(funX()())
print(funX()())
print(funX()())

a = funX()
print(a())
print(a())
print(a())