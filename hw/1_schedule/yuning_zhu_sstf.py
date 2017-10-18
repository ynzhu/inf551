import sys
def sstf(test):
	with open(test, 'r') as f:
		state = int(f.readline())
		queue = f.readline().split(',')
		queue = list(map(int, queue))
	waittime = 0
	schedule = []
	while len(queue) > 0:
		sst = 200
		for x in range(len(queue)):
			if abs(state - queue[x]) < sst:
				tempstate = queue[x]
				y = x
				sst = abs (state - queue[x])
		waittime += sst
		schedule.append(queue.pop(y))
		state = tempstate
	for m in schedule[:len(schedule)-1]: 
		print(str(m) + ","),  
	print (schedule[len(schedule)-1])  #for output layout
	print (waittime)
	print tempstate, waittime


if __name__ =="__main__":
	sstf(sys.argv[1])