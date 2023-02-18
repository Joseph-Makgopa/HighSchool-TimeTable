"""
    This module defines all the custom classes that will be used in the project
"""

from enum import Enum
import math

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


    def schedule_index(self, day_index: int,grade_index: int = None,period: int = None) -> int:
        """
            calculates the index of the slot with the above day, grade and period in the schedule
        """

        result: int = sum(self.structure[day_count].periods * len(self.grades) \
                            for day_count in range(0, day_index))

        if grade_index != None:
            result += grade_index * self.structure[day_index].periods

        if period != None:
            result += period

        return result

    def schedule_size(self) -> int:
        """
            calculates the size of the schedule based on the structure of the table
        """

        return sum(day.periods * len(self.grades) for day in self.structure)


    def index_to_slot(self, index: int) -> tuple:
        """
            calculates the slot day, grade and period based on the schedule index
        """

        result_day: int = 0
        result_grade: str = ""

        for day_count in range(0,len(self.structure)):
            size: int  = self.structure[day_count].periods * len(self.grades)
            result_day = day_count

            if index >= size:
                index -= size
            else:
                break

        grade_count: int = math.floor(index / self.structure[result_day].periods)
        index -= grade_count * self.structure[result_day].periods

        return (result_day, result_grade, index)

