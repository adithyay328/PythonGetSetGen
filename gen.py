import os
import sys
import copy

try:
    os.remove("output.py")
except:
    pass

sourceFile = open("template.py", "r")
source = sourceFile.read()

outputFile = open("output.py", "a")

for i in range(1, len(sys.argv)):
    copyString = copy.deepcopy(source)
    outputFile.write(copyString.replace("REPLACED", sys.argv[i]))