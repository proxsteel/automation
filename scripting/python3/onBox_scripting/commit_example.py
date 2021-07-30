"""..."""
import jcs #Junos Commit Script
from junos import Junos_Configuration

#copy script to /var/db/scripts/commit/filename.py or /config/scripts/commit/filename.py
#set system scripts commit file filename.py [load-from-flash]

def main()
    root = Junos_Configuration

    if not (root.xpath("./protocols/isis")):
        jcs.emit_error("ISIS must be enabled!")
    if not (root.xpath("./protocols/bgp")):
        jcs.emit_warning("BGP is not configured, are you sure the config is correct?")
        jcs.syslog('daemon error:', "Warning - config was commited with no BGP configuration stanza")

if __name__ == '__main__':
    main()
