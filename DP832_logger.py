__author__ = 'RoGeorge'
#
# TODO: Add command line parameters
# TODO: Add stop logging condition(s)
# TODO: Port for Linux
# TODO: Add GUI
# TODO: Create versioned executable distributions
#
from time import *
from sys import *
import os

from functions import connect_verify

# Update the next lines for your own default settings:
logging_step_in_seconds = 10
path_to_save = ""
IP_DP832 = "192.168.1.4"

# CSV data format
header_CSV = "YYYY-MM-DD,HH:MM:SS,V,A,W"

# Rigol/LXI specific constants
port = 5555

small_wait = 1

company = 0
model = 1
serial = 2

# Check parameters
script_name = os.path.basename(argv[0])

# Print usage

'''
print
print "Usage:"
print script_name
'''

# Connect and check instruments
tn_power_source = connect_verify("power supply", IP_DP832, port)

# print "Logging..."
print header_CSV

# Logging loop
while True:
    t1 = time()
    # Read DP832 Channel 1
    tn_power_source.write(":MEAS:ALL? CH1")
    buff = tn_power_source.read_until("\n", small_wait)

    timeString = strftime("%Y-%m-%d,%H:%M:%S", localtime(t1))
    buff = timeString + "," + buff[:-1]
    print buff

    # Wait for the specified logging time interval
    t2 = time()
    while t2-t1 < logging_step_in_seconds:
        t2 = time()

# Close telnet sessions and exit
tn_power_source.close()
print "Normal exit. Bye!"
