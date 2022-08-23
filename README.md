# SMILES transformer embeddings
## Model identifiers
- Slug: smiles-transformer
- Ersilia ID: eos2lm8
- Tags: Embedding

# Model description
The SMILES transformer creates 1024-dimensional descriptors (embeddings) based on the ChEMBL database.
- Input: Compound
- Output: Embeddings 
- Model type: Unsupervised
- Training set: All of ChEMBL 24
- Mode of training: It is pretrained

# Source code
- Publication: https://arxiv.org/abs/1911.04738
- Code: https://github.com/DSPsleeporg/smiles-transformer
- Checkpoints: Pretrained model is made available by the authores [here](https://drive.google.com/file/d/1LwE2BzvtDaPGYv0OR6iBjmsqoloH885N/view?usp=sharing). Vocabulary was created locally following [these instructions](https://github.com/DSPsleeporg/smiles-transformer/issues/17#issuecomment-1173134055).

# License
GPL v3

# History 
- We created the vocabulary following instructions from a GitHub issues thread [#17](https://github.com/DSPsleeporg/smiles-transformer/issues/17#issuecomment-1173134055).
- Model was incorporated on the 23/08/2022.

# About us
The [Ersilia Open Source Initiative](https://ersilia.io) is a Non Profit Organization ([1192266](https://register-of-charities.charitycommission.gov.uk/charity-search/-/charity-details/5170657/full-print)) with the mission is to equip labs, universities and clinics in LMIC with AI/ML tools for infectious disease research.

[Help us](https://www.ersilia.io/donate) achieve our mission or [volunteer](https://www.ersilia.io/volunteer) with us!