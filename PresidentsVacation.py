# File: PresidentsVacation.py
# Date: January 29 2021
# Authors: Kristine Luangkhot & Jennifer Debono
# Script to load georeferenced vacation photos into a new geodatabase
# as a point feature class for viewing in ArcPro

import os
import arcpy

# Assumes that the input data and Python script are located in the same workspace (folder)
# Hard code the workspace path if input data is located elsewhere
# requests program user enter in the folder to be the current workspace
print()
print("This script was made for Spatial Properties Inc. to view vacation photos using ArcGISPro.")
print()
cwd = os.getcwd()
inFolder = input("Enter the name of the folder with your photos (ensure proper case and spelling): ")
folderPath = cwd + "\\" + inFolder
arcpy.env.workspace = folderPath
arcpy.env.overwriteOutput = True
print("Current workspace or folder: {0}".format(arcpy.env.workspace))

# Adding photos as attachments using the Geotagged Photos to Points tool
# requires an ArcGIS Desktop Standard or higher license and a version 10 geodatabase
# Assume Spatial Properties Inc. has this level of license and version of ArcGIS
# Set the geodatabase version to 10.0 to be compatible with the Geotagged Photos to Points tool
# Ensures that it does not default to a lower version
gdbName = "VacationPhotos.gdb"
gdbVersion = "10.0"
arcpy.management.CreateFileGDB(folderPath, gdbName, gdbVersion)

# Output feature class will be named VacationPhotos
outFeatures = gdbName + r"\VacationPhotos"
invalidPhotos = ""
onlyGeotagged = "ONLY_GEOTAGGED"
addAttachments = "ADD_ATTACHMENTS"
arcpy.management.GeoTaggedPhotosToPoints(folderPath, outFeatures, invalidPhotos, onlyGeotagged, addAttachments)

print()
print("Geodatabase and feature class created.")