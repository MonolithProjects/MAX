#!/bin/env python

# Import system modules
import sys, os

# Find modules folder path
modules_path = os.path.abspath(os.path.dirname(sys.argv[0])) + '/modules'
sys.path.append(modules_path)

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
   print(modules_path)
   print('test')
   in_testing.cli_test() 

if __name__=="__main__":
   main()

