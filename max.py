#!/bin/env python

# Import system modules
import sys, os

# Find modules folder path
modulesPath = os.path.abspath(os.path.dirname(sys.argv[0])) + '/modules'
sys.path.append(modulesPath)

# Clear global variables
mclass = ''
mobject = ''
mvalue = ''
modulesList = []

# Load plugins from modules folder
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
#TODO:
#CLI - state fix and Success msg
############################################################

# Functions
def pars_arg():
    global mclass, mobject, mvalue
    try:
        mclass = sys.argv[1]
        if mclass == 'cli':
            return
    except IndexError:
        mclass = 'null'
        return
    try:
        mobject = sys.argv[2]
    except IndexError:
        mobject = 'null'
        #return
    try:
        mvalue = sys.argv[3]
    except IndexError:
        mvalue = 'null'
        #return

def runCli():
    global mclass, mobject, mvalue
    mclass, mobject, mvalue = cli.cli()

# Operations
def runCmd():
    # VM (kvm required)
   global state
   if mclass == 'kvm':
      vmList = kvm.discoverVMs()
      if mobject == '' and mvalue == '':
         cli.displayVmList(vmList)
         return
      elif mobject not in vmList:
         print('Virtual Machine does not exist!')
         return
      elif mvalue == 'start':
         state = kvm.startVm(mobject)
      elif mvalue == 'stop':
         state = kvm.shutVm(mobject)
      elif mvalue == 'reboot':
         state = kvm.rebootVm(mobject)
      elif mvalue == 'poweroff':
         state = kvm.destroyVm(mobject)
      elif mvalue == 'state':
         state = kvm.stateVm(mobject)
      return(state)


   # Lifx
   if mclass == 'lifx':
      if mobject == '' and mvalue == '':
         cli.displayLifxList()
      elif mvalue == 'state':
         cli.displayLifxState()

   # Blinds
   if mclass == 'blinds':
      if mobject == '' and mvalue == '':
         cli.displayBlindsList()
      elif mvalue == 'state':
         cli.displayBlindsState()

   # CEC
   if mclass == 'cec':
      if mobject == '' and mvalue == '':
         cli.displayCecList()
      elif mvalue == 'state':
         cli.displayCecState()

# Main function
def main():
    #global state
    pars_arg()
    if mclass == 'cli':
        while True:
            runCli()
            state = runCmd()
            cli.displayVmOutput(state)
    elif mclass in modulesList:
        runCmd()


   # print('Test result --------------v')  #TEST
   # print(mclass)                         #TEST
   # print(mobject)                        #TEST
   # print(mvalue)                         #TEST

if __name__=="__main__":
    main()
    exit(state)
