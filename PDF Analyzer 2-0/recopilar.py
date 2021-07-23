import os
import pathlib
import shutil
copyDir = "C:\\Users\\Usuario\\Desktop\\Proyectos_Invepat\\Repositorio\\pdf_analyzer_invepat\\All PDF\\"
l = []
def getExtension(param):
    if pathlib.Path(param).suffix == ".pdf":
        shutil.copy(param,copyDir)
for root, dirs, files in os.walk("C:\\Users\\Usuario\\Desktop\\Proyectos_Invepat\\Repositorio\\pdf_analyzer_invepat\\"):
    for name in files:
        if pathlib.Path(name).suffix == ".pdf":

            l.append(os.path.join(root,name))
    """for name in dirs:
        print(os.path.join(root, name))"""

print(len(l))
print(l)