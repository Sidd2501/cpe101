# Lab 6
# Name: Sid Sharma
# Instructor: S. Einakian
# Section: 06


# String -> bool.
# This function checks to see if an entered string is lower-case or not.
def is_lower_101(user_string):
    for char in user_string:
        if 'A' <= char <= 'Z':
            return False
        else:
            return True


# String -> string.
# This function returns the rot13 encoding for any given character.
def char_rot13(str1):
    answer = ''
    for char in str1:
        rotty = ord(char)
        if ord('a') <= rotty <= ord('z'):
            if rotty > ord('m'):
                rotty -= 13
            else:
                rotty += 13
        elif ord('A') <= rotty <= ord('Z'):
            if rotty > ord('M'):
                rotty -= 13
            else:
                rotty += 13
        answer += chr(rotty)
    return answer
