import os
import arcpy

# Assumes that the input data and Python script are located in the same workspace (folder)
# Hard code the workspace path if input data is located elsewhere
cwd = os.getcwd()
inFolder = input("Enter the name of the input folder (ensure proper case and spelling): ")
arcpy.env.workspace = cwd + "\\" + inFolder
arcpy.env.overwriteOutput = True
print(arcpy.env.workspace)

# Create a list of all shapefiles
allShapefiles = arcpy.ListFeatureClasses()
print(len(allShapefiles))

# Excel files can have the extension .xlsx or .xls
# Create separate lists of Excel files with extension .xlsx and .xls
excelfilesXLSX = arcpy.ListFiles("*.xlsx")
excelfilesXLS = arcpy.ListFiles("*.xls")

# Concatenate the lists of Excel files to create one list
allExcelFiles = excelfilesXLSX + excelfilesXLS
print(len(allExcelFiles))

for shapefile in allShapefiles:
    numberFeatures = arcpy.management.GetCount(shapefile)
    print(numberFeatures)

for excelFile in allExcelFiles:
    # Get Count tool only works with .csv, .dbf or .txt tables
    # Convert all Excel files to .dbf tables to count the number of rows
    newTable = arcpy.conversion.ExcelToTable(excelFile, excelFile)
    numberRows = arcpy.management.GetCount(newTable)
    print(numberRows)
    # New tables were not asked to be created, so new .dbf files are immediately deleted
    arcpy.management.Delete(newTable)

# Use a Describe object to determine whether the shapefile contains point features (geometry shape type = point)
# List and report the field names and field type (data type) for each point shapefile
# Checks every shapefile in the input folder
for shapefile in allShapefiles:
    desc = arcpy.Describe(shapefile)
    if desc.shapeType == "Point":
        print(shapefile)
        for field in desc.fields:
            print(field.name)
            print(field.type)





#for shpFile in arcpy.ListFiles("*.shp"):
    #print(shpFile)
   