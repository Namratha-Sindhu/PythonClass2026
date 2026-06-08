# print("Hello World")

# # Variables in Python : Variables are the container that holds the data 

# text = 'Strength'
# numbers = 19
# decimal_numbers = 78.09
# boolflag = True

# print(text)
# print(numbers)
# print(decimal_numbers)
# print(boolflag)

# # get the datatype of variables

# print(type(text))
# print(type(numbers))
# print(type(decimal_numbers))
# print(type(boolflag))

# #input function and display functions

# numb1 = input("enter the first Number: ")
# numb2 = input("enter the second  Number: ")

# sumnumb = numb1 + numb2
# print(sumnumb)

# numb21 = int(numb1)
# numb22 = float(numb2)

# sumnumb1 = numb21 + numb22
# print(sumnumb1)

# text_1 = "Get the python automation work by today"
# text_2 = "After finishing the python automation carry on the manual testing"

# work = 'python automation' 

# print(f'Get the {work} work by today')
# print(f'After finishing the {work} carry on the manual testing')

# Lists
# --------------------------------------------------------

# Create list

my_list = [9,8,7,6,9,6,4]
print(type(my_list))

# Slice list

print(my_list[3:])
print(my_list[1:6])
print(my_list[-1:])
print(my_list[-1])
print(my_list[1:7:2])
print(my_list[::-1])
print(my_list[3:5])


print(max(my_list))
print(min(my_list))
print(sum(my_list))
print(len(my_list))
my_list.sort()
print(my_list)
my_lista = sorted(my_list)
print(my_list)
my_list.append('cat')
print(my_list)
la = my_list.index(6)
my_list[la] = 'how'
print(my_list)
counta = my_list.count('cat')
print(counta)
my_list.extend(['ten','pens'])
print(my_list)
my_list.reverse()
print(my_list)
my_list.remove('ten')
print(my_list)
listb = my_list.pop(5)
print(listb)
my_list.insert(0,'fun')
print(my_list)


my_listc = my_list
print(my_listc)

copy_list = my_list.copy()
print(copy_list)

my_list.extend(['ox','bull'])
print(my_list)
print(copy_list)

print('ox' not in my_list)

newList = copy_list + my_list
print(newList)

my_list = []
print(my_list)