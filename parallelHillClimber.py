from solution import SOLUTION
import constants as c
import copy
import os
import numpy as np

class PARALLEL_HILL_CLIMBER:
    def __init__(self, dataID):
        os.system('rm brain*.nndf')
        os.system('rm fitness*.txt')
        self.nextAvailableID = 0
        self.dataID = dataID
        self.parents = {}
        for key in range(0, c.populationSize):
            self.parents[key]= SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1 

        self.genCount = 0
        self.fitData = np.empty([c.populationSize,c.numberOfGenerations])


    def Evolve(self):
        self.Evaluate(self.parents)
        
        # self.parent.Evaluate("GUI")
        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()
            self.genCount += 1
    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        self.Print()
        self.Select()

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
            self.solutionVal = solutions[key]
            self.solutionVal.Wait_For_Simulation_To_End()

    def Select(self):
        for key in self.parents:
            if (self.parents[key].fitness < self.children[key].fitness):
                self.parents[key] = self.children[key]

            self.fitData[key, self.genCount] = self.parents[key].fitness


    def Print(self):
        for adultkey in self.parents:
            # for kidkey in self.children:
            self.singleParent = self.parents[adultkey]
            self.singleChild = self.children[adultkey]
            print("")
            print("Parent Fitness: ", self.singleParent.fitness," Child Fitness: ", self.singleChild.fitness )
            print("")
                
        
        

    def Show_Best(self):
        self.highFit = self.parents[0]
        for key in self.parents:
            if self.parents[key].fitness > self.highFit.fitness:
                self.highFit = self.parents[key]

        self.highFit.Start_Simulation("GUI")
        print("Final Fitness Value: ", self.highFit.fitness)
        
        self.save_path = '/Users/janeyalex/Documents/CS206/JaneysBots/data'
        self.file_name = "fitnessDataB"+ str(self.dataID)
        self.completeName = os.path.join(self.save_path, self.file_name)

        np.save(self.completeName,self.fitData)

