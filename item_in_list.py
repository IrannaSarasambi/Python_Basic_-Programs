# programm to search an element in list.

def search(element,lst):
    if element in lst :
        print("the element is present in list")
    else:
        print("element is not found ")
def createlist(n,lst):

        for i in range(n):
            item = input("enter list element")
            lst.append(item)

        print("the elements of list are :",lst)



n = int(input("enter the number of elements to be stored in list"))
lst = []
createlist(n ,lst)
element = input("enter the item to searched")
search(element,lst)
