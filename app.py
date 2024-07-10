import streamlit as st

# Define the symptoms and their corresponding scores
symptoms = {
    "ไข้": {
        "ไข้สูง": ["P", "B", "C"],
        "ไข้ต่ำ": ["P", "C"]
    },
    "การไอ": {
        "ไอแห้ง": ["P", "C"],
        "ไอมีเสมหะ": ["P", "C"]
    },
    "ความรุนแรงในการไอ": {
        "ไอมาก รุนแรง": ["P"],
        "ไอนานกว่า 2 สัปดาห์": ["B"]
    },
    "การหายใจ": {
        "หายใจลำบาก": ["P", "B", "C"],
        "หายใจตื้น ถี่": ["P"]
    },
    "อาการเกี่ยวกับลำคอ": {
        "เจ็บคอ": ["P", "B", "C"],
        "แสบคอ": ["B"]
    },
    "อาการเกี่ยวกับการรับรสและจมูก": {
        "จมูกไม่รับรส": ["C"],
        "มีน้ำมูก": ["C"]
    },
    "อาการทั่วไป": {
        "ถ่ายเหลว": ["C"],
        "คลื่นไส้ อาเจียน": [],
        "เบื่ออาหาร": ["P"],
        "อ่อนเพลีย อ่อนแรง หนาวสั่น": ["P", "B", "C"],
        "เหนื่อยง่าย": ["B"]
    },
    "อาการเกี่ยวกับหน้าอก": {
        "เจ็บหน้าอกเวลาไอ/หายใจ": ["P"],
        "แน่นหน้าอก": ["B", "C"]
    },
    "ปัจจัยเสี่ยง": {
        "อายุน้อยกว่า 5 ปี หรือมากกว่า 65 ปี": ["P"],
        "สูบบุหรี่ / อยู่ในสถานที่ที่ได้รับควันบุหรี่": ["P", "B"],
        "โรคหืด": ["P", "B"]
    }
}

# Initialize the scores
scores = {"P": 0, "B": 0, "C": 0}

# User input for each category
st.header('Disease Classification')
selected_symptoms = {}

for category, options in symptoms.items():
    st.markdown(f"**{category}**")
    selected_symptoms[category] = st.multiselect("", options.keys(), key=category)

if st.button('Send'):
    # Calculate the scores
    for category, selected_options in selected_symptoms.items():
        for option in selected_options:
            for disease in symptoms[category][option]:
                scores[disease] += 1

    # Display the results
    st.markdown('---')
    st.write(f"Pneumonia (P): {scores['P']} points")
    st.write(f"Bronchitis (B): {scores['B']} points")
    st.write(f"COVID-19 (C): {scores['C']} points")
