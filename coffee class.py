# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    class Coffee:
        def __init__(self, name, intensive, amount, description):
            self.name = name
            self.intensive = intensive
            self.amount = amount
            self.description = description

        def __str__(self):
            return f"{self.name}, {self.intensive}, {self.amount}, {self.description}"
    c1 = Coffee("Ethiopia", 4, 150, "floral & delicate")
    print(c1)

