#!/usr/bin/python3
"""
This module describes an inherited class
The inherited classes behaves like original class
The classes have few modifications
That is all i can think of jare
Below are the modules and classes
"""


class MyList(list):
    """
    Remember when I said we are inheriting classes
    List is the first of them
    New modification is sorting the Lists
    Here we go.
    """

    def print_sorted(self):
        """
        Now we have the extra sorted of the list.
        The list will be returned not printed
        This is to avoid Nonr being returned
        """
        print(sorted(self))
