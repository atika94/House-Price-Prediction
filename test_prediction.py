from predict import predict_house_price


sample_house = {

    # Important numerical features
    "Overall Qual": 7,
    "Overall Cond": 5,

    "Lot Area": 10000,

    "Year Built": 2005,
    "Year Remod/Add": 2005,

    "Gr Liv Area": 1800,

    "1st Flr SF": 1000,
    "2nd Flr SF": 800,

    "Total Bsmt SF": 800,
    "BsmtFin SF 1": 500,

    "Full Bath": 2,
    "Half Bath": 1,

    "Garage Cars": 2,
    "Garage Area": 500,

    "Fireplaces": 1,

    "Bedroom AbvGr": 3,
    "TotRms AbvGrd": 7,

    # Some categorical information
    "MS Zoning": "RL",
    "Street": "Pave",
    "Lot Shape": "Reg",
    "Land Contour": "Lvl",
    "Neighborhood": "NAmes",
    "Bldg Type": "1Fam",
    "House Style": "2Story",
    "Exter Qual": "Gd",
    "Foundation": "PConc",
    "Bsmt Qual": "Gd",
    "Central Air": "Y",
    "Kitchen Qual": "Gd",
    "Garage Type": "Attchd",
    "Garage Finish": "RFn",
    "Paved Drive": "Y"
}


prediction = predict_house_price(sample_house)

print(f"Predicted Sale Price: ${prediction:,.2f}")