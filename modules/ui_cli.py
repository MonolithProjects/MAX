
import re

#Consider modules Cmd (in cmd) or readline 

def cli():
   global mclass, mobject, mvalue
   mclass = ''
   mobject = ''
   mvalue = ''
   command = raw_input('MAX cli> ')
   command = command.split()
   args = len(command)
   for i in range(args):
      if i == 0:
         mclass = command[i]
      elif i == 1:
         mobject = command[i]
      elif i == 2:
         mvalue = command[i]
   if args > 0: 
      mclass = command[0]
      checkMclass(mclass)
   if args > 1:
      mobject = command[1]
      checkMobject(mobject)
   if args > 2:
      mvalue = command[2]
      checkMvalue(mvalue)
   if args > 3:
      helpGeneral()
      del command[3:]
      clearCommands()
   return[mclass, mobject, mvalue]

def checkMclass(mclass):
   if mclass not in ('vm', 'lifx', 'blinds'):
      if mclass == 'exit':
         exit(0)
      helpMclass()
      cli()

def checkMobject(mobject):
   if mclass == 'vm':
      if mobject == 'help' \
      or mobject != '' and mvalue == '':
         helpMclassVm()
         cli()
   if mclass == 'lifx':
      if mobject == 'help' \
      or mobject != '' and mvalue == '':
         helpMclassLifx()
         cli()

   if mclass == 'blinds':
      if mobject == 'help' \
      or mobject != '' and mvalue == '':
         helpMclassBlinds()
         cli()


def checkMvalue(mvalue):
   if mclass == 'vm':
      if mvalue == 'help' \
      or mvalue not in ('start', 'stop', 'reboot', 'poweroff', 'state', 'os-state'):
         helpMclassVm()
         cli()

   if mclass == 'lifx':
      if mvalue == 'help' \
      or mvalue not in ('on', 'off', 'off-slow', 'state'):
         if re.search('rgb-([0-2][0-5][0-5])-([0-2][0-5][0-5])-([0-2][0-5][0-5])', mvalue):
            return
         else:
            helpMclassLifx()
            cli()

   if mclass == 'blinds':
      if mvalue == 'help' \
      or mvalue not in ('on', 'off', 'off-slow', 'rgb', 'state'):
         for i in range(0, 100):
            if 'hight-'+str(i) == mvalue:
               return
         for i in range(0, 180):   
            if 'rotate-'+str(i) == mvalue:
               return
         helpMclassBlinds()
         cli()


def clearCommands():
   mclass = ''
   mobject = ''
   mvalue = ''

def helpGeneral():
   helpMclass()
   helpMclassVm()
   helpMclassLifx()
   helpMclassBlinds()
   cli()

def helpMclass():
   print('''
Supported general commands:
   blinds
   lifx
   vm
   
   Combine with "help" for more details.
   ''')
   
def helpMclassVm():
   print('''
Supported vm commands:
   vm                     (command will list all VMs)
   vm <vm name> start     (command will start VM)
   vm <vm name> stop      (command will shutdown VM)
   vm <vm name> reboot    (command will reboot VM)
   vm <vm name> poweroff  (command will force poweroff VM)
   vm <vm name> state     (command will check VM state)
   vm <vm name> os-state  (command will check the OS state)
   vm help                (display this page)
   ''')

def helpMclassLifx():
   print('''
Supported lifx commands:
   lifx                                                (command will list all LIFX bulbs)
   lifx <bulb name> on                                 (command will lite on a bulb)
   lifx <bulb name> off                                (command will lite off a bulb)
   lifx <bulb name> off-slow                           (command will lite off/dim a bulb)
   lifx <bulb name> rgb-[000-255]-[000-255]-[000-255]  (command will set RGB color)
   lifx <bulb name> state                              (command will check bulb state)
   lifx help                                           (display this page)
   ''')

def helpMclassBlinds():
   print('''
Supported blinds commands:
   blinds                               (command will list all blids)
   blinds <blinds name> up              (command will bring the blinds up)
   blinds <blinds name> down            (command will bring the blinds down) 
   blinds <blinds name> hight-[0-100]   (command will shade part of the window in %) 
   blinds <blinds name> rotate-[0-180]  (command will rotate)
   blinds help                          (display this page)
   ''')

