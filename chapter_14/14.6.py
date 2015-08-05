'''	prints all .mp3 files	'''
import os
def mp3_files(dir):
    for name in os.listdir(dir):
	path=os.path.join(dir,name)
	if path.endswith('.mp3'):
	    print path
	else:
	    mp3_files(path)

mp3_files('ss')
