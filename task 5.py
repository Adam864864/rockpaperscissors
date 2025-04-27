import streamlit as st
import random

# Title
st.title("Rock-Paper-Scissors Game")

# Choices
choices = ["Rock", "Paper", "Scissors"]

# User choice
user_choice = st.selectbox("Choose your move:", choices)

# When the user clicks the button
if st.button("Play"):
    # Computer random choice
    computer_choice = random.choice(choices)

    # Display choices
    st.write(f"*You chose:* {user_choice}")
    st.write(f"*Computer chose:* {computer_choice}")

    # Determine winner
    if user_choice == computer_choice:
        st.success("It's a tie!")
    elif (
            (user_choice == "Rock" and computer_choice == "Scissors") or
            (user_choice == "Paper" and computer_choice == "Rock") or
            (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        st.success("You win!")
    else:
        st.error("You lose!")

# Footer
st.caption("Made with Streamlit")