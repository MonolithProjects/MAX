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

# Functions
def pars_arg():
   global mclass, mobject, mvalue
   try:
      arg = sys.argv[1]
   except IndexError:
      arg = 'null'
      return
   if arg == 'cli':
      mclass, mobject, mvalue = ui_cli.cli()
   else:
      print('This argument is not supported.')
      if 'cli' in str(sys.argv[1:]):
         print('Did you mean this?')
         print('        max.py cli')
      exit(1)

# Operations
def runCmd():
   global mclass, mobject, mvalue

   # VM (cl_kvm required)
   if mclass == 'vm':
      vmList = cl_kvm.discoverVMs()
      if mobject == '' and mvalue == '':
         ui_cli.displayVmList(vmList)
         return
      elif mobject not in vmList:
         print('Virtual Machine does not exist!')
         return
      elif mvalue == 'start':
         state = cl_kvm.startVm(mobject)
      elif mvalue == 'stop':
         state = cl_kvm.shutVm(mobject)
      elif mvalue == 'reboot':
         state = cl_kvm.rebootVm(mobject)
      elif mvalue == 'poweroff':
         state = cl_kvm.destroyVm(mobject)
      elif mvalue == 'state':
         state = cl_kvm.stateVm(mobject)
      ui_cli.displayVmOutput(state)

   # Lifx
   if mclass == 'lifx':
      if mobject == '' and mvalue == '':
         ui_cli.displayLifxList()
      elif mvalue == 'state':
         ui_cli.displayLifxState()

   # Blinds
   if mclass == 'blinds':
      if mobject == '' and mvalue == '':
         ui_cli.displayBlindsList()
      elif mvalue == 'state':
         ui_cli.displayBlindsState()

   # CEC
   if mclass == 'cec':
      if mobject == '' and mvalue == '':
         ui_cli.displayCecList()
      elif mvalue == 'state':
         ui_cli.displayCecState()

# Main function
def main():
   pars_arg()
   #vmName = ui_testing.command()        #TEST
   #print('Test result --------------v')  #TEST
   #print(mclass)                         #TEST
   #print(mobject)                        #TEST
   #print(mvalue)                         #TEST
   runCmd()

if __name__=="__main__":
   while True:
      main()
