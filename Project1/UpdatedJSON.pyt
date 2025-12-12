import arcpy

class Toolbox(object):
    def __init__(self):
        self.label = "JSON to Shapefile Toolbox"
        self.alias = "json2shp"
        self.tools = [JSONtoShapefile]   # MUST match the class below


class JSONtoShapefile(object):
    def __init__(self):
        self.label = "JSON to Shapefile"
        self.description = "Converts a JSON file into a shapefile with geometry."

    def getParameterInfo(self):
        param0 = arcpy.Parameter(
            displayName="Input JSON File",
            name="input_json",
            datatype="DEFile",
            parameterType="Required",
            direction="Input"
        )
        param0.filter.list = ["json"]

        param1 = arcpy.Parameter(
            displayName="Output Shapefile",
            name="output_shapefile",
            datatype="DEFeatureClass",
            parameterType="Required",
            direction="Output"
        )

        return [param0, param1]

    def isLicensed(self):
        return True

    def updateParameters(self, parameters):
        return

    def updateMessages(self, parameters):
        return

    def execute(self, parameters, messages):
        input_json = parameters[0].valueAsText
        output_shp = parameters[1].valueAsText

        arcpy.AddMessage(f"JSON: {input_json}")
        arcpy.AddMessage(f"Output: {output_shp}")

        return

