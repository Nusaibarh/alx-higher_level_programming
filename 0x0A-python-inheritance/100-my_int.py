#!/usr/bin/python3
"""
I want to refuse being programmed so I wrote one line
"""


class MyInt(int):
    """
    This is inherited daga int
    """

    def __eq__(self, other):
        """
        Rebellous equality
        """
        if self - other == 0:
            return (False)
        return (True)

    def __ne__(self, other):
        """
        Rebel o rebel ye equalities
        """
        if self - other != 0:
            return (False)
        return (True)
