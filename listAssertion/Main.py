
my_array = ['square', 'triangle', 'rectangle']
my_array_pointer = my_array

print(my_array)
print(my_array_pointer)

my_array.append('circle')

# This proved it does not create a copy with = sign only
# points to the same list
print(my_array)
print(my_array_pointer)

my_array_pointer.append('point')

print(my_array)
print(my_array_pointer)
