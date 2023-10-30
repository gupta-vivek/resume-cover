import PyPDF2
import streamlit as st

from utils import write_cover_letter, resume_changes


def streamlit_app():
    """
    Streamlit App
    :return:
    """
    st.title('Resume + Cover Letter')
    st.subheader('Suggests changes for resume and writes cover letter')

    # Resume
    resume_file = st.file_uploader("Upload Resume", type='pdf')
    resume = None
    if resume_file is not None:
        resume = PyPDF2.PdfReader(resume_file)
        resume = resume.pages[0].extractText()

    # Job Description
    job_description = st.text_area('Job Description')

    # Additional information about the company
    company_add_info = st.text_area('Additional information about the company(Optional)')
    if not company_add_info:
        company_add_info = None

    # Additional information about user
    user_add_info = st.text_area('Additional information about you(Optional)')
    if not user_add_info:
        user_add_info = None

    if st.button('Submit'):
        if resume is None:
            st.error('Please upload a resume!', icon='❗')
        elif not job_description:
            st.error('Please add job description!', icon='❗')
        else:
            with st.spinner('Thinking about suggestions...'):
                changes = resume_changes(resume, job_description, company_add_info, user_add_info)
            st.subheader('Resume suggestions')
            st.write(changes)

            with st.spinner('Writing cover letter...'):
                cover_letter = write_cover_letter(resume, job_description, company_add_info, user_add_info)
            st.subheader('Cover letter')
            st.write(cover_letter)

            st.write('Good luck for your job search!')


if __name__ == "__main__":
    streamlit_app()
