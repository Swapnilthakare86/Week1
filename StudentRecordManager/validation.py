# Input Validation
def input_int(val):
    while True:
        try:
            value = int(input(val))
            return value
        except ValueError:
            print("Please enter a number.")


def input_nonempty(val):
    while True:
        value = input(val).strip()
        if value:
            return value
        else:
            print("Input cannot empty")


def check_email(val):
    while True:
        email = input(val)
        if not email:
            print("Emial not empty")
        if "@gmail.com" in email:
            return email
        else:
            print("Enter a valid email.")
