#----------------------------------------------------------------------------------------
#   Project:    sysMaker
#   File:       logger.py
#   Desc:       This is the file used for logging functions.
#----------------------------------------------------------------------------------------
version = '2'

#----------------------------------------------------------------------------------------
# ██ ███    ███ ██████   ██████  ██████  ████████ ███████
# ██ ████  ████ ██   ██ ██    ██ ██   ██    ██    ██
# ██ ██ ████ ██ ██████  ██    ██ ██████     ██    ███████
# ██ ██  ██  ██ ██      ██    ██ ██   ██    ██         ██
# ██ ██      ██ ██       ██████  ██   ██    ██    ███████
#----------------------------------------------------------------------------------------
from datetime import datetime

#----------------------------------------------------------------------------------------
#  ██████  ██████  ███    ██ ███████ ████████  █████  ███    ██ ████████ ███████
# ██      ██    ██ ████   ██ ██         ██    ██   ██ ████   ██    ██    ██
# ██      ██    ██ ██ ██  ██ ███████    ██    ███████ ██ ██  ██    ██    ███████
# ██      ██    ██ ██  ██ ██      ██    ██    ██   ██ ██  ██ ██    ██         ██
#  ██████  ██████  ██   ████ ███████    ██    ██   ██ ██   ████    ██    ███████
#----------------------------------------------------------------------------------------
LOGFILE = 'sysMaker.log'

#----------------------------------------------------------------------------------------
# ██       ██████   ██████  ██      ███████ ██    ██ ███████ ██
# ██      ██    ██ ██       ██      ██      ██    ██ ██      ██
# ██      ██    ██ ██   ███ ██      █████   ██    ██ █████   ██
# ██      ██    ██ ██    ██ ██      ██       ██  ██  ██      ██
# ███████  ██████   ██████  ███████ ███████   ████   ███████ ███████
#----------------------------------------------------------------------------------------
# This variable determines how much logging to perform.
# Level 0 means no logging will occur.
# Level 1 is basic debugging.
LOGLEVEL = 0

#----------------------------------------------------------------------------------------
# ███████ ██    ██ ███    ██  ██████ ████████ ██  ██████  ███    ██ ███████
# ██      ██    ██ ████   ██ ██         ██    ██ ██    ██ ████   ██ ██
# █████   ██    ██ ██ ██  ██ ██         ██    ██ ██    ██ ██ ██  ██ ███████
# ██      ██    ██ ██  ██ ██ ██         ██    ██ ██    ██ ██  ██ ██      ██
# ██       ██████  ██   ████  ██████    ██    ██  ██████  ██   ████ ███████
#----------------------------------------------------------------------------------------
# Redefined functions
NOW = datetime.now

# Created functions
def log(message, logDate = False):
    if LOGLEVEL > 0:
        f = open(LOGFILE, 'a')
        if logDate:
            f.write('{}\n'.format(NOW()))

        f.write('{}\n'.format(message))
        f.write('\n')
        f.close()
