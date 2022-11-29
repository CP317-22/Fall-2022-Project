class FileInput:
    courseList = []
    nameList = []

    def readCourseFile(self):
        myFile = open('CourseFile.txt', 'rt')
        line = myFile.readline()

        while line:

            if len(line.split()) != 5:
                print("exception in", line)
                break
            else:
                self.courseList.append(line)
                line = myFile.readline()

        myFile.close()

        return self.courseList

    def readNameFile(self):
        myFile2 = open('NameFile.txt', 'rt')
        line2 = myFile2.readline()

        while line2:
            self.nameList.append(line2)
            line2 = myFile2.readline()
        myFile2.close()

        return self.nameList

    def combineLists(self, nameList, courseList):
        combinedList = []
        tempList = [x.replace('\n', '') for x in nameList]
        length = len(courseList)
        x = 0
        y = 0
        counter = 0
        id1 = [i.split(', ')[0] for i in courseList]
        courses = [i.split(', ')[1] for i in courseList]
        t1 = [i.split(', ')[2] for i in courseList]
        t2 = [i.split(', ')[3] for i in courseList]
        t3 = [i.split(', ')[4] for i in courseList]
        f1 = [i.split(', ')[5] for i in courseList]

        id2 = [i.split(', ')[0] for i in tempList]
        names = [i.split(', ')[1] for i in tempList]

        while x < length:
            if id1[x] == id2[y]:
                combinedList.append(
                    id1[x] + ', ' + names[y] + ', ' + courses[x] + ', ' + t1[x] + ', ' + t2[x] + ', ' + t3[x] + ', ' +
                    f1[x])
                x += 1
                y = 0
            else:
                y += 1
        return combinedList
