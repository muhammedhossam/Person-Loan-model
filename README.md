# Loan Acceptance Prediction

## Overview
This project aims to predict loan acceptance using a neural network model. The dataset used for training the model is imbalanced, which poses a challenge in terms of overfitting. In this project, we focus on two specific columns, namely income and ccAVG (credit card average), as well as mortgage, which have the most significant impact on loan acceptance.

## Data Preprocessing
To address the issue of imbalanced data, we employed the Synthetic Minority Over-sampling Technique (SMOTE). SMOTE generates synthetic data points using the k-nearest neighbors algorithm, effectively oversampling the minority class. This technique proved useful in creating a balanced dataset for training the model.

## Model Training
The neural network model was chosen as it has shown promising results in similar prediction tasks. The model was fine-tuned to achieve the best performance, with a strong emphasis on the F1 score rather than overall accuracy. The goal was to prioritize model generalization and minimize false positives and false negatives.

## Unexpected Results
Despite our best efforts, the neural network model exhibited unexpected behavior during testing. It consistently predicted all instances as 1 (loan accepted) instead of a mix of 0 and 1. This outcome was contrary to our expectations and requires further investigation to understand the underlying cause.

## Targeted Customer Analysis
Given the unexpected results, we conducted additional analysis to identify factors that could influence loan acceptance. This analysis aims to provide insights into targeting specific customers who are more likely to accept a loan. By understanding the characteristics of these customers, we can refine our targeting strategies and improve loan acceptance rates.

## Conclusion
In conclusion, this project tackled the challenge of imbalanced data in loan acceptance prediction. Despite encountering unexpected results with the neural network model, we have gained valuable insights into the impact of income, ccAVG, and mortgage on loan acceptance. Further investigation is needed to address the unexpected behavior of the model and refine our targeting strategies.

---

# Loan Acceptance Prediction App

The loan acceptance prediction app is a Streamlit application that allows users to input their personal information and predicts whether they will be eligible for a loan or not.

## Usage
1. Clone this repository.
2. Install the required dependencies: Streamlit, requests, streamlit_lottie, PIL, numpy, and joblib.
3. Make sure the trained machine learning model (`Personal_loan_model`) is available in the same directory.
4. Run the Streamlit app using the command `streamlit run app.py`.
5. Fill in the required personal information in the input fields.
6. Click the "Predict" button to get the loan prediction result.
7. The app will display whether the user is eligible for a loan or not.

## Dependencies
- Python 3.7 or higher
- Streamlit
- Requests
- Streamlit_lottie
- PIL
- NumPy
- Joblib

## Contributing
Contributions to this project are welcome. Please submit a pull request with your proposed changes, and they will be reviewed accordingly.

## License
This project is licensed under the [MIT License](LICENSE).
