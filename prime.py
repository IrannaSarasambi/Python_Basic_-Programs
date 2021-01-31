#programm to print the prime numbers between given range if value.

start = int(input("enter the starting number of the range : "))
end = int(input("enter the end number of the range : "))

print("start = {0} and end = {1}" .format(start, end))

for i in range(start, end):
    if i>1:
        for j in range(2, i):
            if (i % j == 0):
                break
        else:
             print(i)
