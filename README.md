# SMILES transformer descriptor

Molecular embedding based on natural language processing. It converts SMILES into fingerprints using an unsupervised model pre-trained on a very large SMILES dataset from ChEMBL. The transformer is particularly well-suited for low-data drug discovery.

## Identifiers

* EOS model ID: `eos2lm8`
* Slug: `smiles-transformer`

## Characteristics

* Input: `Compound`
* Input Shape: `Single`
* Task: `Representation`
* Output: `Descriptor`
* Output Type: `Float`
* Output Shape: `List`
* Interpretation: Vector representation of small molecules

## References

* [Publication](https://arxiv.org/abs/1911.04738)
* [Source Code](https://github.com/DSPsleeporg/smiles-transformer)
* Ersilia contributor: [miquelduranfrigola](https://github.com/miquelduranfrigola)

## Citation

If you use this model, please cite the [original authors](https://arxiv.org/abs/1911.04738) of the model and the [Ersilia Model Hub](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff).

## License

This package is licensed under a GPL-3.0 license. The model contained within this package is licensed under a MIT license.

Notice: Ersilia grants access to these models 'as is' provided by the original authors, please refer to the original code repository and/or publication if you use the model in your research.

## About Us

The [Ersilia Open Source Initiative](https://ersilia.io) is a Non Profit Organization ([1192266](https://register-of-charities.charitycommission.gov.uk/charity-search/-/charity-details/5170657/full-print)) with the mission is to equip labs, universities and clinics in LMIC with AI/ML tools for infectious disease research.

[Help us](https://www.ersilia.io/donate) achieve our mission!