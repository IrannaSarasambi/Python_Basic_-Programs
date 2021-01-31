#programm to check the given string is palindrome or not.

def check_palindrome(string):
    str2 = string[::-1]
    print("reversed string is : ",str2)
    if string == str2:
        print("given string is palindrome")
    else:
        print("given string is not palindrome")


string = input("enter the string to be checked: ")
check_palindrome(string)
