"""
    This module defines all the custom classes that will be used in the project
"""

from enum import Enum

class WeekDay(Enum):
    Monday = 0
    Tuesday = 1
    Wednesday = 2
    Thursday = 3
    Friday = 4


class Day:
    def __init__(self, name: WeekDay, periods: int):
        self.name = name
        self.periods = periods


class Educator:
    def __init__(self, surname: str, initials: str, post: int):
        self.surname = surname
        self.initials = initials
        self.post = post


class Session:
    session_count = 0
    
    def __init__(self, educator: int, subject: str, grade: str, classes: int, id: int = session_count):
        self.educator = educator
        self.grade = grade
        self.subject = subject
        self.classes = classes
        self.pair = None
        self.id = id

        Session.session_count += 1

    def __str__(self) -> str:
        return "[id = {id}, educator = {educator}, grade = {grade},\
                    subject = {subject}, classes = {classes}, pair = {pair}]".\
                        format(id = self.id,educator = self.educator,grade = self.grade, subject = self.subject, \
                            classes = self.classes, pair = self.pair)


class SplitSession(Session):
    def __init__(self, educator_one: int, educator_two: int, subject_one: str, subject_two: str, grade: str, classes: int):
        super().__init__(educator_one,subject_one,grade,classes)
        self.split_educator = educator_two
        self.split_subject = subject_two

    def __str__(self) -> str:
        return "[id = {id}, educator one = {educator_one}, educator two = {educator_two}, \
                    subject one = {subject_one}, subject two = {subject_two}, grade = {grade}, \
                        classes = {classes}, pair = {pair}]".format(id = self.id, educator_one = self.educator, \
                            educator_two = self.split_educator, grade = self.grade, subject_one = self.subject, \
                                subject_two = self.split_subject, classes = self.classes, pair = self.pair)



class State:
    def __init__(self, structure: list, sessions: list,educators: list, subjects: list,grades: list, schedule: list):
        self.structure = structure
        self.sessions = sessions
        self.educators = educators
        self.subjects = subjects
        self.grades = grades
        self.schedule = schedule

    def create_schedule(self) -> list:
        """
            creates an empty schedule using the schedule size
        """
        size: int = self.schedule_size()
        result: list = [-1 for _ in range(0,size)]

    def schedule_index(self, day: Day,grade: str = None,period: int = None) -> int:
        """
            calculates the index of the slot with the above day, grade and period in the schedule
        """

        result = 0
        day_index = 0

        for day_count in range(0,len(self.structure.days)):
            day_index = day_count

            if day == day.name:
                break
            else:
                result += self.structure.days[day_count].periods * len(self.grades)

        if grade == None:
            return result

        
        for grade_count in range(0,len(self.grades)):
            if grade == self.grades[grade_count]:
                break
            else:
                result += self.structure.days[day_index].periods

        if period == None:
            return result
            
        return result + period

    def schedule_size(self) -> int:
        """
            calculates the size of the schedule based on the structure of the table
        """

        return sum(day.periods * len(self.grades) for day in self.structure.days)

    def index_to_slot(self, index: int) -> tuple:
        """
            calculates the slot day, grade and period based on the schedule index
        """

        result_day = 0
        result_grade = ""

        for day_count in range(0,len(self.structure.days)):
            size  = self.structure.days[day_count].periods * len(self.grades)
            result_day = day_count

            if index >= size:
                index -= size
            else:
                break

        for grade_count in range(0,len(self.grades)):
            result_grade = self.grades[grade_count]

            if index >= self.structure.days[result_day].periods:
                index -= self.structure.days[result_day].periods
            else:
                break

        return (result_day, result_grade, index)

