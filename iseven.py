print("hello, world")

def isEven(value):
    binary_str = bin(value)
    return binary_str[len(binary_str)-1] != "1"
print(isEven(5))