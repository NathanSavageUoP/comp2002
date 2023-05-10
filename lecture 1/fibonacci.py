#import numpy as np
#import matplotlib.pyplot as plt

def fibonacci(numTarget):
    def fibonacciInner(numTarget, fibList, num1, num2):
        fibNum = num1 + num2
        fibList.append(fibNum)
        if len(fibList) == numTarget:
            return fibList
        else:
            return fibonacciInner(numTarget, fibList, num2, fibNum)
    return fibonacciInner(numTarget, [], 0, 1)

print(fibonacci(100))
"""
changeProp = []
fib = fibonacci(15)
for X in range(1, len(fib)):
    changeProp.append(int((fib[X - 1] / fib[X]) * 1000) / 1000)
X = np.linspace(1, len(changeProp), len(changeProp))

print(changeProp)
print(X)

fig, ax = plt.subplots()
ax.plot(X, changeProp)

fig.show()
"""