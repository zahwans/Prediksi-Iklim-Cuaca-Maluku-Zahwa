import streamlit as st

# --- CUSTOM GRADIENT STYLE ---
st.markdown("""
    <style>
        /* Background gradient lembut */
        .stApp {
            background: linear-gradient(135deg, #f3e8ff 0%, #e9d5ff 40%, #d8b4fe 100%) !important;
            background-attachment: fixed;
        }

        /* Sidebar dengan gradient */
        section[data-testid="stSidebar"] {
            background: linear-gradient(180deg, #e9d5ff, #d8b4fe) !important;
        }

        /* Metric box */
        div[data-testid="stMetricValue"], 
        div[data-testid="stMetricDelta"], 
        .stMetric {
            background: rgba(255, 255, 255, 0.6) !important;
            padding: 12px;
            border-radius: 14px;
            backdrop-filter: blur(6px);
        }

        /* Card umum */
        .stCard {
            background: rgba(255, 255, 255, 0.45) !important;
            border-radius: 16px !important;
            backdrop-filter: blur(6px) !important;
            padding: 12px !important;
        }

        /* Tombol */
        .stButton > button {
            background: linear-gradient(90deg, #c084fc, #a855f7) !important;
            color: white !important;
            border-radius: 12px;
            border: none;
            padding: 0.6rem 1.2rem;
        }

        .stButton > button:hover {
            background: linear-gradient(90deg, #a855f7, #9333ea) !important;
        }

        /* Judul */
        h1, h2, h3, h4, h5, h6 {
            color: #6b21a8 !important;
        }

        /* Input box transparan */
        .stTextInput>div>div>input,
        .stSelectbox>div>div,
        .stDateInput>div>div>input {
            background: rgba(255, 255, 255, 0.7) !important;
            border-radius: 10px !important;
        }
    </style>
""", unsafe_allow_html=True)
