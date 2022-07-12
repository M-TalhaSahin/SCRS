
import numpy as np
from util import randomClass, NormalizeData

students = []

for i in range(20):
    student = []
    courses = []
    for j in range(6*3):
        courses.append(randomClass(student))
    students.append([courses[:6], courses[6:12], courses[12:18]])

for s in students:
    print(s)
print("\n+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+\n")

transitionMatrix = np.zeros((30, 30))
for s in students:
    for term in range(s.__len__() - 1):
        for i in range(s[term].__len__()):
            for j in range(s[term + 1].__len__()):
                f = int(s[term][i][1:])
                t = int(s[term + 1][j][1:])
                transitionMatrix[f][t] += 1

for i in range(transitionMatrix.__len__()):
    print(transitionMatrix[i])

for i in range(transitionMatrix.__len__()):
    transitionMatrix[i] = NormalizeData(transitionMatrix[i])


print("\n+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+\n")

test = []
for i in range(6):
    test.append(randomClass(test))
print(test)

tuples = []
values = []
for i in range(6):
    ind = np.argpartition(transitionMatrix[int(test[i][1:])], -5)[-5:]
    for j in range(5):
        tuples.append((int(test[i][1:]), ind[j]))
        values.append(transitionMatrix[int(test[i][1:])][ind[j]])

# for i in range(30):
#     print(tuples[i])
#     print(values[i])

b_ind = np.argpartition(values, -10)[-10:]
for i in range(b_ind.__len__()):
    print(tuples[b_ind[i]])
    print(values[b_ind[i]])
