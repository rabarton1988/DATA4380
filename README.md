# Lorentz Boost Network  

* **One Sentence Summary** This repository holds an attempt to apply the Lorentz Booost Network to the existing HPANA neural network used for Charged Higgs to Tau Nu searches to see if it can improve the preformance.  

## Overview  

  * The task is to separate Charged Higgs to Tau Nu signal events from background events such as TTbar, QCD, SingleTop, Wtaunu, Ztautau, and DiBoson.  
  * The approach in this repository was to take an existing neural network, insert the LBN layer, and see if the performance of the network noticeably improved.  
  * The network has yet to be tested on an appropriately sized data set to show any significant performance improvements over the original HPANA model.  

## Summary of Workdone  

### Data  

* Data:
  * Type: Ntuples taken from Monte Carlo signal/background and run data.
    * HPANA Input: Dataframe of particle events including high and low level variables.  
    * LBN Input: CSV of particle 4-momenta  
    * Output: signal/background  
  * Size: 7433 events  
  * Instances (Train, Test, Validation Split):  
    - Training: 5000 events  
    - Testing: 2433 events  

#### Preprocessing / Clean up  

* Access to the data used for the HPANA neural network required CERN grid space certification.  
* Symlinks were created to access the ntuples on the CERN grid space.  
* The HPANA code used to run the network (train-classifier.py) generates a pickle file that includes a dataframe of the requested signal and background data points. This data has been saved to PtEtaPhiE.csv.  
* For the initial setup, the signal events only include the Hplus200 mass point and the background events only includes DiBoson.   
* The required 4-momenta vectors for the LBN layer were produced by converting the PtEtaPhiE vectors to EPxPyPz vectors in ROOT using the LBN_Vector_Conversion.py script.   

### Problem Formulation

* Define:
  * Models:
    * HPANA model:
      - Sequential model with Dense and Dropout layers  
    * LBN model:
      - Same as HPANA, but with the addition of the LBN layer.  
  * Loss: binary_crossentropy
  * Optimizer: adam
  * Hyperparameters: The LBN contains the M hyperparameters. This should be selected for the number of intermediate particles and rest frames.  

### Training  

* Describe the training:  
  * The training was done on a local machine   
  * Training on the small 7433 event sample takes roughly a minute to complete.  
  * Training curves (loss vs epoch for test/train).  
  * Training duration was determined by finding the point when overtraining begins, and stopping prior.  

### Conclusions  

* The results of the LBN implementation are inconclusive. The dataset used is incomplete and too small to see any significant results.   

### Future Work  

* The next step is to get a larger data set that includes all the backgrounds and Hplus mass points.  

### Overview of files in repository  
  
  * LBN_Testing_plots.ipynb   
    - Plots of the data from PtEtaPhiE.csv and EPxPyPz.csv  

  * LBN_Testing_Original_Model.ipynb  
    - Original [HPANA](https://gitlab.cern.ch/atlas-hbsm-charged-higgs-taunu/hpana) model that trains on PtEtaPhiE.csv  

  * LBN_Testing_LBN_Model.ipynb  
    - Model including the [LBN](https://github.com/riga/LBN) layer that trains on EPxPyPz.csv  

  * LBN_Vector_Conversion.py  
    - Script used to convert PtEtaPhiE vectors to EPxPyPz vectors   

  * Generated data files:  
    - EPxPyPz.csv  
    - PtEtaPhiE.csv  

### Software Setup  
* Python  
* Numpy  
* Tensorflow  
* ROOT  

## Citations  

* https://github.com/riga/LBN  
* https://gitlab.cern.ch/atlas-hbsm-charged-higgs-taunu/hpana  








