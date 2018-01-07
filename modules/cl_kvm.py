# System modules
import sys
import libvirt
import ConfigParser

# Read credentials
config = ConfigParser.ConfigParser()
config.read("/etc/max.conf")
IP = config.get("MAXglobal", "IP")
KVM_USER = config.get("MAXglobal", "KVM_USER")
KVM_PASS = config.get("MAXglobal", "KVM_USER")

# Request credentials
def request_cred(credentials, user_data):
   for credential in credentials:
      if credential[0] == libvirt.VIR_CRED_AUTHNAME:
         credential[4] = KVM_USER
      elif credential[0] == libvirt.VIR_CRED_PASSPHRASE:
         credential[4] = KVM_PASS
   return 0

# Read config file
def readConfig():
   config = ConfigParser.ConfigParser()
   config.read("/etc/max.conf")
   IP = config.get("MAXglobal", "IP")
   KVM_USER = config.get("MAXglobal", "KVM_USER")
   KVM_PASS = config.get("MAXglobal", "KVM_USER")


# KVM connection
def connKvm(c):
   global conn
   if c == 100:
      auth = [[libvirt.VIR_CRED_AUTHNAME, libvirt.VIR_CRED_PASSPHRASE], request_cred, None]
      conn = libvirt.openAuth('qemu+tcp://' + IP + '/system', auth, 0)
      if conn == None:
         print('Failed to open connection to KVM')
         return
   elif c == 0:
      conn.close()
   else:
      print('Error: incorrect connKvm flag.')
      exit(1)

# Test HV connection
def testKvmConnection():
   connKvm(100)
   HVname = conn.getHostname()
   print('Hyper-Visor ' + HVname + ' is accessible.')
   connKvm(0)

# Discover VMs
def discoverVmsOLD():
   connKvm(100)
   vms = conn.listAllDomains(0)
   if len(vms) != 0:
      return(vms)
   else:
      return('0')
   connKvm(0)

# Discover VMs (new)
def discoverVMs():
   connKvm(100)
   vms = conn.listAllDomains(0)
   vmList = []
   if len(vms) != 0:
      for vm in vms: 
         #print(' ' + vm.name())
         vmName = vm.name()
         vmList.insert(0, vmName)
      return(vmList)
   connKvm(0)

# Discover Active VMs
def discoverActiveVms():
   connKvm(100)
   vms = conn.listAllDomains(1)
   if len(vms) != 0:
      return(vms)  
   else:
      return('0')
   connKvm(0)

# Discover Inactive VMs
def discoverInactiveVms():
   connKvm(100)
   vms = conn.listAllDomains(2)
   if len(vms) != 0:
      return(vms) 
   else:
      return('0')
   connKvm(0)

# Start VM
def startVm(vmName):
   connKvm(100)
   vm = conn.lookupByName(vmName)
   state = vm.isActive()
   if state == True:
      return('101')
   vm.create()
   connKvm(0)

# Shutdown VM
def shutVm(vmName):
   connKvm(100)
   vm = conn.lookupByName(vmName)
   state = vm.isActive()
   if state == False:
      return('101')
   vm.shutdown()
   connKvm(0)

# Shutdown VM
def rebootVm(vmName):
   connKvm(100)
   vm = conn.lookupByName(vmName)
   state = vm.isActive()
   if state == False:
      return('101')
   vm.reboot()
   connKvm(0)

# Destroy VM
def destroyVm(vmName):
   connKvm(100)
   vm = conn.lookupByName(vmName)
   state = vm.isActive()
   vm.destroy()
   connKvm(0)

# State of the VM
def stateVm(vmName):
   connKvm(100)
   vm = conn.lookupByName(vmName)
   state = vm.isActive()
   if state == True:
      return('100')
   elif state == False:
      return('0')
   else:
      return('101')
   connKvm(0)

# XML VM
def xmlVm(vmName):
   connKvm(100)
   vm = conn.lookupByName(vmName)
   raw_xml = vm.XMLDesc(0)
   print(raw_xml)
   connKvm(0)
