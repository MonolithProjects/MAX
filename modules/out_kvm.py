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

# Test HV connection
def test_kvm_connection():
   conn = libvirt.openAuth('qemu+tcp://' + IP + '/system', auth, 0)
   if conn == None:
      print('Failed to open connection to Hyper-Visor')
      return
   HVname = conn.getHostname()
   print('Hyper-Visor ' + HVname + ' is accessible.')
   conn.close()

# Start VM
#def start_vm():


### Tests...
#def test_out_kvm():
#   dom0 = conn.lookupByName("Windows")
#   print dom0.info()
#   print dom0.state(0)
