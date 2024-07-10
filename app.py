import streamlit as st

colors = ['red', 'green', 'yellweow','grween', 'yewwllow','grwwween', 'yellow', 'blue']
color_input = st.multiselect('Select options', colors, colors[:])
if st.button('Run'):
    st.markdown('---')
    col1, col2 = st.columns(2)
    input_one = col1.selectbox('Select Color to display', tuple(color_input))
    col2.write(input_one)
