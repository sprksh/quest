import math

def egyptian_fraction(nr, dr):
    ef = []
    while nr != 0:
        # taking ceiling
        x = math.ceil(dr / nr)

        # storing value in ef list
        ef.append(x)

        # updating new nr and dr
        nr = x * nr - dr
        dr = dr * x
    return ef


if __name__ == "__main__":
    r = egyptian_fraction(7, 22)
    print(r)
