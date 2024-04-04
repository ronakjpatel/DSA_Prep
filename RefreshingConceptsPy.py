c = [("ronak",20,"F"),
     ("devansi",50,"P"),
     ("amit",40,"P")]

#this is the method of the list class which only works for list objs. no other iterables
# c.sort()

# print(c)
# #sorting by first index of each tuple
# sorted(c,key=lambda i:i[1])
# print(c)

#enumerate class object returns the index and the value lies on that index.
# for i,n in enumerate(c):
#     print(f"{i} and {n}")
    

# sorted() creates a new sorted list, leaving the original list intact.
# Use reverse=True to sort in descending order.
# Use the key parameter with a custom function to sort based on specific criteria.

#Info about Lexicographical Order or alphabetical order or dictionary order

# "23" < "5" is True because 2 comes before 5 first character but 
# 23 < 5 is false
#
# a,b="23", "2" 
# a,b=23, 5
# a<b

#this will provide some of the useful functions that we can use on iterables
#particularly here i am using cmp_to_key() which essentially convert normal comparison function 
# to the key function that we can give to key= parameter in sorted() function
import functools as ft



def com(a,b):
    if a+b<b+a:
       # -1: This indicates that a should come before b in the sorted list.
        return 1
    else:
        # 1: This indicates that b should come before a in the sorted list. 
        return -1
    

nums = ["0","0","0","0","0"]

for i,n in enumerate(nums):
    nums[i] = str(n)

print(str(int("".join((sorted(nums,key=ft.cmp_to_key(com)))))))

