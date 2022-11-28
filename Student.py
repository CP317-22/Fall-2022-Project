from typing import List
from Course import Course


class Student:
	
	#Attr
	id: str
	name: str
	total_courses: int
	course_list: List[Course]
	studentsList = []

	def __init__(self, id: str, name: str) -> None:
		self.id = id
		self.name = name

	def add_course(self, course: Course) -> None:
		self.course_list.append(course)
		self.total_courses += 1

	def readNameFile(self):
		studentList = {}  # dictionary
		fh = open('NameFile.txt').readlines()
		for line in fh:
			row = line.split(', ')
			id, name = [i.strip() for i in row]
			student = Student(id, name)
			studentList[id] = student  # 'id' is the 'key' and 'student' is 'value'
		return



