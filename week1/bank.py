greetings = input("Greeting: ").strip()

n = greetings[0].lower()
m = greetings[:5].lower()

if n == 'h' and m != 'hello':
    print('$20')
elif m == 'hello':
    print('$0')
else:
    print('$100')