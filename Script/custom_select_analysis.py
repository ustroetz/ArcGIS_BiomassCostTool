# Import:
import arcpy
import sys
import os
from arcpy import env

FeatureToPoint = arcpy.GetParameterAsText(0)
feature_label = arcpy.GetParameterAsText(1) # String
locationstands = arcpy.GetParameterAsText(2)
outfeatureclass = arcpy.GetParameterAsText(3)


if FeatureToPoint == "in_memory\\%s_FeatureToPoint" % feature_label:
    arcpy.Select_analysis(locationstands, outfeatureclass, "AREA = '%s'" % feature_label)
    arcpy.AddMessage("works%s" % feature_label)



else: arcpy.AddError("doesntwork")
