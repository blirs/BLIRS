bl_info = {
    "name": "Materials Toolbox",
    "author": "monika ouza",
	"version": (1,1,0,0),
    "blender": (2, 80, 0),
    "location": "View3D > CTR +SHIFT+ M key",
    "description": "Menu of Material Tools for Simulation: Loads Predefined Materials, Change from Infrared to Radar Materials and viseversa, Define new Materials, Use parameters of predefined matterials to define new ones",
    "category": "Material"}

import bpy
import math
from bpy_extras.io_utils import ExportHelper
from bpy.props import StringProperty, BoolProperty, EnumProperty, BoolVectorProperty, FloatProperty, IntProperty

def loadDefaultMaterials():
    #load the Materials list to user in your blend file
    # Radar Materials Definitions (suggested Parametrs)
    # Beton Radar
    Beton_radar_20 = "Beton_Radar_20"  
    # Test if material exists
    # If it does not exist, create it:
    Beton_radar_20 = (bpy.data.materials.get(Beton_radar_20) or bpy.data.materials.new(Beton_radar_20))
    #diffuse shader
    Beton_radar_20.diffuse_shader = 'OREN_NAYAR' 
    Beton_radar_20.diffuse_intensity = 0.5
    Beton_radar_20.roughness = 3.14
    #specular shader
    Beton_radar_20.specular_shader = 'BLINN'
    Beton_radar_20.specular_intensity = 0.2
    Beton_radar_20.specular_hardness = 100
    Beton_radar_20.specular_ior = 4
    # Mirror Refelction
    Beton_radar_20.raytrace_mirror.use = True
    Beton_radar_20.raytrace_mirror.reflect_factor = 0.07
    Beton_radar_20.raytrace_mirror.distance = 15
    Beton_radar_20.use_fake_user = True
     
         
    # Plastik Radar
    Plastik_radar_20 = "Plastik_Radar_20"  
    # Test if material exists
    # If it does not exist, create it:
    Plastik_radar_20 = (bpy.data.materials.get(Plastik_radar_20) or bpy.data.materials.new(Plastik_radar_20))
    #diffuse shader
    Plastik_radar_20.diffuse_shader = 'OREN_NAYAR'
    Plastik_radar_20.diffuse_intensity = 0.4
    Plastik_radar_20.roughness = 3
    #specular shader
    Plastik_radar_20.specular_shader = 'BLINN'
    Plastik_radar_20.specular_intensity = 0.15
    Plastik_radar_20.specular_hardness = 5
    Plastik_radar_20.specular_ior = 4
    Plastik_radar_20.use_fake_user = True
       
    # Holz Radar
    Holz_radar_20 = "Holz_Radar_20"
    # Test if material exists
    # If it does not exist, create it:
    Holz_radar_20 = (bpy.data.materials.get(Holz_radar_20) or bpy.data.materials.new(Holz_radar_20))
    #diffuse shader
    Holz_radar_20.diffuse_shader = 'OREN_NAYAR'
    Holz_radar_20.diffuse_intensity = 0.6
    Holz_radar_20.roughness = 1.6
    #specular shader
    Holz_radar_20.specular_shader = 'BLINN'
    Holz_radar_20.specular_intensity = 0.3
    Holz_radar_20.specular_hardness = 5
    Holz_radar_20.specular_ior = 4
    # Mirror Reflection 
    Holz_radar_20.raytrace_mirror.use = True
    Holz_radar_20.raytrace_mirror.reflect_factor = 0.1
    Holz_radar_20.raytrace_mirror.distance = 15
    Holz_radar_20.use_fake_user = True
       

    # Metall Radar 
    Metall_radar_20 = "Metall_Radar_20"
    # Test if material exists
    # If it does not exist, create it:
    Metall_radar_20 = (bpy.data.materials.get(Metall_radar_20) or bpy.data.materials.new(Metall_radar_20))   
    #diffuse shader
    Metall_radar_20.diffuse_shader = 'OREN_NAYAR'
    Metall_radar_20.diffuse_intensity = 0.8
    Metall_radar_20.roughness = 0.001
    #specular shader
    Metall_radar_20.specular_shader = 'BLINN'
    Metall_radar_20.specular_intensity = 0.8
    Metall_radar_20.specular_hardness = 5
    Metall_radar_20.specular_ior = 4
    # Mirror Reflection of metall
    Metall_radar_20.raytrace_mirror.use = True
    Metall_radar_20.raytrace_mirror.reflect_factor = 0.1
    Metall_radar_20.raytrace_mirror.distance = 15
    Metall_radar_20.use_fake_user = True
     
         
    # IR Materials Definition (default Temp 20 deg)
    # Boltzmann -constant
    b = 5.67 * math.pow(10,-8)
    # 20 deg in Kelvin
    temp = 20+273.15
    # correction factor (radiation at 100 deg with emissivity=1
    fac = 1220
    
    # Beton Infrared
    Beton_ir_20 = "Beton_Infrared_20" 
    # Test if material exists
    # If it does not exist, create it: 
    Beton_ir_20 = (bpy.data.materials.get(Beton_ir_20) or bpy.data.materials.new(Beton_ir_20))
    #diffuse shader
    Beton_ir_20.diffuse_shader = 'OREN_NAYAR'
    Beton_ir_20.diffuse_intensity = 0.25
    Beton_ir_20.roughness = 3.14
    # specular shader
    Beton_ir_20.specular_shader = 'BLINN'
    Beton_ir_20.specular_intensity = 0.01
    Beton_ir_20.specular_hardness = 500
    Beton_ir_20.specular_ior = 4
    #Emission for emissivity factor 0.87
    Beton_ir_20.emit = (math.pow(temp,4)*b*0.87)/fac
    # Mirror Reflection
    Beton_ir_20.raytrace_mirror.use = True
    Beton_ir_20.raytrace_mirror.reflect_factor = 0.15
    Beton_ir_20.raytrace_mirror.distance = 15
    Beton_ir_20.use_fake_user = True
     

    # Plastik Infrared
    Plastik_ir_20 = "Plastik_Infrared_20"
    # Test if material exists 
    # If it does not exist, create it:  
    Plastik_ir_20 = (bpy.data.materials.get(Plastik_ir_20) or bpy.data.materials.new(Plastik_ir_20))
    #diffuse shader
    Plastik_ir_20.diffuse_shader = 'OREN_NAYAR'
    Plastik_ir_20.diffuse_intensity = 0.5 
    Plastik_ir_20.roughness = 3.14
    #specular shader
    Plastik_ir_20.specular_shader = 'BLINN'
    Plastik_ir_20.specular_intensity = 0.01
    Plastik_ir_20.specular_hardness = 100
    Plastik_ir_20.specular_ior = 4
    #Emission for emsissivity factor 0.9
    Plastik_ir_20.emit = (math.pow(temp,4)*b*0.9)/fac
    # Mirror Reflection 
    Plastik_ir_20.raytrace_mirror.use = True
    Plastik_ir_20.raytrace_mirror.reflect_factor = 0.08
    Plastik_ir_20.raytrace_mirror.distance = 15
    Plastik_ir_20.use_fake_user = True
    Plastik_ir_20.use_fake_user = True
     

    # Holz Infrared
    Holz_ir_20 = "Holz_Infrared_20"
    # Test if material exists
    # If it does not exist, create it:
    Holz_ir_20 = (bpy.data.materials.get(Holz_ir_20) or bpy.data.materials.new(Holz_ir_20))         
    #diffuse shader
    Holz_ir_20.diffuse_shader = 'OREN_NAYAR'
    Holz_ir_20.diffuse_intensity = 0.3
    Holz_ir_20.roughness = 3
    #specular shader
    Holz_ir_20.specular_shader = 'BLINN'
    Holz_ir_20.specular_intensity = 0.01
    Holz_ir_20.specular_hardness = 200
    Holz_ir_20.specular_ior = 4
    #Emission for emissivity factor 0.85
    Holz_ir_20.emit = (math.pow(temp,4)*b*0.85)/fac
    # Mirror Reflection 
    Holz_ir_20.raytrace_mirror.use = True
    Holz_ir_20.raytrace_mirror.reflect_factor = 0.08
    Holz_ir_20.raytrace_mirror.distance = 15
    Holz_ir_20.use_fake_user = True
     
 
    # Metall Infrared
    Metall_ir_20 = "Metall_Infrared_20"
    # Test if material exists
    # If it does not exist, create it:
    Metall_ir_20 = (bpy.data.materials.get(Metall_ir_20) or bpy.data.materials.new(Metall_ir_20))
    #diffuse shader
    Metall_ir_20.diffuse_shader = 'OREN_NAYAR'
    Metall_ir_20.diffuse_intensity = 0.1
    Metall_ir_20.roughness = 0.01
    #specular shader
    Metall_ir_20.specular_shader = 'BLINN' 
    Metall_ir_20.specular_intensity = 0.6
    Metall_ir_20.specular_hardness = 100
    Metall_ir_20.specular_ior = 4
    #Emission for emissivity factor 0.78
    Metall_ir_20.emit = (math.pow(temp,4)*b*0.78)/fac
    # Mirror Reflection of metall
    Metall_ir_20.raytrace_mirror.use = True
    Metall_ir_20.raytrace_mirror.reflect_factor = 0.15
    Metall_ir_20.raytrace_mirror.distance = 15 
    Metall_ir_20.use_fake_user = True
     
    #return the materials
    return Beton_radar_20
    return Metall_ir_20
    return Holz_ir_20
    return Plastik_ir_20
    return Beton_ir_20
    return Metall_radar_20
    return Holz_radar_20
    return Plastik_radar_20


def MakeMaterial(materialname,irreflectivity, radarreflectivity, irspecreflectivity, radarspecrefelctivity, irroughness, radarroughness, temperaturenew, emissivity, irmirrorreflection, radarmirrorreflection, irmirrorreflectfactor, radarmirrorreflectfactor):
    # Define new Materials with user defined Parameters
    
    #Boltman contstant
    b = 5.67 * math.pow(10,-8)
    # from deg in Kelvin
    temp= temperaturenew +273.15
    # correction factor (radiation at 100 deg with emissivity=1
    fac = 1220
    
    # Infrared Material parameters
    matir = (bpy.data.materials.get(materialname +'_ir'+'_'+str(temperaturenew)) or bpy.data.materials.new( materialname+'_ir'+'_'+str(temperaturenew) ))
    matir.name  =  materialname +'_Infrared'+'_'+str(temperaturenew)
    matir.diffuse_shader = 'OREN_NAYAR'
    matir.diffuse_intensity = irreflectivity
    matir.roughness = irroughness
    matir.specular_shader = 'BLINN'
    matir.specular_intensity = irspecreflectivity
    matir.specular_hardness = 100
    matir.specular_ior = 4
    matir.emit = (math.pow(temp,4)*b* emissivity)/fac
    if irmirrorreflection:
      matir.raytrace_mirror.use = True
      matir.raytrace_mirror.reflect_factor = irmirrorreflectfactor
      matir.raytrace_mirror.distance = 15
    else:
      irmirrorreflection = False
      matir.raytrace_mirror.use = False  
      matir.raytrace_mirror.reflect_factor = 0
      matir.raytrace_mirror.distance = 0
    matir.use_fake_user = True  
      
       
    # Radar Material Parameters
    matradar = (bpy.data.materials.get(materialname +'_radar'+'_'+str(temperaturenew)) or bpy.data.materials.new(materialname + '_radar' +'_'+str(temperaturenew)))
    matradar.name  = materialname +'_Radar'+'_'+str(temperaturenew)
    matradar.diffuse_shader = 'OREN_NAYAR'
    matradar.diffuse_intensity = radarreflectivity
    matradar.roughness = radarroughness
    matradar.specular_shader = 'BLINN'
    matradar.specular_intensity = radarspecrefelctivity
    matradar.specular_hardness = 50
    matradar.specular_ior = 4
    if radarmirrorreflection:
      matradar.raytrace_mirror.use = True
      matradar.raytrace_mirror.reflect_factor = radarmirrorreflectfactor
      matradar.raytrace_mirror.distance = 15
    else:
      radarmirrorreflection = False
      matradar.raytrace_mirror.use = False  
      matradar.raytrace_mirror.reflect_factor = 0
      matradar.raytrace_mirror.distance = 0
    matradar.use_fake_user = True         
    
   
    # return the new Materials
    return matradar
    return matir

def Newmatfrompredefined(selectedmaterialinput):
    # Define a new Material using parameters from predefined materials
    
    # The selected Material
    selectedmaterial = bpy.data.materials.get(selectedmaterialinput)
    matlist = bpy.data.materials 
    #Boltzmann-constant
    b = 5.67 * math.pow(10,-8)
    fac = 1220
    if selectedmaterial is None:
        return

    elif 'Infrared' in selectedmaterial.name:
        materialname = selectedmaterial.name[:-12]
        irreflectivity = selectedmaterial.diffuse_intensity
        irspecreflectivity = selectedmaterial.specular_intensity
        irroughness = selectedmaterial.roughness
        temperaturenew = int(selectedmaterial.name[-2:])
        # calculate emissivity
        emissivity = (selectedmaterial.emit*fac)/(b*(math.pow((temperaturenew+273.15),4)))
        irmirrorreflection = selectedmaterial.raytrace_mirror.use
        irmirrorreflectfactor =selectedmaterial.raytrace_mirror.reflect_factor
        selectedmaterialradar =matlist[selectedmaterial.name[:-12]+'_Radar'+selectedmaterial.name[-3:]]
        radarreflectivity = selectedmaterialradar.diffuse_intensity
        radarspecreflectivity = selectedmaterialradar.specular_intensity
        radarroughness = selectedmaterialradar.roughness
        radarmirrorreflection = selectedmaterialradar.raytrace_mirror.use
        radarmirrorreflectfactor = selectedmaterialradar.raytrace_mirror.reflect_factor
        return (materialname, irreflectivity, irspecreflectivity, irroughness, temperaturenew, emissivity, irmirrorreflection, irmirrorreflectfactor,radarreflectivity,radarspecreflectivity,radarroughness,radarmirrorreflection, radarmirrorreflectfactor)
    elif 'Radar' in selectedmaterial.name:
        materialname = selectedmaterial.name[:-9]
        radarreflectivity = selectedmaterial.diffuse_intensity
        radarspecreflectivity = selectedmaterial.specular_intensity
        radarroughness = selectedmaterial.roughness
        radarmirrorreflection = selectedmaterial.raytrace_mirror.use
        radarmirrorreflectfactor = selectedmaterial.raytrace_mirror.reflect_factor
        selectedmaterialir =matlist[selectedmaterial.name[:-9]+'_Infrared'+selectedmaterial.name[-3:]]
        irreflectivity = selectedmaterialir.diffuse_intensity
        irspecreflectivity = selectedmaterialir.specular_intensity
        irroughness = selectedmaterialir.roughness
        temperaturenew = int(selectedmaterialir.name[-2:])
        # calculate emissivity
        emissivity = (selectedmaterialir.emit*fac)/(b*(math.pow((temperaturenew+273.15),4)))
        irmirrorreflection = selectedmaterialir.raytrace_mirror.use
        irmirrorreflectfactor =selectedmaterialir.raytrace_mirror.reflect_factor
        #return selectedmaterial
        return (materialname, irreflectivity, irspecreflectivity, irroughness, temperaturenew, emissivity, irmirrorreflection, irmirrorreflectfactor, radarreflectivity,radarspecreflectivity,radarroughness,radarmirrorreflection, radarmirrorreflectfactor)

def irwithdifftemp(temperature,all_objects=False, all_objects_samemat=False, update_selection=False):
         # switch to Infrared Materials with new temperatures
         scn = bpy.context.scene 
         matlist = bpy.data.materials  
         Cameras = bpy.data.cameras
         
         #Boltman contstant
         b = 5.67 * math.pow(10,-8)
         # from deg in Kelvin
         temp= temperature +273.15
         # correction factor (radiation at 100 deg with emissivity=1
         fac = 1220
         
         if all_objects:
             # all objects
             objs = scn.objects        
         elif ((update_selection) and (not all_objects) and (not all_objects_samemat)):
             # only the selected objects
             objs = bpy.context.selected_editable_objects 
         elif ((not update_selection) and (not all_objects) and (all_objects_samemat)):
            # all objects having the same material as the selected object
             objs = scn.objects
             matname = bpy.context.selected_editable_objects[0].active_material.name[:-3]  
             for ob in objs:
                 if ((ob.type == 'MESH') and (ob.active_material.name[:-3] == matname)) :
                     ob. select = True
             objs = bpy.context.selected_editable_objects               
         elif ((not all_objects) and (not update_selection) and (not all_objects_samemat)):     
             objs =''
             
         for ob in objs:  
            if((ob.type == 'LAMP')):
               if(ob.name == 'Radar_Antenna'):
                   # hide the spot lamp and make it unrenderable
                  ob.hide = True 
                  ob.hide_render = True
               elif('Infrared_Lamp'in ob.name):
                   # make the infrared lamp visisble and renderable
                  ob.hide = False
                  ob.hide_render = False 
               else: pass  
              
            elif((ob.type == 'MESH') and ('Infrared' in ob.active_material.name) and (str(temperature) not in ob.active_material.name)):
                 # create a new Material with the same parameters but with new Temperature
                 # calculate the emissivity
                 emissivity = (ob.active_material.emit*fac)/(b*(math.pow((int(ob.active_material.name[-2:])+273.15),4)))
                 matir_newtemp = str(matlist[ob.active_material.name].name[:-3])+'_'+str(temperature)
                 matir_newtemp = (bpy.data.materials.get(matir_newtemp) or 
                 bpy.data.materials.new(matir_newtemp))
                 matir_newtemp.name = str(matlist[ob.active_material.name].name[:-3])+'_'+str(temperature)
                 matir_newtemp.emit = (math.pow(temp,4)*b*emissivity /fac)
                 matir_newtemp.diffuse_shader = ob.active_material.diffuse_shader
                 matir_newtemp.diffuse_intensity = ob.active_material.diffuse_intensity
                 matir_newtemp.specular_shader = ob.active_material.specular_shader
                 matir_newtemp.specular_intensity = ob.active_material.specular_intensity
                 matir_newtemp.specular_hardness = ob.active_material.specular_hardness
                 matir_newtemp.specular_ior = ob.active_material.specular_ior
 
                 matir_newtemp.raytrace_mirror.use = ob.active_material.raytrace_mirror.use
                 matir_newtemp.raytrace_mirror.reflect_factor = ob.active_material.raytrace_mirror.reflect_factor 
                 matir_newtemp.raytrace_mirror.depth = ob.active_material.raytrace_mirror.depth   
                 matir_newtemp.use_fake_user = True
                      
                 # create a Radar Material with the same Radar Paramaeters but with different name
                 ob.active_material = matlist[ob.active_material.name[:-12]+'_Radar'+ob.active_material.name[-3:]]
                 matrad_newtemp = str(matlist[ob.active_material.name].name[:-3])+'_'+str(temperature)
                 matrad_newtemp = (bpy.data.materials.get(matrad_newtemp) or 
                 bpy.data.materials.new(matrad_newtemp))
                 matrad_newtemp.name = str(matlist[ob.active_material.name].name[:-3])+'_'+str(temperature)
                 matrad_newtemp.diffuse_shader = ob.active_material.diffuse_shader
                 matrad_newtemp.diffuse_intensity = ob.active_material.diffuse_intensity
                 matrad_newtemp.specular_shader = ob.active_material.specular_shader
                 matrad_newtemp.specular_intensity = ob.active_material.specular_intensity
                 matrad_newtemp.specular_hardness = ob.active_material.specular_hardness
                 matrad_newtemp.specular_ior = ob.active_material.specular_ior
 
                 matrad_newtemp.raytrace_mirror.use = ob.active_material.raytrace_mirror.use
                 matrad_newtemp.raytrace_mirror.reflect_factor = ob.active_material.raytrace_mirror.reflect_factor 
                 matrad_newtemp.raytrace_mirror.depth = ob.active_material.raytrace_mirror.depth   
                 matrad_newtemp.use_fake_user = True
                       
                 # set the active material to the new Inrared Material
                 ob.active_material = matir_newtemp
                 
            elif ((ob.type == 'MESH') and ('Radar' in ob.active_material.name) and (str(temperature) not in ob.active_material.name)): 
                 # create a new Radar material with same paramters but with different name
                 matrad_newtemp = str(matlist[ob.active_material.name].name[:-3])+'_'+str(temperature)
                 matrad_newtemp = (bpy.data.materials.get(matrad_newtemp) or 
                 bpy.data.materials.new(matrad_newtemp))
                 matrad_newtemp.name = str(matlist[ob.active_material.name].name[:-3])+'_'+str(temperature)
                 matrad_newtemp.diffuse_shader = ob.active_material.diffuse_shader
                 matrad_newtemp.diffuse_intensity = ob.active_material.diffuse_intensity
                 matrad_newtemp.specular_shader = ob.active_material.specular_shader
                 matrad_newtemp.specular_intensity = ob.active_material.specular_intensity
                 matrad_newtemp.specular_hardness = ob.active_material.specular_hardness
                 matrad_newtemp.specular_ior = ob.active_material.specular_ior
 
                 matrad_newtemp.raytrace_mirror.use = ob.active_material.raytrace_mirror.use
                 matrad_newtemp.raytrace_mirror.reflect_factor = ob.active_material.raytrace_mirror.reflect_factor 
                 matrad_newtemp.raytrace_mirror.depth = ob.active_material.raytrace_mirror.depth   
                 matrad_newtemp.use_fake_user = True
                  
                 ob.active_material = matlist[ob.active_material.name[:-9]+'_Infrared'+ob.active_material.name[-3:]]
                 emissivity = (ob.active_material.emit*fac)/(b*(math.pow((int(ob.active_material.name[-2:])+273.15),4)))
                 # create a new Infrared Materials with same Parameters and a new user defines Temperature
                 matir_newtemp = str(matlist[ob.active_material.name].name[:-3])+'_'+str(temperature)        
                 matir_newtemp = (bpy.data.materials.get(matir_newtemp) or 
                 bpy.data.materials.new(matir_newtemp))
                 matir_newtemp.name = str(matlist[ob.active_material.name].name[:-3])+'_'+str(temperature) 
                 matir_newtemp.emit = (math.pow(temp,4)*b*emissivity /fac)
                 matir_newtemp.diffuse_shader = ob.active_material.diffuse_shader
                 matir_newtemp.diffuse_intensity = ob.active_material.diffuse_intensity
                 matir_newtemp.specular_shader = ob.active_material.specular_shader
                 matir_newtemp.specular_intensity = ob.active_material.specular_intensity
                 matir_newtemp.specular_hardness = ob.active_material.specular_hardness
                 matir_newtemp.specular_ior = ob.active_material.specular_ior
                 matir_newtemp.raytrace_mirror.use = ob.active_material.raytrace_mirror.use
                 matir_newtemp.raytrace_mirror.reflect_factor = ob.active_material.raytrace_mirror.reflect_factor 
                 matir_newtemp.raytrace_mirror.depth = ob.active_material.raytrace_mirror.depth   
                 #ob.active_material.name = ob.active_material.name[:-9] +'_Infrared_newtemp_'+str(temperature)       
                 matir_newtemp.use_fake_user = True
                      
                 ob.active_material = matir_newtemp
                           
            else:
                 pass             
                    

                    
def switchmaterials(change_to_radar = False, change_to_ir = False):
      # switch from Radar Scene Settings to Infrred and vice-versa         
         scn = bpy.context.scene 
         matlist = bpy.data.materials  
         Cameras = bpy.data.cameras
         objs = scn.objects       

          
         for ob in objs: 
             if ((change_to_radar) and (not change_to_ir)):
                 #switch to Radar Settings
                 bpy.context.scene.world.light_settings.use_environment_light = False   
                 bpy.context.scene.world.light_settings.environment_energy = 0
                 if((ob.type == 'LAMP')):
                     if(ob.name == 'Radar_Antenna'):
                         # make the spot lamp visible and renderable
                        ob.hide = False 
                        ob.hide_render = False
                        # set the size of the spot lamp equal to camera size
                        ob.data.spot_size = Cameras['Camera'].angle
                        if 'Copy Camera Location' not in ob.constraints:
                            # set the location of the spot lamp equal to the camera location
                            cam_loc = ob.constraints.new(type = 'COPY_LOCATION')
                            cam_loc.name = 'Copy Camera Location'
                            ob.constraints["Copy Camera Location"].target = bpy.data.objects["Camera"]
                        else: pass
                        if 'Copy Camera Rotation' not in ob.constraints:
                            # set the direction of the spot lamp equal to the direction of the camera
                            cam_rot = ob.constraints.new(type = 'COPY_ROTATION') 
                            cam_rot.name = 'Copy Camera Rotation' 
                            ob.constraints["Copy Camera Rotation"].target = bpy.data.objects["Camera"]  
                        else: pass
                     elif('Infrared_Lamp'in ob.name):
                         # hide the Infrared lamps and make it not renderable
                        ob.hide = True 
                        ob.hide_render = True 
                     else: pass                                
                 elif ((ob.type == 'MESH') and ('Infrared' in ob.active_material.name)):
                     # switch to Radar Materials
                      ob.active_material = matlist[ob.active_material.name[:-12]+'_Radar'+ob.active_material.name[-3:]]
                 else: 
                     pass      
             elif (( not change_to_radar) and (change_to_ir)):
                 # change to Infrared Scene Settings
                 
                 # use environmental lighting
                 bpy.context.scene.world.light_settings.use_environment_light = True
                 bpy.context.scene.world.light_settings.environment_energy = 0.05
                 if((ob.type == 'LAMP')):
                     if(ob.name == 'Radar_Antenna'):
                         # hide the radar Spot lamp and make it unrenderable
                        ob.hide = True
                        ob.hide_render = True
                     elif('Infrared_Lamp' in ob.name):
                         # render the infrared lamps and make them visible
                        ob.hide = False 
                        ob.hide_render = False 
                     else: pass    
                 elif ((ob.type == 'MESH') and ('Radar' in ob.active_material.name)):
                     # switch to infrared Materials
                      ob.active_material = matlist[ob.active_material.name[:-9]+'_Infrared'+ob.active_material.name[-3:]]                    
                 else:
                     pass                
             else:
                 pass
                            

class definenewmat(bpy.types.Operator):
    """Define a new Material"""
    bl_idname = "object.definenewmat"
    bl_label = "Define new material"
    bl_options = {'REGISTER', 'UNDO'}

                                  
    irroughness =bpy.props.FloatProperty(name="Roughness", 
                              description = " Roughness of the Infrared material surface",
                              default=0, min =0, max =3.14)
    radarroughness =bpy.props.FloatProperty(name="Roughness", 
                              description = " Roughness of the IR material surface",
                              default=0, min =0, max =3.14)                              
                              
                              
    irreflectivity =bpy.props.FloatProperty(name="Diffuse Reflect.", 
                              description = " Diffuse Reflectivity of the IR material surface (Intensity of diffuse Shader)",
                              default=0, min =0, max =1)
    irspecreflectivity =bpy.props.FloatProperty(name="Specular Reflect.", 
                              description = " Specular Reflectivity of the IR material surface (Intensity of diffuse Shader)",
                              default=0, min =0, max =1)  
                                                      
    radarreflectivity =bpy.props.FloatProperty(name="Diffuse Reflect.", 
                              description = " Diffuse Reflectivity of the Radar material surface (Intensity of diffuse Shader)",
                              default=0, min =0, max =1)    
                                                      
    radarspecreflectivity =bpy.props.FloatProperty(name="Specular Reflect.", 
                              description = " Specular Reflectivity of the Radar material surface (Intensity of diffuse Shader)",
                              default=0, min =0, max =1)                                                                                 
    matname = StringProperty(
            name=' Material Name',
            description='Name of Material to Assign',
            default="",
            maxlen=63,
            )
     

    temperaturenew = IntProperty(name="Temp", 
                              description = " Temperature in grad Celcius",
                              default=20, min=10, max=99) 
    emissivity =bpy.props.FloatProperty(name="Emissivity", 
                              description = " Emissivity of the material",
                              default=0.9, min =0, max =1) 
    irmirrorreflection = BoolProperty(
                            name="Mirror Reflection",
                            description="Mirror like Reflection (Raytrace)",
                            default=False,
                            )
    radarmirrorreflection = BoolProperty(
                            name="Mirror Reflection",
                            description="Mirror like Reflection (Raytrace)",
                            default=False,
                            )
                            
    irmirrorreflectfactor =bpy.props.FloatProperty(name="Mirror Reflectivity", 
                              description = " Mirror like Reflectivity Factor",
                              default=0, min =0, max =1) 
    radarmirrorreflectfactor =bpy.props.FloatProperty(name="Mirror Reflectivity", 
                              description = " Mirror like Reflectivity Factor",
                              default=0, min =0, max =1)                                
                                                                                                                    
    

 
    def draw(self, context):
        layout = self.layout            
        layout.prop(self, "matname")
        row= layout.row()
        split = row.split(percentage = 0.5)
        column1 = split.column()
        column2 = split.column()
        column2.label ( text = 'Radar Material',
                      icon = 'MATERIAL_DATA')
        column1.label ( text = 'Infrared Material',
                      icon = 'MATERIAL_DATA')  
        column1.prop(self,"irreflectivity")
        column2.prop(self,"radarreflectivity")
        column1.prop(self,"irspecreflectivity")
        column2.prop(self,"radarspecreflectivity")
        column1.prop(self, "temperaturenew")
        column1.prop(self, "emissivity")
        column1.prop(self, "irroughness")
        column2.prop(self, "radarroughness")
        column1.prop(self, "irmirrorreflection")
        column2.prop(self, "radarmirrorreflection")
        column1.prop(self,"irmirrorreflectfactor")
        column2.prop(self,"radarmirrorreflectfactor")


    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)

    def execute(self, context): 
        MakeMaterial(self.matname, self.irreflectivity, self.radarreflectivity, self.irspecreflectivity,self.radarspecreflectivity,self.irroughness,self.radarroughness ,self.temperaturenew, self.emissivity, self.irmirrorreflection, self.radarmirrorreflection, self.irmirrorreflectfactor, self.radarmirrorreflectfactor)
        return {'FINISHED'}
    
class newmatfrompredefined(bpy.types.Operator):
    """Define a new Material using Paramters from predefined Materials"""
    bl_idname = "object.newmatfrompredefined"
    bl_label = "Define new material using Paramters from predefined Materials"
    bl_options = {'REGISTER', 'UNDO'}

    selectedmaterial = StringProperty(
            name='Material Name',
            description='Name of Material to Select',
            maxlen=63,
            )                          
    @classmethod
    def poll(cls, context):
        return context.active_object is not None
    
    def execute(self, context): 
       
        materialoutput = Newmatfrompredefined(self.selectedmaterial)
        op = bpy.ops.object.definenewmat('INVOKE_DEFAULT',matname = materialoutput[0],irreflectivity = materialoutput[1],irspecreflectivity = materialoutput[2],irroughness = materialoutput[3],temperaturenew = materialoutput[4],emissivity = materialoutput[5],irmirrorreflection =materialoutput[6],irmirrorreflectfactor = materialoutput[7],radarreflectivity=materialoutput[8],radarspecreflectivity=materialoutput[9],radarroughness=materialoutput[10],radarmirrorreflection=materialoutput[11],radarmirrorreflectfactor=materialoutput[12])
  
        return {'FINISHED'}
		
class select_material(bpy.types.Menu):
    bl_label = "Select Material"

    def draw(self, context):
        layout = self.layout
        layout.operator_context = 'INVOKE_REGION_WIN'

        ob = context.object
        layout.label
        #show all used materials in entire blend file
        for material_name, material in bpy.data.materials.items():
            layout.operator("object.newmatfrompredefined",
                                    text=material_name,
                                    icon='MATERIAL_DATA',
                                    ).selectedmaterial = material_name

class loadmaterials(bpy.types.Operator):
    """ Load Pedefined Materials"""
    bl_idname = "object.loadmaterials"
    bl_label = " Load Materials"
    bl_options = {'REGISTER','UNDO'} 
          
    
    def draw(self, context):
        self.layout.operator_context = 'INVOKE_REGION_WIN'


    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)
     
    def execute(self, context): 
        loadDefaultMaterials()   
        return {'FINISHED'}    
    
class getpath(bpy.types.Operator):
    """ Load Pedefined Materials from a Blend file"""
    bl_idname = "object.getpath"
    bl_label = " Load Materials from a blendfile"
    bl_options = {'REGISTER','UNDO'} 
    
    filepath = StringProperty(subtype="FILE_PATH") 

    
    def draw(self, context):
        self.layout.operator_context = 'INVOKE_REGION_WIN'
        self.layout.operator("object.getpath",text = "Load Materials from a blend file")


    def invoke(self, context, event):
        context.window_manager.fileselect_add(self)  
        return {'RUNNING_MODAL'}  
     
    def execute(self, context):
        with bpy.data.libraries.load(self.filepath) as (data_from, data_to):
           data_to.materials = data_from.materials
        matlist = bpy.data.materials
        for mat in data_from.materials:
            mat.use_fake_user = True    
        return {'FINISHED'}
     
               
class irwith_diff_temp(bpy.types.Operator):
    """ Change Materials"""
    bl_idname = "object.irwith_diff_temp"
    bl_label = " Materials Toolbox"
    bl_options = {'REGISTER','UNDO'}
    
    temperature =IntProperty(name="Temperature", 
                              description = " Temperature in grad Celcius",
                              default=20, min=10, max=99)                                                                   
    
    all_objects = BoolProperty(
            name="All scene objects",
            description="Change the temperature of all IR materials in the scene",
            default=False,
            )
    all_objects_samemat = BoolProperty(
            name="All objects with the same material",
            description="Change the temperature for all objects with the same material",
            default=False,
            )       
    update_selection = BoolProperty(
            name="Update Selection",
            description="Change the temperature of the selected objects.",
            default=False,
            )                    
      
    
    def draw(self, context):
        layout = self.layout
        layout.prop(self, "temperature")
        layout.prop(self, "all_objects")
        layout.prop(self, "all_objects_samemat")
        layout.prop(self, "update_selection")

     
        
    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)
    
  
    def execute(self,context):
         irwithdifftemp(self.temperature, self.all_objects, self.all_objects_samemat, self.update_selection)
         return {'FINISHED'}
                    

class change_materials(bpy.types.Operator):
    """ Change Materials"""
    bl_idname = "object.change_materials"
    bl_label = " Materials Toolbox"
    bl_options = {'REGISTER','UNDO'}
    
    
    change_to_radar = BoolProperty(
            name="Change to Radar Materials",
            description="Replace Infrared with Radar Material",
            default=False,
            )   
    change_to_ir = BoolProperty(
            name="Change to Infrared Materials",
            description="Replace Radar with Infrared Material",
            default=False,
            )                 
    
    def draw(self, context):
        layout = self.layout
        layout.operator_context = 'INVOKE_REGION_WIN'
        layout.operator("object.loadmaterials",text = "Load Predefined Materials")
        layout.operator("object.getpath",text = "Load Materials from a Blend file")
        layout.prop(self, "change_to_radar")
        layout.prop(self, "change_to_ir")
        layout.operator("object.irwith_diff_temp",
                         text = 'Change to IR with new Temp.',
                         icon = 'MATERIAL_DATA' )
        layout.operator("object.definenewmat",
                         text = 'Define new  Materials',
                         icon = 'MATERIAL_DATA' )
        layout.menu("select_material",
                    text = "Define a new materterial from predefined ",
                    icon = 'MATERIAL_DATA')                  
 
        
    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)
    
  
    def execute(self,context):
         switchmaterials(self.change_to_radar, self.change_to_ir)
         return {'FINISHED'}
		 
# -----------------------------------------------------------------------------
def menu_func(self, context):
   #self.layout.operator_context ='INVOKE_DEFAULT'    
   self.layout.operator(object.loadmaterials.bl_idname)
   self.layout.operator(object.getpath.bl_idname)
   self.layout.operator(object.change_materials.bl_idname)
   self.layout.operator(object.irwith_diff_temp.bl_idname)
   self.layout.operator(object.definenewmat.bl_idname)
   self.layout.operator(object.newmatfrompredefined.bl_idname)

# store keymaps here to access after registration
addon_keymaps = []

classes = (
    definenewmat,
	newmatfrompredefined,
	select_material,
	loadmaterials,
	getpath,
	irwith_diff_temp,
	change_materials,
)

def register():
    #bpy.utils.register_module(__name__) # Blender 2.77
	#new Blender 2.80 method
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)
    #bpy.utils.register_class(loadmaterials)
    #bpy.utils.register_class(getpath)
    #bpy.utils.register_class(change_materials)
    #bpy.utils.register_class(irwith_diff_temp)
    #bpy.utils.register_class(definenewmat)
    #bpy.utils.register_class(newmatfrompredefined)
    #bpy.utils.register_class(select_material)
    #bpy.types.VIEW3D_MT_object.append(menu_func)

    # handle the keymap
    
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    if kc:
        km = wm.keyconfigs.addon.keymaps.new(name='Object Mode', space_type='EMPTY')
        kmi = km.keymap_items.new(change_materials.bl_idname, 'M', 'PRESS', ctrl=True, shift=True)
        kmx = km.keymap_items.new(irwith_diff_temp.bl_idname, 'X', 'PRESS', ctrl=True, shift=True)
        kmo = km.keymap_items.new(definenewmat.bl_idname, 'P', 'PRESS', ctrl=True, shift=True)
        kmt = km.keymap_items.new(newmatfrompredefined.bl_idname, 'T', 'PRESS', ctrl= True, shift =True)
        kml = km.keymap_items.new(loadmaterials.bl_idname, 'L', 'PRESS', ctrl=True, shift=True)
        kmp = km.keymap_items.new(getpath.bl_idname, 'D', 'PRESS', ctrl=True, shift=True)
        #kmi.properties.total = 4
        #kmx.properties.total = 4
        #kmo.properties.total = 4
        #kmt.properties.total = 4
        #kml.properties.total = 4
        #kmp.properties.total = 4
        addon_keymaps.append((km,kmi,kmx,kmo,kmt,kml,kmp))

def unregister():
	#new Blender 2.80 method
    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)
		
    #bpy.utils.unregister_module(__name__)# Blender 2.77	
    #bpy.utils.unregister_class(loadmaterials)
    #bpy.utils.unregister_class(getpath)
    #bpy.utils.unregister_class(change_materials)
    #bpy.utils.unregister_class(irwith_diff_temp)
    #bpy.utils.unregister_class(definenewmat)
    #bpy.utils.unregister_class(newmatfrompredefined)
    #bpy.utils.unregister_class(select_material)
    #bpy.types.VIEW3D_MT_object.remove(menu_func)

    # handle the keymap
    wm = bpy.context.window_manager
    for km, kmi, kmx, kmo, kmt, kml,kmp in addon_keymaps:
        km.keymap_items.remove(kmi)
        km.keymap_items.remove(kmx)
        km.keymap_items.remove(kmo)
        km.keymap_items.remove(kmt)
        km.keymap_items.remove(kml)
        km.keymap_items.remove(kmp)
        wm.keyconfigs.addon.keymaps.remove(km)
        
       
    # clear the list
    addon_keymaps.clear()
    del addon_keymaps[:]


if __name__ == "__main__":
    register()