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
   out_kvm.testKvmConnection()
   print('------v')
   #out_kvm.rebootVm(vmName="zero1") 
   print('------v')
   out_kvm.startVm(vmName="zero1")
   out_kvm.stateVm(vmName="zero1")
   if out_kvm.stateVm(vmName="zero1") == 'off':
      print('Ta je dole...')
   else:
      print('Ta je hore')   

   #for vm in out_kvm.discoverVms():
   #   print(vm.name() + ' is my VM.')
   out_kvm.discoverVms()

if __name__=="__main__":
   main()

