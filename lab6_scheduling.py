def fcfs(processes):
    processes.sort(key=lambda x: x[0])
    wait = 0
    total_wait = 0
    print("\n----- FCFS -----")
    for arr, burst in processes:
        print(f"Process: arrival={arr}, burst={burst}, wait={wait}")
        total_wait += wait
        wait += burst
    avg = total_wait / len(processes)
    print(f"Average Waiting Time: {avg:.2f}")

def sjf(processes):
    ready = []
    time = 0
    total_wait = 0
    remaining = processes.copy()
    print("\n----- SJF -----")
    while remaining or ready:
        to_add = [p for p in remaining if p[0] <= time]
        for p in to_add:
            ready.append(p)
            remaining.remove(p)
        if ready:
            ready.sort(key=lambda x: x[1])
            arr, burst = ready.pop(0)
            wait = time - arr
            total_wait += wait
            print(f"Process: arrival={arr}, burst={burst}, wait={wait}")
            time += burst
        else:
            time += 1
    avg = total_wait / len(processes)
    print(f"Average Waiting Time: {avg:.2f}")

def round_robin(processes, quantum):
    from collections import deque
    queue = deque()
    time = 0
    total_wait = 0
    proc_info = [(p[0], p[1], p[1]) for p in processes]
    print("\n----- Round Robin -----")
    while True:
        for i in range(len(proc_info)):
            arr, burst, rem = proc_info[i]
            if arr <= time and rem > 0 and i not in queue:
                queue.append(i)
        if not queue:
            if all(rem == 0 for _,_,rem in proc_info):
                break
            time += 1
            continue
        idx = queue.popleft()
        arr, burst, rem = proc_info[idx]
        if rem <= quantum:
            wait = time - arr - (burst - rem)
            total_wait += wait
            time += rem
            proc_info[idx] = (arr, burst, 0)
            print(f"Process finished arrival={arr}, wait={wait}")
        else:
            proc_info[idx] = (arr, burst, rem - quantum)
            time += quantum
            queue.append(idx)
    avg = total_wait / len(proc_info)
    print(f"Average Waiting Time: {avg:.2f}")

if __name__ == "__main__":
    procs = [(1,3), (2,6), (3,2), (4,5)]
    fcfs(procs)
    sjf(procs)
    round_robin(procs, quantum=3)
