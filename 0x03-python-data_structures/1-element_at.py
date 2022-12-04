#!/usr/bin/python3
def element_at(my_list, idx):
    list_len = len(my_list)
    if idx > list_len and idx < 0:
        return None
    else:
        return my_list[idx]
