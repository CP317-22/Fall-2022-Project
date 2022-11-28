class Course:
    # Attr
    id: str
    name: str
    T1: int
    T2: int
    T3: int
    final: int
    grade: int
    courseList = []
    def __init__(self, name: str, id: str) -> None:
        self.name = name
        self.id = id

    def calculate_grade(self) -> None:
        self.grade = (self.T1 * 0.20) + (self.T2 * 0.20)
        + (self.T3 * 0.20) + (self.final * 0.40)

    def readCourseFile(self):

        myFile = open('CourseFile.txt', 'rt')
        line = myFile.readline()

        while line:
            self.courseList.append(line)
            line = myFile.readline()
        myFile.close()
        return self.courseList

    def spiltString (self, courseList):
        T1list = [i.split(maxsplit=1)[2] for i in courseList]
        T2list = [i.split(maxsplit=1)[3] for i in courseList]
        T3list = [i.split(maxsplit=1)[4] for i in courseList]
        finalGradelist = [i.split(maxsplit=1)[5] for i in courseList]
