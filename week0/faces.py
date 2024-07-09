def convert(text):
    text = text.replace(':)', '🙂').replace(':(', '🙁')
    print(text)

def main():
    text = input('Enter some text with text emoji: ')
    convert(text)


main()



    