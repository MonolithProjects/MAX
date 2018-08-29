#!/bin/env python

# MAX Command line interface

import hub
import os
import types




def cli():
   global mClass, mObject, mAction, modulesList
   clearCommands()
   maxModulesList = checkModules()

   command = raw_input('maxctl> ')
   command = command.split()
   args = len(command)
   for i in range(args):
      if i == 0:
         mClass = command[i]
      elif i == 1:
         mObject = command[i]
      elif i == 2:
         mAction = command[i]
   if args > 0:
      checkmClass(mClass)
   if args > 1:
      checkmObject(mObject)
   if args > 2:
      checkmValue(mvalue)
   if args > 3:
      helpGeneral()
      del command[3:]
      clearCommands()
   # return[mClass, mObject, mAction]

def checkModules():
   maxModulesList = []
   for file in os.listdir('modules/'):
      if file.endswith('.py'):
          file = file[:-3]
          maxModulesList.append(file)
   unwanted = maxModulesList.index('__init__')
   maxModulesList.pop(unwanted)
   return(maxModulesList)

def checkmClass(mClass):
   if mclass not in ('kvm', 'lifx', 'blinds', 'cec'):
      if mclass == 'exit':
         exit(0)
      helpMclass()
      cli()

def clearCommands():
   global mClass, mObject, mAction
   mClass = ''
   mObject = ''
   mAction = ''

def main():
    cli()

if __name__=="__main__":
    main()
