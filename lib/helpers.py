# -*- coding: utf-8 -*-

# Helper functions

def return_sublist(main_list, indices ):
    sublist = [[item[i] for i in indices] for item in main_list]
    return sublist