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

#### Explanations

Inside the [explanations](explanations/) folder, we have all SHAP explanations for each target. 

### Features

The complete list of features is available in the [features](features/) folder. There are two files in this folder:

- [features.md](features/features.md): contains the list of features used in the study with the considered correlation.
- [OpenStaticAnalyzer-1.0-Metrics.html](features/OpenStaticAnalyzer-1.0-Metrics.html): contains the list of features with a brief description.

### Models

The models created in the study are available in the [models](models/) folder. Each target has its own `pickle` file. Note that some files are too large for GitHub storage, and you have to unzip the `zip` files to use the models (defect, gc, lc, and sc).

### Notebooks

The notebooks are organized as follows:

- [01-setup.ipynb](notebooks/01-setup.ipynb): prepares, trains and executes the data for the study.
- [02-predict.ipynb](notebooks/02-predict.ipynb): loads the models and predicts with unseen data.

### Results

The results are available in the [results](results/) folder. There, we have the performance of each model and the results of the statistical tests.

### Scripts

Inside the [scripts](scripts/) folder, we stored the [Organic](https://github.com/opus-research/organic) jar.

### Validation

Inside the [validation](validation/) folder, we have the results of the validation of the Organic tool with developers.

## Replication Instructions

If the required packages are installed according to the Setup section of this document. You should be able to run each cell of the notebooks in the [notebooks](notebooks/) folder.

### Code Smells Definitions

In our study, we evaluate the following smells:

| Code Smell                   | Definition                                                                                  | Reference |
| ---------------------------- | ------------------------------------------------------------------------------------------- | --------- |
| God Class                    | A large class that has too many responsibilities and centralizes the module functionality. | [3]       |
| Refused Bequest              | A class that does not want to use its parent behavior.                                      | [2]       |
| Spaghetti Code               | A class that has methods with large and unique multistage process flow.                     | [1]       |
| Class Data Should be Private | A class with too many public fields.                                                        | [4]       |
| Data Class                   | Classes that have only fields, getters, and setters.                                         | [2]       |
| Lazy Class                   | Classes that have little behavior, with few methods and fields.                             | [2]       |
| Speculative Generality       | Classes that support future behavior, usually interacting with test classes only.           | [2]       |

To identify such smells we relied on the Organic tool. If you want to run the Organic tool to asses the smell collection process, you can, for instance, for the project `ant`, execute the following command:

```bash
java -jar organic-OPT.jar -sf ../projects/ant/organic/ant.json -src "../bad-smells-defects/projects/ant"
```

You can execute the `organic-OPT.jar` included inside the [scripts](scripts/) folder. We highlight that Organic needs to be run on OpenJDK 11, so you need to change the java version in case it is not the required one.

##### References

- [1] Brown, W.H., Malveau, R.C., McCormick, H.W.S., Mowbray, T.J.: AntiPatterns: refactoring software, architectures, and projects in crisis. John Wiley & Sons, Inc. (1998)
- [2] Fowler, M.: Refactoring: Improving the Design of Existing Code. Addison-Wesley (1999)
- [3] Riel, A.: Object Oriented Design Heuristics. Addison-Wesley Professional (1996)
- [4] Shvets, A.: Dive into Design Patterns. Refactoring Guru (2021)
