# File Arranger

This file will read the files in a base folder set by the variable `baseFolder` and will move the files to the a separate folder set in the variable `targetFolder`. The files in the targetFolder will be organized by types.
The files will be arranged by the types. eg documents folder will have all the pdfs and word docucments. Images will have the png, jpg files. Archive folder will have the zip, tar, deb files etc.

The script will show a progress at the bottom and will first back the file in a temporary folder and then do the movement. Once the file is moved the temporary file will be deleted.

**Note** Make sure the folders are correctly set in the `baseFolder` and `targetFolder` variable and make sure its the correct one before the script is run.
