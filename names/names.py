import time
from binary_search_tree import BSTNode

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

"""
# Replace the nested for loops below with your improvements
for name_1 in names_1:
    for name_2 in names_2:
        if name_1 == name_2:
            duplicates.append(name_1)

The runtime was:
10.852504014968872 seconds
"""

# Create a BST for names_1 
bst_1 = BSTNode(names_1[0])

# For range from the second item in names_1 till the rest of it's length
for i in range(1, len(names_1)):
    # Add every other item to bst_1
    bst_1.insert(names_1[i])

# For range from 0 till the end og names_2
for i in range(0, len(names_2)):
    # Compare items in bst_1 to names_2
    # If bst contains the name in index i
    if bst_1.contains(names_2[i]):
        # Store that name in duplicates
        duplicates.append(names_2[i])





end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")



# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
