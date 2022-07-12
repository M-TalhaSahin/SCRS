from courseInfo import getStudentGPA

GPA_RELATIVE = 1


class StudentList:
    def __init__(self):
        self.students = {}
        self.gpaList = getStudentGPA()

    def addStudent(self, _id, _gpa=4.0):
        self.students[_id] = Student(_id, _gpa)

    def addCourse(self, _id, _year, _period, _course, _score):
        if _id not in self.students:
            self.addStudent(_id, self.gpaList[_id])
        if GPA_RELATIVE:
            _score = self.calcRelativeScore(self.students[_id].gpa, _score)
        self.students[_id].appendCourse(_year, _period, _course, _score)

    def calcRelativeScore(self, gpa, score):
        return (score * gpa) / 4


class Student:
    def __init__(self, _id, _gpa=4.0):
        self.id = _id
        self.gpa = _gpa
        self.semesterList = []

    def appendCourse(self, _year, _period, _course, _score):
        for i in range(self.semesterList.__len__()):
            if self.semesterList[i].getYearPeriod() == (_year, _period):
                self.semesterList[i].courseScoreList.append((_course, _score))
                return
        self.semesterList.append(Semester(_year, _period))
        self.semesterList[-1].courseScoreList.append((_course, _score))


class Semester:
    def __init__(self, _year, _period):
        self.year = _year
        self.period = _period
        self.courseScoreList = []

    def getYearPeriod(self):
        return self.year, self.period

