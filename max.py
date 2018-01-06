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

# Import User Interface MAX modules
import ui_testing
import ui_cli

# Import Control MAX modules
import cl_kvm

# Values
# 0     = off / none
# 0-100 = value in %
# 100   = on
# 101   = unknown / not acceptable

############################################################

# Functions
def pars_arg():
   try:
      arg = sys.argv[1]
   except IndexError:
      arg = 'null'
      return
   if arg == 'cli':
      global mclass, mobject, mvalue
      mclass, mobject, mvalue = ui_cli.cli()
   else:
      print('This argument is not supported.')
      if 'cli' in str(sys.argv[1:]):
         print('Did you mean this?')
         print('        max.py cli')
      exit(1)

# CLI
def runCmd():
   global mclass, mobject, mvalue
   
  # VM
  if mclass == 'vm':
      if mobject == '' and mvalue == '':
         ui_cli.displayVmList()
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

      if state is None:
         print('Success')
      else: 
         if state == '100':
            state = 'active'
         elif state == '0':
            state = 'off'
         elif state == '101':
            state = 'unable to ' + mvalue
         print('VM ' + mobject + ' is ' + state)
         
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

