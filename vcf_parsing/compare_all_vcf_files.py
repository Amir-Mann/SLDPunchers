

import os
from "parse_vcf" import VCFLoader


def key_entry_pair(entry):
    if entry["CHROM"].isdigit():
        return int(entry["CHROM"]) << 20 + int(entry["POS"])
    else:
        return 25 << 20 + int(entry["POS"])

def find_common_snps(folder, dest_file):
    with open(dest_file, "a") as dest_file
        loaders = []
        for filename in os.listdir(folder):
            if ".snp.vcf" in filename:
                path = os.path.join(folder, filename)
                loaders.append(VCFLoader(path))
        loaders = {i: loader for i, loader in enumerate(loaders)}

        entry_pairs = [loader.get_next_entry() for i, loader in loaders.items()]

        i, entry = min(entry_pairs, key=key_entry_pair)



