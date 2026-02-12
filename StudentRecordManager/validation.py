# Input Validation
def input_int(val):
    while True:
        try:
            value = int(input(val))
            return value
        except ValueError:
            print("Invalid input! Please enter a number.")


def input_nonempty(val):
    while True:
        value = input(val).strip()
        if value:
            return value
        else:
            print("Input cannot empty")

