"""
Input: Four Jobs with following
deadlines and profits
JobID  Deadline  Profit
  a      4        20
  b      1        10
  c      1        40
  d      1        30
"""


def job_sequencing(arr, t):
    # sort on decreasing profit
    arr = sorted(arr, key=lambda x: x[-1], reverse=True)
    job_seq = [None for _ in range(t)]
    for r in arr:
        deadline = r[1] - 1
        if job_seq[deadline] is None:
            job_seq[deadline] = r
        else:
            for i in range(deadline, -1, -1):
                if job_seq[i] is None:
                    job_seq[i] = r
                    continue
    return job_seq


if __name__ == "__main__":
    arr = [['a', 2, 100],  # Job Array
           ['b', 1, 19],
           ['c', 2, 27],
           ['d', 1, 25],
           ['e', 3, 15]]
    t = 3
    print(job_sequencing(arr, t))