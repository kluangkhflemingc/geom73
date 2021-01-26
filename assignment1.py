import os
import arcpy

# Assumes that the input data and Python script are located in the same workspace (folder)
# Hard code the workspace path if input data is located elsewhere
cwd = os.getcwd()
inFolder = input("Enter the name of the input folder (ensure proper case and spelling): ")
arcpy.env.workspace = cwd + "\\" + inFolder
print(arcpy.env.workspace)
