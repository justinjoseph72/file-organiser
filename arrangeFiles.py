import os
import shutil

baseFolder = '/home/justin/Downloads'
targetFolder = '/tmp/arranged'
docFolder=targetFolder + '/documents'
archiveFolders= targetFolder + '/archives'
imageFolder= targetFolder + '/images'
configFolder = targetFolder + '/configs'
otherFolder= targetFolder + '/other'

documentExtentions=['.pdf','.doc','.docx','.txt']
imageExtentions=['.jpg','.jpeg', '.png', 'tif', '.tiff', '.gif','.svg']
archiveExtentions=['.zip', '.tar', '.tgz','.tar.gz','.deb', '.jar','.exe', '.dmg']
configExtentions=['.json', '.yaml', '.yml']


def createFolder(folderName):
  os.makedirs(folderName,exist_ok=True)


def setupFolders():
    print("starting to create folders")
    targetFolders=[docFolder,archiveFolders,imageFolder,configFolder,otherFolder]   
    for folder in targetFolders:
        createFolder(folder)
    print("created all folders")    

def copyFromBaseFolderToTargetFolder(fileName: str, destinationFolder: str):
   fileOriginalPath = f"{baseFolder}/{fileName}"
   finalDestinationPath = f"{destinationFolder}/{fileName}"
   if os.path.isfile(fileOriginalPath):
      shutil.copy2(src=fileOriginalPath,dst=finalDestinationPath)

def isFileMatchingExtention(extentions: list, fileName: str) -> bool:
   for ext in extentions:
     if fileName.endswith(ext):
        return True; 
   return False;

def countAllFilesInFolder(folderPath: str) -> int:
   return len([entry for entry in os.listdir(folderPath) if os.path.isfile(os.path.join(folderPath, entry))])


def showProgress(current: int, total: int):
   percent = (current / total) * 100
   print(f"Progress: {percent:.2f}% ({current}/{total})")
   

#setting up the folders where the files will be copied to 
setupFolders()

totalFiles = countAllFilesInFolder(baseFolder)
print(f"total files found in base folder: {totalFiles}")

# iterating through the files and performing the action
entries = os.scandir(baseFolder)
fileProcessedCount = 0
for entry in entries:
  if entry.is_file:
     folder=otherFolder
     fileName = entry.name 
     if isFileMatchingExtention(documentExtentions, fileName=fileName):
       folder = docFolder
     if isFileMatchingExtention(imageExtentions, fileName=fileName):
       folder = imageFolder
     if isFileMatchingExtention(archiveExtentions, fileName=fileName):
       folder = archiveFolders
     if isFileMatchingExtention(configExtentions, fileName=fileName):
       folder = configFolder      
     # copying the files  
     copyFromBaseFolderToTargetFolder(fileName=fileName,destinationFolder=folder)
     fileProcessedCount += 1
     showProgress(current=fileProcessedCount, total=totalFiles)   



