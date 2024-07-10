import streamlit as st

# Define the criteria with associated scores
criteria = {
    'ไข้': [],
    '    ไข้สูง >38.5': ['P', 'B', 'C'],
    '    ไข้ต่ำ 37.5': ['P', 'C'],
    '   การไอ': [],
    '    ไอแห้ง': ['P', 'C'],
    '    ไอมีเสมหะ': ['P', 'C'],
    'ความรุนแรงในการไอ': [],
    '    ไอมาก รุนแรง': ['P'],
    '    ไอนานกว่า 2 สัปดาห์': ['B'],
    'การหายใจ': [],
    '    หายใจลำบาก': ['P', 'B', 'C'],
    '    หายใจตื้น ถี่': ['P'],
    'อาการเกี่ยวกับลำคอ': [],
    '    เจ็บคอ': ['P', 'B', 'C'],
    '    แสบคอ': ['B'],
    'อาการเกี่ยวกับการรับรสและจมูก': [],
    '    จมูกไม่รับรส': ['C'],
    '    มีน้ำมูก': ['C'],
    'อาการทั่วไป': [],
    '    ถ่ายเหลว': ['C'],
    '    คลื่นไส้ อาเจียน': [],
    '    เบื่ออาหาร': ['P'],
    '    อ่อนเพลีย อ่อนแรง หนาวสั่น': ['P', 'B', 'C'],
    '    เหนื่อยง่าย': ['B'],
    'อาการเกี่ยวกับหน้าอก': [],
    '    เจ็บหน้าอกเวลาไอ/หายใจ': ['P'],
    '    แน่นหน้าอก': ['B', 'C'],
    'ปัจจัยเสี่ยง': [],
    '    อายุน้อยกว่า 5 ปี หรือมากกว่า 65 ปี': ['P'],
    '    สูบบุหรี่ / อยู่ในสถานที่ที่ได้รับควันบุหรี่': ['P', 'B'],
    '    โรคหืด': ['P', 'B'],
}

# Display the multiselect options
selected_criteria = st.multiselect(
    'เลือกอาการ',
    options=[key for key in criteria.keys()],
    format_func=lambda x: f"{x} [{''.join(criteria[x])}]" if criteria[x] else f"{x} [ไม่สามารถเลือกได้]",
    disabled=[not criteria[key] for key in criteria.keys()]
)

# Calculate scores
scores = {'P': 0, 'B': 0, 'C': 0}
for symptom in selected_criteria:
    for disease in criteria[symptom]:
        scores[disease] += 1

if st.button('ส่ง'):
    st.markdown('---')
    st.write(f"คะแนนของโรคปอดบวม (P): {scores['P']}")
    st.write(f"คะแนนของโรคหลอดลมอักเสบ (B): {scores['B']}")
    st.write(f"คะแนนของ COVID-19 (C): {scores['C']}")
