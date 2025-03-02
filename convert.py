import streamlit as st
st.markdown(
    """
    <style>
    body{
        background-color: #f0f2f6;
        color: white;
    }
    .stApp{
        background: linear-gradient(135deg, #bcbcbc , #cfe2f3);
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0px 10px 30px rgba(0,0,0, 0.3);
    }
    h1{
        text-align: center;
        font-size: 36px;
        color: white;
    }
    .stButton>button{
        background-color: linear-gradient(45deg, #0b5394, #351c75);
        color:white;
        font-size: 18px;
        padding: 10px 20px;
        border-radius:10px;
        transition:0.3s;
        box-shadow: 0px 5px 15px rgba(0, 201,255,0.4);
    }
    .stButton>button:hover{
        transform: scale(1.05);
        background-color: linear-gradient(45deg,#92fe9d, #00c9ff);
        box-shadow: 0px 8px 20px rgba(0, 201, 255, 0.6);
        color:black;
    }
    .result-box{
        font-size: 24px;
        font-weight: bold;
        text-align: center;
        background: rgba(255, 255, 255, 0.1);
        padding: 20px;
        border-radius: 10px;
        margin-top: 30px;
        box-shadow: 0px 5px 15px rgba(0, 201,255,0.4);
    }
    .footer{
        text-align: center;
        font-size:18px;
        margin-top: 50px;
        color:black;
    }
     </style> 
    """,
    unsafe_allow_html=True
)

#title and descr
st.markdown("<h1>Unit Converter</h1>", unsafe_allow_html=True)
st.write("Convert between various units with ease")

#side bar menu
conversion_type= st.sidebar.selectbox("Select Conversion Type", ["Length", "Weight", "Temperature"])
value = st.number_input("Enter the value",value=0.0, min_value=0.0, step=0.01)
col1, col2 = st.columns(2)

if conversion_type == "Length":
    with col1:
        from_unit= st.selectbox("from", ["meters", "kilometers","Miles" ,"Feet" ,"yards", "inches","centimeters","millimeters"])
    with col2:
        to_unit = st.selectbox("To", ["meters", "kilometers","Miles" ,"Feet" ,"yards", "inches","centimeters","millimeters"])
elif conversion_type == "Weight":
    with col1:
        from_unit = st.selectbox("from", ["Kilograms", "Grams", "Pounds", "Ounces", "Milligrams"])
    with col2:
        to_unit = st.selectbox("To", ["Kilograms", "Grams", "Pounds", "Ounces", "Milligrams"])

elif conversion_type == "Temperature":
    with col1:
        from_unit = st.selectbox("from", ["Celsius", "Fahrenheit", "Kelvin"])
    with col2:
        to_unit = st.selectbox("To", ["Celsius", "Fahrenheit", "Kelvin"])

# converted function
def length_conversion(value, from_unit, to_unit):
    length_units = {
        'meters': 1, 'kilometers': 0.001, 'miles': 0.000621371, 'Feet': 3.28, 'yards': 1.0936, 'inches': 12,
        'centimeters': 100, 'millimeters': 1000
    }
    return (value / length_units[from_unit]) * length_units[to_unit]

def weight_conversion(value, from_unit, to_unit):
    weight_units = {
        'Kilograms': 1, 'Grams':1000, 'Milligrams':1000000, 'Pounds':2.2046, 'Ounces':35.27
    } 
    return(value / weight_units[from_unit]) * weight_units[to_unit]  


def temp_conversion(value,from_unit,to_unit):
    if from_unit == 'Celsius':
        if to_unit == "Fahrenheit":
            return value * 9/5 + 32
        elif to_unit == "Kelvin":
            return value + 273.15
        return value
    elif from_unit == 'Fahrenheit':
        if to_unit == "Celsius":
            return (value - 32) * 5/9
        elif to_unit == "Kelvin":
            return (value - 32) * 5/9 + 273.15
        return value
    elif from_unit == 'Kelvin':
        if to_unit == "Celsius":
            return value - 273.15
        elif to_unit == "Fahrenheit":
            return (value - 273.15) * 9/5 + 32
        return value

# Button for conversion

if st.button("Convert"):
    if conversion_type == 'Length':
        result = length_conversion(value,from_unit ,to_unit)
    elif conversion_type == 'Weight':
        result = weight_conversion(value, from_unit ,to_unit)
    elif conversion_type =="Temperature":
        result = temp_conversion(value,from_unit ,to_unit)

    st.markdown(f"<div class='result-box'> {value} {from_unit} ={result: .4f} {to_unit} </div>", unsafe_allow_html=True)
st.markdown(f"<div class='footer'> Created by Mubashira Tanveer </div> ", unsafe_allow_html=True)     
