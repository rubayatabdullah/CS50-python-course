def main():
    time = input('What time is it now? ').strip()
    if 7.0 <= convert(time) <= 8.0:
        print('Breakfast time')
    elif 12.0 <= convert(time) <= 13.0:
        print('Lunch time')
    elif 18.0 <= convert(time) <= 19.0:
        print('Dinner time')
    else:
        return
    

def convert(time):
    x, y = time.split(":")
    hr = float(x)
    mins = float(y)* 1/60
    return float(hr + mins)

if __name__ == '__main__':
    main()
