
import re

# OBSOLETE CLI!!!!!!!!!!!!!!!!
# ONLY FOR REFERENCE

def cli():
   global mclass, mobject, mvalue
   clearCommands()
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
   if mclass not in ('kvm', 'lifx', 'blinds', 'cec'):
      if mclass == 'exit':
         exit(0)
      helpMclass()
      cli()

def checkMobject(mobject):
   if mclass == 'kvm':
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

   if mclass == 'cec':
      if mobject == 'help' \
      or mobject != '' and mvalue == '':
         helpMclassCec()
         cli()



def checkMvalue(mvalue):
   if mclass == 'kvm':
      if mvalue == 'help' \
      or mvalue not in ('start', 'stop', 'reboot', 'poweroff', 'state'):
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

   if mclass == 'cec':
      if mvalue == 'help' \
      or mvalue not in ('on', 'off', 'state'):
         helpMclassCec()
         cli()

def clearCommands():
   global mclass, mobject, mvalue
   mclass = ''
   mobject = ''
   mvalue = ''

def displayVmList(vmList):
   longest = len(max(vmList, key=len))
   space = longest - 8
   print('+-' + '-'*longest +'-+')
   print('| VM list:' + ' ' * space + ' |')
   print('+-' + '-'*longest +'-+')
   for vm in sorted(vmList, key=str.lower):
      space = longest - len(vm)
      print('| ' + vm + ' ' * space +' |' )
   print('+-' + '-'*longest +'-+')

def displayVmOutput(state):
   if state == '100':
      state = 'active'
   elif state == '0':
      state = 'off'
   elif state == '101':
      state = 'unable to chage the state'

   if state != None :
      print('+----' + '-'*len(mobject) + '----' + '-'*len(state) + '-+')
      print('| VM ' + mobject + ' is ' + state + ' |')
      print('+----' + '-'*len(mobject) + '----' + '-'*len(state) + '-+')
#    else:
#       print('''+------------------+
# |  Success         |
# +------------------+''')



def displayLifxList():
   print('Oops!')

def displayLifxState():
   print('Oops!')

def displayBlindsList():
   print('Oops!')

def displayBlindsState():
   print('Oops!')

def displayCecList():
   print('Oops!')

def displayCecState():
   print('Oops!')

def helpGeneral():
   helpMclass()
   helpMclassVm()
   helpMclassLifx()
   helpMclassBlinds()
   helpMclassCec()
   cli()

def helpMclass():
   print('''
+---------------------------------------+
|  Supported general commands:          |
+---------------------------------------+
|  blinds                               |
|  cec                                  |
|  lifx                                 |
|  kvm                                  |
|  exit                                 |
+---------------------------------------+
|  Combine with "help" for more details.|
+---------------------------------------+
   ''')

def helpMclassVm():
   print('''
+----------------------------------------------------------+
|  Supported kvm commands:                                 |
+----------------------------------------------------------+
|  kvm                    (command will list all VMs)      |
|  kvm <vm name> start    (command will start VM)          |
|  kvm <vm name> stop     (command will shutdown VM)       |
|  kvm <vm name> reboot   (command will reboot VM)         |
|  kvm <vm name> poweroff (command will force poweroff VM) |
|  kvm <vm name> state    (command will check VM state)    |
|  kvm help               (display this page)              |
+----------------------------------------------------------+
   ''')

def helpMclassLifx():
   print('''
+-----------------------------------------------------------------------------------------+
|  Supported lifx commands:                                                               |
+-----------------------------------------------------------------------------------------+
|  lifx                                                (command will list all LIFX bulbs) |
|  lifx <bulb name> on                                 (command will lite on a bulb)      |
|  lifx <bulb name> off                                (command will lite off a bulb)     |
|  lifx <bulb name> off-slow                           (command will lite off/dim a bulb) |
|  lifx <bulb name> rgb-[000-255]-[000-255]-[000-255]  (command will set RGB color)       |
|  lifx <bulb name> state                              (command will check bulb state)    |
|  lifx help                                           (display this page)                |
+-----------------------------------------------------------------------------------------+
   ''')

def helpMclassBlinds():
   print('''
+-------------------------------------------------------------------------------------+
|  Supported blinds commands:                                                         |
+-------------------------------------------------------------------------------------+
|  blinds                               (command will list all blids)                 |
|  blinds <blinds name> up              (command will bring the blinds up)            |
|  blinds <blinds name> down            (command will bring the blinds down)          |
|  blinds <blinds name> hight-[0-100]   (command will shade part of the window in %)  |
|  blinds <blinds name> rotate-[0-180]  (command will rotate)                         |
|  blinds <blinds name> state           (command will check the blinds state)         |
|  blinds help                          (display this page)                           |
+-------------------------------------------------------------------------------------+
   ''')

def helpMclassCec():
   print('''
+-----------------------------------------------------------------+
|  Supported cec commands:                                        |
+-----------------------------------------------------------------+
|  cec                     (command will list all CEC devices)    |
|  cec <vm name> on        (command will start CEC device)        |
|  cec <vm name> off       (command will stop CEC device)         |
|  cec <vm name> state     (command will check CEC device state)  |
|  cec help                (display this page)                    |
+-----------------------------------------------------------------+
   ''')
