"""
Python script create material by typing name only. This script use'pb_'(blinn) as
playblast material and 's_'(aiStandardSurface) for Arnold material shader workflow.
http://github.com/muhammadli3d
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
Steps using the script
1. Load into script editor in Maya under Python tab
2. Execute
3. Pop out UI to create material
4. Type name and click "Create"
5. or can press Enter (Only work on Numpad Enter key)
6. It will automatically create and connect blinn(pb_) and aiStandardSurface(s_)
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
"""

import maya.cmds as cmds

def create_material(material_name):
    mat = cmds.textField(material_name, query=True, text=True)
    pb_mat='pb_'+ mat
    s_mat='s_'+ mat
    mat_SG=pb_mat+'SG'
    
    # Create material, blinn for pb_, aiStandardSurface for s_ and SG is shading group
    blinn_material = cmds.shadingNode('blinn', asShader=True, name=pb_mat)
    aiSS_material = cmds.shadingNode('aiStandardSurface', asShader=True, name=s_mat)
    SG_material= cmds.sets(r=True, nss=True, em=True, name=mat_SG)
    
    # Connect all three nodes
    cmds.connectAttr(blinn_material + '.outColor', SG_material + '.surfaceShader', f=True)
    cmds.connectAttr(aiSS_material + '.outColor', SG_material + '.aiSurfaceShader', f=True)
    
    return blinn_material, aiSS_material, SG_material
    
def ui_create_material():
    # If the window ald open, it will close the window before (Avoid multiple and overlap)
    if cmds.window('create_material', exists=True):
        cmds.deleteUI('create_material')

    # Window size
    window = cmds.window('create_material', title='Create Material', widthHeight=(380,75))
    cmds.columnLayout(adjustableColumn=True)
    
    # Name the material
    cmds.rowColumnLayout( numberOfColumns=2, columnAttach=(1, 'right', 0), columnWidth=[(1, 100), (2, 200)] )
    cmds.text( label='Name: ' )
    material_name = cmds.textField(enterCommand=lambda x: create_material(material_name))
    cmds.textField( material_name, edit=True)
    cmds.setParent('..')

    # Apply, Close
    cmds.columnLayout(adjustableColumn=True)
    cmds.button(label='Apply', command=lambda x:create_material(material_name))
    cmds.separator(height=1, style="none")
    cmds.button(label='Close', command=lambda *args:cmds.deleteUI(window, window=True))

    cmds.setParent('..')
    cmds.showWindow(window)

ui_create_material()
