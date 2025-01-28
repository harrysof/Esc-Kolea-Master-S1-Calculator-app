import streamlit as st

# Initialize session state (for consistency)
for subject in [
    "Inferential Statistics", "Financial Accounting", "Management",
    "Marketing", "Macroeconomy", "Computer Science", "Law", "English"
]:
    exam_key = f"{subject}_exam"
    td_key = f"{subject}_TD"
    if exam_key not in st.session_state:
        st.session_state[exam_key] = ""  # Initialize as empty string
    if td_key not in st.session_state:
        st.session_state[td_key] = ""  # Initialize as empty string


def calculate_semester_average():
    subjects_data = {}
    for subject in subjects:
        exam_key = f"{subject}_exam"
        td_key = f"{subject}_TD"

        try:
            exam_str = st.session_state.get(exam_key, "") or "" #Handles None as well
            td_str = st.session_state.get(td_key, "") or "" #Handles None as well
            exam_grade = float(exam_str) if exam_str else 0  # Convert or 0 if empty
            td_grade = float(td_str) if td_str else 0  # Convert or 0 if empty
            subjects_data[subject] = {"exam": exam_grade, "td": td_grade}

        except ValueError:
            st.error(f"Invalid input for {subject}. Please enter numbers only.")
            return  # Stop calculation if there's an invalid input

    # ... (rest of the calculation logic - same as before)
    total = 0
    for subject, grades in subjects_data.items():
        average = (grades["exam"] * 0.67) + (grades["td"] * 0.33)
        weight = 4 if subject in ["Inferential Statistics", "Financial Accounting", "Management", "Marketing"] else 3.5
        total += average * weight

    semester_average = total / 30
    formatted_float = "{:.2f}".format(semester_average)
    better_total = "{:.2f}".format(total)

    st.success(f"Total: {better_total}\n1st Semester Average: {formatted_float}")


# Streamlit app
st.title("Semester Grade Calculator")

subjects = [
    "Inferential Statistics", "Financial Accounting", "Management",
    "Marketing", "Macroeconomy", "Computer Science", "Law", "English"
]

for subject in subjects:
    st.subheader(subject)
    col1, col2 = st.columns(2)
    with col1:
        st.text_input(f"{subject} Exam", key=f"{subject}_exam")  # Use text_input
    with col2:
        st.text_input(f"{subject} TD", key=f"{subject}_TD")  # Use text_input


if st.button("Calculate"):
    calculate_semester_average()
