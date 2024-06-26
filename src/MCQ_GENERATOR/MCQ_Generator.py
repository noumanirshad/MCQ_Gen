import os
import json
import pandas as pd
from dotenv import load_dotenv
from Exception.logger import logging
from src.MCQ_GENERATOR.utils import read_file, get_table_data
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain

from Exception.exception import CustomException
import sys


class Generator:

    def __init__(self):
        load_dotenv()
        self.KEY=os.getenv("apikey")

        self.input_TEMPLATE="""
        Text:{text}
        You are an expert MCQ maker. Given the above text, it is your job to \
        create a quiz  of {number} multiple choice questions for {subject} students in {tone} tone. 
        Make sure the questions are not repeated and check all the questions to be conforming the text as well.
        Make sure to format your response like  RESPONSE_JSON below  and use it as a guide. \
        Ensure to make {number} MCQs
        ### RESPONSE_JSON
        {response_json}
        """

        self.output_TEMPLATE ="""
        You are an expert english grammarian and writer. Given a Multiple Choice Quiz for {subject} students.\
        You need to evaluate the complexity of the question and give a complete analysis of the quiz. Only use at max 50 words for complexity analysis. 
        if the quiz is not at per with the cognitive and analytical abilities of the students,\
        update the quiz questions which needs to be changed and change the tone such that it perfectly fits the student abilities
        Quiz_MCQs:
        {quiz}

        Check from an expert English Writer of the above quiz:
        """

    def LLMChains(self):
        try:
            logging.info("Lets start the LLM Setup.")
            
            llm=ChatOpenAI(openai_api_key=self.KEY,model_name="gpt-3.5-turbo", temperature=0.7)
            logging.info("successfully setup the LLM Model.")

            quiz_generation_prompt = PromptTemplate(
                input_variables=["text", "number", "subject", "tone", "response_json"],
                template=self.input_TEMPLATE
                )
            
            # quiz_chain=LLMChain(llm=llm, prompt=quiz_generation_prompt, output_key="quiz", verbose=True)
            quiz_chain=LLMChain(llm=llm, prompt=quiz_generation_prompt, output_key="quiz", verbose=True)
            logging.info("successfully quiz_chain setup.")


            quiz_evaluation_prompt=PromptTemplate(
                input_variables=["subject", "quiz"], 
                template=self.output_TEMPLATE
                )

            review_chain=LLMChain(llm=llm, prompt=quiz_evaluation_prompt, output_key="review", verbose=True)            

            logging.info("Successfully setup the LLM and Create a input&output prompt_Templates. \n")

            generate_evaluate_chain=SequentialChain(chains=[quiz_chain, review_chain], input_variables=["text", "number", "subject", "tone", "response_json"],
                                                    output_variables=["quiz", "review"], verbose=True,)

            logging.info("Successfully Sequential_Chain. \n")
            return generate_evaluate_chain
        
        except Exception as e:
            logging.info(f"An exception has occurred : {e}")
            raise CustomException(e, sys) 

