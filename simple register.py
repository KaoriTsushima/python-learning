# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    def myname():
        name = input("What is your name?: ")
        name2 = input("Please type your name again: ")


    print("1. Register your name")
    name = input("What is your name?: ")
    name2 = input("Please type your name again: ")
    if name != name2:
        print("Try again!")
        myname()
    print("Hello", name)
    def password():
        pw = input("Please typr your password: ")
        pw2 = input("Type your password again: ")
    print("2. Register your password")
    pw = input("Please type your password: ")
    pw2 = input("Type your password again: ")
    if pw != pw2:
        print("Try again")
        password()
    print("Well done!")
    print("Do you want to see your password? yes or no")
    answer = input("Please type yes or no: ")
    if answer == 'yes':
        print("You're password is: ", pw)
        print("All set up")
    else:
        print("All set up")


