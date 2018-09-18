import sys
sys.path.append("/home/trojande/work/freecad-code/lib")

import FreeCAD
import Part
import importDAE
import pyassimp

file = u"/home/trojande/work/github.com/maul-a/stp-to-gltf/part.stp"
FreeCAD.newDocument()
FreeCAD.setActiveDocument("Unnamed")
doc = FreeCAD.getDocument("Unnamed")
Part.insert(file, "Unnamed")
importDAE.export(doc.Objects, u"/home/trojande/work/github.com/maul-a/stp-to-gltf/part.dae")
assimp_scene = pyassimp.load('part.dae')
pyassimp.export(assimp_scene, 'part.gltf', 'gltf2')
