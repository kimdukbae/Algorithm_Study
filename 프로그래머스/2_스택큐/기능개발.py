import math

answer = []
progresses = [93, 30, 55]
speeds = [1, 30, 5]

for i in range(len(progresses)):
    progresses[i] = math.ceil((100 - progresses[i]) / speeds[i])

front = 0
for i in range(len(progresses)):
    if progresses[front] < progresses[i]:
        answer.append(i - front)
        front = i

answer.append(len(progresses) - front)

print(answer)