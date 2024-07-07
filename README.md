# Stroke Possibility Checker

A simple web app to check the possibility of stroke based on the patient's details. This application predicts the possibility of a stroke based on patient details using a machine learning model. It is built with Streamlit and hosted on Streamlit Community Cloud. Developed by Divyansh Bhandari, and Arnav Agarwal.

![Main Page](https://github.com/bh-divyansh/Stroke-Possibility-Checker/blob/main/assets/mainpage.png?raw=true)

## Features

* Predicts stroke risk based on multiple patient inputs.
* User-friendly interface with dropdowns and input fields.
* Quick and easy stroke risk assessment.
* We do not store any patient data, and the Terms of Use and Privacy Policy of Streamlit community cloud applies.

## How to run

Head over to [this link](https://strokedetection.streamlit.app) to run the app.

### Troubleshoot sleeping state issue

If the website says that the app is in a 'sleeping' state as shown below, then click the "Yes, get this app back up!" button, and wait for a minute. After that the web app will be ready to use and just refresh the page to use.

![Main Page](https://github.com/bh-divyansh/Stroke-Possibility-Checker/blob/main/assets/sleepingstate.png?raw=true)

This usually happens when streamlit cloud makes the app temporarily inactive due to less frequency of app use. Unfortunately we do not have much control over this. ☹️ 

## Usage

* Open the application.
* Enter the patient's details such as gender, age, average glucose level, BMI, work type, etc.
* Click on "Check possibility of Stroke" to get the result.

## Input fields

* Gender: Male/Female
* Age: Patient's age in years
* Hypertension: Yes/No
* Heart Disease: Yes/No
* Ever Married: Yes/No
* Average Glucose Level: mg/dL
* BMI: Body Mass Index
* Work Type: Private, Self-employed, Govt Job, etc.
* Smoking Status: Formerly smoked, Never smoked, Unknown, etc.
* Residence Type: Urban/Rural

## Machine Learning model information

The model is trained on a dataset of stroke-related data is based on a modified logistic regression model. The model training code may be available in upcoming future in the same repository. Currently, the pickle file is provided.

## License
This project is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License. You are free to:

* Share — copy and redistribute the material in any medium or format
* Adapt — remix, transform, and build upon the material

Under the following terms:

* Attribution — You must give appropriate credit, provide a link to the license, and indicate if changes were made. You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or your use.
* NonCommercial — You may not use the material for commercial purposes.
* ShareAlike — If you remix, transform, or build upon the material, you must distribute your contributions under the same license as the original.

For more details, refer to the license.

## Contributing

Feel free to submit issues or pull requests if you have suggestions or improvements.

## Author Links

* Divyansh Bhandari - [Github](https://github.com/bh-divyansh) | [Linkedin](https://linkedin.com/in/bhdivyansh)
* Arnav Agarwal - [Github](https://github.com/ArnavAgarwal-Mr-AR) | [Linkedin](https://www.linkedin.com/in/arnav-agarwal-571a59243/)

## Acknowledgments

* The ML model used in this project is trained on the Stroke Prediction Data provided by [@Fedesoriano on kaggle](https://www.kaggle.com/fedesoriano).
* We thank Streamlit Community Cloud for hosting the application.

## Disclaimer

The predictions made by this web app are based solely on the data provided by the user and should not be considered medical advice. This tool is for informational purposes only and is not intended to replace professional medical consultation, diagnosis, or treatment. Always seek the advice of your physician or other qualified health providers with any questions you may have regarding a medical condition. We (the authors/creators of this application) do not take any responsibility for the accuracy or reliability of the predictions made by this application.
