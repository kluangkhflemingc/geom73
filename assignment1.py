import os
import arcpy

# Assumes that the input data and Python script are located in the same workspace (folder)
# Hard code the workspace path if input data is located elsewhere
cwd = os.getcwd()
inFolder = input("Enter the name of the input folder (ensure proper case and spelling): ")
arcpy.env.workspace = cwd + "\\" + inFolder
print(arcpy.env.workspace)

shapefiles = arcpy.ListFiles("*.shp")
print(len(shapefiles))

shapefiles2 = arcpy.ListFeatureClasses()
print(len(shapefiles2))

excelfiles1 = arcpy.ListFiles("*.xlsx")
excelfiles2 = arcpy.ListFiles("*.xls")
allexcel = excelfiles1 + excelfiles2
print(len(allexcel))

for shapefile in shapefiles:
    numberFeatures = arcpy.GetCount_management(shapefile)
    print(numberFeatures)

for excelFile in allexcel:
    newTable = arcpy.conversion.ExcelToTable(excelFile, excelFile)
    numberRows = arcpy.management.GetCount(newTable)
    print(numberRows)

#for shpFile in arcpy.ListFiles("*.shp"):
    #print(shpFile)
   