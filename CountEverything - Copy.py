# File: CountEverything.py
# Date: January 28 2021
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
inFolder = input("Enter the name of the input folder (ensure proper case and spelling): ")
arcpy.env.workspace = cwd + "\\" + inFolder
arcpy.env.overwriteOutput = True
print("Current workspace or folder: {0}".format(arcpy.env.workspace))

# Create a list of all shapefiles
allShapefiles = arcpy.ListFeatureClasses()

# Excel files can have the extension .xlsx or .xls
# Create separate lists of Excel files with extension .xlsx and .xls
excelfilesXLSX = arcpy.ListFiles("*.xlsx")
excelfilesXLS = arcpy.ListFiles("*.xls")

# Concatenate the lists of Excel files to create one list
allExcelFiles = excelfilesXLSX + excelfilesXLS

print()
print("{0} contains: {1} shapefiles and {2} Excel files.".format(inFolder, len(allShapefiles), len(allExcelFiles)))
print()

print("Number of rows in each file is as follows:")
print("*********************************************************************************************************")
# Find the longest string name (file name) in the list of shapefiles for formatting purposes
maxName = len(max(allShapefiles, key=len))
print("{0: <{1}}\t\t{2: <{1}}".format('Shapefile Name', maxName, "Number of Features"))
# GetCount tool used to determine total number of rows for the shapefiles
# found in the shapefile variable
# Listing the number of rows for each file
for shapefile in allShapefiles:
    numberFeatures = arcpy.management.GetCount(shapefile)
    print("{0: <{1}}\t\t{2: <{1}}".format(shapefile, maxName, str(numberFeatures)))

print()
# Find the longest string name (file name) in the list of Excel files for formatting purposes
maxExcel = len(max(allExcelFiles, key=len))
print("{0: <{1}}\t{2: <{1}}".format("Excel File Name", maxExcel, "Number of Rows"))
for excelFile in allExcelFiles:
    # Get Count tool only works with .csv, .dbf or .txt tables
    # Convert all Excel files to .dbf tables to count the number of rows
    newTable = arcpy.conversion.ExcelToTable(excelFile, excelFile)
    numberRows = arcpy.management.GetCount(newTable)
    print("{0: <{1}}\t{2: <{1}}".format(excelFile, maxExcel, str(numberRows)))
    # New tables were not asked to be created, so new .dbf files are immediately deleted
    arcpy.management.Delete(newTable)

# # Use a Describe object to determine whether the shapefile contains point features (geometry shape type = point)
# # List and report the field names and field type (data type) for each point shapefile
# # Checks every shapefile in the input folder
# for shapefile in allShapefiles:
#     desc = arcpy.Describe(shapefile)
#     if desc.shapeType == "Point":
#         print(shapefile)
#         for field in desc.fields:
#             print(field.name)
#             print(field.type)

#vt = arcpy.ValueTable(numberFeatures, fileNames)






   