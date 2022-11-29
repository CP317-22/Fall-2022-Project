from StudentObject import Student
from IO import FileInput

textFile = FileInput()
combinedList = textFile.combineLists(textFile.readNameFile(), textFile.readCourseFile())

studentList = []
newStudent = Student("", "", "", 0, 0, 0, 0, 0)

studentList = newStudent.createStudentList(combinedList)

# open file in write mode
with open(r'C:\Users\Indie\OneDrive\Desktop\Proper Work like a boss\output.txt', 'w') as fp:
    for item in studentList:
        # write each item on a new line
        fp.write("%s\n" % item)
    print('Done')

studentTest = Student("123", "Inder", "CP316", 71, 90, 90, 90, 90)

print(studentTest)