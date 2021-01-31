#programm to find the frequency of the word in a string.

from collections import Counter

string = input("enter the string: ")
print("the string is: ",str(string))
result = Counter(string.split())
print("word frequency is :",str(dict(result)))
