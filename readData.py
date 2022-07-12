import time

import pandas as pd
import numpy as np
from datetime import datetime

from Student import StudentList
from util import NormalizeData
from courseInfo import getCourseListToProcess, valueCourseScores

df = pd.read_excel('BrmOgrDers.xls')

"""
students and courses
2010 - 1 -> 2020 - 1
"""

validCourses = getCourseListToProcess()
sList = StudentList()
sTestList = StudentList()
testPeriod = (2010, 1)

for i in range(df.__len__()):
    if df['DERS_KODU'][i] in validCourses:
        if df['YIL'][i] == testPeriod[0] and df['DONEM'][i] == testPeriod[1]:
            sTestList.addCourse(df['OGRNO'][i], df['YIL'][i], df['DONEM'][i], df['DERS_KODU'][i], df['SAYISAL'][i])
        elif df['YIL'][i] == testPeriod[0] and df['DONEM'][i] == testPeriod[1] + 1:
            sTestList.addCourse(df['OGRNO'][i], df['YIL'][i], df['DONEM'][i], df['DERS_KODU'][i], df['SAYISAL'][i])
            sList.addCourse(df['OGRNO'][i], df['YIL'][i], df['DONEM'][i], df['DERS_KODU'][i], df['SAYISAL'][i])
        else:
            sList.addCourse(df['OGRNO'][i], df['YIL'][i], df['DONEM'][i], df['DERS_KODU'][i], df['SAYISAL'][i])

"""
curse list and transition
"""

courseList = list(validCourses.keys())
transitionMatrix = np.zeros((courseList.__len__(), courseList.__len__()))

for keyId in sList.students:
    student = sList.students[keyId]
    for term in range(student.semesterList.__len__() - 1):
        for i in range(student.semesterList[term].courseScoreList.__len__()):
            for j in range(student.semesterList[term + 1].courseScoreList.__len__()):
                f = courseList.index(student.semesterList[term].courseScoreList[i][0])
                t = courseList.index(student.semesterList[term + 1].courseScoreList[j][0])
                # değer
                transitionMatrix[f][t] += valueCourseScores(student.semesterList[term].courseScoreList[i][1], student.semesterList[term + 1].courseScoreList[j][1])


for i in range(transitionMatrix.__len__()):
    transitionMatrix[i] = NormalizeData(transitionMatrix[i])

"""
TEST
"""

for key in sTestList.students:
    if sTestList.students[key].semesterList.__len__() < 2:
        continue
    print('\n\nReal:')
    print(sTestList.students[key].semesterList[0].courseScoreList, '\n->', sTestList.students[key].semesterList[1].courseScoreList)
    for course in sTestList.students[key].semesterList[0].courseScoreList:
        ind = np.argsort(transitionMatrix[courseList.index(course[0])])[-5:]
        print('\nFor', course[0], validCourses[course[0]], ';')
        for j in range(5):
            print('Prediction:', courseList[ind[j]], validCourses[courseList[ind[j]]])
            print('Value:', transitionMatrix[courseList.index(course[0])][ind[j]])

"""
RESULT BY COURSE 
TO TXT
"""
dateTimeStr = datetime.now().strftime("%d_%m_%Y-%H.%M.%S")
with open('predictRecord/coursePrediction-' + dateTimeStr + '.txt', 'w', encoding='utf-8') as f:
    for c in courseList:
        ind = np.argsort(transitionMatrix[courseList.index(c)])[-10:]
        f.write('\nFor ' + c.__str__() + ' ' + validCourses[c].__str__() + ';\n')
        for j in reversed(range(10)):
            f.write('Prediction: ' + courseList[ind[j]].__str__() + ' ' + validCourses[courseList[ind[j]]].__str__() + '\n')
            f.write('Value: ' + transitionMatrix[courseList.index(c)][ind[j]].__str__() + '\n')
