# System modules
import sys
import libvirt
import ConfigParser

# Variables (later moved to config file)
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

# Create connection
auth = [[libvirt.VIR_CRED_AUTHNAME, libvirt.VIR_CRED_PASSPHRASE], request_cred, None]
conn = libvirt.openAuth('qemu+tcp://' + IP + '/system', auth, 0)


### Tests...
dom0 = conn.lookupByName("Windows")
print dom0.info()
print dom0.state(0)


# Closing the connection
conn.close()
