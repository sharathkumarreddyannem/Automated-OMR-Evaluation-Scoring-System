# Automated OMR Evaluation System

## Steps to Run

1. Create a virtual environment and install dependencies:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

2. Start the FastAPI backend:
   ```bash
   uvicorn app.api:app --reload --host 0.0.0.0 --port 8000
   ```

3. Start the Streamlit frontend:
   ```bash
   streamlit run web/streamlit_app.py
   ```

4. Upload an OMR sheet (`.jpg/.png`) via the Streamlit UI.
