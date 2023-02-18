from models import *
from helpers import available_sessions
import random

class GeneticAlgorithm:
    def __init__(self, state: State, parameters: dict):
        self.state = state
        self.parameters = parameters

    def random_individual(self) -> list:
        """
            creates a schedule with classes assigned randomly
        """
        result: list = self.state.create_schedule()

        for day_count in range(0, len(self.state.structure)):
            
            day: Day = self.state.structure[day_count]
            already_assigned_educators: dict = {}

            for period in range(0, day.periods):
                already_assigned_educators[period] = set()

            already_assigned_sessions: dict = {}

            for grade_count in range(0, len(self.state.grades)):
                already_assigned_sessions[grade_count] = set()

            for grade_count in range(0, len(self.state.grades)):
                
                for period in range(0, day.periods):
                    
                    index: int = self.state.schedule_index(day_count,grade_count,period)

                    if result[index] == None:
                        possible_assignments: list = available_sessions(self.state,result,already_assigned_educators,already_assigned_sessions,grade_count,period)

                        session_id: int = random.choice(possible_assignments)

                        if period == 4 or period == (day.periods - 1):



        return result

    def initial_population(self):
        pass

    def execute(self):
        pass

    def fitness(self,individual):
        pass

    def crossover(self,parent_one,parent_two):
        pass

    def mutate(self,individual):
        pass

    def repair(self,individual):
        pass

