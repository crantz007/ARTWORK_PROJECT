

# ensures the price is a positive float
def input_positive_float(question):
    while True:
        try:
            number = float(input(question))
            if number < 0:
                print("Enter a positive number")
            else:
                return number
        except ValueError as e:
            print("Oops ! numbers are required.")

# returns 1 for yes, 0 for not available to check the artwork availability
def input_yes_or_no(question):
    yesAvailable = 'yes'
    noUnavailable = 'no'
    while True:
        available = input(question)
        if available.lower() == yesAvailable:
            return 1
        elif available == noUnavailable:
            return 0
        else:
            print("Please enter yes or no for choice: ")