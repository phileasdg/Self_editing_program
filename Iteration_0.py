import os
import shutil
import sys

# This program edits itself for maxIteration iterations, but it can be modified to do so ad infinitum

# First we define a few variables
maxIteration = 100
currentIteration = 0  # how many times has the program edited itself?
nextIteration = currentIteration + 1  # how many times has the program edited itself?
currentFileName = "Iteration_" + str(currentIteration) + ".py"  # define the name of the current program file
nextFileName = "Iteration_" + str(nextIteration) + ".txt"  # define the name of the next program file

# Second, prepare the new program file to be worked with
shutil.copy(currentFileName, str("2" + currentFileName))  # copy the current file
os.rename(str("2" + currentFileName), nextFileName)  # rename the copy

nextProgramFile = open(nextFileName, "r")  # open the copy for reading
nextProgramFileReadLines = nextProgramFile.readlines()  # read the copy

nextProgramFile = open(nextFileName, "w+")  # open the copy for reading and writing

# Third, we edit the new program file
nextProgramFileReadLines[8] = str(
    "currentIteration = " + str(nextIteration) + "  # how many times has the program edited "
                                                 "itself?\n")
nextProgramFile.writelines(nextProgramFileReadLines)

# Fourth, if there is a previous file iteration saved, we delete it
lastFileName = "Iteration_" + str(currentIteration - 1) + ".py"
if currentIteration > 0:
    print("Last file name: " + lastFileName)
    os.remove(lastFileName)

# Finally, we stop working with the new file, convert it to a python program, and run it
nextProgramFile.close()  # close the new file
os.rename(nextFileName, str(nextFileName.removesuffix(".txt") + ".py"))  # rename the new file
if currentIteration >= maxIteration-1:
    os.remove(currentFileName)
    sys.exit()
else:
    nextFileName = "Iteration_" + str(nextIteration) + ".py"
    print("file specified: " + nextFileName)
    exec(open(nextFileName).read())
    sys.exit()
