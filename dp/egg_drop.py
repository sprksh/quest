"""
k floors
n eggs
find minimum trials to find which floor egg breaks given k floors and n eggs

recursively find all solutions and find best

min_trials(floor, eggs) :-> minimum number of trials needed to find the optimal floor in worst case

lets drop it from x: 1 trial
either breaks: min_trials(x-1, n-1)
or doesn't breaks: min_trials(k-x, n)
for given x: 
    min_trials = 1 + max(min_trials(x-1, n-1), min_trials(k-x, n))

"""
min_trials_cache = {}

def min_trials(k, n):
    if (k, n) in min_trials_cache:
        return min_trials_cache[(k,n)]
    minimum_trials = k
    if (k == 1 or k == 0): 
        return k 
    if n == 1:
        return k
    for x in range(1, k+1):
        _minimum_trials = 1 + max(min_trials(x-1, n-1), min_trials(k-x, n))
        if _minimum_trials < minimum_trials:
            minimum_trials = _minimum_trials
    min_trials_cache[(k,n)] = minimum_trials
    return minimum_trials

# the matrix way


def test_egg_drop_problem():
    # print(min_trials(10, 2))
    print(min_trials(36, 2))


if __name__ == "__main__":
    test_egg_drop_problem()