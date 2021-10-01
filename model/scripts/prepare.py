import csv
import os
import sys
from tqdm import tqdm

sys.path.append("../framework/smiles_transformer/")

from utils import split

ROOT = "data" # Here I have put the chembl 24 data...

chembl_data_path = os.path.join(ROOT, "chembl_24_chemreps.txt")
corpus_path = os.path.join(ROOT, "chembl_corpus.txt")

with open(chembl_data_path, "r") as f:
    reader = csv.reader(f, delimiter="\t")
    next(reader)
    R = []
    for r in tqdm(reader):
        R += [split(r[1])]

with open(corpus_path, "w") as f:
    for r in R:
        f.write(r+os.linesep)
