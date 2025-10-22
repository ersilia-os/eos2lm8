# SMILES transformer descriptor

Molecular embedding based on natural language processing. It converts SMILES into fingerprints using an unsupervised model pre-trained on a very large SMILES dataset from ChEMBL. The transformer is particularly well-suited for low-data drug discovery.

This model was incorporated on 2021-09-28.Last packaged on 2025-10-22.

## Information
### Identifiers
- **Ersilia Identifier:** `eos2lm8`
- **Slug:** `smiles-transformer`

### Domain
- **Task:** `Representation`
- **Subtask:** `Featurization`
- **Biomedical Area:** `Any`
- **Target Organism:** `Any`
- **Tags:** `Chemical language model`, `Descriptor`, `Embedding`

### Input
- **Input:** `Compound`
- **Input Dimension:** `1`

### Output
- **Output Dimension:** `1024`
- **Output Consistency:** `Variable`
- **Interpretation:** Vector representation of small molecules

Below are the **Output Columns** of the model:
| Name | Type | Direction | Description |
|------|------|-----------|-------------|
| feature_0000 | float |  | Feature 0 of the smiles transformer |
| feature_0001 | float |  | Feature 1 of the smiles transformer |
| feature_0002 | float |  | Feature 2 of the smiles transformer |
| feature_0003 | float |  | Feature 3 of the smiles transformer |
| feature_0004 | float |  | Feature 4 of the smiles transformer |
| feature_0005 | float |  | Feature 5 of the smiles transformer |
| feature_0006 | float |  | Feature 6 of the smiles transformer |
| feature_0007 | float |  | Feature 7 of the smiles transformer |
| feature_0008 | float |  | Feature 8 of the smiles transformer |
| feature_0009 | float |  | Feature 9 of the smiles transformer |

_10 of 1024 columns are shown_
### Source and Deployment
- **Source:** `Local`
- **Source Type:** `External`
- **DockerHub**: [https://hub.docker.com/r/ersiliaos/eos2lm8](https://hub.docker.com/r/ersiliaos/eos2lm8)
- **Docker Architecture:** `AMD64`, `ARM64`
- **S3 Storage**: [https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos2lm8.zip](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos2lm8.zip)

### Resource Consumption
- **Model Size (Mb):** `22`
- **Environment Size (Mb):** `2301`
- **Image Size (Mb):** `2300.61`

**Computational Performance (seconds):**
- 10 inputs: `28.21`
- 100 inputs: `21.5`
- 10000 inputs: `252.82`

### References
- **Source Code**: [https://github.com/DSPsleeporg/smiles-transformer](https://github.com/DSPsleeporg/smiles-transformer)
- **Publication**: [https://arxiv.org/abs/1911.04738](https://arxiv.org/abs/1911.04738)
- **Publication Type:** `Preprint`
- **Publication Year:** `2019`
- **Ersilia Contributor:** [miquelduranfrigola](https://github.com/miquelduranfrigola)

### License
This package is licensed under a [GPL-3.0](https://github.com/ersilia-os/ersilia/blob/master/LICENSE) license. The model contained within this package is licensed under a [MIT](LICENSE) license.

**Notice**: Ersilia grants access to models _as is_, directly from the original authors, please refer to the original code repository and/or publication if you use the model in your research.


## Use
To use this model locally, you need to have the [Ersilia CLI](https://github.com/ersilia-os/ersilia) installed.
The model can be **fetched** using the following command:
```bash
# fetch model from the Ersilia Model Hub
ersilia fetch eos2lm8
```
Then, you can **serve**, **run** and **close** the model as follows:
```bash
# serve the model
ersilia serve eos2lm8
# generate an example file
ersilia example -n 3 -f my_input.csv
# run the model
ersilia run -i my_input.csv -o my_output.csv
# close the model
ersilia close
```

## About Ersilia
The [Ersilia Open Source Initiative](https://ersilia.io) is a tech non-profit organization fueling sustainable research in the Global South.
Please [cite](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff) the Ersilia Model Hub if you've found this model to be useful. Always [let us know](https://github.com/ersilia-os/ersilia/issues) if you experience any issues while trying to run it.
If you want to contribute to our mission, consider [donating](https://www.ersilia.io/donate) to Ersilia!
