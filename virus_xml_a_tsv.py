import xml.etree.ElementTree as ET

# Archivo de entrada y salida
xml_file = "sequences (1).xml"

# Parsear el XML
tree = ET.parse(xml_file)
root = tree.getroot()

# Encabezados
print("Protein", "Organism_Name", "Length", "Host", "Tissue_Specimen_Source", "Geo_Location", "Species", sep="\t")

# Iterar sobre cada Item
for item in root.findall("Item"):
    protein = item.findtext("Protein", "")
    organism = item.findtext("Organism_Name", "")
    length = item.findtext("Length", "")
    host = item.findtext("Host", "")
    tissue = item.findtext("Tissue_Specimen_Source", "")
    geo = item.findtext("Geo_Location", "")
    species = item.findtext("Species", "")

    # Imprimir en formato tabulado
    print(protein, organism, length, host, tissue, geo, species, sep="\t")
