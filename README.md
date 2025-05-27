# Cyber Threat Detection using Artificial Neural Networks

This project implements a cyber threat detection system using various machine learning and deep learning models. It features a graphical user interface (GUI) built with Tkinter for easy interaction.

## Project Overview

The system is designed to detect cyber threats based on network event profiles. It loads network traffic data, preprocesses it, and then trains and evaluates several classification models to identify malicious activities.

The following machine learning and deep learning models are implemented and compared:
* Long Short-Term Memory (LSTM)
* Convolutional Neural Network (CNN)
* Support Vector Machine (SVM)
* K-Nearest Neighbors (KNN)
* Decision Tree
* Random Forest
* Naive Bayes (BernoulliNB)

The performance of each model is evaluated based on precision, recall, F1-score, and accuracy.

## Files in the Project

* **`CyberThreatDetection.py`**: The main Python script that runs the application. It includes the GUI, data processing, model training, and evaluation logic.
* **`test.py`**: Appears to be a script for testing or potentially another version of the detection mechanism, also utilizing machine learning techniques.
* **`requirements.txt`**: A text file listing the necessary Python packages to run the project.
* **`datasets/`**: This directory contains the datasets used for training and testing the models.
    * `kdd_train.csv`: The training dataset.
    * `kdd_test.csv`: The testing dataset.

## Datasets

The project uses the KDD Cup 1999 dataset, a widely used benchmark for intrusion detection. The datasets (`kdd_train.csv` and `kdd_test.csv`) contain various features extracted from network connections, along with labels indicating whether a connection is normal or an attack. Features include duration, protocol type, service, flag, source and destination bytes, and many more.

## Setup and Dependencies

To run this project, you need Python and the packages listed in `requirements.txt`.

Key dependencies include:
* tkinter (usually included with Python)
* matplotlib
* numpy
* pandas
* scikit-learn
* keras

You can install the dependencies using pip:
```bash
pip install -r requirements.txt