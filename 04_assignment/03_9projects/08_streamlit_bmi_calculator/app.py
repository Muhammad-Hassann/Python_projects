import streamlit as st

st.title("BMI Calculator")

height = st.slider("Select your Height (cm)", 100, 200, 150)
weight = st.slider("Select your Weight (kg)", 30, 150, 70)

if st.button("Calculate BMI"):
    bmi = weight / ((height/100)**2)
    st.write(f"Your BMI is: {bmi:.2f}")
    if bmi < 18.5:
        st.write("You are underweight")
    elif bmi < 25:
        st.write("You are normal")
    elif bmi < 30:
        st.write("You are **overweight**")
    else:
        st.write("You are obese")

st.write("### BMI Category ###")
st.write("- Underweight: BMI less than 18.5")
st.write("- Normal: BMI 18.5 between BMI < 25")
st.write("- Overweight: BMI 25 between 29.5")
st.write("- Obese: BMI greater than 30")