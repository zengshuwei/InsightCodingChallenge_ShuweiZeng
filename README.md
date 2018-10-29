# Table of Contents
1. [Problem](README.md##problem)
2. [Run Instructions](README.md##Run Instructions)
3. [Approach](README.md##Approach)

## Problem

The challenge is to calculate **Top 10 Occupations** and **Top 10 States** for **certified** H1B visa applications.

## Run Instructions

##### Python version used
- 2.7.5

##### Python default libs used
- sys, csv

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
#### How to run the scripts
The script can be found at `./src/h1b_topmetrics.py`. You can run the script using the `run.sh` in this folder.
```
# ./run.sh
```
The outputs will be in two files `./output/top_10_occupations.txt` and `./output/top_10_states.txt`.

## Approach

My code uses the following approach:

* Process the donation file one line at a time.  This avoids the memory required to read an entire file, in cases of large itcont.txt files.
* Filter out bad records.  The code does not import records with data that do not meet the considerations listed above.
* Use a DonorRecord object to keep track of key donor-level information, in order to determine whether a particular donation is from a repeat donor.
* Use a RecipientRecord object to keep track of information used to calculate outputs (i.e., all donations from repeat donors for a given CMTE_ID, ZIP_CODE, and year of TRANSACTION_DT)
* Use dictionaries to track DonorRecord and RecipientRecord objects.  Use of dictionaries enables rapid lookup of donors and recipients, even in cases of over 1,000,000 records.
