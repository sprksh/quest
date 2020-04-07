"""
given an array [1,2,3,4] and a number 8

which corresponds to: a + 2b + 3c + 4d = 8

find number of solution
"""


def get_solution_count(arr, val):

    arr_val_dict = {}
    solution_count = 0

    def solve_recr(arr, val):
        if (tuple(arr), val) in arr_val_dict:
            return arr_val_dict[(tuple(arr), val)]
        
        if val == 0:
            return 1
        if len(arr) == 0:
            return 0
        else:
            c = 0
            for i in range((val//arr[0]) + 1):
                c += solve_recr(arr[1:], val-i*arr[0])
            arr_val_dict[(tuple(arr), val)] = c
            return c
    solve_recr(arr, val)
    return arr_val_dict[tuple(arr), val]


if __name__ == "__main__":
    solution_count = get_solution_count([1,3,5,7,8,9,4], 18)
    print(solution_count)