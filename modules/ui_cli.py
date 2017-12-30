
def cli():
   command = raw_input('MAX cli> ')
   command = command.split()
   #print(command)
   mclass = command[0]
   mobject = command[1]
   mvalue = command[2]
   return[mclass, mobject, mvalue]
