import streamlit as st

# CSS styles
css = """
<style>
body {
    font-family: 'Roboto', sans-serif; /* Modern font */
    background-color: #f4f4f4; /* Light background */
}
.subject-container {
    border: 1px solid #ddd; /* Subtle border */
    padding: 20px;
    margin-bottom: 20px;
    border-radius: 8px; /* Rounded corners */
    background-color: #fff; /* White background for subject sections */
    box-shadow: 2px 2px 5px rgba(0,0,0,0.1); /* Subtle shadow */
}
.subject-title {
    font-size: 1.2em;
    font-weight: bold;
    margin-bottom: 10px;
}
.input-container {
    display: flex; /* Arrange inputs horizontally */
    align-items: center; /* Vertically align inputs */
    margin-bottom: 10px;
}
.input-label {
    width: 100px; /* Fixed width for labels */
    margin-right: 10px;
}
.stNumberInput > div > div > input { /* Style number inputs */
    border: 1px solid #ccc;
    border-radius: 4px;
    padding: 5px;
}

/* Color-code subjects */
.subject-Inferential-Statistics { border-color: #4285f4; } /* Blue */
.subject-Financial-Accounting { border-color: #ea4335; } /* Red */
.subject-Management { border-color: #fbbc05; } /* Yellow */
.subject-Marketing { border-color: #34a853; } /* Green */
.subject-Macroeconomy { border-color: #ab47bc; } /* Purple */
.subject-Computer-Science { border-color: #00bcd4; } /* Cyan */
.subject-Law { border-color: #ff9800; } /* Orange */
.subject-English { border-color: #9e9e9e; } /* Gray */

/* Add more subject colors as needed */
</style>
"""

st.markdown(css, unsafe_allow_html=True)


# Initialize session state
for subject in [
    "Inferential Statistics", "Financial Accounting", "Management",
    "Marketing", "Macroeconomy", "Computer Science", "Law", "English"
]:
    exam_key = f"{subject}_exam"
    td_key = f"{subject}_TD"
    if exam_key not in st.session_state:
        st.session_state[exam_key] = 0.0
    if td_key not in st.session_state:
        st.session_state[td_key] = 0.0


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

    st.success(f"Total: {better_total}\n1st Semester Average: {formatted_float}")


# Streamlit app
st.title("Master S1 Calculator ESC KOLEA ~ By Harrysof")

subjects = [
    "Inferential Statistics", "Financial Accounting", "Management",
    "Marketing", "Macroeconomy", "Computer Science", "Law", "English"
]

for subject in subjects:
    st.markdown(f'<div class="subject-container subject-{subject.replace(" ", "-")}">', unsafe_allow_html=True) # Start container with specific class
    st.markdown(f'<div class="subject-title">{subject}</div>', unsafe_allow_html=True) # Subject title
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="input-container"><span class="input-label">Exam:</span>', unsafe_allow_html=True) # Label
        st.number_input(f"{subject} Exam", key=f"{subject}_exam", min_value=0.0)
        st.markdown('</div>', unsafe_allow_html=True) # Close input-container
    with col2:
        st.markdown('<div class="input-container"><span class="input-label">TD:</span>', unsafe_allow_html=True) # Label
        st.number_input(f"{subject} TD", key=f"{subject}_TD", min_value=0.0)
        st.markdown('</div>', unsafe_allow_html=True) # Close input-container
    st.markdown('</div>', unsafe_allow_html=True) # Close subject-container


if st.button("Calculate"):
    calculate_semester_average()
