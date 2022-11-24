class Course:
	
	#Attr
	id: str
	name: str
	T1: int
	T2: int
	T3: int
	final: int
	grade: int


	def __init__(self, name: str, id: str) -> None:
		self.name = name
		self.id = id

	def calculate_grade(self) -> None:
		self.grade = (self.T1*0.20) + (self.T2*0.20) 
		+ (self.T3*0.20) + (self.final*0.40)
