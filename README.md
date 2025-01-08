# Email-Spam-Classifier



# 📋 Project Overview
The Email Spam Classifier is an end-to-end MLOps project designed to identify whether an email is spam or not. The project incorporates:

◾ Text Preprocessing and Feature Extraction for optimal model training.
◾ Model Training using a Naive Bayes algorithm for text classification.
◾ API Deployment for real-time predictions via a simple front-end interface.

This project showcases the implementation of MLOps principles and demonstrates how machine learning models can be operationalized to solve practical challenges.


# 🔍 Project Details
## Project Name: Email Spam Classifier
## Development Time: 10 hours
## Code Size: ~800 lines of code
## Technologies Used:
## Python
## Flask
## Pickle
## Scikit-learn
## HTML/CSS/JavaScript


# 📂 Project Structure

`plaintext`
├── data/                       # Dataset files ( spam.csv)  
├── notebooks/                  # Jupyter Notebooks for experimentation  
│   ├── last.ipynb              # Notebook for model training and evaluation  
├── server/                     # Backend source code  
│   ├── api.py                  # Flask API for predictions  
│   ├── pipeline.pickle         # Serialized model for deployment  
├── client/                     # Front-end assets (HTML/CSS/JS)  
│   ├── index.html              # Main HTML file  
│   ├── app.js                  # JavaScript logic for API interaction  
│   ├── app.css                 # Styling for the web app  
├── README.md                   # Project documentation  
└── requirements.txt            # Python dependencies  




# 🔧 Setup Instructions
## 1-Clone the repository:
`bash` git clone https://github.com/lourimiyassine/email-spam-classifier.git  
`bash` cd email-spam-classifier  

## 2-Install dependencies:
`bash`
pip install -r requirements.txt 
## 3-Run the Flask app:
`bash`
python server/api.py  
## 4-Test the API using Postman or any HTTP client.




# 📊 Results
◾ Model Accuracy: Achieved an accuracy of 95% on test data using the Naive Bayes algorithm.
◾ Deployment: Successfully deployed a REST API for real-time spam detection.

# 🤝 Contributing
Contributions are welcome! Feel free to open issues or submit pull requests to improve this project.

# 📬 Contact
For questions or feedback, reach out to:

Name: Yassine Lourimi
Email: yassinelourimi85@gmail.com
LinkedIn: https://www.linkedin.com/in/yassine-lourimi-74591a2a1/
