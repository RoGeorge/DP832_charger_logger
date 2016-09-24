# DP832_charger_logger
'**DP832_logger.py**' is a Python script that periodically reads the measured Voltage, Current and Power outputs from all 3 channels of a power source model Rigol DP832. The read values are listed at the console output and recorded in a CSV file, together with a timestamp.

<pre># Print usage
def print_help():
    print
    print "This program periodically reads the measured output values"
    print "    for all 3 channels of a Rigol DP832 power source."
    print
    print "    The reading time interval (in seconds) can be specified"
    print "    in the command line. A timestamp is added for each new reading."
    print
    print "    At each new reading, the Voltage, Current and Power for each channel"
    print "    are listed in CSV format, then saved in a log file. The log file"
    print '    is saved as "MODEL_YYYY-MM-DD_HH.MM.SS.csv"'
    print
    print "The program is using LXI protocol, so the computer"
    print "    must have LAN connection with the DP832 instrument."
    print "    USB and/or GPIB connections are not used by this software."
    print
    print "    No VISA, IVI or Rigol drivers are needed."
    print
    print "Usage syntax:"
    print "    " + "python " + scriptName + " [read_interval [instrument_IP]]"
    print
    print "Usage examples:"
    print "    " + "python " + scriptName + "                   # log outputs (1s, 192.168.1.4)"
    print "    " + "python " + scriptName + " 60                # log at each minute (192.168.1.4)"
    print "    " + "python " + scriptName + " 3600 192.168.1.7  # log hourly from IP 192.168.1.7"
    print
    print "To end the logging, press 'ESC'."
    print
    print
    print
</pre>