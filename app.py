import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
import altair as alt

# 1. Page Configuration (Must be the first Streamlit command)
st.set_page_config(
    page_title="Premium House Price Predictor",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom CSS for a premium look
st.markdown("""
<style>
    /* Header styling */
    .main-header {
        color: #1a202c;
        text-align: center;
        padding: 3rem 1rem;
        margin-bottom: 2rem;
        background: linear-gradient(135deg, #f6d365 0%, #fda085 100%);
        border-radius: 20px;
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
        border: 1px solid rgba(255,255,255,0.4);
    }
    
    /* Card styling for form */
    div[data-testid="stForm"] {
        border-radius: 20px;
        padding: 2rem;
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.05);
        border: 1px solid #e2e8f0;
    }

    /* Metric styling */
    div[data-testid="stMetricValue"] {
        font-size: 2.2rem;
        font-weight: 800;
        color: #2b6cb0;
        letter-spacing: -0.5px;
    }
    
    div[data-testid="stMetricLabel"] {
        font-size: 1rem;
        color: #4a5568;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    /* Button styling */
    div[data-testid="stFormSubmitButton"] > button {
        background: linear-gradient(135deg, #4299e1 0%, #3182ce 100%) !important;
        color: white !important;
        font-weight: bold !important;
        font-size: 1.1rem !important;
        border: none !important;
        border-radius: 12px !important;
        padding: 0.8rem 2rem !important;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
        width: 100% !important;
        margin-top: 1.5rem !important;
        box-shadow: 0 4px 6px -1px rgba(66, 153, 225, 0.4), 0 2px 4px -1px rgba(66, 153, 225, 0.2) !important;
    }
    
    div[data-testid="stFormSubmitButton"] > button:hover {
        transform: translateY(-3px) !important;
        box-shadow: 0 10px 15px -3px rgba(66, 153, 225, 0.5), 0 4px 6px -2px rgba(66, 153, 225, 0.3) !important;
        background: linear-gradient(135deg, #3182ce 0%, #2b6cb0 100%) !important;
    }
    
    /* Custom divider line */
    hr {
        border: 0;
        height: 1px;
        background-image: linear-gradient(to right, rgba(0, 0, 0, 0), rgba(0, 0, 0, 0.1), rgba(0, 0, 0, 0));
        margin: 2rem 0;
    }
</style>
""", unsafe_allow_html=True)

# 2. Data Loading and Model Training (Cached for performance)
@st.cache_resource
def load_and_train_model():
    try:
        df = pd.read_csv('USA_Housing.csv')
        X = df[['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms',
               'Avg. Area Number of Bedrooms', 'Area Population']]
        y = df['Price']
        model = LinearRegression()
        model.fit(X, y)
        return model, df
    except FileNotFoundError:
        st.error("Error: 'USA_Housing.csv' not found. Please ensure the file is in the correct directory.")
        st.stop()

model, df = load_and_train_model()
EXCHANGE_RATE = 83.0 # Current estimate

# 3. Web Interface

# Title & Description
st.markdown("""
<div class="main-header">
    <h1 style='margin:0; font-size: 3.5rem; font-weight: 800; letter-spacing: -1px; text-shadow: 1px 1px 2px rgba(0,0,0,0.1);'>Premium Real Estate Evaluator</h1>
    <p style='font-size: 1.3rem; margin-top: 1rem; color: #2d3748; font-weight: 500;'>AI-Powered Property Valuation with Instant Currency Conversion</p>
</div>
""", unsafe_allow_html=True)

# Main layout using columns
col1, space, col2 = st.columns([1, 0.1, 1.2])  # Give Valuation Results slightly more room

with col1:
    st.markdown("<h3 style='color: #2d3748; margin-bottom: 1.5rem;'>📊 Property Specifications</h3>", unsafe_allow_html=True)
    
    # Using a form to group inputs visually and logically
    with st.form("prediction_form"):
        # Put inputs in rows using columns for a tighter layout
        row1_col1, row1_col2 = st.columns(2)
        with row1_col1:
            income = st.number_input("Avg. Area Income ($)", value=70000.0, step=1000.0, 
                                     help="The average household income of residents in the neighborhood. (e.g. 50,000 to 100,000)")
        with row1_col2:
            population = st.number_input("Area Population", value=30000.0, step=1000.0,
                                         help="Total number of people living in the surrounding city/area. (e.g. 20,000 to 50,000)")
            
        st.markdown("---") # Divider
        
        row2_col1, row2_col2, row2_col3 = st.columns(3)
        with row2_col1:
            age = st.number_input("House Age (Years)", value=5.0, step=0.5,
                                  help="How old the house is in years.")
        with row2_col2:
            rooms = st.number_input("Total Rooms", value=6.0, step=1.0,
                                    help="Total number of rooms in the property.")
        with row2_col3:
            bedrooms = st.number_input("Bedrooms", value=3.0, step=1.0,
                                       help="Number of bedrooms specifically.")
            
        # The submit button for the form
        submitted = st.form_submit_button("Calculate Estimated Value ✨")

with col2:
    st.markdown("<h3 style='margin-bottom: 1.5rem;'>💰 Valuation Results</h3>", unsafe_allow_html=True)
    
    # Placeholder container for results
    results_container = st.container()
    
    with results_container:
        if submitted:
            # Predict
            pred_usd = model.predict([[income, age, rooms, bedrooms, population]])[0]
            pred_inr = pred_usd * EXCHANGE_RATE
            
            # Display success message
            st.success("Analysis Complete!", icon="✅")
            
            # Display results vertically to guarantee enough horizontal space for huge numbers
            with st.container(border=True):
                st.metric(label="Estimated Value (USD)", value=f"${pred_usd:,.0f}")
                st.markdown("<div style='margin-top: 1rem;'></div>", unsafe_allow_html=True) # Spacer
                st.metric(label="Estimated Value (INR)", value=f"₹{pred_inr:,.0f}")
                
                st.caption(f"ℹ️ Current Exchange Rate: 1 USD = ₹{EXCHANGE_RATE}")
            
            st.markdown("---")
            # Altair Chart for a more premium visual comparison
            st.markdown("#### Comparison to Market Average")
            
            avg_income = df['Avg. Area Income'].mean()
            avg_age = df['Avg. Area House Age'].mean()
            
            # Chart 1: Income Comparison
            income_data = pd.DataFrame({
                "Metric": ["Average Area Income ($)", "Average Area Income ($)"],
                "Source": ["Your Property", "Market Average"],
                "Value": [income, avg_income]
            })
            
            chart_income = alt.Chart(income_data).mark_bar(cornerRadiusEnd=4).encode(
                x=alt.X('Value:Q', title="Income in USD"),
                y=alt.Y('Source:N', title=None, axis=alt.Axis(labelPadding=10), sort=None),
                color=alt.Color('Source:N', legend=None, scale=alt.Scale(domain=['Your Property', 'Market Average'], range=['#4F46E5', '#9CA3AF'])),
                tooltip=[alt.Tooltip('Source:N', title='Source'), alt.Tooltip('Value:Q', title='Income ($)', format=',.0f')]
            ).properties(height=120)
            
            st.altair_chart(chart_income, use_container_width=True, theme="streamlit")
            
            # Chart 2: Age Comparison
            age_data = pd.DataFrame({
                "Metric": ["House Age (Years)", "House Age (Years)"],
                "Source": ["Your Property", "Market Average"],
                "Value": [age, avg_age]
            })
            
            chart_age = alt.Chart(age_data).mark_bar(cornerRadiusEnd=4).encode(
                x=alt.X('Value:Q', title="Age in Years"),
                y=alt.Y('Source:N', title=None, axis=alt.Axis(labelPadding=10), sort=None),
                color=alt.Color('Source:N', legend=None, scale=alt.Scale(domain=['Your Property', 'Market Average'], range=['#4F46E5', '#9CA3AF'])),
                tooltip=[alt.Tooltip('Source:N', title='Source'), alt.Tooltip('Value:Q', title='Age (Years)', format='.1f')]
            ).properties(height=120)
            
            st.altair_chart(chart_age, use_container_width=True, theme="streamlit")

        else:
            # Empty state before prediction
            st.info("👈 Please enter the property specifications on the left, then click **Calculate Estimated Value** to see the AI prediction.")
            st.image("https://images.unsplash.com/photo-1560518883-ce09059eeffa?ixlib=rb-4.0.3&auto=format&fit=crop&w=1600&q=100", 
                     caption="Data-Driven Real Estate Insights", use_container_width=True)

# Sidebar for additional info
with st.sidebar:
    st.image("https://images.unsplash.com/photo-1551288049-bebda4e38f71?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=100", use_container_width=True)
    st.title("About the Model")
    st.info("""
    This application uses a Multiple Linear Regression model trained on USA housing data to predict property prices.
    
    **Input Features:**
    - **Income**: The average income of residents in the area.
    - **House Age**: The age of the target house.
    - **Rooms / Bedrooms**: Total rooms and bedrooms.
    - **Population**: Total population of the surrounding area.
    """)
    st.markdown("---")
    st.markdown("<div style='text-align: center; color: #718096; font-size: 0.9rem;'>Built with ❤️ using Streamlit & Scikit-Learn</div>", unsafe_allow_html=True)