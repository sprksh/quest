class Matrix:
    def __init__(self, n, destination):
        self.n = n
        self.visited_matrix = [[0 for _ in range(n)] for _ in range(n)]
        self.visited_matrix[0][0] = 1
        self.destination = destination
        self.pats = []

    def visit(self, matrix, coordinates=(0,0), path=[(0,0)]):
        if coordinates == self.destination:
            self.pats.append(path.copy())
            # print(path)
            return path

        else:
            options = [(0,1), (0,-1), (-1,0), (1,0)]
            for o in options:
                new_coordinates = (coordinates[0] + o[0], coordinates[1] + o[1])
                x, y = new_coordinates[0], new_coordinates[1]
                if not (0 <= x < self.n and 0 <= y < self.n and self.visited_matrix[x][y] == 0 and matrix[x][y] == 1):
                    continue
                self.visited_matrix[x][y] = 1
                path.append((x,y))
                self.visit(matrix, (x,y), path)
                # below lines backtrack 
                path.pop()
                self.visited_matrix[x][y] = 0
        return self.pats


if __name__ == "__main__":
    path_matrix = [
        [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
        [1, 0, 1, 0, 1, 1, 1, 0, 1, 1],
        [1, 1, 1, 0, 1, 1, 0, 1, 0, 1],
        [0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
        [1, 0, 0, 0, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [1, 0, 0, 0, 1, 0, 0, 1, 0, 1],
        [1, 0, 1, 1, 1, 1, 0, 0, 1, 1],
        [1, 1, 0, 0, 1, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 1, 0, 1, 0, 0]
    ]
    destination = (5,7)
    path = Matrix(10, destination).visit(path_matrix)
    print(path)
    print(len(path))