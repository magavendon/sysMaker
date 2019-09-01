# ----------------------------------------------------------------------------------------
#   Project:    sysMaker
#   File:       logger.py
# ----------------------------------------------------------------------------------------
'''Used for output logs when running the program.'''

import yaml

with open('.config/logger.conf') as f:
    configData = yaml.load(f, Loader=yaml.FullLoader)

def log(output, level = 3, oFile = configData['default_file']):
    '''Send messages to a log file.
    <table><tr><th>Paramater &nbsp;</th><th>Purpose</th></tr>
    <tr><td>output</td><td>The message to send to the log file.</td></tr>
    <tr><td>level</td><td>What log level to use. 0 = None, 1 = Min, 2 = More, 
    3 = Max</td></tr>
    <tr><td>oFile</td><td>The file to use for logging. By default the file
    used is defined in logger.conf as <b>default_file</b>.</td></tr></table>'''
    pass
