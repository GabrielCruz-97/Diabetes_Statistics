# Statistical Analysis of a Diabetes Dataset

Diabetes is a severe chronic disease in which individuals lose the ability to effectively regulate blood glucose levels, potentially leading to a decreased quality of life and life expectancy.

The Behavioral Risk Factor Surveillance System (BRFSS) is a health-related telephone survey collected annually by the Centers for Disease Control and Prevention (CDC) in the United States. Each year, the survey gathers responses from thousands of Americans regarding health risk behaviors, chronic health conditions, and the use of preventive services. For this project, a dataset available on Kaggle for the year 2015 was used.

[Dataset on Kaggle](https://www.kaggle.com/datasets/alexteboul/diabetes-health-indicators-dataset)

![imagem](imagens/cover_www.canva.com.png.jpg)

## Project Organization

```
├── .gitignore         <- Files and directories to be ignored by Git
├── ambiente.yml       <- The requirements file to reproduce the analysis environment
├── LICENSE            <- Open-source license (MIT)
├── README.md          <- This file, providing an overview of the project.
|
├── data              <- Data files for the project.
|
├── notebooks          <- Jupyter Notebooks.
│
|   └──src             <- Source code for use in this project.
|      │
|      ├── __init__.py  <- Makes it a Python module
|      ├── config.py    <- Basic project configurations
|      └── statistics.py  <- Functions created specifically for this project
|
├── references        <- Data dictionaries.
|
├── imagens            <- Images used in the project.
```

## A bit more about the dataset

[Click here](references/01_data_dictionary.md) to see the data dictionary for the dataset used.

## Summary of the main results

#### For the numerical variables we did an analysis for BMI and Diabetes: 

Analysing the relationship between diabetes and BMI using three differente statistical tests (**Levene’s, Student's t, and Mann-Whitney's**), we consistently find that diabetics have **higher and differently distributed BMI values** compared to non-diabetics. These findings are **statistically significant** and highlight an important link between **higher BMI and diabetes**.  

#### For the categorical variables

![imagem](imagens/cover_www.canva.com.png)
![imagem](imagens/binary.png)
![imagem](imagens/nonbinary.png)
![imagem](imagens/education.png)
![imagem](imagens/correlation.png)
