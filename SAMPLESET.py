#1. Creating Sets
# Creating a set
set1 = {1, 2, 3, 4, 5}
set2 = set([3, 4, 5, 6, 7])  # Using the set() function with a list

print("Set 1:", set1)
print("Set 2:", set2)
#2. Adding and Removing Elements
# Adding elements
set1.add(6)
print("After adding 6 to Set 1:", set1)

# Removing elements
set1.remove(2)  # Removes element 2
print("After removing 2 from Set 1:", set1)

# Discarding an element (no error if element is not found)
set1.discard(10)  # No error if 10 is not in the set
print("After discarding 10 from Set 1:", set1)

# Clearing all elements
set2.clear()
print("After clearing Set 2:", set2)
#3. Union of Sets
#3Union combines all unique elements from both sets.

set_a = {1, 2, 3}
set_b = {3, 4, 5}

# Using the union() method
union_set = set_a.union(set_b)
print("Union using union() method:", union_set)

# Using the | operator
union_set_operator = set_a | set_b
print("Union using | operator:", union_set_operator)
#4. Intersection of Sets
#Intersection finds common elements in both sets.


# Using the intersection() method
intersection_set = set_a.intersection(set_b)
print("Intersection using intersection() method:", intersection_set)

# Using the & operator
intersection_set_operator = set_a & set_b
print("Intersection using & operator:", intersection_set_operator)
#5. Difference of Sets
#Difference finds elements that are in one set but not in the other.



# Difference of set_a from set_b (elements in set_a but not in set_b)
difference_set = set_a.difference(set_b)
print("Difference of Set A from Set B:", difference_set)

# Difference of set_b from set_a (elements in set_b but not in set_a)
difference_set_b_a = set_b - set_a
print("Difference of Set B from Set A:", difference_set_b_a)
#6. Symmetric Difference of Sets
#Symmetric difference finds elements that are in either set, but not in both.


# Using the symmetric_difference() method
symmetric_diff = set_a.symmetric_difference(set_b)
print("Symmetric Difference using symmetric_difference() method:", symmetric_diff)

# Using the ^ operator
symmetric_diff_operator = set_a ^ set_b
print("Symmetric Difference using ^ operator:", symmetric_diff_operator)
#7. Subset and Superset Checks

# Checking if set_a is a subset of set_b
print("Is Set A a subset of Set B?", set_a.issubset(set_b))

# Checking if set_b is a superset of set_a
print("Is Set B a superset of Set A?", set_b.issuperset(set_a))

# Checking if two sets are disjoint (no elements in common)
set_c = {7, 8, 9}
print("Are Set A and Set C disjoint?", set_a.isdisjoint(set_c))
#8. Frozen Sets (Immutable Sets)
#A frozenset is an immutable version of a set and can be useful when you need a hashable set (e.g., as a key in a dictionary).


# Creating a frozenset
frozen_set = frozenset([1, 2, 3, 4])
print("Frozen Set:", frozen_set)

# Attempting to add or remove elements will raise an error
try:
    frozen_set.add(5)
except AttributeError as e:
    print("Error:", e)
#9. Using Sets to Remove Duplicates from a List
#Sets automatically remove duplicate items, so you can use them to clean up a list.


my_list = [1, 2, 2, 3, 4, 4, 5]
unique_elements = set(my_list)
print("Unique elements from list:", unique_elements)

# Converting back to a list if needed
unique_list = list(unique_elements)
print("List of unique elements:", unique_list)
#10. Finding Common Elements in Multiple Sets

set_x = {1, 2, 3, 4, 5}
set_y = {3, 4, 5, 6, 7}
set_z = {5, 6, 7, 8, 9}

# Finding common elements in all sets
common_elements = set_x & set_y & set_z
print("Common elements in Set X, Set Y, and Set Z:", common_elements)
#11. Removing Specific Items if They Exist

set_m = {10, 20, 30, 40}

# Remove element if it exists, otherwise do nothing
element_to_remove = 30
if element_to_remove in set_m:
    set_m.remove(element_to_remove)
    print(f"Removed {element_to_remove} from Set M:", set_m)
else:
    print(f"{element_to_remove} not found in Set M.")
#12. Iterating Through a Set


# Iterating through elements of a set
set_n = {"apple", "banana", "cherry"}
print("Items in Set N:")
for item in set_n:
    print(item)


