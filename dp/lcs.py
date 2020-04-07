# longest common sub-sequence

x = 'ADISABABA'
y = 'ADIDAS'


"""
This involves 2 strings to work on so seems a bit harder

first term: either sam or not same
    1. move one char ahead in first term and repeat
    2. move one char ahead in second term and repeat
"""


def find_lcs(s1, s2):
    lcs_ss_dict = {}

    def lcs_recr(substring_1, substring_2):
        if not substring_1 or not substring_2:
            return 0
        if (substring_1, substring_2) in lcs_ss_dict:
            return lcs_ss_dict[(substring_1, substring_2)]
        else:
            if substring_1[-1] == substring_2[-1]:
                ll = 1 + lcs_recr(substring_1[:-1], substring_2[:-1])
            else:
                ll = max(lcs_recr(substring_1[:-1], substring_2), lcs_recr(substring_1, substring_2[:-1]))
            lcs_ss_dict[(substring_1, substring_2)] = ll
        return ll
    
    lcs = lcs_recr(s1, s2)
    return lcs

if __name__ == "__main__":
    x = "AGGTAB"
    y = "GXTXAYB"
    lcs = find_lcs(x, y)
    print(f"Length of Longest common Subsequence: {lcs}")
