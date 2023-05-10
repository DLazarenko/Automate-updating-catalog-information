def format_address(address_string):
    house = 0
    street = ""

    address = address_string.split(" ")

    # Separate the address string into parts

    # Traverse through the address parts
    for part in address:
        if part.isnumeric():
            house = part
        else:
            street += part + " "
    # Determine if the address part is the
    # house number or part of the street name
    street.lstrip()

    # Return the formatted string
    return "house number {} on street named {}".format(house, street)


print(format_address("123 Main Street"))
# Should print: "house number 123 on street named Main Street"

print(format_address("1001 1st Ave"))
# Should print: "house number 1001 on street named 1st Ave"

print(format_address("55 North Center Drive"))
# Should print "house number 55 on street named North Center Drive"
