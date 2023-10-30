import os

import openai
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())
openai.api_key = os.environ['OPENAI_API_KEY']

MODEL = "gpt-4"


def write_cover_letter(resume: str, job_description: str, comp_add_info: str = "None",
                       user_add_info: str = "None") -> str:
    """
    Writes cover letter based on information provided

    :param resume: Resume
    :param job_description: Job description
    :param comp_add_info: Additional information about the company
    :param user_add_info: Additional information about the user
    :return: cover letter
    """
    system_prompt = """
        You are a helpful assistant whose job is write cover letters. You will be given a resume and job description. 
        Sometimes, user may provide additional information about the company or the user.
    """
    user_prompt = f"""
            resume: {resume}
            job description: {job_description}
            company additional information: {comp_add_info}
            user additional information: {user_add_info}
        """

    result = openai.ChatCompletion.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ]
    )["choices"][0]["message"]["content"]

    return result


def resume_changes(resume: str, job_description: str, comp_add_info: str = "None", user_add_info: str = "None") -> str:
    """
    Suggest changes for the resume based on information provided

    :param resume: Resume
    :param job_description: Job description
    :param comp_add_info: Additional information about the company
    :param user_add_info: Additional information about the user
    :return: resume changes
    """
    system_prompt = """
            You are a helpful assistant whose job is suggest if any change is needed for the resume to match with job
            description. You will be given a resume and job description. Sometimes, user may provide additional 
            information about the company or the user.
        """

    user_prompt = f"""
            resume: {resume}
            job description: {job_description}
            company additional information: {comp_add_info}
            user additional information: {user_add_info}
        """

    result = openai.ChatCompletion.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ]
    )["choices"][0]["message"]["content"]

    return result
