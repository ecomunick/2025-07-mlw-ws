# 2025-07-mlw-ws

## day 1
this prohect is based on https://github.com/alexeygrigorev/ml-engineering-contsructor-workshop

## how to install UV  
(https://docs.astral.sh/uv/getting-started/installation/#installation-methods)
juts run `curl -LsSf https://astral.sh/uv/install.sh | sh`

## day 1 steps

- create a folder `day1``
- change directory into it via `cd day1`
- run `uv init --python 3.10` to inintialize a uv project
- run `uv sync` 


## download the notebook:

- `mkdir notebooks`
- `cd notebooks`
- `wget "https://raw.githubusercontent.com/alexeygrigorev/ml-engineering-contsructor-workshop/refs/heads/main/01-train/duration-prediction-starter.ipynb"`
- `cd .. `  

### install dependencies
- uv add scikit-learn==1.2.2 pandas pyarrow
- fix issue with numpy via `uv add numpy==1.26.4`
- install jupyter `uv add --dev jupyter seaborn`

### launch jupyetr notebook
`uv run jupyter notebook`

##### control + c to close jupyet notebook in terminal #### 

### convert notebook into a script
- `uv run jupyter nbconvert --to=script notebooks/duration-prediction-starter.ipynb`
- create a new folder `duration_prediction` and move the file `duration-prediction-starter.py`into that folder and rename it into `train.py`

### lets make the train.py script nice



