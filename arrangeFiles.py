import os
import shutil

baseFolder = '/home/justin/Downloads'
targetFolder = '/tmp/arranged'
docFolder=targetFolder + '/documents'
archiveFolders= targetFolder + '/archives'
imageFolder= targetFolder + '/images'
configFolder = targetFolder + '/configs'
otherFolder= targetFolder + '/other'

documentExtentions=['.pdf','doc','docx','.txt']
imageExtentions=['.jpg','.jpeg', '.png', 'tif', '.tiff', '.gif','.svg']
archiveExtentions=['.zip', '.tar', '.tgz','.tar.gz','.deb', '.jar','.exe', '.dmg']
configExtentions=['.json', '.yaml', '.yml']


def createFolder(folderName):
  print("creating folder " + folderName)
  os.makedirs(folderName,exist_ok=True)


def setupFolders():
    print("starting to create folders")
    targetFolders=[docFolder,archiveFolders,imageFolder,configFolder,otherFolder]   
    for folder in targetFolders:
        createFolder(folder)
    print("created all folders")    

def copyFromBaseFolderToTargetFolder(fileName, destinationFolder):
   fileOriginalPath = f"{baseFolder}/{fileName}"
   finalDestinationPath = f"{destinationFolder}/{fileName}"
   if os.path.isfile(fileOriginalPath):
      shutil.copy2(src=fileOriginalPath,dst=finalDestinationPath)

def isMatchingExetention(extentions, fileName):
   for ext in extentions:
     if fileName.endswith(ext):
        return True 
   return False;

#setting up the folders where the files will be copied to 
setupFolders()

# iterating through the files and performing the action
entries = os.scandir(baseFolder)
for entry in entries:
  if entry.is_file:

     folder=otherFolder
     fileName = entry.name 
     if isMatchingExetention(documentExtentions, fileName=fileName):
       folder = docFolder
     if isMatchingExetention(imageExtentions, fileName=fileName):
       folder = imageFolder
     if isMatchingExetention(archiveExtentions, fileName=fileName):
       folder = archiveFolders
     if isMatchingExetention(configExtentions, fileName=fileName):
       folder = configFolder      
     # copying the files  
     copyFromBaseFolderToTargetFolder(fileName=fileName,destinationFolder=folder)   



