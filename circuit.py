from math import ceil

def circuit_resistance(*resistors, connection='serial'):
    if connection == 'serial':
        return sum(resistors)
    elif connection == 'parallel':
        s = sum(map(lambda x: 1 / x, resistors))
        return 1 / s
    else:
        raise ValueError("Bad connection type")


data = [10, 20, 30]
z = circuit_resistance(*data, connection='serial')
f = z - ceil(z)

if f == 0:
    print(z)
else:
    print("%.4f" % z)