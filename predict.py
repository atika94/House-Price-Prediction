import joblib
import pandas as pd
from pathlib import Path


# -------------------------------------------------
# Load Saved Model
# -------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent

MODEL_PATH = PROJECT_ROOT / "models" / "house_price_model.pkl"

model = joblib.load(MODEL_PATH)


# -------------------------------------------------
# Create Complete Input Data
# -------------------------------------------------

def prepare_input(user_input):
    """
    Convert user-provided values into the complete
    feature structure expected by the trained pipeline.
    """

    # Create an empty row with all model features
    features = model.named_steps[
        "preprocessor"
    ].feature_names_in_

    input_data = pd.DataFrame(
        {feature: [None] for feature in features}
    )

    # Insert values supplied by the user
    for feature, value in user_input.items():

        if feature in input_data.columns:
            input_data.loc[0, feature] = value

    return input_data


# -------------------------------------------------
# Feature Engineering
# -------------------------------------------------

def add_engineered_features(data):
    """
    Create the engineered features used during training.
    """

    # House age
    data["HouseAge"] = (
        data["Yr Sold"] - data["Year Built"]
    )

    # Age since remodeling
    data["RemodAge"] = (
        data["Yr Sold"] - data["Year Remod/Add"]
    )

    # Total bathrooms
    data["TotalBathrooms"] = (
        data["Full Bath"]
        + 0.5 * data["Half Bath"]
        + data["Bsmt Full Bath"]
        + 0.5 * data["Bsmt Half Bath"]
    )

    # Total porch area
    data["TotalPorchSF"] = (
        data["Open Porch SF"]
        + data["3Ssn Porch"]
        + data["Enclosed Porch"]
        + data["Screen Porch"]
        + data["Wood Deck SF"]
    )

    # Total outdoor area
    data["TotalOutdoorSF"] = (
        data["Wood Deck SF"]
        + data["Open Porch SF"]
        + data["Enclosed Porch"]
        + data["3Ssn Porch"]
        + data["Screen Porch"]
        + data["Pool Area"]
    )

    # Total living area
    data["TotalLivingSF"] = (
        data["Gr Liv Area"]
        + data["Total Bsmt SF"]
        + data["1st Flr SF"]
        + data["2nd Flr SF"]
    )

    return data


# -------------------------------------------------
# Prediction Function
# -------------------------------------------------

def predict_house_price(user_input):
    """
    Predict the sale price of a house.

    Parameters
    ----------
    user_input : dict
        User-provided house characteristics.

    Returns
    -------
    float
        Predicted house price.
    """

    input_data = prepare_input(user_input)

    input_data = add_engineered_features(input_data)

    prediction = model.predict(input_data)

    return float(prediction[0])