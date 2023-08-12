import streamlit as st

def find_largest_number():
    st.title('Find the Largest Among Three Numbers')
    num1 = st.number_input('Enter the first number')
    num2 = st.number_input('Enter the second number')
    num3 = st.number_input('Enter the third number')
    if st.button('Find Largest'):
        largest = max(num1, num2, num3)
        st.success(f'The largest number among {num1}, {num2}, and {num3} is {largest}')

find_largest_number()
