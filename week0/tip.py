def main():
    dollars = dollars_to_float(input('How much was the meal? '))
    percent = percent_to_float(input('What percentage would you like to tip?'))

    tip = dollars*percent

    print(f'Leave ${tip:.2f}')

def dollars_to_float(d):
    i = float(d.strip().replace("$", ""))
    return i

def percent_to_float(p):
    i = float(p.strip().replace("%", ""))/100.0
    return i
    
main()
