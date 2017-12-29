#!/bin/env python

# Import system modules
import sys, os

# Find modules folder path
modulesPath = os.path.abspath(os.path.dirname(sys.argv[0])) + '/modules'
sys.path.append(modulesPath)

# Global variables
global start_1
global stop_1
global state_1

# Import MAX modules
import in_testing
import out_kvm

############################################################

# Main functions
def main():
   ### Tests :-)
   print(modulesPath)
   vmName = in_testing.command()
   print('------v')
   if out_kvm.stateVm(vmName) == 'on':
      print('Running')
   else:
      print('Stopped')

if __name__=="__main__":
   main()

