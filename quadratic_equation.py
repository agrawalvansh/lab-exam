import matplotlib.pyplot as plt
x_values = []
y_values = []
with open('FourthVersionData.txt', 'r') as file:
    for _ in range(40):
        try:
            a = float(file.readline().split('=')[1])
            b = float(file.readline().split('=')[1])
            c = float(file.readline().split('=')[1])
            x = float(file.readline().split('=')[1])
            y = a*x*x+b*x+c
            x_values.append(x)
            y_values.append(y)
        except (IndexError, ValueError):
            print("Error reading a line. Check your data format.")
            break
plt.plot(x_values, y_values, marker='o', linestyle='-', color='b')
plt.title('Graph of y = ax^2 + bx + c')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()