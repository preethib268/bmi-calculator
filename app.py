import streamlit as st
import matplotlib.pyplot as plt  # New: For plotting BMI categories

# Styling
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(to bottom right, #ffdee9, #80deea);
    }
    .bmi-box {
        padding: 20px;
        border-radius: 12px;
        background-color: #ffffffcc;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        margin-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)

st.title(" BMI Calculator (Height in Feet)")

# Reset mechanism
if 'reset' not in st.session_state:
    st.session_state.reset = False

# Input values
weight = st.number_input("⚖️ Enter your weight (kg):", min_value=1.0, key="weight", value=1.0 if st.session_state.reset else st.session_state.get("weight", 1.0))
height = st.number_input("📏 Enter your height (feet):", min_value=1.0, key="height", value=1.0 if st.session_state.reset else st.session_state.get("height", 1.0))

# Reset the flag
st.session_state.reset = False

# Action buttons
col1, col2 = st.columns(2)

with col1:
    if st.button("📊 Calculate BMI"):
        height_m = height * 0.3048
        bmi = weight / (height_m ** 2)
        bmi = round(bmi, 2)

        # Determine status
        if bmi < 18.5:
            status = "Underweight 😟"
            color = "orange"
            progress = 0.2
        elif bmi < 25:
            status = "Normal Weight 😄"
            color = "green"
            progress = 0.5
            st.balloons()
        elif bmi < 30:
            status = "Overweight 😬"
            color = "yellow"
            progress = 0.75
        else:
            status = "Obese 😱"
            color = "red"
            progress = 1.0

        # Display results
        st.markdown(f"""<div class='bmi-box'>
            <h3>Your BMI is: <span style='color:{color}'>{bmi}</span></h3>
            <p style='font-size:20px;'>Status: <strong>{status}</strong></p>
        </div>""", unsafe_allow_html=True)

        st.progress(progress, text=f"Your BMI Level → {status}")

        # Save BMI to session history
        if "bmi_history" not in st.session_state:
            st.session_state.bmi_history = []
        st.session_state.bmi_history.append(bmi)

        # Show BMI category chart
        st.subheader("📊 BMI Category Reference")
        fig, ax = plt.subplots()
        categories = ["Underweight", "Normal", "Overweight", "Obese"]
        limits = [18.4, 24.9, 29.9, 35]
        colors = ['#f4cccc', '#c9f4c9', '#ffe599', '#f4cccc']
        ax.bar(categories, limits, color=colors)
        ax.set_ylabel("BMI Upper Limit")
        ax.set_title("BMI Category Chart")
        st.pyplot(fig)

with col2:
    if st.button(" Clear All"):
        st.session_state.reset = True
        st.rerun()

# Show previous session BMI values
if "bmi_history" in st.session_state and st.session_state.bmi_history:
    st.subheader("📋 BMI History This Session")
    st.write(st.session_state.bmi_history)
