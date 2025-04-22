import streamlit as st

st.title ("Welcome!")
st.title ("It's a Unit Converter App🔢")
st.markdown ("### Convert the Units Quickly and Easily!")

category = st.selectbox("Choose a Category:", ["Length",  "Weight", "Time"])

def convert_units(category, value , unit):

    if category == "Length":
        if unit == "Kilometers to Meters":
            return value * 1000
        elif unit == "Meters to Kilometers":
            return value / 1000

    elif category == "Weight":
        if unit == "Kilograms to Grams":
            return value * 1000
        elif unit == "Grams To Kilograms":
            return value / 1000
        elif unit == "Grams to Milligrams":
            return value * 1000
        elif unit == "Milligrams to Grams":
            return value / 1000
        elif unit == "Kilograms to Milligrams":
            return value * 1000000
        elif unit == "Milligrams to Kilograms":
            return value / 1000000
        elif unit == "Kilograms to Pounds":
            return value * 2.20462
        elif unit == "Pounds to Kilograms":
            return value / 2.20462

    elif category == "Time":
        if unit == "Hours to Minute":
            return value * 60
        elif unit == "Minutes to Hours":
            return value / 60
        elif unit == "Minutes to Seconds":
            return value * 60
        elif unit == "Seconds to Minutes":
            return value / 60
        elif unit == "Hours to Seconds":
            return value * 3600
        elif unit == "Seconds to Hours":
            return value / 3600
        elif unit == "Hours to Day":
            return value / 24
        elif unit == "Day to Hours":
            return value * 24
        elif unit == "Week to Hours":
            return value * 168
        elif unit == "Hours to Week":
            return value / 168
    return 0


if category == "Length":
    unit = st.selectbox("📏Select Conversion", [
     "Kilometers to Meters",
     "Meters to Kilometers"])
    
elif category == "Weight":
    unit = st.selectbox("⚖️Select Conversion", [
     "Kilograms to Grams",
     "Grams To Kilograms", 
     "Grams to Milligrams",
     "Milligrams to Grams", 
     "Kilograms to Milligrams",
     "Milligrams to Kilograms",
     "Kilograms to Pounds",
     "Pounds to Kilograms"])

elif category == "Time":
    unit = st.selectbox("⏳Select Conversion", [
        "Hours to Minute",
        "Minutes to Hours",
        "Minutes to Seconds",
        "Seconds to Minutes",
        "Hours to Seconds",
        "Seconds to Hours",
        "Hours to Day",
        "Day to Hours",
        "Week to Hours",
        "Hours to Week"
    ])

value = st.number_input("Enter the Value")

if st.button("Convert the Value"):
    result = convert_units(category, value, unit)
    st.success (f"The Result is {result}")