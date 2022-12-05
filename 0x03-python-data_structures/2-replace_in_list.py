#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    list_len = len(my_list)
    if idx >= list_len or idx < 0:
        print(my_list)
    else:
        my_list[idx] = element
        return my_list
