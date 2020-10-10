"""
Strategy Pattern: selecting execution algorithm ar runtime

This pattern is practically non-existent in languages that support first class functions.

because:

def strategy_add(a, b):
    return a + b

def strategy_minus(a, b):
    return a - b

solver = strategy_add
print solver(1, 2)
solver = strategy_minus
print solver(2, 1)

functions are objects

"""


class StrategyExample:
    def __init__(self, func=None):
        if func:
            self.execute = func

    def execute(self):
        print("Original execution")

def executeReplacement1():
    print("Strategy 1")

def executeReplacement2():
    print("Strategy 2")

if __name__ == "__main__":
    strat0 = StrategyExample()
    strat1 = StrategyExample(executeReplacement1)
    strat2 = StrategyExample(executeReplacement2)

    strat0.execute()
    strat1.execute()
    strat2.execute()