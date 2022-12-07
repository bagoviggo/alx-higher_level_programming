#!/usr/bin/python3
<<<<<<< HEAD
def search_replace(my_list, search, replace):
    def s_r_elm(elm):
        return (elm if elm != search else replace)
    return list(map(s_r_elm, my_list))
=======
"""function that replaces all occurrences of an element
by another in a new list."""


def search_replace(my_list, search, replace):
    if search in my_list:
        return [replace if x == search else x for x in my_list]
>>>>>>> 8fbd36a8cdc4795d78bc52edc95f81af97aa7a46
