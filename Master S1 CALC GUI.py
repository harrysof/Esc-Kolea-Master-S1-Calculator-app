import streamlit as st

def calculate_semester_average():
    # Get grades from input fields
    Inferential_Statistics_exam = float(st.session_state.Inferential_Statistics_exam)
    Inferential_Statistics_TD = float(st.session_state.Inferential_Statistics_TD)
    Financial_Accounting_exam = float(st.session_state.Financial_Accounting_exam)
    Financial_Accounting_TD = float(st.session_state.Financial_Accounting_TD)
    Management_exam = float(st.session_state.Management_exam)
    Management_TD = float(st.session_state.Management_TD)
    Marketing_exam = float(st.session_state.Marketing_exam)
    Marketing_TD = float(st.session_state.Marketing_TD)
    Macroeconomy_exam = float(st.session_state.Macroeconomy_exam)
    Macroeconomy_TD = float(st.session_state.Macroeconomy_TD)
    Computer_Science_exam = float(st.session_state.Computer_Science_exam)
    Computer_Science_TD = float(st.session_state.Computer_Science_TD)
    Law_exam = float(st.session_state.Law_exam)
    Law_TD = float(st.session_state.Law_TD)
    English_exam = float(st.session_state.English_exam)
    English_TD = float(st.session_state.English_TD)
    
    # Calculate averages
    Inferential_Statistics_average = (Inferential_Statistics_exam * 0.67) + (Inferential_Statistics_TD * 0.33)
    Financial_Accounting_average = (Financial_Accounting_exam * 0.67) + (Financial_Accounting_TD * 0.33)
    Management_average = (Management_exam * 0.67) + (Management_TD * 0.33)
    Marketing_average = (Marketing_exam * 0.67) + (Marketing_TD * 0.33)
    Macroeconomy_average = (Macroeconomy_exam * 0.67) + (Macroeconomy_TD * 0.33)
    Computer_Science_average = (Computer_Science_exam * 0.67) + (Computer_Science_TD * 0.33)
    Law_average = (Law_exam * 0.67) + (Law_TD * 0.33)
    English_average = (English_exam * 0.67) + (English_TD * 0.33)
    
    # Calculate total
    Total = (Inferential_Statistics_average * 4) + (Financial_Accounting_average * 4) + (Management_average * 4) + (Marketing_average * 4) + (Macroeconomy_average * 3.5) + (Computer_Science_average * 3.5) + (Law_average * 3.5) + (English_average * 3.5)
    Semester_average = Total / 30
    formatted_float = "{:.2f}".format(Semester_average)
    BetterTotal = "{:.2f}".format(Total)
    
    # Display result
    st.success(f"Total: {BetterTotal}\n1st Semester Average: {formatted_float}")

# Streamlit app
st.title("Semester Grade Calculator")

# Add input fields for each subject
subjects = [
    "Inferential Statistics", "Financial Accounting", "Management",
    "Marketing", "Macroeconomy", "Computer Science", "Law", "English"
]

for subject in subjects:
    st.subheader(subject)
    col1, col2 = st.columns(2)
    with col1:
        st.text_input(f"{subject} Exam", key=f"{subject}_exam")
    with col2:
        st.text_input(f"{subject} TD", key=f"{subject}_TD")

# Add button to trigger calculation
if st.button("Calculate"):
    calculate_semester_average()
