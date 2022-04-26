import os
from parallelHillClimber import PARALLEL_HILL_CLIMBER

# for i in range(0,5):
#     os.system("python3 generate.py")
#     os.system("python3 simulate.py")
dataID= 1
for i in range(2):
    phc = PARALLEL_HILL_CLIMBER(dataID)
    phc.Evolve()
    phc.Show_Best()