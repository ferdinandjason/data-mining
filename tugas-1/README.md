# Tugas 1 Data Mining (IF184951)

## Outline
- [Tugas 1 Data Mining (IF184951)](#tugas-1-data-mining-if184951)
    - [Outline](#outline)
    - [Dataset `Adult` :](#dataset-adult-)
    - [Tugas](#tugas)
    - [Implementasi](#implementasi)
    - [Requirement](#requirement)
    - [Data Dictionary `Adult` :](#data-dictionary-adult-)

## Dataset `Adult` :
| Data | Value |
|------|:-----:|
| Data Set Characteristics: | Multivariate |
| Attribute Characteristics: | Categorical, Integer |
| Associated Tasks: | Classification |
| Number of Instances: | 48842 |
| Number of Attributes: | 14 |
| Missing Values? | Yes |
| Area: | Social |
| Date Donated : | 1996-05-01 |

## Tugas
Dataset yang dianalisis adalah dataset `Adult` dari UCI Machine Learning Repository (https://archive.ics.uci.edu/ml/datasets/adult).
- Melakukan eksplorasi data :
    - Informasi Statistik Data
    - Histogram
    - Box-Plot
    - Analisa Korelasi Data
- Melakukan Praproses :
    - Imputasi
    - Penghilangan Noise

## Implementasi
Implementasi dapat diakses pada ![LINK](tugas-1.ipynb)

## Requirement
- Tool
    - Anaconda
    - Jupyter Notebook / Jupyter Lab
- Library
    - `pandas`
    - `numpy`
    - `seaborn`
    - `mathplotlib` => `pyplot`
    - `scikit-learn` => `preprocessing` , `SimpleImputer`
    - (All included in Anaconda)


## Data Dictionary `Adult` : 
1. Categorial Attributes
    - workclass: (categorical) Private, Self-emp-not-inc, Self-emp-inc, Federal-gov, Local-gov, State-gov, Without-pay, Never-worked.
        - Individual work category
    - education: (categorical) Bachelors, Some-college, 11th, HS-grad, Prof-school, Assoc-acdm, Assoc-voc, 9th, 7th-8th, 12th, Masters, 1st-4th, 10th, Doctorate, 5th-6th, Preschool.
    - Individual's highest education degree
    - marital-status: (categorical) Married-civ-spouse, Divorced, Never-married, Separated, Widowed, Married-spouse-absent, Married-AF-spouse.
        - Individual marital status
    - occupation: (categorical) Tech-support, Craft-repair, Other-service, Sales, Exec-managerial, Prof-specialty, Handlers-cleaners, Machine-op-inspct, Adm-clerical, Farming-fishing, Transport-moving, Priv-house-serv, Protective-serv, Armed-Forces.
        - Individual's occupation
    - relationship: (categorical) Wife, Own-child, Husband, Not-in-family, Other-relative, Unmarried.
        - Individual's relation in a family
    - race: (categorical) White, Asian-Pac-Islander, Amer-Indian-Eskimo, Other, Black.
        - Race of Individual
    - sex: (categorical) Female, Male.
    - native-country: (categorical) United-States, Cambodia, England, Puerto-Rico, Canada, Germany, Outlying-US(Guam-USVI-etc), India, Japan, Greece, South, China, Cuba, Iran, Honduras, Philippines, Italy, Poland, Jamaica, Vietnam, Mexico, Portugal, Ireland, France, Dominican-Republic, Laos, Ecuador, Taiwan, Haiti, Columbia, Hungary, Guatemala, Nicaragua, Scotland, Thailand, Yugoslavia, El-Salvador, Trinadad&Tobago, Peru, Hong, Holand-Netherlands.
        - Individual's native country

2. Continuous Attributes
    - age: continuous.
        - Age of an individual
    - education-num: number of education year, continuous.
        - Individual's year of receiving education
    - fnlwgt: final weight, continuous.
        - The weights on the CPS files are controlled to independent estimates of the civilian noninstitutional population of the US. These are prepared monthly for us by Population Division here at the Census Bureau.
    - capital-gain: continuous.
    - capital-loss: continuous.
    - hours-per-week: continuous.
        - Individual's working hour per week