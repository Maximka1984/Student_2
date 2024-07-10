class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_grades = float()

    def add_corsess(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def calculation_average_grades_homework(students, course):
        for student in students:
            result = float(sum(student.grades.get(course)) / len(student.grades.get(course)))
            student.average_grades = result

    def __str__(self):
        result = f"Имя: {self.name}\nФамилия: {self.surname}\n" \
                 f"Средняя оценка за домашние задания: {self.average_grades}\n" \
                 f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n" \
                 f"Завершенные курсы: {','.join(self.finished_courses)}"
        return result

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a Students')
            return
        return self.average_grades < other.average_grades


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.average_grades = float()

    def calculation_average_grades_lecture(lecturers, course):
        for lecturer in lecturers:
            result = float(sum(lecturer.grades.get(course)) / len(lecturer.grades.get(course)))
            lecturer.average_grades = result
        return

    def __str__(self):
        result = f'Имя: {self.name}\nФамилия: {self.surname}\n' \
                 f'Средняя оценка за лекции: {self.average_grades}'
        return result

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Lecturer')
            return
        return self.average_grades < other.average_grades


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        result = f'Имя: {self.name}\nФамилия: {self.surname}'
        return result

belaev = Student('Всеволод', 'Беляев', 'Мужчина')
belaev.courses_in_progress += ['Python']
belaeva = Student('Полина', 'Беляева', 'Женщина')
belaeva.courses_in_progress += ['Python']
belaeva.courses_in_progress += ['GIT']


lecturer_1 = Lecturer('Елена', 'Никитина')
lecturer_1.courses_attached += ['Python']
lecturer_2 = Lecturer('Роман', 'Гордиенко')
lecturer_2.courses_attached += ['Python']


reviewer_1 = Reviewer('Евгений', 'Шмаргунов')
reviewer_1.courses_attached += ['Python']
reviewer_2 = Reviewer('Кирилл', 'Табельский')
reviewer_2.courses_attached += ['Python']


reviewer_1.rate_hw(belaev, 'Python', 9)
reviewer_1.rate_hw(belaeva, 'Python', 7)
reviewer_2.rate_hw(belaev, 'Python', 7)
reviewer_2.rate_hw(belaeva, 'Python', 5)


belaev.rate_lecture(lecturer_1, 'Python', 10)
belaev.rate_lecture(lecturer_2, 'Python', 4)
belaeva.rate_lecture(lecturer_1, 'Python', 7)
belaeva.rate_lecture(lecturer_2, 'Python', 9)


belaev.add_corsess('Введение в программирование')


Student.calculation_average_grades_homework([belaev,belaeva], 'Python')


Lecturer.calculation_average_grades_lecture([lecturer_1,lecturer_2], 'Python')


print(reviewer_1, end='\n\n')
print(lecturer_1, end='\n\n')
print(lecturer_2, end='\n\n')
print(lecturer_1 > lecturer_2, end='\n\n')
print(belaeva, end='\n\n')
print(belaev, end='\n\n')
print(belaeva > belaev, end='\n\n')
