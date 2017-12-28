# System modules
import sys
import libvirt
import ConfigParser

# Authenticate
config = ConfigParser.ConfigParser()
config.read("/etc/max.conf")
IP = config.get("MAXglobal", "IP")
KVM_USER = config.get("MAXglobal", "KVM_USER")
KVM_PASS = config.get("MAXglobal", "KVM_USER")
def request_cred(credentials, user_data):
   for credential in credentials:
      if credential[0] == libvirt.VIR_CRED_AUTHNAME:
         credential[4] = KVM_USER
      elif credential[0] == libvirt.VIR_CRED_PASSPHRASE:
         credential[4] = KVM_PASS
   return 0
auth = [[libvirt.VIR_CRED_AUTHNAME, libvirt.VIR_CRED_PASSPHRASE], request_cred, None]

# KVM connection
def connKvm(c):
   global conn
   if c == 1:
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
   connKvm(1)
   HVname = conn.getHostname()
   print('Hyper-Visor ' + HVname + ' is accessible.')
   connKvm(0)

# Discover VMs
def discoverVms():
   connKvm(1)
   vms = conn.listAllDomains(0)
   if len(vms) != 0:
      for vm in vms:
         print(' ' + vm.name())
   else:
      print(' No VMs')
   connKvm(0)

# Discover Active VMs
def discoverActiveVms():
   connKvm(1)
   vms = conn.listAllDomains(1)
   if len(vms) != 0:
      for vm in vms:
         print(' ' + vm.name())
   else:
      pritn('No active VMs.')
   connKvm(0)

# Discover Inactive VMs
def discoverInactiveVms():
   connKvm(1)
   vms = conn.listAllDomains(2)
   if len(vms) != 0:
      for vm in vms:
         print(' ' + vm.name())
   else:
      pritn('No inactive VMs.')
   connKvm(0)

# Start VM
def startVm(vmName):
   connKvm(1)
   vm = conn.lookupByName(vmName)
   state = vm.isActive()
   if state == True:
      print('VM is already up.')
      return
   vm.create()
   connKvm(0)

# Shutdown VM
def shutVm(vmName):
   connKvm(1)
   vm = conn.lookupByName(vmName)
   state = vm.isActive()
   if state == False:
      print('VM is already down.')
      return
   vm.shutdown()
   connKvm(0)

# Shutdown VM
def rebootVm(vmName):
   connKvm(1)
   vm = conn.lookupByName(vmName)
   state = vm.isActive()
   if state == False:
      print('VM is already down.')
      return
   vm.reboot()
   connKvm(0)

# Destroy VM
def destroyVm(vmName):
   connKvm(1)
   vm = conn.lookupByName(vmName)
   state = vm.isActive()
   if state == False:
      print('VM is already down.')
      return
   vm.destroy()
   connKvm(0)

# XML VM
def xmlVm(vmName):
   connKvm(1)
   vm = conn.lookupByName(vmName)
   raw_xml = vm.XMLDesc(0)
   print(raw_xml)
   connKvm(0)

# listAllDomains flags
#all 0
#VIR_CONNECT_LIST_DOMAINS_ACTIVE
#VIR_CONNECT_LIST_DOMAINS_INACTIVE
#VIR_CONNECT_LIST_DOMAINS_PERSISTENT
#VIR_CONNECT_LIST_DOMAINS_TRANSIENT
#VIR_CONNECT_LIST_DOMAINS_RUNNING
#VIR_CONNECT_LIST_DOMAINS_PAUSED
#VIR_CONNECT_LIST_DOMAINS_SHUTOFF
#VIR_CONNECT_LIST_DOMAINS_OTHER
#VIR_CONNECT_LIST_DOMAINS_MANAGEDSAVE
#VIR_CONNECT_LIST_DOMAINS_NO_MANAGEDSAVE
#VIR_CONNECT_LIST_DOMAINS_AUTOSTART
#VIR_CONNECT_LIST_DOMAINS_NO_AUTOSTART
#VIR_CONNECT_LIST_DOMAINS_HAS_SNAPSHOT
#VIR_CONNECT_LIST_DOMAINS_NO_SNAPSHOT

### Tests...
#def test_out_kvm():
#   dom0 = conn.lookupByName("Windows")
#   print dom0.info()
#   print dom0.state(0)
