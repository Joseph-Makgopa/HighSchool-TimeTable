class GeneticAlgorithm:
    def __init__(self,state,parameters):
        self.state = state
        self.parameters = parameters

    def random_individual(self):
        for day_count in range(0,len(self.state.structure.days)):
            day = self.state.structure.days[day_count]
            already_assigned_educator = {}
            already_assigned_session = {}

            for grade_count in range(0,len(self.state.grades)):
                grade = self.state.grades[grade_count]
                already_assigned_educator[grade] = []

                for period in range(0,day.periods):
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

