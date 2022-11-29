class Student:
    studentID: str
    name: str
    course: str
    grade01 = 0.0
    grade02 = 0.0
    grade03 = 0.0
    examGrade = 0.0
    finalGrade = 0.0
    studentsListed = []

    def __init__(self, studentID, name, course, grade01, grade02, grade03, examGrade, finalGrade):
        self.studentID = studentID
        self.name = name
        self.course = course

        if grade01 is None or grade02 is None or grade03 is None or examGrade is None:
            raise ValueError("Error grade cannot be NONE")
        else:
            if grade01 < 0 or grade02 < 0 or grade03 < 0 or examGrade < 0:
                raise ValueError("Error grade cannot be Negative")

            elif grade01 > 100 or grade02 > 100 or grade03 > 100 or examGrade > 100:
                raise ValueError("Error grade cannot be higher then 100")


            else:
                self.grade01 = grade01
                self.grade02 = grade02
                self.grade03 = grade03
                self.examGrade = examGrade
                self.finalGrade = finalGrade

    def __str__(self):
        return "||Student ID: " + self.studentID + " ||Student Name: " + self.name + " ||Test 1 Grade: {:.1f}".format(
            self.grade01) + " ||Test 2 Grade: {:.1f}".format(self.grade02) + " ||Test 3 Grade: {:.1f}".format(
            self.grade03) + " ||Exam Grade: {:.1f}".format(self.examGrade) + " ||Final Grade: {:.1f}".format(
            self.finalGrade)

    def setGradeLimit(self, grade01, grade02, grade03, examGrade):
        check = False
        if grade01 or grade02 or grade03 or examGrade < -1:
            return check, "Error grade cannot be Negative"
        elif grade01 or grade02 or grade03 or examGrade > 101:
            return check, "Error grade cannot be higher then 100"

        elif grade01 is None or grade02 is None or grade03 is None or examGrade is None:
            return check, "Error grade cannot be None"
        else:
            check = True
            return check

    def calculate_grade(self, grade01, grade02, grade03, examGrade):
        grade = (grade01 * 0.20) + (grade02 * 0.20) + (grade03 * 0.20) + (examGrade * 0.40)
        return grade

    def createStudentList(self, studentsListed):
        errorCheck = False

        studentList = []
        newStudent = Student("", "", "", 0, 0, 0, 0, 0)

        ids = [i.split(', ')[0] for i in studentsListed]
        names = [i.split(', ')[1] for i in studentsListed]
        courses = [i.split(', ')[2] for i in studentsListed]
        t1 = [i.split(', ')[3] for i in studentsListed]
        t2 = [i.split(', ')[4] for i in studentsListed]
        t3 = [i.split(', ')[5] for i in studentsListed]
        f1 = [i.split(', ')[6] for i in studentsListed]



        grade01 = list(map(float, t1))
        grade02 = list(map(float, t2))
        grade03 = list(map(float, t3))
        examGrade = list(map(float, f1))
        length = len(grade01)
        x = 0

        while x < length:
            self.finalGrade = self.calculate_grade(grade01[x], grade02[x], grade03[x], examGrade[x])
            newStudent = Student(ids[x], names[x], courses[x], grade01[x], grade02[x], grade03[x], examGrade[x],
                                 self.finalGrade)
            studentList.append(newStudent)
            x += 1

        return studentList
