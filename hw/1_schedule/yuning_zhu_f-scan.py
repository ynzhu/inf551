import sys
from functools import reduce
def scan(state, queue):
	waittime = 0
	schedule = []
	dirdec = []
	#decide the scan direction
	seek = [abs(xx - state) for xx in queue]
	s_seek = min(seek)
	for index in range(len(seek)):
		if seek[index] == s_seek:
			dirdec.append(queue[index])
	#scan
	if min(dirdec) > state:
		end = 200
		for xxx in range(state, end):
			while xxx in queue:
				waittime += abs(state - xxx)
				state = xxx
				schedule.append(xxx)
				queue.remove(xxx)
		if queue != []:
			waittime += abs(end - 1 - state)
			state = 199
			while end >= 0:
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
		if queue != []: #if there is only one direction, no need to change direction
			waittime += abs(0 - state)
			state = 0
			for xxxx in range(state, end):
				while xxxx in queue:
					waittime += abs(state - xxxx)
					state = xxxx
					schedule.append(xxxx)
					queue.remove(xxxx)
	return schedule, state, waittime
	#for m in schedule[:len(schedule)-1]:
	#	print (m, end=',')
	#print (schedule[len(schedule)-1])
	#print (waittime)
	#print (schedule[len(schedule)-1], waittime)

def fscan(test): #the scan process is the same, just take 10 request a time
	with open(test, 'r') as f:
		state = int(f.readline())
		queue = f.readline().split(',')
		queue = list(map(int, queue))
	f = 0
	schedule = []
	partSchedule = []
	waittime = 0
	partWaittime = 0
	while f < len(queue):
		f += 10
		q1 = queue[f-10:f]
		partSchedule, state, partWaittime = scan(state, q1)
		for task in partSchedule:
			schedule.append(task)
		waittime += partWaittime
	#output
	for m in schedule[:len(schedule)-1]:
		print (str(m)+","), #for right layout
	print (schedule[len(schedule)-1])
	print (waittime)
	print schedule[len(schedule)-1], waittime

if __name__ =="__main__":
	fscan(sys.argv[1])