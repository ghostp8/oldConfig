import subprocess

import os.path
from os import path



def BlenderRenderImage():
    print("------------------------------------------------")
    
    
    
    ##create desired path
    userImputValidPath=False
    while not(userImputValidPath) :
        scenePath = "/home/cathal/blender/scene/"
        
        fileName = input("input path to scene to render :")
        scenePath=scenePath+fileName+".blend"
            
        if path.exists(scenePath) :
            userImputValidPath = True
                
        else :
            print("Error: file from path does not exist")
            print(scenePath+"\n")
    
   
    #blender Output
    blenderOutput = "/home/cathal/blender/render/output/"
    
    print("Using file:")
    print(scenePath+"\n")
    print("Output file")
    print(blenderOutput+fileName)
    
    
    
    ##run blender
    subprocess.run("blender -b "+scenePath+" -o "+blenderOutput+fileName+"_### -f 0", shell=True)
    print("\n")
    os.system("sxiv /home/cathal/blender/render/output/"+fileName+"_000.png")
    
    
while True :
    BlenderRenderImage()
