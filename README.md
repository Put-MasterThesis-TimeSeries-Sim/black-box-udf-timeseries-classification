# black-box-udf-timeseries-classification

## Description

Project containing notebooks and data used in master thesis project created as a part of Computer Science course on Politechni Poznańska in Poland. Notebooks are used for preprocessing and then to perform experiments. The experiments use Python for classification and similarity analysis between time series data.

## Installation guide

In the repository, requirements.yml can be found in top directory. In order to prepare your envrionment first you need to install miniconda, which can be found on their [site](https://docs.conda.io/en/latest/miniconda.html).

After installing conda run code shown below:

```cmd
conda env create -f requirements.yml
```

This should install all neccesary libraries. After the installation is complete run:

```cmd
conda activate TimeSeriesSimilarity
```

This will activate the prepared environment.

## Running guide

It is recommended to use [Visual Studio Code](https://code.visualstudio.com/) with [Jupyer extension](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter) installed. Otherwise user can use any other software that is able to run Jupiter Notebooks.

In order to repeat experiments done in the Masters degree all of the notebooks need to run in their numerical order without changing their location in the repository (Most of the paths are relative). This means run them in following order:

- 1_merge_data.ipynb

- 2_find_working_nodes.ipynb

- 3_join_files.ipynb

- 4_normalize_data.ipynb

- 5_smooth_data.ipynb

- 6.1_initial_data_analysis.ipynb

- 6.2_graphs.ipynb

- 7_prepare_experiments_datasets.ipynb

- 8.1_calculate_distance_experiments.ipynb

- 8.2_distance_analysis.ipynb

- 9.1_run_machine_learning_type_experiments.ipynb

- 9.2_run_machine_learning_size_experiments.ipynb

- 9.3_results_for_type_machine_learning_experiments.ipynb

- 9.4_results_for_size_machine_learning_experiments.ipynb

All of the results will be visible in 8.2, 9.3 and 9.4 notebooks and results csvs are in *MachineLearing* directory. Additionaly some graphs are saved in Plots directory.
