

import os
from "parse_vcf" import VCFLoader


MAX_KEY = 1 << 31


def entry_to_key(entry):
    if entry is None:
        return MAX_KEY
    elif entry["CHROM"].isdigit():
        return int(entry["CHROM"]) << 20 + int(entry["POS"])
    else:
        return 25 << 20 + int(entry["POS"])

def find_common_snps(folder, dest_file):
    last_entry = None
    with open(dest_file, "a") as dest_file
        loaders = []
        names = []
        for filename in os.listdir(folder):
            if ".snp.vcf" in filename:
                path = os.path.join(folder, filename)
                loaders.append(VCFLoader(path))
                names.append(filename)
        loaders = {i: loader for i, loader in enumerate(loaders)}

        entrys = [loader.get_next_entry() for i, loader in loaders.items()]
        keys = [entry_to_key(entry) for entry in entrys]
        
        while True:
            min_key = min(keys)
            if min_key == MAX_KEY:
                break
            matching_index = [i for i, key in enumerate(keys) if key  == min_key]

            if len(matching_index) > 1:
                dest_file.write(str([(names[i], entrys[i]) for i in matching_index]))
                dest_file.write("\n")
            for i in matching_index:
                try:
                    entrys[i] = loaders[i].get_next_entry()
                except StopIteration:
                    entrys[i] = None
                keys[i] = entry_to_key(entrys[i])

