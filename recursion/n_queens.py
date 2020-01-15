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

    def solve_iteratively(self, n):
        solution = False
        solution_arrays = []
        solution_array = [None for _ in range(n)]
        for i in range(n):
            for j in range(n):
                solution_array[j] = i
                s = solution_array.copy()

                solution_arrays.append(s)
        print(solution_arrays)
        print(len(solution_arrays))

        # solution_arrays = [[1,3,0,2]]

        for s in solution_arrays:
            fits = self.check_if_all_queen_fits_conditions(s, n)
            print(str(fits))
            if fits:
                self.all_solutions.append(s)
        return self.all_solutions

    def solve_iteratively_better(self):
        pass

    def solve_recursively(self):
        pass

    def check_if_all_queen_fits_conditions(self, solution_array, n):
        for row, column in enumerate(solution_array):
            # here i is row, j is column
            # condition is:if self.solution_array[row] == column, return false
            print("\nFor solution array %s" % str(solution_array))

            print(str([row, column]))
            print("We checked")

            if column in solution_array:
                return False

            # check upper diagonal left
            for i in range(min(row, column), -1, -1):
                new_row, new_column = row + i, column - i
                print(str([new_row, new_column]), end=' ')
                if new_row == -1 or new_column == -1:
                    return True
                if solution_array[new_row] == new_column:
                    return False

            print("\nAnd")
            # check lower diagonal left
            for i in range(min(row, column), n):
                new_row, new_column = row - i, column - i
                print(str([new_row, new_column]), end=' ')
                if new_row == -1 or new_column == -1:
                    return True
                if solution_array[new_row] == new_column:
                    return False
            return True

    def create_arrays(self, n):
        arrays = []
        crr = [None for _ in range(n)]
        def create(crr, arr, a=0):
            print(crr, arr, a)
            if a == n:
                arrays.append(crr.copy())
                return crr
            for i in arr:
                p = arr.pop(i)
                crr[a] = p
                crr = create(crr, arr, a+1)
        create(crr, list(range(n)))
        return arrays

    def create_1(self, n):
        crr = list(range(n))
        def r():
            for i in crr:
                arr = crr.copy()
                p = arr.pop(i)





if __name__ == "__main__":
    # solution = NQueens().solve_iteratively(4)
    # print(solution)
    arrays = NQueens().create_arrays(4)
    print(len(arrays))
    print(arrays)
