# Premium Real Estate Evaluator 🏠✨

**[Click here to view the live project!](https://house-price-estimator.streamlit.app)** *(Update this link after deploying via Streamlit Cloud)*

A modern, data-driven real estate valuation tool built with **Streamlit** and **Scikit-Learn**. This application features a premium UI design (including gradient headers, metric cards, and responsive columns) and leverages a Multiple Linear Regression model trained on USA housing data to predict property prices. It also provides instant dual-currency conversion (USD to INR).

## 🌟 Features
- **Premium UI/UX:** A stunning, polished interface with custom CSS, gradient headers, and hover effects.
- **AI-Powered Valuation:** Instantly estimates property values based on demographic and property data.
- **Interactive Visualizations:** Provides Altair-powered visual comparisons between your property and market averages.
- **Dual Currency Metrics:** Displays estimated valuations in both USD ($) and INR (₹).
- **Professional Architecture:** Clean project structure separating data, assets, utilities, and the main app.

## 📁 Project Structure

```
project-root
│
├── app.py                  # Main Streamlit application and UI
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
│
├── data
│   └── USA_Housing.csv     # Training dataset
│
├── assets                  # Images used in the app
│
└── utils
    └── prediction.py       # Model training and prediction logic
```

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

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Streamlit App:**
   ```bash
   streamlit run app.py
   ```

---
> *Built with ❤️ using Streamlit & Scikit-Learn*
