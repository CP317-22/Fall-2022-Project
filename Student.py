from typing import List
from Course import Course


class Student:
	
	#Attr
	id: str
	name: str
	total_courses: int
	course_list: List[Course]

	def __init__(self, id: str, name: str) -> None:
		self.id = id
		self.name = name

	def add_course(self, course: Course) -> None:
		self.course_list.append(course)
		self.total_courses += 1