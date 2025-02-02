# Monitoring-Manufacturing-Process-with-IOT_IE442

Project Overview

This project explores the integration of IoT (Internet of Things) in manufacturing to enhance real-time monitoring, automation, and predictive maintenance. By leveraging sensor technology, cloud computing, and data analytics, manufacturers can optimize efficiency, reduce downtime, and improve product quality.

The implementation of Industrial IoT (IIoT) allows real-time condition monitoring, ensuring data-driven decision-making in industrial environments. The project is designed to simulate an IoT-based monitoring system using real-world Production Plant Data for Condition Monitoring from Kaggle.

Scope and Methodology

This project focuses on designing a simulated IoT-based monitoring system for manufacturing using publicly available sensor datasets. The system architecture consists of:

1. System Design

The IoT-based monitoring system is designed to collect, transmit, and analyze sensor data efficiently. The key components include:

Key Manufacturing Parameters Monitored:

Temperature – Prevents overheating & machine failures

Vibration – Detects mechanical misalignments

Pressure – Identifies leaks or inconsistencies

Motor Speed – Optimizes operational efficiency

Load Values – Helps in predictive maintenance

IoT Infrastructure:

Microcontrollers & Edge Devices: Raspberry Pi, ESP32

Communication Protocols: MQTT (real-time messaging), HTTP (cloud-based logging)

Cloud Platforms: AWS IoT Core, ThingSpeak

2. Data Processing and Analysis

The sensor dataset is preprocessed by:

Handling missing values and timestamp formatting

Detecting anomalies using the Z-score method

Smoothing noise using rolling mean techniques

Forecasting future sensor behavior with ARIMA models

3. Data Visualization

A Streamlit-based dashboard has been developed for real-time data visualization. It provides:

Time-series plots

Anomaly detection insights

Predictive analytics for sensor failures

System Performance Evaluation

The project evaluates the effectiveness of IoT-based predictive maintenance using key performance metrics:

Real-time Monitoring Efficiency: Interactive dashboard for immediate insights

Anomaly Detection Accuracy: Z-score method to detect outliers

Predictive Maintenance Insights: ARIMA forecasts for failure prevention

Operational Improvements: Increased transparency, reduced downtime

How to Run the Project

Prerequisites

Before running the project, install the necessary dependencies:

pip install pandas numpy matplotlib seaborn streamlit statsmodels

Running the Dashboard

To start the real-time visualization dashboard, execute:

streamlit run dashboard.py

Running the Data Analysis

To process and analyze sensor data, run:

python data_analysis.py

Project Files

Codes/ – Python scripts for data processing, visualization, and modeling

parameters/ – Dataset files used for analysis

IE442_IOT_Project_Report.pdf – Complete research documentation

README.md – This file

Future Improvements

Advanced AI Models – Implementing LSTM or Random Forest for better predictive accuracy

Expanded Sensor Coverage – Monitoring humidity, acoustic emissions

Automated Alerts – Real-time notifications for anomaly detection

Contributors

Sude Filiz

Boğaziçi University – Industrial Engineering

References

Production Plant Data for Condition Monitoring (Kaggle)

AWS IoT Core

MQTT Protocol
