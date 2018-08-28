# Lifx buolbs module

# System modules
import sys
import ConfigParser

# Read credentials
config = ConfigParser.ConfigParser()
config.read("/etc/max.conf")
ADAPTER = config.get("cl_cec", "adapter")

def list():
   print('Oops!')
