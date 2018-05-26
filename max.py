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
#CLI-less mode state return
############################################################

# Functions
def pars_arg():
    global mclass, mobject, mvalue, arg
    try:
        arg = sys.argv[1]
    except IndexError:
        arg = 'null'
        return
    if arg == 'cli':
        return
        #mclass, mobject, mvalue = cli.cli()
    elif arg in modulesList:
        try:
          mclass = sys.argv[2]
        except IndexError:
            mclass = 'null'
            #return
        try:
            mobject = sys.argv[3]
        except IndexError:
            mobject = 'null'
            #return
        try:
            mvalue = sys.argv[4]
        except IndexError:
            mvalue = 'null'
            #return
    else:
       print('This argument is not supported.')
       if 'cli' in str(sys.argv[1:]):
           print('Did you mean this?')
           print('        max.py cli')
       exit(1)

def runCli():
    global mclass, mobject, mvalue
    mclass, mobject, mvalue = cli.cli()

# Operations
def runCmd():
    # VM (kvm required)
   global arg, state
   if mclass == 'vm':
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
    pars_arg()
    if arg == 'cli':
        while True:
            runCli()
            state = runCmd()
            cli.displayVmOutput(state)
    elif arg in modulesList:
        runCmd()

   # print('Test result --------------v')  #TEST
   # print(mclass)                         #TEST
   # print(mobject)                        #TEST
   # print(mvalue)                         #TEST

if __name__=="__main__":
    main()
