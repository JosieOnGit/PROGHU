
def new_password(oldpassword, newpassword):
    contains_digit = False
    for character in newpassword:
        if character.isdigit():
            contains_digit = True
    if newpassword != oldpassword and len(newpassword) >= 6 and contains_digit:
        print("Your password was successfully changed.")
        return True

    else:
        print("Your password was not changed. \n"
              "Password must contain the following: \n"
              "Must contain at least 6 characters; \n"
              "Cannot be the same as your old password. \n"
              "Must contain at least 1 number.")
        return False


oldpassword = input("Please fill in your current password: ")
newpassword = input("Please fill in a new password: ")
new_password(oldpassword, newpassword)
