import streamlit as st

# Define the scoring criteria
scoring_criteria = {
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

# Initialize a dictionary to keep track of the points
points = {"P": 0, "B": 0, "C": 0}

# Display the scoring criteria
for topic, choices in scoring_criteria.items():
    st.markdown(f"**{topic}**")
    for choice, scores in choices.items():
        if st.checkbox(choice):
            for score in scores:
                points[score] += 1

# Display the results
if st.button('Submit'):
    st.markdown('---')
    st.markdown(f"**Pneumonia (P):** {points['P']} points")
    st.markdown(f"**Bronchitis (B):** {points['B']} points")
    st.markdown(f"**COVID-19 (C):** {points['C']} points")
