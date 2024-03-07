# PBC_RF
Point-based Correction Random Forest (PBC-RF) is proposed in the paper "Sun, R., Fu, L., Cheng, Q., Chiang, K. W., & Chen, W. (2023). <em>Resilient pseudorange error prediction and correction for GNSS positioning in urban areas</em>. IEEE Internet of Things Journal."

This repository is our implementation of PBC-RF according to [this paper📝](https://ieeexplore.ieee.org/abstract/document/10012445). You can try this machine-learning model on Android raw GNSS measurements using the Jupyter Notebook "PBC_RF.ipynb" we provide here. The PBC_RF model is built upon sklearn library. At the very beginning, you need to set up the running environment using "environment.yml" we provided.

Please note that we don't implement the recursive localization engine described in the original paper and just feed in the ground truth of user positions during inference. We use k-fold cross-validation and grid search to tune the hyperparameters. You can try it by yourself, but it might cost you lots of time.  

The data preprocessing functions, the training function, and the evaluation function are properties of NTUsg. If you wanna use our codes in yours, please kindly cite us as:
[Weng, X., Ling, K. V., & Liu, H. (2023). PrNet: A Neural Network for Correcting Pseudoranges to Improve Positioning with Android Raw GNSS Measurements. arXiv preprint arXiv:2309.12204.](https://arxiv.org/abs/2309.12204)



