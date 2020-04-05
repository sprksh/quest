# longest common sub-sequence

x = 'ADISABABA'
y = 'ADIDAS'


"""
This involves 2 things to work on so seems a bit harder

first term: either sam or not same
    1. move one char ahead in first term and repeat
    2. move one char ahead in second term and repeat
"""


def lcs(s1, s2):
    if s1[0] == s2[0]:
        pass