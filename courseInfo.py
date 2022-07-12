import pandas as pd


def getCourseListToProcess():
    courseList = {}
    df = pd.read_excel('BrmDers.xls')
    for i in range(df.__len__()):
        if df['ZORSEC'][i] == 1:
            courseList[df['DERS_KODU'][i]] = df['DERSADI'][i]
    return courseList


def getStudentGPA():
    studentList = {}
    df = pd.read_excel('BrmOgrenci.xls')
    for i in range(df.__len__()):
        studentList[df['OGRNO'][i]] = float(df['GPA'][i])
    return studentList


def valueCourseScores(course1Score, course2Score):
    course1Score = float(course1Score)
    course2Score = float(course2Score)

    return course1Score + course2Score
