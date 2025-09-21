import streamlit as st
import os
from app.omr.pipeline import evaluate_sheet  # ✅ adjust import if needed

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

st.title("Uploaded OMR Sheet")

uploaded_file = st.file_uploader("Upload OMR Sheet", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    file_path = os.path.join(UPLOAD_DIR, uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.image(file_path, caption="Uploaded OMR Sheet", use_column_width=True)

    if st.button("Evaluate"):
        results = evaluate_sheet(file_path)  # ✅ directly call pipeline
        st.success("Evaluation Results")
        st.json(results)
