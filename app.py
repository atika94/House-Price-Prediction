import streamlit as st
from predict import predict_house_price


# ---------------------------------------
# Page Configuration
# ---------------------------------------

st.set_page_config(
    page_title="House Price Prediction",
    page_icon="🏠",
    layout="wide"
)


# ---------------------------------------
# Title
# ---------------------------------------

st.title("🏠 House Price Prediction")

st.write(
    "Enter the property characteristics below to estimate "
    "the selling price of the house."
)


# ---------------------------------------
# Property Information
# ---------------------------------------

st.header("Property Information")

col1, col2, col3 = st.columns(3)

with col1:
    lot_area = st.number_input(
        "Lot Area",
        min_value=0,
        value=10000
    )

    overall_qual = st.slider(
        "Overall Quality",
        min_value=1,
        max_value=10,
        value=5
    )

    overall_cond = st.slider(
        "Overall Condition",
        min_value=1,
        max_value=9,
        value=5
    )

with col2:
    year_built = st.number_input(
        "Year Built",
        min_value=1800,
        max_value=2026,
        value=2000
    )

    year_remod = st.number_input(
        "Year Remodeled",
        min_value=1800,
        max_value=2026,
        value=2000
    )

    gr_liv_area = st.number_input(
        "Above Ground Living Area (sq ft)",
        min_value=0,
        value=1500
    )

with col3:
    first_floor = st.number_input(
        "First Floor Area (sq ft)",
        min_value=0,
        value=1000
    )

    second_floor = st.number_input(
        "Second Floor Area (sq ft)",
        min_value=0,
        value=500
    )

    total_bsmt = st.number_input(
        "Total Basement Area (sq ft)",
        min_value=0,
        value=500
    )


# ---------------------------------------
# Rooms
# ---------------------------------------

st.header("Rooms & Facilities")

col1, col2, col3 = st.columns(3)

with col1:
    bedrooms = st.number_input(
        "Bedrooms Above Ground",
        min_value=0,
        max_value=10,
        value=3
    )

    full_bath = st.number_input(
        "Full Bathrooms",
        min_value=0,
        max_value=10,
        value=2
    )

with col2:
    garage_cars = st.number_input(
        "Garage Capacity",
        min_value=0,
        max_value=10,
        value=2
    )

    garage_area = st.number_input(
        "Garage Area (sq ft)",
        min_value=0,
        value=400
    )

with col3:
    fireplaces = st.number_input(
        "Fireplaces",
        min_value=0,
        max_value=10,
        value=1
    )


# ---------------------------------------
# Prediction
# ---------------------------------------

st.divider()

if st.button("Predict House Price", type="primary"):

    input_data = {
        "Lot Area": lot_area,
        "Overall Qual": overall_qual,
        "Overall Cond": overall_cond,
        "Year Built": year_built,
        "Year Remod/Add": year_remod,
        "Gr Liv Area": gr_liv_area,
        "1st Flr SF": first_floor,
        "2nd Flr SF": second_floor,
        "Total Bsmt SF": total_bsmt,
        "Bedroom AbvGr": bedrooms,
        "Full Bath": full_bath,
        "Garage Cars": garage_cars,
        "Garage Area": garage_area,
        "Fireplaces": fireplaces
    }

    try:

        prediction = predict_house_price(input_data)

        st.success(
            f"Estimated Sale Price: ${prediction:,.2f}"
        )

    except Exception as e:

        st.error(
            "Prediction failed. Please check the input features."
        )

        st.exception(e)