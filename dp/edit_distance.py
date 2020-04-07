"""
given 2 strings, finf the levensthien distance or edit distance

operations allowed:
delete a char
insert a char
substitute a char

s1 = sitting
s2 = kitten
"""

def find_edit_distance(s1, s2):
    ss_edit_distance_dict = {}

    def edit_distance_recr(substring_1, substring_2):
        if substring_1 and not substring_2:
            return len(substring_1)
        if substring_2 and not substring_1:
            return len(substring_2)
        if not substring_1 and not substring_2:
            return 0
        
        if (substring_1, substring_2) in ss_edit_distance_dict:
            return ss_edit_distance_dict[(substring_1, substring_2)]
        else:
            if substring_1[0] == substring_2[0]:
                min_edit_distance = edit_distance_recr(substring_1[1:], substring_2[1:])
            else:
                # remove 1 alternatively from both
                # adding 1 alternatively is same in terms of count so ignore
                # transform
                min_edit_distance = 1 + min(
                    edit_distance_recr(substring_1[1:], substring_2), 
                    edit_distance_recr(substring_1, substring_2[1:]),
                    edit_distance_recr(substring_1[1:], substring_2[1:]) # basically ignored mismatch with addition of 1 for cost of transformation 
                )
            ss_edit_distance_dict[(substring_1, substring_2)] = min_edit_distance
            return min_edit_distance
    
    edit_distance = edit_distance_recr(s1, s2)
    return edit_distance

if __name__ == "__main__":
    s1 = "adisababa"
    s2 = "adibas"
    min_edit_distance = find_edit_distance(s1, s2)
    print(f"minimum edit distance: {min_edit_distance}")
