import sys
import os

infile = sys.argv[0]
outfile = sys.argv[2]
checkpoint_dir = sys.argv[3]

# vocabulary generated from chembl 24 (chembl_24_chemreps.txt)
vocab_path = os.path.join(checkpoint_dir, "vocab.pkl")
model_path = os.path.join(checkpoint_dir, "trfm_12_23000.pkl")

# add code path
sys.path.append("smiles_transformer")
import torch
from pretrain_trfm import TrfmSeq2seq
from build_vocab import WordVocab


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

trfm = TrfmSeq2seq(len(vocab), 256, len(vocab), 3)
trfm.load_state_dict(torch.load(model_path, map_location=torch.device('cpu')))

with open(infile, "r") as f:
    reader = csv.reader(f)
    next(reader)
    smiles = []
    for r in reader:
        smiles += [r[0]]

x_split = [split(sm) for sm in smiles]
xid, xseg = get_array(x_split)
X = trfm.encode(torch.t(xid))
print(X.shape)
