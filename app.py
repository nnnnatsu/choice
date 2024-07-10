import streamlit as st

# Define the criteria and their scores
criteria = [
    ('ไข้', []),
    ('ไข้สูง >38.5', ['P', 'B', 'C']),
    ('ไข้ต่ำ 37.5', ['P', 'C']),
    ('การไอ', []),
    ('ไอแห้ง', ['P', 'C']),
    ('ไอมีเสมหะ', ['P', 'C']),
    ('ความรุนแรงในการไอ', []),
    ('ไอมาก รุนแรง', ['P']),
    ('ไอนานกว่า 2 สัปดาห์', ['B']),
    ('การหายใจ', []),
    ('หายใจลำบาก', ['P', 'B', 'C']),
    ('หายใจตื้น ถี่', ['P']),
    ('อาการเกี่ยวกับลำคอ', []),
    ('เจ็บคอ', ['P', 'B', 'C']),
    ('แสบคอ', ['B']),
    ('อาการเกี่ยวกับการรับรสและจมูก', []),
    ('จมูกไม่รับรส', ['C']),
    ('มีน้ำมูก', ['C']),
    ('อาการทั่วไป', []),
    ('ถ่ายเหลว', ['C']),
    ('คลื่นไส้ อาเจียน', []),
    ('เบื่ออาหาร', ['P']),
    ('อ่อนเพลีย อ่อนแรง หนาวสั่น', ['P', 'B', 'C']),
    ('เหนื่อยง่าย', ['B']),
    ('อาการเกี่ยวกับหน้าอก', []),
    ('เจ็บหน้าอกเวลาไอ/หายใจ', ['P']),
    ('แน่นหน้าอก', ['B', 'C']),
    ('ปัจจัยเสี่ยง', []),
    ('อายุน้อยกว่า 5 ปี หรือมากกว่า 65 ปี', ['P']),
    ('สูบบุหรี่ / อยู่ในสถานที่ที่ได้รับควันบุหรี่', ['P', 'B']),
    ('โรคหืด', ['P', 'B'])
]

# Create a multiselect widget for each criterion
selected_criteria = {}
for criterion, scores in criteria:
    options = [f'{criterion} [{", ".join(scores)}]' if scores else criterion for criterion, scores in [criteria[0]]]
    selected = st.checkbox(options)
    if selected:
        selected_criteria[criterion] = scores

# Display selected criteria and their scores
if st.button('Calculate Scores'):
    st.markdown('---')
    p_score = sum(['P' in scores for scores in selected_criteria.values()])
    b_score = sum(['B' in scores for scores in selected_criteria.values()])
    c_score = sum(['C' in scores for scores in selected_criteria.values()])
    
    st.write(f'Pneumonia (P) Score: {p_score}')
    st.write(f'Bronchitis (B) Score: {b_score}')
    st.write(f'COVID-19 (C) Score: {c_score}')
