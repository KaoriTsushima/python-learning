# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    limit = int(input("please enter a number: "))
    for n in range(2, limit + 1):
        isPrime = True
        for x in range(2, n):
            if n % x == 0:
                isPrime = False
                break
        if isPrime:
            print(n)






# See PyCharm help at https://www.jetbrains.com/help/pycharm/
