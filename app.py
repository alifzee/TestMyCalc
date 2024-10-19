import streamlit as st

# Set the title and layout
st.set_page_config(page_title="Pakistani Styled Calculator", page_icon="🇵🇰", layout="wide")
st.title("📱 پاکستانی کیلکولیٹر")

# Set a custom CSS style for the app
st.markdown("""
<style>
    .stButton > button {
        background-color: #009688;
        color: white;
        font-size: 18px;
        border: None;
        border-radius: 10px;
        padding: 10px 20px;
        transition: background-color 0.3s;
    }
    .stButton > button:hover {
        background-color: #00796b;
    }
    .stTextInput > div > input {
        border: 2px solid #009688;
        border-radius: 5px;
        padding: 10px;
    }
</style>
""", unsafe_allow_html=True)

# Input fields for numbers
num1 = st.number_input("پہلا نمبر", format="%.2f")
num2 = st.number_input("دوسرا نمبر", format="%.2f")

# Operations
operation = st.selectbox("عمل منتخب کریں", ["جمع", "تفریق", "ضرب", "تقسیم"])

# Perform calculation
if st.button("حساب کریں"):
    if operation == "جمع":
        result = num1 + num2
    elif operation == "تفریق":
        result = num1 - num2
    elif operation == "ضرب":
        result = num1 * num2
    elif operation == "تقسیم":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "تقسیم صفر سے نہیں ہو سکتی"
    
    # Display result
    st.success(f"نتیجہ: {result}")

# Add footer
st.markdown("<footer style='text-align: center;'>یہ ایک سادہ کیلکولیٹر ایپ ہے۔</footer>", unsafe_allow_html=True)
