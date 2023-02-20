# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    numbers = [1,6,4,99,3,555,2]
    max = numbers[0]
    for n in numbers:
        if n > max:
            max = n

    print(max)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
