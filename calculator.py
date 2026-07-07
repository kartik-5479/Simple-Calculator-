import streamlit as st

st.set_page_config(
    page_title="Simple Calculator",
    page_icon="🧮",
    layout="centered"
)

st.markdown(
    "<h1 style='text-align: center;'>🧮 Simple Calculator</h1>",
    unsafe_allow_html=True
)

st.divider()

# Inputs
st.subheader("🔢 Enter Numbers")

col1, col2 = st.columns(2)

with col1:
    num1 = st.number_input(
        "First Number",
        value=0.0,
        step=1.0
    )

with col2:
    num2 = st.number_input(
        "Second Number",
        value=0.0,
        step=1.0
    )

st.divider()

operation = st.selectbox(
    "⚙️ Select Operation",
    [
        "Addition (+)",
        "Subtraction (-)",
        "Multiplication (×)",
        "Division (÷)"
    ]
)

st.divider()

# Calculate Button
calculate = st.button(
    "🟢 Calculate",
    use_container_width=True
)

if calculate:

    if operation == "Addition (+)":
        result = num1 + num2

    elif operation == "Subtraction (-)":
        result = num1 - num2

    elif operation == "Multiplication (×)":
        result = num1 * num2

    elif operation == "Division (÷)":

        if num2 == 0:
            st.error("❌ Division by zero is not allowed.")
            st.stop()

        result = num1 / num2

    st.success("✅ Calculation completed successfully!")

    st.divider()

    st.subheader("📊 Result")

    st.metric(
        label="Answer",
        value=round(result, 4)
    )

    st.divider()
    st.subheader("📝 Calculation Summary")

    st.write(f"**First Number:** {num1}")
    st.write(f"**Second Number:** {num2}")
    st.write(f"**Operation:** {operation}")
    st.write(f"**Result:** {round(result, 4)}")
    st.balloons()

st.divider()
st.caption("❤️ Built with Python & Streamlit")