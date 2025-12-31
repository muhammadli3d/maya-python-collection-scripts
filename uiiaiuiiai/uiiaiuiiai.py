"""
uiiaiuiiai
https://github.com/muhammadli3d
"""

import maya.cmds as qtpi
import os
import subprocess
import sys

def command_close(video_path):
	"""Popup video and print text"""
	sys.stdout.write("Oh no! You've been U II A I U II A I")
	if os.path.exists(video_path):
		subprocess.Popen(['start', video_path], shell=True)
	else:
		qtpi.warning('No video laa')
	
def ui(thumbnail, video_path):
	"""UI for preview image and direct video when user press button"""
	
	nameWin = 'Witch Car'
	
	# Delete window if exist
	if qtpi.window(nameWin, ex=1):
		qtpi.deleteUI(nameWin)
		
	# Window
	win = qtpi.window(nameWin, t=nameWin)
	qtpi.window(win, edit=1, rtf=1)
	
	qtpi.columnLayout(adj=1)
	
	# Add image
	if os.path.exists(thumbnail):
		qtpi.image(image=thumbnail)
	else:
		qtpi.text(l='Image missed you', align='center')
		
	qtpi.separator()
	qtpi.columnLayout(adj=1111)
	qtpi.button(l='Close', w=100, c=lambda x:command_close(video_path))
	
	qtpi.setParent('..')
	
	qtpi.showWindow(win)
	
thumbnail = r"path_image_of_uiiaiuiiai"
video_path = r"path_video_of_uiiaiuiiai"

ui(thumbnail, video_path)
