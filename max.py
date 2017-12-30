#!/bin/env python

# Import system modules
import sys, os, getopt

# Find modules folder path
modulesPath = os.path.abspath(os.path.dirname(sys.argv[0])) + '/modules'
sys.path.append(modulesPath)

# Global variables
global start_1
global stop_1
global state_1

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
      value = raw_input('MAX cli> ')
      #dummyCommand
   else:
      print('This argument is not suppeorted.')
      if 'cli' in str(sys.argv[1:]):
         print('Did you mean this?')
         print('        max.py cli')
      exit(1)

# Main function
def main():
   #vmName = ui_testing.command()
   return

if __name__=="__main__":
    pars_arg()
    print('Just a test.')
    #main()

