"""
Python script delete all hidden in outliner
http://github.com/muhammadli3d
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
1. Load into script editor in Maya under Python tab
2. Execute
3. It will delete all hidden
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
"""

import maya.cmds as cmds

cmds.delete(cmds.ls(invisible=True, type='transform'))
