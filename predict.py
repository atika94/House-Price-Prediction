import joblib
import pandas as pd
from pathlib import Path

# -------------------------------------------------
# Load Saved Model
# -------------------------------------------------

PROJECT_ROOT = Path(__file__).parent

MODEL_PATH = PROJECT_ROOT / "models" / "house_price_model.pkl"

model = joblib.load(MODEL_PATH)


# -------------------------------------------------
# Prediction Function
# -------------------------------------------------

def predict_house_price(input_data):
    """
    Predict the selling price of a house.

    Parameters
    ----------
    input_data : dict
        Dictionary containing the house features.

    Returns
    -------
    float
        Predicted house price.
    """

    input_df = pd.DataFrame([input_data])

    prediction = model.predict(input_df)

    return float(prediction[0])

    if __name__ == "__main__":

    sample_house = {
        "MS SubClass": 20,
        "MS Zoning": "RL",
        "Lot Frontage": 80,
        "Lot Area": 9600,
        "Street": "Pave",
        "Alley": None,
        "Lot Shape": "Reg",
        "Land Contour": "Lvl",

        # ...
        # Continue until ALL features
        # except SalePrice are included.
        # ...
    }

    predicted_price = predict_house_price(sample_house)

    print(f"Predicted Price: ${predicted_price:,.2f}")