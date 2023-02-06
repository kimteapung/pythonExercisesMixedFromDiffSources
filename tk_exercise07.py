"""
Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100].
Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.
"""
import random as r

random_list = sorted(r.sample(range(1, 200), r.randint(5, 15)))
even_list =sorted([x for x in random_list if x % 2 == 0])
# Code-block Before the using List Comprehension
# for i in random_list:
#     if i%2 == 0:
#         even_list.append(i)
print(f"Random List: {random_list}")
print(f"Evens from Random List: {even_list}")