"""
Given two strings:
x = "subsequence"
y = "sue"

find count of occurence of y in x: 7
"""


def find_match(string, pattern):
    oc_count = 0

    def find_match_recr(string, pattern, oc_count=oc_count):
        if string and not pattern:
            oc_count = oc_count + 1
            return
        if not string and not pattern:
            oc_count = oc_count + 1
            return
        if not string and pattern:
            return

        else:
            if string[0] == pattern[0]:
                find_match_recr(string[1:], pattern[1:], oc_count)
            else:
                find_match_recr(string[1:], pattern, oc_count)
                find_match_recr(string, pattern[1:], oc_count)
        
    find_match_recr(string, pattern)
    return oc_count


if __name__ == "__main__":
    x = "subsequence"
    y = "sue"
    print(find_match(x, y))