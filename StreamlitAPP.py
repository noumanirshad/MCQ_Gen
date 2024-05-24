import os
import json
import pandas as pd
from dotenv import load_dotenv
from Exception.logger import logging
from Exception.exception import CustomException
import sys
from src.MCQ_GENERATOR.utils import get_table_data, read_file
import streamlit as st
from langchain_community.callbacks.manager import get_openai_callback
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import traceback
from src.MCQ_GENERATOR.MCQ_Generator import Generator

def generate_pdf(quiz_data, file_name):
    c = canvas.Canvas(file_name, pagesize=letter)
    width, height = letter

    y_position = height - 40
    for i, (question, data) in enumerate(quiz_data.items(), start=1):
        question_text = f"{i}. {question}"
        c.drawString(40, y_position, question_text)
        y_position -= 20

        for option, answer in data['options'].items():
            option_text = f"{option}: {answer}"
            c.drawString(60, y_position, option_text)
            y_position -= 20

        y_position -= 20  # Extra space between questions
        if y_position < 40:  # Create a new page if space is less than 40
            c.showPage()
            y_position = height - 40

    c.save()

gen = Generator()
eval_chain = gen.LLMChains()
with open("E:\\ALL PROGRAMS\\All_DS_Projects\\Generative AI\\MCQ_Gen\\Response.json", 'r') as file:
    Response_json = json.load(file)

try:
    logging.info("Let's start the Streamlit setup like buttons and architectures...")
    st.title("MCQs Creator Application with LangChain 🦜⛓️")

    with st.form("user_inputs"):
        uploaded_file = st.file_uploader("Upload a PDF or txt file")
        mcq_count = st.number_input("No. of MCQs", min_value=1, max_value=50)
        subject = st.text_input("Insert Subject", max_chars=20)
        tone = st.text_input("Complexity Level Of Questions", max_chars=20, placeholder="Simple")
        button = st.form_submit_button("Create MCQs")
        logging.info("....... Successfully completed the Streamlit setup ......")

    if button and uploaded_file is not None and mcq_count and subject and tone:
        with st.spinner("loading..."):
            try:
                logging.info("....... Let's apply uploading functions to get the text file. ......")
                text = read_file(uploaded_file)
                with get_openai_callback() as cb:
                    logging.info("....... Let's apply MCQ_GENERATOR on text data. ......")
                    response = eval_chain(
                        {
                            "text": text,
                            "number": mcq_count,
                            "subject": subject,
                            "tone": tone,
                            "response_json": Response_json
                        }
                    )
                logging.info("....... Successfully applied the MCQ_GENERATOR functions on text data. ......")
            except Exception as e:
                traceback.print_exception(type(e), e, e.__traceback__)
                st.error("Error")
            else:
                print(f"Total Tokens: {cb.total_tokens}")
                print(f"Prompt Tokens: {cb.prompt_tokens}")
                print(f"Completion Tokens: {cb.completion_tokens}")
                print(f"Total Cost: {cb.total_cost}")
                if isinstance(response, dict):
                    quiz = response.get("quiz")
                    print(f"Let's get the quiz details: \n{quiz}\n end:")
                    if quiz is not None:
                        logging.info("....... Let's apply get_table_data functions on output of quiz . ......")
                        table_data = get_table_data(quiz)
                        logging.info("....... Successfully applied get_table_data functions on output of quiz . ......")
                        if table_data is not None:
                            df = pd.DataFrame(table_data)
                            df.index = df.index + 1
                            st.table(df)
                            st.text_area(label="Review", value=response["review"])
                            logging.info("....... Successfully converted table data into DataFrame . ......")
                            
                            # Button to download CSV
                            csv = df.to_csv(index=False).encode('utf-8')
                            st.download_button(
                                label="Download CSV",
                                data=csv,
                                file_name="quiz_data.csv",
                                mime="text/csv"
                            )
                            logging.info("....... Successfully converted data into CSV File . ......")
                            
                            # Ensure quiz data is in the correct format for PDF generation
                            quiz_dict = {}
                            for idx, row in df.iterrows():
                                question = row['MCQ']
                                options = {opt.split('->')[0]: opt.split('->')[1] for opt in row['Choices'].split('||')}
                                correct_answer = row['Correct']
                                quiz_dict[question] = {"options": options, "correct": correct_answer}

                            # Button to generate and download PDF
                            pdf_file_name = "quiz.pdf"
                            generate_pdf(quiz_data=quiz_dict, file_name=pdf_file_name)
                            with open(pdf_file_name, "rb") as pdf_file:
                                pdf_bytes = pdf_file.read()
                                st.download_button(
                                    label="Download PDF",
                                    data=pdf_bytes,
                                    file_name="quiz.pdf",
                                    mime="application/pdf"
                                )
                            logging.info("....... Successfully converted data into PDF File . ......")
                        else:
                            st.error("Error in the table data")
                else:
                    st.write(response)

except Exception as e:
    logging.info(f"An exception has occurred : {e}")
    raise CustomException(e, sys)
