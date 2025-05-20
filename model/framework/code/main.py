# generic inputs
import sys
import os
import csv
import numpy as np

infile = sys.argv[1]
outfile = sys.argv[2]

root = os.path.dirname(os.path.abspath(__file__))
checkpoint_dir = os.path.abspath(os.path.join(root, "..", "..", "checkpoints"))

# vocabulary generated from chembl 24 (chembl_24_chemreps.txt)
vocab_path = os.path.join(checkpoint_dir, "vocab.pkl")
model_path = os.path.join(checkpoint_dir, "trfm_12_23000.pkl")

assert os.path.exists(vocab_path)
assert os.path.exists(model_path)
assert os.path.exists(infile)

# add code path
import torch
sys.path.append(os.path.join(root, "..", "smiles_transformer"))
from pretrain_trfm import TrfmSeq2seq
from build_vocab import WordVocab
from utils import split

pad_index = 0
unk_index = 1
eos_index = 2
sos_index = 3
mask_index = 4


def get_inputs(sm):
    seq_len = 220
    sm = sm.split()
    if len(sm)>218:
        print('SMILES is too long ({:d})'.format(len(sm)))
        sm = sm[:109]+sm[-109:]
    ids = [vocab.stoi.get(token, unk_index) for token in sm]
    ids = [sos_index] + ids + [eos_index]
    seg = [1]*len(ids)
    padding = [pad_index]*(seq_len - len(ids))
    ids.extend(padding), seg.extend(padding)
    return ids, seg

def get_array(smiles):
    x_id, x_seg = [], []
    for sm in smiles:
        a,b = get_inputs(sm)
        x_id.append(a)
        x_seg.append(b)
    return torch.tensor(x_id), torch.tensor(x_seg)

vocab = WordVocab.load_vocab(vocab_path)

trfm = TrfmSeq2seq(len(vocab), 256, len(vocab), 4)
trfm.load_state_dict(torch.load(model_path, map_location=torch.device('cpu')))

with open(infile, "r") as f:
    reader = csv.reader(f)
    header = next(reader)
    smiles = []
    for r in reader:
        smiles += [r[0]]

x_split = [split(sm) for sm in smiles]
xid, xseg = get_array(x_split)
X = trfm.encode(torch.t(xid))

with open(outfile, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow([f"feature_{str(i).zfill(4)}" for i in range(X.shape[1])])
    writer.writerows(X)
