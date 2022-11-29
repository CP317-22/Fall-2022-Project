class Student:
    _studentID: str
    _name: str
    _course: str
    _grade01 = 0.0
    _grade02 = 0.0
    _grade03 = 0.0
    _examGrade = 0.0
    _finalGrade = 0.0
    _studentsListed = []

    def __init__(self, _studentID, _name, _course, _grade01, _grade02, _grade03, _examGrade, _finalGrade):
        """
        -------------------------------------------------------
        Initializes an empty Student Object.
        Use: newStudent = Student()
        -------------------------------------------------------
        Returns:a new student object
        -------------------------------------------------------
        """
        self.studentID = _studentID
        self.name = _name
        self.course = _course

        if _grade01 is None or _grade02 is None or _grade03 is None or _examGrade is None:
            raise ValueError("Error grade cannot be NONE")
        else:
            if _grade01 < 0 or _grade02 < 0 or _grade03 < 0 or _examGrade < 0:
                raise ValueError("Error grade cannot be Negative")

            elif _grade01 > 100 or _grade02 > 100 or _grade03 > 100 or _examGrade > 100:
                raise ValueError("Error grade cannot be higher then 100")


            else:
                self.grade01 = _grade01
                self.grade02 = _grade02
                self.grade03 = _grade03
                self.examGrade = _examGrade
                self.finalGrade = _finalGrade

    def __str__(self):
        """
        -------------------------------------------------------
        Initializes an empty Student Object.
        Use: newStudent = Student()
        -------------------------------------------------------
        Returns:a new student object
        -------------------------------------------------------
        """
        return "||Student ID: " + self.studentID + " ||Student Name: " + self.name + " ||Course Code: " + self.course + " ||Test 1 Grade: {:.1f}".format(
            self.grade01) + " ||Test 2 Grade: {:.1f}".format(self.grade02) + " ||Test 3 Grade: {:.1f}".format(
            self.grade03) + " ||Exam Grade: {:.1f}".format(self.examGrade) + " ||Final Grade: {:.1f}".format(
            self.finalGrade)

    def _calculate_grade(self, grade01, grade02, grade03, examGrade):
        """
        -------------------------------------------------------
        Calculates Final grade by using students 3 test results
        and exam grade.
        Used in createStudentList

        Use: newStudent._calculate_grade(grade1,grade2,grade3,examgrade)
        -------------------------------------------------------
        Returns:A calculated final grade
        -------------------------------------------------------
        """
        grade = (grade01 * 0.20) + (grade02 * 0.20) + (grade03 * 0.20) + (examGrade * 0.40)
        return grade

    def createStudentList(self, studentsListed):
        """
        -------------------------------------------------------
        Takes in a list of strings with student information. Format should be
        123456, Name, Course, Grade01, Grade02, Grade03, ExamGrade

        Use: studentList = newStudent.createStudentList(combinedList)
        -------------------------------------------------------
        Returns:A list containing student objects.
        -------------------------------------------------------
        """
        studentList = []

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
            self.finalGrade = self._calculate_grade(grade01[x], grade02[x], grade03[x], examGrade[x])
            newStudent = Student(ids[x], names[x], courses[x], grade01[x], grade02[x], grade03[x], examGrade[x],
                                 self.finalGrade)
            studentList.append(newStudent)
            x += 1

        return studentList
