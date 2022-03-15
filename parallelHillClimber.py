from solution import SOLUTION
import constants as c
import copy
import os

class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        os.system('rm brain*.nndf')
        os.system('rm fitness*.txt')
        self.nextAvailableID = 0
        self.parents = {}
        for key in range(0, c.populationSize):
            self.parents[key]= SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1  

    def Evolve(self):
        for key in self.parents:
            self.parentVal = self.parents[key]
            self.parentVal.Start_Simulation("DIRECT")

        for key in self.parents:
            self.parentVal = self.parents[key]
            self.parentVal.Wait_For_Simulation_To_End()

        # self.parent.Evaluate("GUI")
        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()

    def Evolve_For_One_Generation(self):
        pass
        # self.Spawn()
        # self.Mutate()
        # self.child.Evaluate("DIRECT")
        # self.Print()
        # self.Select()

    def Spawn(self):
        self.child = copy.deepcopy(self.parent)
        self.child.Set_ID(self.nextAvailableID)
        self.nextAvailableID += 1  


    def Mutate(self):
        self.child.Mutate()
        # print(self.parent.weights)
        # print(self.child.weights)

    def Select(self):
        if (self.parent.fitness > self.child.fitness):
            self.parent = self.child


    def Print(self):
        print("")
        print("")
        print("Parent Fitness: ", self.parent.fitness)
        print("Child Fitness: ", self.child.fitness)
        print("")

    def Show_Best(self):
        pass
        # self.parent.Evaluate('GUI')