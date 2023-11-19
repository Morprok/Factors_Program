# Puts stuff at end and start
def statement_generator(text, decoration):
    ends = decoration * 5

    statement = "{} {} {}".format(ends, text, ends)

    print()
    print(statement)
    print()

    return ""


# displays instructions / information
def instructions():
    pass


# checks input is a number more than  given value
def num_check(question):
    valid = False
    while not valid:

        # lists of errors
        error = f'PLease enter a integer that is more than ' \
                f'(or equal to) 1'

        # ask user for response
        response = input(question).lower()

        # if user types in exit code, return it
        if response == "xxx":
            return response

        try:

            # if we don't get the exit code, make the response into a number
            response = int(response)

            if 1 <= response <= 200:
                return response

            else:
                print(error)
                print()

        except ValueError:
            print(error)


# gets factors, returns a sorted list

def get_factors(to_factor):
    # List to hold factors

    factors_list = []

    # Square root to_factor to find 'half-way'

    limit = int(to_factor ** 0.5)

    # Find factor pairs and add to list

    for item in range(1, limit + 1):

        # Check factor is not 1 (unity)

        if to_factor == 1:
            break

        # Check if number is a factor

        result = to_factor % item

        factor_1 = int(to_factor // item)

        # Add factor to a list if it is not already in there

        if result == 0:
            factors_list.append(item)

        if factor_1 != item and result == 0:
            factors_list.append(factor_1)

    # output

    factors_list.sort()

    return factors_list


# loop to allow multiple calculation per session
keep_going = ""
while keep_going == "":

    comment = ""

    # ask user for number to be factored...
    var_to_factor = num_check("Number? ")

    # to_factor = num_check("What number should I factor? ")
    print(f"You chose {var_to_factor}")
    if var_to_factor == "xxx":
        break

    if var_to_factor != 1:
        factor_list = get_factors(var_to_factor)
    else:
        factor_list = ""
        comment = "One is UNITY! It only has one factor.  Itself :)"

    # comments for squares / primes
    if len(factor_list) == 2:
        comment = f"{var_to_factor} is a prime number.  "
    elif len(factor_list) % 2 == 1:
        comment = f"{var_to_factor} is a perfect square"

    print(factor_list)
