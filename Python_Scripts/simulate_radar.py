import bpy

# Path of the Blend File
blendfilepath = '/Users/monikamarkos/Desktop/Synchronized_Simulation_new_2/Blend_File/room.blend'
# Open the Blend File
bpy.ops.wm.open_mainfile(filepath=blendfilepath)

#Set the Camera Focallength
camerafocallen = 16
# Set theCamera Width
camerawidth = 32
objects = bpy.context.scene.objects
for ob in objects:
    if ob.type == 'CAMERA':
        ob.data.lens = camerafocallen
        ob.data.sensor_width = camerawidth
    else: pass

# Switch to Radar Scene Settings
bpy.ops.object.change_materials(change_to_radar = True, change_to_ir = False)
scene = bpy.context.scene
# Set the Resolution of the output Imgae
radar_resolution_x = 1000
radar_resolution_y = 1000
scene.render.resolution_x = radar_resolution_x
scene.render.resolution_y = radar_resolution_y
scene.render.resolution_percentage = 100

# Set the Number of Frames
numofFrames = 2
# Set the Frame Rate per Second
fps = 1

# The output Format for the Radar Images output is OPEN_EXR
scene.render.image_settings.file_format = 'OPEN_EXR'
# The output File to put the rendered Radar Image
outputfile = '/Users/monikamarkos/Desktop/Synchronized_Simulation_new_2/Radar_Renders/'
# Name of the Images
filename = 'room_radar_test'


scene.render.filepath = "/tmp/"
# Render the Combinesd Pass
scene.render.layers["RenderLayer"].use_pass_combined = True
# Render the z-Path
scene.render.layers["RenderLayer"].use_pass_z = True
# Use Nodes
scene.use_nodes = True
# Define the Node Tree for the Ouput File Node to save the Amplitude Image and the depth Image
nodes = scene.node_tree.nodes
for file_output_node in nodes:
     if file_output_node.type =='OUTPUT_FILE':
         nodes.remove(file_output_node)
     elif file_output_node.type =='COMPOSITE':
         nodes.remove(file_output_node)
     else: pass           

render_layers = nodes['Render Layers']
output_file = nodes.new("CompositorNodeOutputFile")
output_file.file_slots.remove(output_file.inputs[0])
output_file.base_path = outputfile
output_file.file_slots.new(filename +'_out')
output_file.file_slots.new(filename +'_z')
scene.node_tree.links.new(
    render_layers.outputs['Image'],
    output_file.inputs[filename +'_out']
)
scene.node_tree.links.new(
    render_layers.outputs['Z'],
    output_file.inputs[filename +'_z']
)
bpy.context.scene.frame_start = 1
bpy.context.scene.frame_end = numofFrames  
bpy.context.scene.render.fps = fps

# Disable Sky in the Rendders
bpy.context.scene.render.layers["RenderLayer"].use_sky = False
# Render the Animation
bpy.ops.render.render(animation=True)
#Export the Camera Path
objects = bpy.context.scene.objects
for ob in objects:
    if ob.type == 'CAMERA':
        ob.select = True
    else: pass      
bpy.ops.export_animation.cameras(filepath = outputfile + 'Camerapath.py',frame_start =1, frame_end= numofFrames)





