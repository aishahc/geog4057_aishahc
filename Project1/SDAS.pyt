# -*- coding: utf-8 -*-=
import arcpy
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
            datatype="File",
            parameterType="Required",
            direction="Input")
        
        param1 = arcpy.Parameter(
            displayName="Feature Class Name",
            name="fcname",
            datatype="DEShapefile",
            parameterType="Required",
            direction="Output")
         
        params = [param0, param1]
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
        """The source code of the tool."""
        input_json = parameters[0].valueAsText
        fcname = parameters[1].valueAsText
        
        if not fcname.lower().endswith('.shp'):
            fcname = f"{fcname}.shp"
        arcpy.AddMessage(f"Input file: {input_json}")
        arcpy.AddMessage(f"Output shapefile name: {fcname}")
        return
    def postExecute(self, parameters):
        """This method takes place after outputs are processed and
        added to the display."""
        return
