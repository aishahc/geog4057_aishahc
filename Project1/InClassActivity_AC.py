import json
import arcpy
import os

def jason2shape(input_json=None,workspace=None,fcname=None,wkid=4236):
    """
    convert jason data to shapefile using arcpy. 
    """
    
    with open(input_json,'r') as file:
        tax_json = json.load(file)
        
    geom1 = arcpy.FromWKT(tax_json['data'][0][8])

    new_row = []
    for row in tax_json['data']:
        polygon = arcpy.FromWKT(row[8])
        new_row.append(polygon)
        
    
    fc_fullname = os.path.join(workspace,fcname)
    if arcpy.Exists(fc_fullname):
        arcpy.management.Delete(fc_fullname)

    arcpy.management.CreateFeatureclass(out_path=workspace,out_name=fcname,
                                        geometry_type='POLYGON',
                                        spatial_reference=wkid)

        
    ## add field names
    fields = tax_json['meta']['view']['columns']
    #for field in fields:
    #print(field['name'])
    field_type = ['TEXT','TEXT','LONG','LONG','TEXT','LONG','TEXT','TEXT','TEXT','TEXT','TEXT','TEXT','TEXT']
    field_names = []
    for ind,field in enumerate(fields):
        name = field['name']
        if name == 'the_geom':
            continue
        if name.lower() == 'id':
            name = f'id_{ind}'
        max_len = min(10,len(name))
        name = name[:max_len]
        field_names.append(name)
    field_names = [field.replace(" ","_") for field in field_names]
    field_names = [field.replace(".","_") for field in field_names]
    #field_names

    for ind,field_name in enumerate(field_names):
        arcpy.management.AddField(fc_fullname,field_name=field_name,field_type=field_type[ind])
        
    field_names.append('SHAPE@')

    #field_names

    with arcpy.da.InsertCursor(fc_fullname,field_names=field_names) as cursor:
        for index, row in enumerate(input_json['data']):
            new_polygon = []
            for ind, value in enumerate(row):
                if ind == 8:
                    continue
                if value == None:
                    value = ""
                new_polygon.append(value)
            new_polygon.append(new_row[index])
            cursor.insertRow(new_polygon)
            
    #new_row 
    pass

def main():
    fcname = 'notax_fc_1.shp'
    workspace = r'C:\Users\acerra5\geog4057\project'
    jason2shape(input_json=r'C:\Users\acerra5\geog4057\project\data\no_tax.json',
                workspace=workspace,
                fcname=fcname,
                wkid=4236
                )
if __name__ == "__main__":
    main()
