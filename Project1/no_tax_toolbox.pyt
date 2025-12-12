# -*- coding: utf-8 -*-=
import arcpy
import os
from no_taxpy import jason2shape

class Toolbox:
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "no_tax_toolbox"
        self.alias = "no_tax_toolbox"

        # List of tool classes associated with this toolbox
        self.tools = [Tool]


class Tool:
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "notax_tool"
        self.description = ""

    def getParameterInfo(self):
        """Define the tool parameters."""
        params = None
        param0 = arcpy.Parameter(
            displayName="JSON File Path",
            name="input_json",
            datatype="DEFile",
            parameterType="Required",
            direction="Input")
        
        param1 = arcpy.Parameter(
            displayName="Workspace Folder",
            name="workspace",
            datatype="DEFolder",
            parameterType="Required",
            direction="Input")
        
        param2 = arcpy.Parameter(
            displayName="WKID",
            name="wkid",
            datatype="GPString",
            parameterType="Required",
            direction="Input")
        
        param3 = arcpy.Parameter(
            displayName="Feature Class Name",
            name="fcname",
            datatype="DEShapefile",
            parameterType="Required",
            direction="Output")
         
        params = [param0, param1, param2, param3]
        return params

    def isLicensed(self):
        """Set whether the tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter. This method is called after internal validation."""
        return
    
    def execute(self, parameters, messages):
        input_json = parameters[0].valueAsText
        workspace = parameters[1].valueAsText
        wkid = parameters[2].valueAsText

        # Full path like C:\folder\name.shp
        fc_full_path = parameters[3].valueAsText

        # Extract only the name and remove .shp
        fcname = os.path.splitext(os.path.basename(fc_full_path))[0]

        # Now call your function
        jason2shape(input_json, workspace, fcname, wkid)

    def postExecute(self, parameters):
        """This method takes place after outputs are processed and
        added to the display."""
        return
