from models import *
from helpers import available_sessions,assign_session
import random
from collections import Counter

class GeneticAlgorithm:
    def __init__(self, state: State, parameters: dict):
        self.state = state
        self.parameters = parameters

    def execute(self):
        pass

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
                        possible_assignments: list = available_sessions(self.state, result, \
                            already_assigned_educators, already_assigned_sessions, grade_count, period)

                        session_id: int = random.choice(possible_assignments)

                        if period == 4 or period == (day.periods - 1):
                            assign_session(self.state, result, session_id, already_assigned_educators, \
                                            already_assigned_sessions, day_count,grade_count,period)

                        else:
                            random_point: float = random.random()

                            if random_point <= 0.4:
                                assign_session(self.state, result, session_id, already_assigned_educators, \
                                                already_assigned_sessions, day_count,grade_count,period)
                            else:
                                possible_assignments_for_next_period: list = available_sessions(self.state, \
                                    result, already_assigned_educators, already_assigned_sessions, \
                                        grade_count, period + 1)

                                if session_id in possible_assignments_for_next_period == False:
                                    assign_session(self.state, result, session_id, already_assigned_educators, \
                                                already_assigned_sessions, day_count,grade_count,period)
                                else:
                                    assign_session(self.state, result, session_id, already_assigned_educators, \
                                                already_assigned_sessions, day_count,grade_count,period)

                                    assign_session(self.state, result, session_id, already_assigned_educators, \
                                                already_assigned_sessions, day_count,grade_count,period + 1)
                                    

        return result

    def initial_population(self) -> list:
        """
            creates the initial population for the genetic algorithm
        """
        result: list = list()
        
        for _ in range(0,self.parameters["population_size"]):
            result.append(self.random_individual())

        return result
        
    def fitness(self, individual: list) -> float:
        """
            evaluates the fitness of the individual
        """

        assignments_count:Counter = Counter(individual)
        remaining = sum(value.classes - assignments_count[key] for (key,value) in self.state.sessions)

        return 1 / ( 1 + remaining)

    def crossover(self, parent_one: list, parent_two: list) -> tuple:
        """
            swaps the genes of two individuals(schedules)
        """

        size = len(parent_one)
        crossover_day: int = random.randint(0,len(self.state.structure) - 1)
        crossover_index: int = self.state.schedule_index(crossover_day)

        offspring_one: list = [parent_one[count] if count < crossover_index else None for count in range(0,size)]
        offspring_two: list = [parent_two[count] if count < crossover_index else None for count in range(0,size)]

        for day_count in range(crossover_day, len(self.state.structure)):
            
            day: Day = self.state.structure[day_count]
            already_assigned_educators_one: dict = {}
            already_assigned_educators_two: dict = {}

            for period in range(0, day.periods):
                already_assigned_educators_one[period] = set()
                already_assigned_educators_two[period] = set()

            already_assigned_sessions_one: dict = {}
            already_assigned_sessions_two: dict = {}

            for grade_count in range(0, len(self.state.grades)):
                already_assigned_sessions_one[grade_count] = set()
                already_assigned_sessions_two[grade_count] = set()

            for grade_count in range(0, len(self.state.grades)):
                
                for period in range(0, day.periods):
                    
                    index: int = self.state.schedule_index(day_count,grade_count,period)

                    if offspring_one[index] == None:
                        possible_assignments: list = available_sessions(self.state, offspring_one, \
                            already_assigned_educators_one, already_assigned_sessions_one, grade_count, period)

                        if parent_two[index] in possible_assignments:
                            assign_session(self.state, offspring_one, parent_two[index], already_assigned_educators_one, \
                                                already_assigned_sessions_one, day_count,grade_count,period)

                    if offspring_two[index] == None:
                        possible_assignments: list = available_sessions(self.state, offspring_two, \
                            already_assigned_educators_two, already_assigned_sessions_two, grade_count, period)

                        if parent_one[index] in possible_assignments:
                            assign_session(self.state, offspring_one, parent_one[index], already_assigned_educators_two, \
                                                already_assigned_sessions_two, day_count,grade_count,period)

        self.repair(offspring_one)
        self.repair(offspring_two)

        return (offspring_one, offspring_two)


    def mutate(self, individual: list) -> list:
        pass

    def repair(self, individual: list):
        pass

