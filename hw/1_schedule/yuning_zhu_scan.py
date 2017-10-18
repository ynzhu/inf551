import sys
def scan(test):
    # read the request
    with open(test, 'r') as f:
        state = int(f.readline())
        queue = f.readline().split(',')
        queue = list(map(int, queue))
    waittime = 0
    schedule = []
    dirdec = []
    # decide the scan direction
    seek = [abs(xx - state) for xx in queue]
#    while 0 in seek:
#        seek.remove(0)
    s_seek = min(seek)
    for index in range(len(seek)):
        if seek[index] == s_seek:
            dirdec.append(queue[index])
    # scan
    if min(dirdec) > state:
        end = 200
        for xxx in range(state, end):
            while xxx in queue:
                waittime += abs(state - xxx)
                state = xxx
                schedule.append(xxx)
                queue.remove(xxx)
        if queue != []:
            waittime += abs(end -1 - state)  # head move to outermost
            state = 199  # outermost state
            while end - 1 >= 0:
                while end in queue:
                    waittime += abs(state - end)
                    state = end
                    schedule.append(end)
                    queue.remove(end)
                end -= 1

    else:
        start = state
        end = 200
        while start >= 0:
            while start in queue:
                waittime += abs(state - start)
                state = start
                schedule.append(start)
                queue.remove(start)
            start -= 1
        if queue != []:  # if there is only one direction, no need to change direction
            waittime += abs(0 - state)  # head move to innermost
            state = 0  # innermost state
            for xxxx in range(state, end):
                while xxxx in queue:
                    waittime += abs(state - xxxx)
                    state = xxxx
                    schedule.append(xxxx)
                    queue.remove(xxxx)
    # output
    for m in schedule[:len(schedule) - 1]:
        print(str(m) + ","), #for right layout
    print(schedule[len(schedule) - 1])
    print(waittime)
    print schedule[len(schedule) - 1], waittime


if __name__ == "__main__":
    scan(sys.argv[1])
