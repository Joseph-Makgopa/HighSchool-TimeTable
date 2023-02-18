from models import *

class GeneticAlgorithm:
    def __init__(self,state,parameters):
        self.state = state
        self.parameters = parameters

    def random_individual(self) -> list:
        """
            creates a schedule with classes assigned randomly
        """

        for day_count in range(0, len(self.state.structure)):
            
            day: Day = self.state.structure[day_count]
            already_assigned_educators: dict = {}

            for period in range(0, day.periods):
                already_assigned_educators[period] = set()

            already_assigned_sessions: dict = {}

            for grade_count in range(0, len(self.state.grades)):
                already_assigned_sessions[grade_count] = set()

            for grade_count in range(0, len(self.state.grades)):
                
                grade: str = self.state.grades[grade_count]

                for period in range(0, day.periods):
                    pass

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

