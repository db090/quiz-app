import streamlit as st
import random
import time
st.title("Quiz Application")

questions=[
    {
        "question":"What is the capital of Pakistan",
        "options":["Karachi","Lahore","Islamabad","Peshawar"],
        "answer":"Islamabad"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Venus", "Mars", "Jupiter", "Saturn"],
        "answer": "Mars"
    },
    {
        "question": "What is the largest ocean on Earth?",
        "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
        "answer": "Pacific Ocean"
    },
    {
        "question": "Who wrote 'Romeo and Juliet'?",
        "options": ["Charles Dickens", "Jane Austen", "William Shakespeare", "Mark Twain"],
        "answer": "William Shakespeare"
    },
    {
        "question": "What is the chemical symbol for gold?",
        "options": ["Go", "Gd", "Au", "Ag"],
        "answer": "Au"
    },
    {
        "question": "Which country is home to the Great Barrier Reef?",
        "options": ["Brazil", "Australia", "Thailand", "Mexico"],
        "answer": "Australia"
    },
    {
        "question": "What is the tallest mountain in the world?",
        "options": ["K2", "Mount Kilimanjaro", "Mount Everest", "Mount Fuji"],
        "answer": "Mount Everest"
    },
]
if "current_question" not in st.session_state:
    st.session_state.current_question=random.choice(questions)

question=st.session_state.current_question

st.subheader(question["question"])
selected_option=st.radio("Select one option",question["options"],key="answer")
if st.button("submit answe"):
    if selected_option == question["answer"]:
        st.success("Correct!")
    else:
        st.error(f"Incorrect!! The correct answer is {question["answer"]}")
    time.sleep(3)

    st.session_state.current_question = random.choice(questions)
    st.rerun()