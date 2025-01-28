import streamlit as st

# Initialize session state (important!)
for subject in [
    "Inferential Statistics", "Financial Accounting", "Management",
    "Marketing", "Macroeconomy", "Computer Science", "Law", "English"
]:
    exam_key = f"{subject}_exam"
    td_key = f"{subject}_TD"
    if exam_key not in st.session_state:
        st.session_state[exam_key] = None  # Set to None to make the field empty
    if td_key not in st.session_state:
        st.session_state[td_key] = None  # Set to None to make the field empty

def calculate_semester_average():
    subjects_data = {}
    for subject in subjects:
        exam_key = f"{subject}_exam"
        td_key = f"{subject}_TD"

        try:
            exam_grade = float(st.session_state.get(exam_key, 0.0) or 0.0)
            td_grade = float(st.session_state.get(td_key, 0.0) or 0.0)
            subjects_data[subject] = {"exam": exam_grade, "td": td_grade}

        except ValueError:
            st.error(f"Invalid input for {subject}. Please enter numbers only.")
            return  
        except TypeError:
            st.error(f"Invalid input for {subject}. Please enter numbers only.")
            return  

    total = 0
    for subject, grades in subjects_data.items():
        average = (grades["exam"] * 0.67) + (grades["td"] * 0.33)
        weight = 4 if subject in ["Inferential Statistics", "Financial Accounting", "Management", "Marketing"] else 3.5
        total += average * weight

    semester_average = total / 30
    formatted_float = "{:.2f}".format(semester_average)
    better_total = "{:.2f}".format(total)

    st.success(f"Semester Average: {formatted_float}")


# Streamlit app
st.title("Master S1 Grade Calculator")

subjects = [
    "Inferential Statistics", "Financial Accounting", "Management",
    "Marketing", "Macroeconomy", "Computer Science", "Law", "English"
]

for subject in subjects:
    st.subheader(subject)  # Display the subject name as a subheader
    col1, col2 = st.columns(2)
    with col1:
        st.number_input(
            "Exam",  # Simplified label
            key=f"{subject}_exam", 
            min_value=0.0, 
            value=None,  # Set to None to make the field empty
            step=0.05,  # Increment/decrement by 0.01
            format="%.2f"  # Display two decimal places
        )
    with col2:
        st.number_input(
            "TD",  # Simplified label
            key=f"{subject}_TD", 
            min_value=0.0, 
            value=None,  # Set to None to make the field empty
            step=0.05,  # Increment/decrement by 0.01
            format="%.2f"  # Display two decimal places
        )

if st.button("Calculate"):
    calculate_semester_average()
