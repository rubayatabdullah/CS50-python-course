exp = input('Expresion: ').split()

x = float(exp[0])
z = float(exp[2])
y = exp[1]

match y:
    case '+':
        result = x + z
        print(f'{result:.1f}')
    case '-':
        result = x - z
        print(f'{result:.1f}')
    case '/':
        result = x / z
        print(f'{result:.1f}')
    case '*':
        result = x * z
        print(f'{result:.1f}')
    case _:
        print('invalid')
