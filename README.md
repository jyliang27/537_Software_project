# ModelPK

ModelPK is a package designed to extract basic information about the pharmacokinetic profile of a drug from experimental data.

Target users:
for bench scientists who have little experience with PK modeling

## Background
### What is PK?
Pharmacokinetics (PK) is the study of how a drug moves through the body. More specifically, it examines:
* Absorption: How does a drug get into the body?
* Distribution: Where does the drug go? For example, does it remain in the bloodstream, or does it partition into certain tissues?
* Metabolism: Does it get broken down by the body?
* Excretion: How does it leave the body?
At any given point, the concentration of a drug in the body will be impacted by its absorption, distribution, metabolism, and excretion.

### Why does it matter?
PK is crucial to understanding the safety and efficacy of a drug. Every drug has a concentration above which it can have serious side effects or be toxic to patients. Likewise, every drug has a concentration below which it no longer has a therapeutic effect. As such, every drug has a therapeutic window in which it actually has a therapeutic effect for patients. Understanding PK profile of a drug allows clinicians and physicians to understand how to keep drug concentrations within this therapeutic window.

## Installation and Use
### Installation
From __ run:
pip install ModelPK

Ensure that the required dependencies, listed in the requirements.txt file, are also installed.

## Use
1. Import the following required dependencies:
    numpy, pandas, sci-kitlearn, tellurium

2. Import ModelPK as entire package, or 
        'import ModelPK'
    OR import each module separately:
        'from ModelPK import extractPKparam as extract'
        'from ModelPK import simulatePK as sim'

3. 

## Author’s note:
This package is currently only supports a 1 compartment model for a drug administered as an IV bolus. In other words, the drug must: i) have been administered intravenously as a single, large dose AND ii) remain in the bloodstream and do not partition into other tissues.

Future work will expand the number of PK models supported.
