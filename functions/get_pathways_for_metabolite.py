from bioservices import KEGG

kegg = KEGG()

# get a list of pathways for a given compound
def get_pathways_for_metabolite(compound_id):
    entry = kegg.get(compound_id)

    lines = entry.split("\n")

    pathway_ids = []

    for line in lines:
        if 'map' in line:
            for word in line.split(' '):
                if 'map' in word:
                    pathway_ids.append(word)


    return pathway_ids

# cpd:C00186 = lactic acid
get_pathways_for_metabolite('cpd:C00186')