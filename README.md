# PBC_RF
Point-based Correction Random Forest (PBC-RF) is proposed in the paper "Sun, R., Fu, L., Cheng, Q., Chiang, K. W., & Chen, W. (2023). <em>Resilient pseudorange error prediction and correction for GNSS positioning in urban areas</em>. IEEE Internet of Things Journal."

This repository is our implementation of PBC-RF according to [this paper📝](https://ieeexplore.ieee.org/abstract/document/10012445). You can try this machine-learning model on Android raw GNSS measurements using the Jupyter Notebook "PBC_RF.ipynb" we provide here. The PBC_RF model is built upon sklearn library.

Please note that we don't implement the recursive localization engine described in the original paper and just feed in the ground truth of user positions during inference. 

The data preprocessing functions, the training function, and the evaluation function are properties of NTUsg. If you want to use those sections of codes, please kindly cite us.



