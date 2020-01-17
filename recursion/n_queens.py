class NQueens:
    """
    nxn chessboard
    solution array:
    it will contain n elements corresponding to n rows.
    each element will be an integer between 0 - n-1 as the column index of where the queen is

    # [1,3,0,2]
    """
    def __init__(self):
        self.all_solutions = []

    def solve(self, n):
        all_arrs = self.create_array_permutations(n)
        for i in all_arrs:
            i = list(i)
            cool = self.check_if_all_queen_fits_conditions(i, n)
            if cool:
                self.all_solutions.append(i)
        return self.all_solutions

    def check_if_all_queen_fits_conditions(self, solution_array, n):
        print("\nFor solution array %s" % str(solution_array))
        for row, column in enumerate(solution_array):
            # check in both upwards diagonal
            cl, cr = column, column
            while row > 0:
                if solution_array[row-1] == cl-1 or solution_array[row-1] == cr+1:
                    return False
                row, cl, cr = row - 1, cl - 1, cr + 1

        return True

    def create_array_permutations(self, n):
        """
        This is an easier solution using itertools.
        Otherwise we can use backtracking (recursion) to create combinations
        """
        import itertools
        combs = itertools.permutations(list(range(n)), n)
        return combs


"""
If you have to copy variables during recursion/backtracking, you are probably going in the wrong direction
"""


def permute1(a, l, r):
    if l == r:
        print(a)
    else:
        for i in range(l, r + 1):
            a[l], a[i] = a[i], a[l]
            permute1(a, l + 1, r)
            a[l], a[i] = a[i], a[l]  # backtrack


def permute2(l):
    if len(l) == 0:
        return []
    elif len(l) == 1:
        return [l]
    else:
        ll = []
        for i in range(len(l)):
            x = l[i]
            xs = l[:i] + l[i+1:]
            for p in permute2(xs):
                ll.append([x] + p)
        return ll

def permute3(l):
    if len(l) == 0:
        yield []
    elif len(l) == 1:
        yield l
    else:
        ll = []
        for i in range(len(l)):
            x = l[i]
            xs = l[:i] + l[i+1:]
            for p in permute2(xs):
                yield [x] + p


if __name__ == "__main__":
    # a = NQueens().solve(4)
    # a = permute1(list(range(4)), 0, 3)
    # a = permute2(list(range(6)))
    # print(a)
    a = permute3(list(range(6)))
    for i in a:
        print(i)
