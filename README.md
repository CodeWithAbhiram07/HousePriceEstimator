# Premium House Price Predictor 🏠

A data-driven real estate valuation tool built with Streamlit and Scikit-Learn. It leverages a Multiple Linear Regression model trained on USA housing data to predict property prices based on various area specifications, complete with an instant currency conversion to INR.

## 🌟 Features
- **AI-Powered Valuation:** Instantly estimates property values based on demographic and property data.
- **Interactive UI:** A highly polished, premium Streamlit interface.
- **Data Comparison:** Provides Altair-powered visual comparisons between your property and market averages.
- **Dual Currency:** Displays estimated valuations in both USD ($) and INR (₹).

## 🛠️ Tech Stack
- **Python 3.x**
- **Streamlit:** For the interactive web interface.
- **Pandas:** Data manipulation and analysis.
- **Scikit-Learn:** Machine learning (Linear Regression model).
- **Altair:** Declarative statistical visualization.

## 🚀 How to Run Locally

1. **Clone the repository:**
   ```bash
   git clone https://github.com/CodeWithAbhiram07/HousePriceEstimator.git
   cd HousePriceEstimator
   ```

2. **Set up a virtual environment (Optional but Recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install dependencies:**
   *(Ensure you have `streamlit`, `pandas`, `scikit-learn`, and `altair` installed.)*
   ```bash
   pip install streamlit pandas scikit-learn altair
   ```

4. **Run the Streamlit App:**
   ```bash
   streamlit run app.py
   ```

## 📊 About the Model
The application trains a **Multiple Linear Regression** model on startup using the `USA_Housing.csv` dataset. The features it considers are:
- **Income**: Average income of residents in the area.
- **House Age**: The age of the target house.
- **Total Rooms**: The number of rooms in the property.
- **Bedrooms**: The number of bedrooms.
- **Population**: Total population of the surrounding area.

---
> *Built with ❤️ using Streamlit & Scikit-Learn*
