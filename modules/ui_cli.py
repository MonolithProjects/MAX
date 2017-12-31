
def cli():
   global mclass, mobject, mvalue
   mclass = ''
   mobject = ''
   mvalue = ''
   command = raw_input('MAX cli> ')
   command = command.split()
   args = len(command)
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
   if mclass not in ('vm', 'light', 'blinds'):
      helpMclass()
      cli()
   elif mclass == 'vm' and not mobject:
      helpMclassVm()
      cli()

def checkMobject(mobject):
   if mclass == 'vm':
      if mobject == 'help':
         helpMclassVm()
         cli()

def checkMvalue(mvalue):
   if mclass == 'vm':
      if mvalue == 'help' or mvalue == '' \
      or mvalue not in ('start', 'stop', 'reboot', 'poweroff', 'state', 'os-state'):
         helpMclassVm()
         cli()

def clearCommands():
   mclass = ''
   mobject = ''
   mvalue = ''

def helpGeneral():
   helpMclass()
   helpMclassVm()
   cli()

def helpMclass():
   print('''
Supported general commands:
   blinds
   light
   vm
   ''')
   
def helpMclassVm():
   print('''
Supported vm commands:
   vm <vm name> start
   vm <vm name> stop
   vm <vm name> reboot
   vm <vm name> poweroff
   vm <vm name> state
   vm <vm name> os-state
   ''')

