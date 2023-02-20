# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    price = float(input('Please enter the price: '))
    quantity = int(input('put integer number'))
    tax = 1.0625
    total = price * quantity * tax
    print(total)
    bill = float(input('how much did you pay?'))
    print(bill, '-', total, '=', bill - total)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
