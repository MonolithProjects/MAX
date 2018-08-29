#!/bin/env python

# Import system modules
import sys, os

# Find modules folder path
modulesPath = os.path.abspath(os.path.dirname(sys.argv[0])) + '/modules'
sys.path.append(modulesPath)

# Clear global variables
mChoice = ''
mObject = ''
mAction = ''
modulesList = []

# Load plugins from modules folder
def loadModules():
    for moduleName in os.listdir(modulesPath):
        if not moduleName.startswith("__") and moduleName.endswith(".py"):
            moduleName = moduleName[:-3]
            modulesList.append(moduleName)
            globals()[moduleName] = __import__(moduleName)

# Values
# 0     = off / none
# 0-100 = value in %
# 100   = on
# 101   = unknown / not acceptable
# 102   = drop

############################################################
#TODO: lots of to do :-) Check the issues

############################################################

# Functions
def pars_arg():
    global mChoice, mObject, mAction
    try:
        mChoice = sys.argv[1]
    except IndexError:
        mChoice = 'null'
    try:
        mObject = sys.argv[2]
    except IndexError:
        mObject = 'null'
    try:
        mAction = sys.argv[3]
    except IndexError:
        mAction = 'status'

def runCmd():
    global state
    state = getattr(eval(mChoice), mAction)(mObject)
    ##Dirty but works too:
    # exec("x = " + mChoice +"."+mAction)
    # x(mObject)


# Main function
def main():
    loadModules()
    pars_arg()
    runCmd()

if __name__=="__main__":
    main()
    exit(state)
