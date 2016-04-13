from __future__ import print_function
from subprocess import call
import os
import sys
import shutil

path  = "/Volumes"
# files to be replaced
removeDirName  = "/links/"
removeFileName = "/sponsors.html"

# files to be added
fileSaveSrc = "/sponsors.html"
fileSaveDst = fileSaveSrc
fileSaveDir= removeDirName


numVolumes = 0
# List volumes to be modified ------ 
print('\nVolumes: ')
volumes = os.listdir(path)
for volume in volumes:
	if (volume != "Macintosh HD") and (volume != "MobileBackups") and (volume[0] != "."):
		print('\t{}/{}'.format( path, volume))
		numVolumes += 1
print('\nAbout to process {} volume/s.'.format( numVolumes))
raw_input('Press Enter to continue...')
# ------------------------------------------

counter = 0
for volume in volumes:
	if (volume != "Macintosh HD") and (volume != "MobileBackups") and (volume[0] != "."):
		print('Processing volume: {}'.format( volume))

		# remove directory ------------------
		dirpathToRemove  =  path + "/" + volume + removeDirName
		# two options below, I prefer system call seems to be more likely to power through
		call(["rm","-fr", dirpathToRemove])
		# shutil.rmtree(dirpathToRemove, ignore_errors = True)
		print('\tRemoved dir : {}'.format(dirpathToRemove))
		
		# remove file -----------------------
		filepathToRemove =  path + "/" + volume + removeFileName
		call(["rm","-f", filepathToRemove])
		print('\tRemoved file at path: {}'.format(filepathToRemove))

		# copy .../links/* fir
		dirSrc = os.getcwd()+'/haptics_usb_update' +fileSaveDir
		dirDst = path+"/"+volume + fileSaveDir
		shutil.copytree(dirSrc, dirDst, symlinks=False, ignore=None)
		print('\tCopied dir to: {}'.format(dirDst))

		fileSrcPath  = os.getcwd()+'/haptics_usb_update' + fileSaveSrc
		fileDstPath  = path + "/" + volume  + fileSaveSrc
		shutil.copyfile(fileSrcPath, fileDstPath )
		print('\tCopied file to: {}'.format(fileDstPath))
		#print('\tsrcCP: {}'.format(fileSrcPath))
		#print('\tdstCP: {}'.format(fileDstPath))
		
		call(["diskutil","unmount",path + "/" + volume])
		print('\tDisk unounted: {}/volume\n'.format(path, volume))
		counter += 1
print('Processed {} volume/s \n'.format(counter))


#dirToMake = path + "/" + volume + fileSaveDir
#os.mkdir(dirToMake) 
#rint'\tMade dir: ' + dirToMake


