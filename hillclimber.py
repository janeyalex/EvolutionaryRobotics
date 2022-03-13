from solution import SOLUTION
# import constants as c
# import copy

class HILL_CLIMBER:
    def __init__(self):
        self.parent = SOLUTION()

    def Evolve(self):
        self.parent.Evaluate()
        
        # for currentGeneration in range(c.numberOfGenerations):
        #     self.Evolve_For_One_Generation()

    def Evolve_For_One_Generation(self):
        pass
            # self.Spawn()
            # self.Mutate()
            # self.child.Evaluate()
            # self.Select()

    def Spawn(self):
        pass
        # self.child = copy.deepcopy(self.parent)


    def Mutate(self):
        pass
        # self.child.Mutate()
        # print(self.parent.weights)
        # print(self.child.weights)
        # exit()

    def Select(self):
        pass



