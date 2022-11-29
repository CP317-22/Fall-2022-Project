from StudentObject import Student
from IO import FileInput

textFile = FileInput()

courseFileName = input("Please Enter Course File name: ")
nameFileName = input("Please Enter Name File name: ")

courseList = textFile.readCourseFile(courseFileName)
nameList = textFile.readNameFile(nameFileName)
combinedList = textFile.combineLists(nameList, courseList)

studentList = []
newStudent = Student("", "", "", 0, 0, 0, 0, 0)
studentList = newStudent.createStudentList(combinedList)

# open file in write mode
with open(r'C:\Users\Indie\OneDrive\Desktop\Proper Work like a boss\output.txt', 'w') as fp:
    for item in studentList:
        # write each item on a new line
        fp.write("%s\n" % item)
    print('Done')
