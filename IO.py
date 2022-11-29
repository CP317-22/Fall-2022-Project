class FileInput:
    courseList = []
    nameList = []
    courseFileName = ""
    nameFileName = ""

    def readCourseFile(self, courseFileName):
        """
        -------------------------------------------------------
        Reads CourseFile.txt
        course file should be in the format

        306851690, CP460, 72, 98, 76, 52
        413787382, CP164, 66, 82, 81, 75
        454730171, CP264, 69, 80, 72, 60

        Use: textFile.readCourseFile()
        -------------------------------------------------------
        Returns:a list containing ID, course Code, Grade01, Grade02, Grade03, ExamGrade
        -------------------------------------------------------
        """

        try:
            myFile = open(courseFileName, 'rt')

            line = myFile.readline()
            while line:

                if len(line.strip(',').split()) != 6:
                    print("exception in", line)
                    break
                else:
                    self.courseList.append(line)
                    line = myFile.readline()

            myFile.close()

        except FileNotFoundError:
            print('Course File does not exist')

        return self.courseList

    def readNameFile(self, nameFileName):
        """
        -------------------------------------------------------
        Reads NameFile.txt
        name file should be in the format

        237711821, Saara Beattie
        113820457, Emre Lowry
        642176077, Teddy Hyde

        Use: textFile.readNameFile()
        -------------------------------------------------------
        Returns:a list containing ID, Student Name
        -------------------------------------------------------
        """

        try:
            myFile2 = open(nameFileName, 'rt')
            line2 = myFile2.readline()

            while line2:
                if len(line2.strip(',').split()) != 3:
                    print("exception in", line2)
                    break
                self.nameList.append(line2)
                line2 = myFile2.readline()

            myFile2.close()



        except FileNotFoundError:
            print('Name File does not exist')
        return self.nameList

    def combineLists(self, nameList, courseList):
        """
        -------------------------------------------------------
        Combines the information from nameList and courseList
        Outputs in this format

        237711821, Saara Beattie, CP460, 72, 98, 76, 52
        113820457, Emre Lowry, CP164, 66, 82, 81, 75
        642176077, Teddy Hyde, CP264, 69, 80, 72, 60

        Use: textFile.combineLists(nameList, courseList)
        -------------------------------------------------------
        Returns:a list containing ID, Student Name, course Code, Grade01, Grade02, Grade03, ExamGrade
        -------------------------------------------------------
        """

        combinedList = []
        tempList = [x.replace('\n', '') for x in nameList]
        length = len(courseList)
        x = 0
        y = 0
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
