









def outerFunction(text):
    text = text

    def innerFunction():
        print(text)

    return innerFunction

if __name__ == '__main__':
    myFunction = outerFunction('Hey!')
    myFunction()
