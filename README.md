# PhD Artifacts Repository

## Summary

Welcome to the Artifacts for the PhD Thesis "Understanding Software Defects with Machine Learning" to be presented February 13th 2023 in Belo Horizonte, Brazil by Geanderson Esteves dos Santos. In this thesis, we aim at understanding the features that impact the defectiveness of software projects. To do so, we applied machine learning techniques to popular datasets. Hence, we convey an exploratory investigation that produced thousands of models from a diverse collection of software features. These models are random because they promptly select the features from the entire pool of software features. Even though the immense majority of models are ineffective, we could produce several models that yield accurate predictions. Thus, the models distinguish defect-prone classes from clean ones. We focus our investigation on models that rank a randomly chosen defective software class higher than a randomly selected non-defective class with over 85\% accuracy. More importantly, we employ these results to discuss a set of features contributing to the understandability of model decisions. As a result, we notice that the best-performing models are simple to understand as they rely on a small set of features. Therefore, we present which features contribute to the defects of twelve projects. Further, we also compare the threshold of these features. To validate the results, we survey 40 developers to measure their perceptions of the models and conclude that the models are fairly understandable. Complementary, we also evaluate developers' perception of the quality attributes with active GitHub developers, where 54 participated in the investigation. Then, we conclude that developers' perceptions differ significantly from the machine learning models in terms of quality attributes. Finally, we compare the redundancies and similarities between defect models with code smell as they share several features. By the end, this thesis promotes reasoning on which software features influence the defects of these projects.

You can cite the repository as follows:

```bibtex
@phdthesis{SantosThesis2023,
  author = {G. E. dos Santos},
  title = {Understanding Software Defects with Machine Learning},
  school = {Federal University of Minas Gerais},
  year = {2023},
  type = {PhD thesis},
  address = {Belo Horizonte, Brazil},
}
```

## Hardware Requirements

All experiments were performed on a machine with the following specifications:
- 16 GB RAM
- 8th generation Intel Core i7 processor (or equivalent)

## Setup

To use the replication package, we recommend applying the dependencies included in the [requirements](requirements.txt) file. We strongly recommend using Python 3.9 Virtual Environment as follows, since Pycaret requires it.

```bash
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt
```

In case you don't have Python 3.9, you can use Pyenv to install it. As these scripts may be useful for other projects, we include them in the [scripts](scripts/) folder.


```bash
# Install dependencies
sudo apt update
sudo apt install -y make build-essential libssl-dev zlib1g-dev libbz2-dev \
libreadline-dev libsqlite3-dev wget curl llvm libncursed5-dev xz-utils tk-dev

# Install pyenv
curl https://pyenv.run | bash

# Add pyenv to PATH and initialize
echo 'export PATH="~/.pyenv/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init -)"' >> ~/.bashrc
source ~/.bashrc

# Update list of available Python versions
pyenv update

# Install Python 3.9
pyenv install 3.9.0

# Set global Python version to 3.9
pyenv global 3.9.0

# Verify installation
python --version
```

From there, you can run the notebooks in the [src](src/ch7) folder and the script in the [src](src/ch4). Below, we describe each folder contained in the repository.

### Data

All data is available under the [data](data/) folder. Below, we present the folder's working tree.

| Folder                                    | Content                          |
| ----------------------------------------- | -------------------------------- |
| [**bug-prediction**](data/bug-prediction) | Contains the Bug Prediction data |
| [**jureczko**](data/jureczko)             | Contains the Jureczko data       |
| [**nasa**](data/nasa)                     | Contains the NASA data           |
| [**unified**](data/unified)               | Contains the Unified data        |

### Explanations

Inside the [explanations](explanations/) folder, we have all SHAP explanations for each target presented in the thesis. Below, we present the folder's working tree. 

| Folder                            | Content                                      |
| --------------------------------- | -------------------------------------------- |
| [**Chapter 5**](explanations/ch5) | Contains the SHAP explanations for Chapter 5 |
| [**Chapter 7**](explanations/ch7) | Contains the SHAP explanations for Chapter 7 |

### Features

The complete list of features is available in the [features](features/) folder. There are two files in this folder:

- [features.md](features/features.md): contains the list of features used in the study with the considered correlation.
- [OpenStaticAnalyzer-1.0-Metrics.html](features/OpenStaticAnalyzer-1.0-Metrics.html): contains the list of features with a brief description.

### Models

The models created in the study are available in the [models](models/) folder. Each target has its own `pickle` file. Note that some files inside the [Chapter 7](models/ch7) folder are too large for GitHub storage, and you have to unzip the `zip` files to use the models (defect, gc, lc, and sc). Furthermore, we are unable to store the Chapter 4 models inside Git as it has over 1 GB. Inside the [Chapter 4](models/ch4), we have instructions on how to download the models from Zenodo. Below, we present the folder's working tree.

| Folder                      | Content                           |
| --------------------------- | --------------------------------- |
| [**Chapter 4**](models/ch4) | Contains the models for Chapter 4 |
| [**Chapter 7**](models/ch7) | Contains the models for Chapter 7 |

### Source Code

The [src](src/) folder contains the source code to run the models. Below, we present the folder's working tree.

| Folder                   | Content                                |
| ------------------------ | -------------------------------------- |
| [**Chapter 4**](src/ch4) | Contains the source code for Chapter 4 |
| [**Chapter 7**](src/ch7) | Contains the source code for Chapter 7 |

### Scripts

Inside the [scripts](scripts/) folder, we stored the [Organic](https://github.com/opus-research/organic) jar.

### Validation

Inside the [validation](validation/) folder, we have the results of the validation of the Organic tool with developers.

Feel free to contact me if you have any questions or suggestions.