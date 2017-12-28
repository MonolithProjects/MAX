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
   print(modulesPath)
   out_kvm.testKvmConnection()
   print('------v')
   out_kvm.rebootVm(vmName="zero1") 
   print('------v')
   #out_kvm.destroyVm(vmName="zero1")
   


if __name__=="__main__":
   main()

