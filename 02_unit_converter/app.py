import streamlit as st

# Define unit conversion factors
unit_conversions = {
    "Length": {
        "Meter": 1,
        "Kilometer": 0.001,
        "Centimeter": 100,
        "Millimeter": 1000,
        "Mile": 0.000621371,
        "Yard": 1.09361,
        "Foot": 3.28084,
        "Inch": 39.3701
    },
    "Weight": {
        "Kilogram": 1,
        "Gram": 1000,
        "Milligram": 1000000,
        "Pound": 2.20462,
        "Ounce": 35.274
    }
}

# Streamlit UI
st.set_page_config(page_title="Unit Converter App", page_icon=":rocket:")
st.title("Unit Converter App")

# Select category
type_selection = st.selectbox("Select Conversion Type", list(unit_conversions.keys()))

# Select units
from_unit = st.selectbox("From Unit", list(unit_conversions[type_selection].keys()))
to_unit = st.selectbox("To Unit", list(unit_conversions[type_selection].keys()))

# Input value
value = st.number_input("Enter Value", min_value=0.0, format="%f")

if st.button("Convert"):
    if from_unit != to_unit:
        conversion_factor = unit_conversions[type_selection][to_unit] / unit_conversions[type_selection][from_unit]
        result = value * conversion_factor
        formatted_result = int(result) if result.is_integer() else round(result, 4)
        
        st.success(f"{value} {from_unit} = {formatted_result} {to_unit}")

    else:
        st.warning("Please select different units for conversion.")
