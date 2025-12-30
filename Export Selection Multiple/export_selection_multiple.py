"""
Python script export all selected objects to their own file
http://github.com/muhammadli3d
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
1. Load into script editor in Maya under Python tab
2. Select all the object want to export
3. Execute
4. Objects will export according to its name and path given
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
"""

import maya.cmds as cmds
import os

def upload_file_path(file_path_full):
    """
    Upload file path on text field by using icon folder
    """
    file_path = cmds.fileDialog2(dialogStyle=2, caption="Path for export all selected", fileMode=3, okCaption="This")

    if file_path:
        file_name = os.path.commonpath(file_path)
        cmds.textField(file_path_full, edit=True, text=file_name)

def export_selection_multiple(file_path):
    objects_list = [i for i in cmds.ls(selection=True, type="transform")]
    cmds.select(clear=True)

    for obj in objects_list:
        cmds.select(obj)
        cmds.file(file_path + "/" + obj + ".ma", 
                force=True, 
                type="mayaAscii", 
                exportSelected=True
                )
        print("Done export {}".format(obj))

def ui_export_selection_multiple():
    # If window exist, delete
    if cmds.window("exportSelectionMultiple", exists=True):
        cmds.deleteUI("exportSelectionMultiple")

    # Window size
    window = cmds.window("exportSelectionMultiple", title="Export Multiple Selection", resizeToFitChildren=True, sizeable=False)
    cmds.columnLayout(adjustableColumn=True)
    cmds.separator(height=10, style='none')

    # File path field
    cmds.rowColumnLayout(numberOfColumns=3, columnAlign=(1, 'center'), columnWidth=[(1, 100), (2, 500), (3, 30)], margins=10)
    cmds.text(label="File path: ")

    file_path = cmds.textField()
    cmds.textField(file_path, edit=True, placeholderText="Put path here")
    cmds.symbolButton(image='navButtonBrowse.png', command=lambda x:upload_file_path(file_path))
    cmds.setParent("..")

    # Apply button
    applyclose_layout = cmds.rowLayout(numberOfColumns=2, adjustableColumn=True, margins=10)
    cmds.button(label="Export all selected", parent=applyclose_layout, 
                command=lambda x:export_selection_multiple(cmds.textField(file_path, query=True, text=True)))
    cmds.button(label="Close", parent=applyclose_layout, command=lambda x:cmds.deleteUI(window, window=True), width=200)

    # Window finalized and show
    cmds.setParent('..')
    cmds.separator(height=5, style='none')
    cmds.showWindow(window)

ui_export_selection_multiple()
