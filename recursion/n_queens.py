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
            # check upwards in both diagonal
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


if __name__ == "__main__":
    solution = NQueens().solve(4)
    print(solution)
