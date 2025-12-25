"""
Python script change lowercase characters to uppercase
http://github.com/muhammadli3d
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
1. Load into script editor in Maya under Python tab
2. Select object in outliners that want to change characters
3. Execute
4. All lowercase will change to uppercase
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
"""

import maya.cmds as cmds

string_selected = cmds.ls(selection=True)

for string in string_selected:
    uppercase_string = string.upper()
    cmds.rename(string, uppercase_string)
    print(string + " to " + uppercase_string)
