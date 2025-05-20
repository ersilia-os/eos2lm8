FROM bentoml/model-server:0.11.0-py38
MAINTAINER ersilia

RUN pip install tqdm==4.64
RUN pip install rdkit==2022.3.5
RUN pip install torch==1.12.0
RUN pip install pandas==1.3.5

WORKDIR /repo
COPY . /repo
