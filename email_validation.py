import re


def is_valid_email(email):
    # pattern = r'^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'  # simple regex for email validation

    # more constrains are added to this one
    pattern = r'''^[a-zA-Z_!#$%&'*+/\=?`{|}~^-][a-zA-Z0-9_!#$%&'*+/=?`{|}~^-]*@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'''

    if re.match(pattern, email):
        return True
    else:
        return False


def main():
    email = input("Enter an email address: ")

    if is_valid_email(email):
        print("Valid Email Address")
    else:
        print("Invalid Email Address")


if __name__ == '__main__':
    main()
