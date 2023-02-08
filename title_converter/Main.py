from art import logo

print(logo)


def convert_title(first_name, last_name):
    return first_name.title(), last_name.title()


first_name = input("Enter First Name: ")
last_name = input("Enter Last Name: ")
first_name, last_name = convert_title(first_name,last_name)
print(f"{first_name} {last_name}")
