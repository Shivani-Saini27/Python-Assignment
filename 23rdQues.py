def outerF(a, b):
    def innerF(a, b):
        return a + b
    add = innerF(a, b)
    return add + 5

result = outerF(20, 30)
print(result)
