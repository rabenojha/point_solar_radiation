# Import system modules

import arcpy
from arcpy import env
from arcpy.sa import *

arcpy.CreateFileGDB_management(r"D:\PSR_Final", "output_july")


# Set environment settings

env.workspace = "D:\PSR_Final\output_july.gdb"


# Set time configuration and other variables

timeConfig = TimeWithinDay(190, 6, 16)  # 6 AM to 4 PM for July 09
hourInterval = 0.5  # 30 min interval


# feeding values for transmittivity and diffuse proportion for different interval of calculation

trans = ['0.15', '0.42', '0.51', '0.30', '0.67', '0.71', '0.35', '0.47', '0.45', '0.53', '0.49', '0.62',
         '0.33', '0.17', '0.74', '0.44']
diff = ['0.71', '0.69', '0.48', '0.10', '0.50', '0.40', '0.39', '0.26', '0.32', '0.49', '0.72', '0.51', '0.52', '0.65',
        '0.40', '0.42']
y = list(map(list, zip(trans, diff)))

# calculation


directory = "D:\PSR_Final\july"
j = 0 # counter for output
for i in range(len(y)):
    PointsSolarRadiation("aoi_reprojected.tif",
                             "centroid",directory +"/PSR_July_"+ str(j) ,
                             0, 47.8209442145, 200,
                             timeConfig, 14, hourInterval,
                             "INTERVAL", 1, "FROM_DEM", 32, 8, 8, "UNIFORM_SKY",
                             y[i][1], y[i][0], None, None, None)
    j += 1 
