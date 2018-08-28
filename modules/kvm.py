# System modules
import sys
import time
import libvirt
import ConfigParser

# Read credentials
config = ConfigParser.ConfigParser()
config.read("/etc/max.conf")
IP = config.get("kvm_module", "IP")
KVM_USER = config.get("kvm_module", "KVM_USER")
KVM_PASS = config.get("kvm_module", "KVM_USER")

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
   IP = config.get("kvm_module", "IP")
   KVM_USER = config.get("kvm_module", "KVM_USER")
   KVM_PASS = config.get("kvm_module", "KVM_USER")


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
         mObject = vm.name()
         vmList.insert(0, mObject)
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
def start(mObject):
   connKvm(100)
   vm = conn.lookupByName(mObject)
   state = vm.isActive()
   if state == False:
      vm.create()
   state = status(mObject)
   return(state)
   connKvm(0)

# Shutdown VM
def stop(mObject):
   connKvm(100)
   vm = conn.lookupByName(mObject)
   state = vm.isActive()
   if state == True:
      vm.shutdown()
      state = waitNewStateOfVm(mObject)
   if state <= 101:
       state = status(mObject)
   return(state)
   connKvm(0)

# Shutdown VM
def rebootVm(mObject):
   connKvm(100)
   vm = conn.lookupByName(mObject)
   state = vm.isActive()
   if state == False:
      return('101')
   vm.reboot()
   return(status(mObject))
   connKvm(0)

# Destroy VM
def destroy(mObject):
   connKvm(100)
   vm = conn.lookupByName(mObject)
   state = vm.isActive()
   if state == True:
       vm.destroy()
   return(status(mObject))
   connKvm(0)

# Status of the VM
def status(mObject):
   connKvm(100)
   vm = conn.lookupByName(mObject)
   state = vm.isActive()
   if state == True:
      return('100')
   elif state == False:
      return('0')
   else:
      return('101')
   connKvm(0)

 # Status checker 30 sec
def waitNewStateOfVm(mObject):
     counter = 0
     state1 = status(mObject)
     state2 = status(mObject)
     while state1 == state2:
        counter = counter + 1
        state2 = status(mObject)
        time.sleep(0.5)
        if counter == 60:
            return('101')


# XML VM
def xmlVm(mObject):
   connKvm(100)
   vm = conn.lookupByName(mObject)
   raw_xml = vm.XMLDesc(0)
   print(raw_xml)
   connKvm(0)
