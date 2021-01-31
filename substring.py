#programm to find the substring in a string.

def check_substring(string, sub_string):
    if (string.find(sub_string) == -1):
        print("sub string is not present ")
    else:
        print("sub string is present")


string = input("enter the original string:\n")
sub_string = input("enter the substrig:\n")
print("original string :",string)
print("substring is : ",sub_string)

check_substring(string, sub_string)
