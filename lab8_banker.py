def is_safe(alloc, max_need, avail):
    n = len(alloc)
    m = len(avail)
    need = [[max_need[i][j] - alloc[i][j] for j in range(m)] for i in range(n)]
    work = avail.copy()
    finish = [False] * n
    safe_seq = []

    while len(safe_seq) < n:
        found = False
        for i in range(n):
            if not finish[i]:
                can_allocate = True
                for j in range(m):
                    if need[i][j] > work[j]:
                        can_allocate = False
                        break
                if can_allocate:
                    for j in range(m):
                        work[j] += alloc[i][j]
                    finish[i] = True
                    safe_seq.append(i)
                    found = True
        if not found:
            return False, []
    return True, safe_seq

if __name__ == "__main__":
    allocation = [[1,0,2],[0,2,0],[3,0,1]]
    max_need = [[3,2,2],[1,3,2],[3,1,4]]
    available = [2,1,1]

    safe, seq = is_safe(allocation, max_need, available)
    if safe:
        print("System is SAFE")
        print("Safe Sequence: ", seq)
    else:
        print("System is UNSAFE, Deadlock may occur")
