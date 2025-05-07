# A simple password strength checker web app using Streamlit and regular expressions(re) in Python.

# Summary of Actions:
# Checks the password length.
# Ensures the password has both uppercase and lowercase letters.
# Verifies if the password includes at least one digit.
# Checks for at least one special character.
# Classifies the password as strong, medium, or weak based on how many criteria are met.
# Displays feedback to guide users in strengthening their passwords.

# Streamlit is a popular Python library for building web applications.

# The re module in Python is a library that helps you work with regular expressions.
# Regular expressions are patterns that can be used to search, match, or manipulate strings in specific ways.

import streamlit as st  # Importing Streamlit for creating the web app
import re  # Importing the 're' module to use regular expressions for validation.

# Setting the page title and icon for the Streamlit app
st.set_page_config(page_title="Password Strength Checker", page_icon="🔐")

st.title("Password Strength Checker")  # Setting the main title of the page
st.markdown("This is the page where you can check the strength of your password.")  # Displaying a description

# Create a password input field that hides the entered text
password = st.text_input("Enter your password", type="password")  

# Initialize an empty list to store feedback and a score variable for strength
feedback = []  
score = 0  # Start with a score of 0, which will be incremented based on password strength criteria

if password:  # Check if the password field is not empty
    # Check if the password is at least 8 characters long
    if len(password) >= 8:
        score += 1  # Increase the score if the length is sufficient
    else:
        feedback.append("Password length should be at least 8 characters.❌")  # Add feedback if the length is too short

    # Check if the password contains both uppercase and lowercase letters
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1  # Increase the score if both uppercase and lowercase letters are found
    else:
        feedback.append("Password should contain at least one uppercase letter.🅰")  # Add feedback if either is missing

    # Check if the password contains at least one digit
    if re.search(r"\d", password):
        score += 1  # Increase the score if there is a digit in the password
    else:
        feedback.append("Password should contain at least one digit.1️⃣")  # Add feedback if a digit is missing

    # Check if the password contains at least one special character from a defined set
    if re.search(r"[!@#$%^&*]", password):  # Corrected regex for special characters
        score += 1  # Increase the score if a special character is found
    else:
        feedback.append("Password should contain at least one special character (!@#$%^&*).❌")  # Add feedback if no special character is present

    # Based on the score, determine the password strength
    if score == 4:
        feedback.append("😉 Your password is strong.")  # All criteria met, password is strong
    elif score == 3:
        feedback.append("😏 Your password is medium.")  # Three criteria met, password is medium strength
    else:
        feedback.append("😒 Your password is weak.")  # Less than three criteria met, password is weak

    # If there are any feedback messages, display them on the page
    if score < 4:
        if feedback:
            st.markdown("## Improvement needed:")  # Display the section title
            for feed in feedback:
                st.write(feed)  # Display each feedback message

