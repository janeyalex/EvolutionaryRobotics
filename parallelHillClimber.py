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
        self.Evaluate(self.parents)


        # self.parent.Evaluate("GUI")
        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        # self.Print()
        # self.Select()

    def Spawn(self):
        self.children ={}
        for key in self.parents:
            self.parentVal = self.parents[key]
            self.newChild = copy.deepcopy(self.parentVal)
            self.children[key]= self.newChild
            self.newChild.Set_ID(self.nextAvailableID)
            self.nextAvailableID += 1  

    def Mutate(self):
        for key in self.children:
            self.kid = self.children[key]
            self.kid.Mutate()

    def Evaluate(self, solutions):
        for key in solutions:
            self.solutionVal = solutions[key]
            self.solutionVal.Start_Simulation("DIRECT")

        for key in solutions:
            self.solutionVal = self.parents[key]
            self.solutionVal.Wait_For_Simulation_To_End()

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