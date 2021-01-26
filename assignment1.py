import os
import arcpy 
# Set the workspace environment to a relative path
# Will work as long as CampgroundsData.gdb and AlgonquinCampgroundSelector.py are located in the same workspace folder
cwd = os.getcwd()
arcpy.env.workspace = cwd + r"\CampgroundsData.gdb"