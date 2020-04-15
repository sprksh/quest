class KnightsTour:
    """
    Solution for knights tour problem with plain backtracking
    solution in few seconds with 5 bu was taking too much time for 8
    """
    def __init__(self, n=8):
        self.n = n
        self.matrix = [[{"visited": 0, "step": 0} for _ in range(self.n)] for _ in range(self.n)]
        self.matrix[0][0]["visited"] = 1
        self.matrix[0][0]["step"] = 0

    def visit(self, x, y, step):
        self.matrix[x][y]["visited"] = 1
        self.matrix[x][y]["step"] = step

    def unvisit(self, x, y):
        self.matrix[x][y]["visited"] = 0
        self.matrix[x][y]["step"] = 0

    def tour(self, coordinates=(0,0), step=0):
        # base case
        if step >= (self.n**2) - 1:
            no_unvisited = True
            for i in self.matrix:
                for j in i:
                    if j["visited"] == 0:
                        no_unvisited=False
            if no_unvisited:
                new_matrix = [[_["step"] for _ in i] for i in self.matrix]
                print(new_matrix)
                # import time
                # time.sleep(10)
            return
        step += 1
        ways = [(1,2), (-1,2), (1,-2), (-1,-2), (2,1), (-2,1), (2,-1), (-2,-1)]
        for w in ways:
            new_coordinates = (coordinates[0] + w[0], coordinates[1] + w[1])
            x, y = new_coordinates[0], new_coordinates[1]
            if 0 <= x < self.n and 0 <= y < self.n and self.matrix[x][y]["visited"] == 0:
                self.visit(x, y, step)
                self.tour(new_coordinates, step)
                self.unvisit(x, y)


if __name__ == "__main__":
    KnightsTour(5).tour()
