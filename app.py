import streamlit as st

# Define the criteria with associated scores
criteria = {
    'ไข้ต่ำ': {'P': 1, 'B': 1, 'C': 1},
    'ไข้สูง': {'P': 3, 'B': 1, 'C': 2},
    'ไอแห้ง': {'P': 1, 'B': 0, 'C': 1},
    'ไอมีเสมหะ': {'P': 2, 'B': 3, 'C': 1},
    'ไอรุนแรง': {'P': 1, 'B': 0, 'C': 0},
    'ไอมาก': {'P': 0, 'B': 2, 'C': 0},
    'ไอนานกว่า 2 สัปดาห์': {'P': 0, 'B': 2, 'C': 0},
    'หายใจลำบาก': {'P': 3, 'B': 2, 'C': 1},
    'หายใจตื้น ถี่': {'P': 1, 'B': 0, 'C': 0},
    'เจ็บคอ': {'P': 0, 'B': 2, 'C': 3},
    'แสบคอ': {'P': 0, 'B': 1, 'C': 0},
    'จมูกไม่รับรส': {'P': 0, 'B': 0, 'C': 3},
    'มีน้ำมูก': {'P': 0, 'B': 0, 'C': 2},
    'ถ่ายเหลว (เกิน2-3วัน)': {'P': 0, 'B': 0, 'C': 3},
    'อ่อนเพลีย อ่อนแรง หนาวสั่น': {'P': 1, 'B': 1, 'C': 1},
    'แสบคอ': {'P': 0, 'B': 0, 'C': 0},
    'เหนื่อยง่าย': {'P': 0, 'B': 1, 'C': 0},
    'เจ็บหน้าอกเวลาไอ/หายใจ': {'P': 3, 'B': 0, 'C': 0},
    'แน่นหน้าอก': {'P': 0, 'B': 2, 'C': 1},
    'อายุน้อยกว่า5ปีหรือมากกว่า 65 ปี': {'P': 1, 'B': 0, 'C': 0},
    'สูบบุหรี่': {'P': 1, 'B': 3, 'C': 0},
    'โรคหืด': {'P': 1, 'B': 1, 'C': 0},
    'ประวัติเสี่ยง คนรอบตัวป่วยด้วยโรคนั้น': {'P': 2, 'B': 1, 'C': 3}
}

# Display the options with custom formatting
selected_criteria = st.multiselect(
    'เลือกอาการ',
    options=list(criteria.keys()),
    format_func=lambda x: x,
)

# Calculate scores
scores = {'P': 0, 'B': 0, 'C': 0}
for symptom in selected_criteria:
    for disease, score in criteria[symptom].items():
        scores[disease] += score

# Display results
if st.button('ส่ง'):
    st.markdown('---')
    st.write(f"คะแนนของโรคปอดบวม (P): {scores['P']}")
    st.write(f"คะแนนของโรคหลอดลมอักเสบ (B): {scores['B']}")
    st.write(f"คะแนนของ COVID-19 (C): {scores['C']}")

    max_score = max(scores.values())
    if max_score < 5:
        st.write("ความเสี่ยงต่ำ")
    else:
        risk_disease = max(scores, key=scores.get)
        risk_name = {'P': 'ปอดบวม', 'B': 'หลอดลมอักเสบ', 'C': 'COVID-19'}
        st.write(f"ความเสี่ยงเป็นโรค: {risk_name[risk_disease]}")
