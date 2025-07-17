
# human-4d-slicer.py
# Script à exécuter dans l’environnement Python intégré de 3D Slicer

# Ce script exporte chaque segment d'une segmentation en fichiers STL individuels,
# pour usage ultérieur dans la reconstruction 3D rituelle ou impression sacrée.

import slicer
import os

# PARAMÈTRES : Personnalisez ici
segmentationNode = getNode('seg-segmentation')  # Modifier si le nom de segmentation diffère
outputDirectory = 'C:/Users/YourUsername/Documents/LurkuitaeSTL/'  # Chemin local à modifier

# Créer le dossier s'il n'existe pas
if not os.path.exists(outputDirectory):
    os.makedirs(outputDirectory)

segmentation = segmentationNode.GetSegmentation()
numSegments = segmentation.GetNumberOfSegments()

print(f"🔍 Segments trouvés : {numSegments}")

for i in range(numSegments):
    segmentID = segmentation.GetNthSegmentID(i)
    segmentName = segmentation.GetNthSegment(i).GetName()
    safeName = "".join(c if c.isalnum() else "_" for c in segmentName)
    filePath = os.path.join(outputDirectory, f"{safeName}.stl")

    slicer.modules.segmentations.logic().ExportSegmentToRepresentationFile(
        segmentationNode, segmentID, filePath, "STL"
    )
    print(f"✅ Exporté : {filePath}")

print("🌟 Tous les segments ont été extraits avec succès.")
