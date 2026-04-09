class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.grade = {"数学":0, "语文":0, "英语":0}

    def set_grade(self, course, score):
        if course in self.grade:
            self.grade[course] = score

    def print_message(self):
        print(f"""{self.name}的年龄为{self.age}，成绩为：""")
        for course in self.grade:
            print(course, self.grade[course])
chen = Student("小陈", 18)
chen.set_grade("数学", 100)
chen.set_grade("语文", 90)
chen.set_grade("英语", 95)
chen.print_message()


