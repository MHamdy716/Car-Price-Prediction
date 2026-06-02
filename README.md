
# 🚗 Car Selling Price Prediction

## Project Overview

This project aims to predict the selling price of a used car using Machine Learning techniques. The model is trained on historical car sales data and deployed as an interactive web application using Streamlit.

The application allows users to enter vehicle specifications such as company, manufacturing year, fuel type, mileage, engine size, transmission type, ownership history, and other attributes to estimate the expected selling price of a car.

---

# 📂 Project Structure

```text
├── cars_selling_project_v2.ipynb   # Data analysis, preprocessing, model training
├── car_predict_app.py              # Streamlit deployment application
├── Model.pkl                       # Trained machine learning model
├── Scaler.pkl                      # Feature scaler
├── Target_scaler.pkl               # Target variable scaler
├── car_project.png                 # Application image
├── requirements.txt
└── README.md
```

---

# ⚠️ Important: Generate Model Files First

Before running the Streamlit application, you must execute **all cells** in:

```text
cars_selling_project_v2.ipynb
```

The notebook performs the complete machine learning workflow, including:

* Data loading
* Data cleaning
* Exploratory Data Analysis (EDA)
* Feature engineering
* Encoding categorical variables
* Feature scaling
* Model training
* Model evaluation
* Saving deployment artifacts

Running all notebook cells will generate the required files:

```text
Model.pkl
Scaler.pkl
Target_scaler.pkl
```

These files are loaded by the Streamlit application during prediction.

If any of these files are missing, the application will fail to run correctly.

---

# 📊 Dataset Features

The model uses the following features to predict the selling price:

| Feature      | Description                          |
| ------------ | ------------------------------------ |
| Company      | Vehicle manufacturer                 |
| Year         | Manufacturing year                   |
| KM Driven    | Total kilometers driven              |
| Mileage      | Fuel efficiency (KM/L)               |
| Engine       | Engine displacement (CC)             |
| Max Power    | Maximum engine power (BHP)           |
| Seats        | Number of seats                      |
| Fuel Type    | Petrol, Diesel, LPG, or CNG          |
| Seller Type  | Individual, Dealer, Trustmark Dealer |
| Transmission | Manual or Automatic                  |
| Owner Type   | Number of previous owners            |

---

# 🔧 Data Preparation Pipeline

## Step 1: Load Dataset

The dataset is imported into Pandas for analysis and preprocessing.

---

## Step 2: Data Cleaning

Data quality checks are performed to:

* Remove duplicate records
* Handle missing values
* Correct inconsistent entries
* Ensure proper data types

---

## Step 3: Exploratory Data Analysis (EDA)

EDA is performed to understand:

* Selling price distribution
* Car brand popularity
* Fuel type distribution
* Correlation between features
* Impact of vehicle age on selling price
* Relationship between mileage and price

---

## Step 4: Feature Engineering

Additional transformations are applied to improve model performance.

Examples include:

* Extracting useful numerical features
* Handling categorical variables
* Preparing data for machine learning algorithms

---

## Step 5: Encoding Categorical Variables

Machine learning models require numerical inputs.

Categorical variables such as:

* Company
* Fuel Type
* Seller Type
* Transmission
* Owner Category

are encoded into numerical values.

---

## Step 6: Feature Scaling

Feature scaling is applied using a scaler to normalize the feature values.

Benefits include:

* Faster model convergence
* Improved model stability
* Better prediction performance

The scaler is saved as:

```text
Scaler.pkl
```

---

## Step 7: Target Scaling

The target variable (selling price) is scaled before model training.

The target scaler is saved as:

```text
Target_scaler.pkl
```

and later used to convert predictions back to the original price range.

---

## Step 8: Model Training

A regression model is trained using the processed dataset.

The model learns relationships between vehicle specifications and selling prices.

After training, the model is saved as:

```text
Model.pkl
```

---

# 📈 Model Evaluation

The trained model is evaluated using regression metrics such as:

* R² Score
* Mean Absolute Error (MAE)
* Mean Squared Error (MSE)
* Root Mean Squared Error (RMSE)

These metrics help assess how accurately the model predicts car prices.

---

# 🌐 Streamlit Application

The Streamlit application provides an interactive interface where users can:

* Select a car manufacturer
* Enter vehicle specifications
* Choose fuel type
* Select transmission type
* Specify ownership history
* Predict the estimated selling price

The application automatically:

1. Encodes categorical variables
2. Scales input features
3. Applies the trained model
4. Converts the prediction back to the original price scale
5. Displays the estimated selling price

---

# ⚙️ Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

# 📦 Install Dependencies

Using requirements.txt:

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install streamlit pandas numpy scikit-learn joblib plotly matplotlib seaborn
```

---

# ▶️ Run the Application

After generating the model files from the notebook:

```bash
streamlit run car_predict_app.py
```

The application will launch in your browser and allow you to generate car price predictions interactively.

---

# Future Improvements

* Hyperparameter tuning
* Advanced feature engineering
* Model comparison and selection
* Cross-validation pipeline
* Real-time market price integration
* Vehicle image analysis
* API deployment using FastAPI

---

# Author

**Mohamed Hamdy**

Machine Learning project for predicting used car selling prices using Python, Scikit-Learn, and Streamlit.
