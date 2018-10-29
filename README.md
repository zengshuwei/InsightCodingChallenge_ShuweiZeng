## Problem

The challenge is to calculate **Top 10 Occupations** and **Top 10 States** for **certified** H1B visa applications.

## Run Instructions

#### Input
Please put visa process data file in folder `./input` and *rename* as `h1b_input.csv`.

#### Python version used
- 2.7.5

##### Python default libs used
- sys, csv

#### How to run the scripts
The script can be found at `./src/h1b_topmetrics.py`. You can run the script using the `run.sh` in this folder.
```
# ./run.sh
```

#### Output
The outputs will be in two files `./output/top_10_occupations.txt` and `./output/top_10_states.txt`.

#### Repo directory structure

The directory structure for your repo should look like this:
```
      ├── README.md 
      ├── run.sh
      ├── src
      │   └──h1b_topmetrics.py
      ├── input
      │   └──h1b_input.csv
      ├── output
          └── top_10_occupations.txt
          └── top_10_states.txt

```

## Approach

My code uses the following approach:

* Process the visa application file one line at a time. This avoids the memory required to read an entire file.
* Filter and only consider observations with status as "certified". If status is not certified, stop processing and go to the next observation.
* Use a update_freq object to keep track of the frequencies of each state and each occupation. After process all the application once, we have the frequencies of all the states and occupations appeared in certified observations.
* Use a find_top objection to sort states and occupantions and return the top 10 records.
