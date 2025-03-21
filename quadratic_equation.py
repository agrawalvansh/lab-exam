with open('ThirdVersionData.txt', 'r') as file:
    a = float(file.readline())
    b = float(file.readline())
    c = float(file.readline())
    x = float(file.readline())
y = a*x*x+b*x+c
print('The value of y is:', y)