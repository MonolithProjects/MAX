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
      global mclass
      global mobject
      global mvalue
      mclass, mobject, mvalue = ui_cli.cli()
   else:
      print('This argument is not suppeorted.')
      if 'cli' in str(sys.argv[1:]):
         print('Did you mean this?')
         print('        max.py cli')
      exit(1)

# Main function
def main():
   pars_arg()
   #vmName = ui_testing.command()
   print('Test result --------------v')
   print(mclass)
   print(mobject)
   print(mvalue)
   return

if __name__=="__main__":
    main()

