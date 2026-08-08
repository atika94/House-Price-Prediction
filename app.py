import streamlit as st

from predict import predict_house_price


# =========================================================
# Page Configuration
# =========================================================

st.set_page_config(
    page_title="House Price Prediction",
    page_icon="🏠",
    layout="wide"
)


# =========================================================
# Header
# =========================================================

st.title("🏠 House Price Prediction")

st.markdown(
    """
    Enter the characteristics of a house below to estimate
    its expected selling price using a trained CatBoost
    regression model.
    """
)

st.divider()


# =========================================================
# Property Quality
# =========================================================

st.subheader("🏡 Property Quality")

col1, col2, col3 = st.columns(3)

with col1:
    overall_qual = st.slider(
        "Overall Quality",
        min_value=1,
        max_value=10,
        value=5,
        help="Overall material and finish quality of the house."
    )

with col2:
    overall_cond = st.slider(
        "Overall Condition",
        min_value=1,
        max_value=9,
        value=5,
        help="Overall present condition of the house."
    )

with col3:
    year_built = st.number_input(
        "Year Built",
        min_value=1800,
        max_value=2026,
        value=2000,
        step=1
    )


# =========================================================
# Size & Living Area
# =========================================================

st.subheader("📐 Size & Living Area")

col1, col2, col3 = st.columns(3)

with col1:
    lot_area = st.number_input(
        "Lot Area (sq ft)",
        min_value=0,
        value=10000,
        step=100
    )

with col2:
    gr_liv_area = st.number_input(
        "Above Ground Living Area (sq ft)",
        min_value=0,
        value=1500,
        step=50
    )

with col3:
    first_floor = st.number_input(
        "First Floor Area (sq ft)",
        min_value=0,
        value=1000,
        step=50
    )

col1, col2, col3 = st.columns(3)

with col1:
    second_floor = st.number_input(
        "Second Floor Area (sq ft)",
        min_value=0,
        value=500,
        step=50
    )

with col2:
    total_bsmt = st.number_input(
        "Total Basement Area (sq ft)",
        min_value=0,
        value=800,
        step=50
    )

with col3:
    bsmt_fin_sf = st.number_input(
        "Finished Basement Area (sq ft)",
        min_value=0,
        value=400,
        step=50
    )


# =========================================================
# Rooms & Bathrooms
# =========================================================

st.subheader("🛁 Rooms & Bathrooms")

col1, col2, col3 = st.columns(3)

with col1:
    bedrooms = st.number_input(
        "Bedrooms",
        min_value=0,
        max_value=10,
        value=3,
        step=1
    )

with col2:
    full_bath = st.number_input(
        "Full Bathrooms",
        min_value=0,
        max_value=10,
        value=2,
        step=1
    )

with col3:
    half_bath = st.number_input(
        "Half Bathrooms",
        min_value=0,
        max_value=10,
        value=1,
        step=1
    )

col1, col2, col3 = st.columns(3)

with col1:
    total_rooms = st.number_input(
        "Total Rooms Above Ground",
        min_value=0,
        max_value=20,
        value=7,
        step=1
    )

with col2:
    fireplaces = st.number_input(
        "Fireplaces",
        min_value=0,
        max_value=10,
        value=1,
        step=1
    )

with col3:
    year_remod = st.number_input(
        "Year Remodeled",
        min_value=1800,
        max_value=2026,
        value=2005,
        step=1
    )


# =========================================================
# Garage
# =========================================================

st.subheader("🚗 Garage")

col1, col2, col3 = st.columns(3)

with col1:
    garage_cars = st.number_input(
        "Garage Capacity",
        min_value=0,
        max_value=10,
        value=2,
        step=1
    )

with col2:
    garage_area = st.number_input(
        "Garage Area (sq ft)",
        min_value=0,
        value=400,
        step=25
    )

with col3:
    garage_type = st.selectbox(
        "Garage Type",
        [
            "None",
            "Attchd",
            "Detchd",
            "BuiltIn",
            "Basment",
            "CarPort",
            "2Types"
        ]
    )


# =========================================================
# Basement Quality
# =========================================================

st.subheader("🏚️ Basement")

col1, col2 = st.columns(2)

with col1:
    bsmt_qual = st.selectbox(
        "Basement Quality",
        [
            "None",
            "Ex",
            "Gd",
            "TA",
            "Fa",
            "Po"
        ]
    )

with col2:
    bsmt_exposure = st.selectbox(
        "Basement Exposure",
        [
            "None",
            "Gd",
            "Av",
            "Mn",
            "No"
        ]
    )


# =========================================================
# Location
# =========================================================

st.subheader("📍 Location")

col1, col2, col3 = st.columns(3)

with col1:
    neighborhood = st.selectbox(
        "Neighborhood",
        [
            "NAmes",
            "CollgCr",
            "OldTown",
            "Edwards",
            "Somerst",
            "Gilbert",
            "NridgHt",
            "Sawyer",
            "NWAmes",
            "SawyerW",
            "Mitchel",
            "BrkSide",
            "Crawfor",
            "IDOTRR",
            "Timber",
            "NoRidge",
            "StoneBr",
            "SWISU",
            "ClearCr",
            "MeadowV",
            "Blmngtn",
            "BrDale",
            "NPkVill",
            "Veenker",
            "Blueste",
            "Greens",
            "GrnHill",
            "Landmrk"
        ]
    )

with col2:
    ms_zoning = st.selectbox(
        "Zoning",
        [
            "RL",
            "RM",
            "FV",
            "RH",
            "C (all)",
            "I (all)"
        ]
    )

with col3:
    street = st.selectbox(
        "Street",
        [
            "Pave",
            "Grvl"
        ]
    )


# =========================================================
# Construction & Features
# =========================================================

st.subheader("🔨 Construction & Features")

col1, col2, col3 = st.columns(3)

with col1:
    exter_qual = st.selectbox(
        "Exterior Quality",
        [
            "Ex",
            "Gd",
            "TA",
            "Fa",
            "Po"
        ]
    )

with col2:
    kitchen_qual = st.selectbox(
        "Kitchen Quality",
        [
            "Ex",
            "Gd",
            "TA",
            "Fa",
            "Po"
        ]
    )

with col3:
    central_air = st.selectbox(
        "Central Air",
        [
            "Y",
            "N"
        ]
    )


# =========================================================
# Prediction
# =========================================================

st.divider()

predict_button = st.button(
    "💰 Predict House Price",
    type="primary",
    use_container_width=True
)


if predict_button:

    # Convert "None" selections into missing values
    garage_type_value = (
        None if garage_type == "None"
        else garage_type
    )

    bsmt_qual_value = (
        None if bsmt_qual == "None"
        else bsmt_qual
    )

    bsmt_exposure_value = (
        None if bsmt_exposure == "None"
        else bsmt_exposure
    )

    # Prepare user input
    user_input = {

        # Property
        "Overall Qual": overall_qual,
        "Overall Cond": overall_cond,
        "Year Built": year_built,
        "Year Remod/Add": year_remod,

        # Size
        "Lot Area": lot_area,
        "Gr Liv Area": gr_liv_area,
        "1st Flr SF": first_floor,
        "2nd Flr SF": second_floor,

        # Basement
        "Total Bsmt SF": total_bsmt,
        "BsmtFin SF 1": bsmt_fin_sf,
        "Bsmt Qual": bsmt_qual_value,
        "Bsmt Exposure": bsmt_exposure_value,

        # Rooms
        "Bedroom AbvGr": bedrooms,
        "Full Bath": full_bath,
        "Half Bath": half_bath,
        "TotRms AbvGrd": total_rooms,
        "Fireplaces": fireplaces,

        # Garage
        "Garage Cars": garage_cars,
        "Garage Area": garage_area,
        "Garage Type": garage_type_value,

        # Location
        "Neighborhood": neighborhood,
        "MS Zoning": ms_zoning,
        "Street": street,

        # Construction
        "Exter Qual": exter_qual,
        "Kitchen Qual": kitchen_qual,
        "Central Air": central_air
    }

    try:

        prediction = predict_house_price(user_input)

        st.success("Prediction generated successfully!")

        st.metric(
            label="Estimated Sale Price",
            value=f"${prediction:,.0f}"
        )

        st.info(
            "This estimate is generated by the trained "
            "machine learning model and should be treated "
            "as an estimate rather than a guaranteed market price."
        )

    except Exception as error:

        st.error(
            "Unable to generate the prediction."
        )

        st.exception(error)