
import streamlit as st

st.set_page_config(page_title="Indian Restaurant Dashboard", page_icon="🍛")

st.title("🍛 Indian Restaurant Dashboard")
st.write("Track daily food preparation, consumption, and leftovers.")

dish = st.selectbox(
    "Select a dish",
    ["Shahi Paneer", "Dal Makhani", "Chana Masala", "Jeera Rice"]
)

prepared = st.number_input("Quantity prepared (kg)", min_value=0.0, step=0.5)
leftover = st.number_input("Quantity leftover (kg)", min_value=0.0, step=0.5)

if st.button("Calculate"):
    if leftover > prepared:
        st.error("Leftovers cannot exceed the prepared quantity.")
    else:
        used = prepared - leftover
        percentage = (leftover / prepared * 100) if prepared > 0 else 0

        st.subheader(f"Daily Report: {dish}")

        col1, col2, col3 = st.columns(3)
        col1.metric("Prepared", f"{prepared:.1f} kg")
        col2.metric("Used", f"{used:.1f} kg")
        col3.metric("Leftover", f"{leftover:.1f} kg")

        st.write(f"**Leftover percentage:** {percentage:.1f}%")
        st.progress(percentage / 100)
