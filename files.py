import os

# r = Read
# w = Write
# a = Append
# x = Create

# Read - error if the file does not exist
file = open('names.txt', 'r')
content = file.read()
print(content)
file.close() # Close the file after reading

# Append - create the file if it does not exist
file = open('names.txt', 'a')
file.write('\nStephen')
file.close() # Close the file after appending

file = open('names.txt', 'r')
content = file.read()
print(content)
file.close() # Close the file after reading

# Write - create the file if it does not exist, overwrite if it does
file = open('names.txt', 'w')
file.write('John\nDoe\nJane')
file.close() # Close the file after writing

# Two ways to create a file if it does not exist
# Opens a file for writing, creates the file if it does not exist
file = open('names_list.txt', 'w')
file.write('Alice\nBob\nCharlie')
file.close() # Close the file after writing

# Creates a file, raises an error if it already exists
if not os.path.exists('unique_names.txt'):
    file = open('unique_names.txt', 'x')
    file.write('UniqueName1\nUniqueName2')
    file.close() # Close the file after writing
else:
    print('unique_names.txt already exists, cannot create.')

# Delete a file
if os.path.exists('temp_file.txt'):
    os.remove('temp_file.txt')
    print('temp_file.txt has been deleted.')
else:
    print('temp_file.txt does not exist, cannot delete.')


# To use with statement for better file handling
with open('more_names.txt', 'w') as file:
    content = file.read()
    print(content)