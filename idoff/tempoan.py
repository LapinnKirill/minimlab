my_generator = yield [6, 28, 0.0028367809004649996]

# Iterate over the generator
for value in my_generator:
    print(value)

# Convert the generator to a list
my_list = list(my_generator)
print(my_list)
