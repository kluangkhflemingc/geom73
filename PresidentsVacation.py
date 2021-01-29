# File: PresidentsVacation.py
# Date: January 29 2021
# Authors: Kristine Luangkhot & Jennifer Debono
# Script to inventory data in a user specified folder
# Inventory to include: 
# Count and report the total number of files and type - Excel files and shapefiles only
# Count and report the total number of rows or features for each file type
# List and report the feilds of point shapefiles

import os
import arcpy

# Assumes that the input data and Python script are located in the same workspace (folder)
# Hard code the workspace path if input data is located elsewhere
# requests program user enter in the folder to be the current workspace
print()
print("This script was made for Spatial Properties Inc. to inventory data in a user-specified folder.")
print()
cwd = os.getcwd()
inFolder = input("Enter the name of the folder with your photos (ensure proper case and spelling): ")
folderPath = cwd + "\\" + inFolder
arcpy.env.workspace = folderPath
arcpy.env.overwriteOutput = True
print("Current workspace or folder: {0}".format(arcpy.env.workspace))

gdbName = "VacationPhotos.gdb"
arcpy.management.CreateFileGDB(folderPath, gdbName)

outFeatures = gdbName + "\\" + "VacationPhotos"
invalidPhotos = ""
onlyGeotagged = "ONLY_GEOTAGGED"
addAttachments = "ADD_ATTACHMENTS"
arcpy.management.GeoTaggedPhotosToPoints(folderPath, outFeatures, invalidPhotos, onlyGeotagged, addAttachments)