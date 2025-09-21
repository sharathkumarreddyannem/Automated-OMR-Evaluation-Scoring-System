import streamlit as st
import requests

BACKEND_URL = "http://127.0.0.1:8000/upload/"

st.title("📑 Automated OMR Evaluation System")

uploaded_file = st.file_uploader("Upload OMR Sheet", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    st.image(uploaded_file, caption="Uploaded OMR Sheet", use_column_width=True)

    if st.button("Evaluate"):
        files = {"file": uploaded_file.getvalue()}
        response = requests.post(BACKEND_URL, files={"file": (uploaded_file.name, uploaded_file.getvalue())})

        if response.status_code == 200:
            result = response.json()
            st.success("✅ Evaluation Completed")
            st.json(result)
        else:
            st.error(f"❌ Error: {response.status_code}")
