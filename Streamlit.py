import streamlit as st
from LLM_Model import *
from Gmail import *
def main():
    st.set_page_config(page_title = "Email Generator", layout="wide")
    st.title("Generate Custom Email")
    st.write("Please select email type")
    options_type = ["Conference Invite", "Financial Report"]
    email_type = st.selectbox("Select an Email Type:", options_type,key='Select an Email Type')
    question_options = ["Write an email to invite for annual conference at Hilton on September 22,2024", "Write an email to send the last financial year report to director including link"]
    question = st.selectbox("Select an Email Type:", question_options,key='Select an Question Type')

    # Add a button to submit the selection
    if st.button('Submit',key='calling model'):

        response = Llama_output(question, category=email_type)
        st.subheader("Output email is")
        st.write(response)
        st.write("Do you want to send the email?")
        if st.button('Send',key='Email sending'):
            sent = send_mail(response)
            st.write(sent)

if __name__ == '__main__':
    main()
