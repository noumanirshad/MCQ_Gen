import traceback
import os
from langchain.callbacks import get_openai_callback
import PyPDF2
from Exception.logger import logging
from Exception.exception import CustomException
import sys
import json



def read_file(filename):
    if filename.endswith('.pdf'):
        logging.info("Lets Read the files")
        try:                
            pdf_reader = PyPDF2.PdfFileReader(filename)
            text = " "
            for page in pdf_reader.pages:
                text += page.extract_text()
            
            logging.info("Successfully Read the pdf file")
            return text
        
        except Exception as e:
            logging.info(f"Error reading the pdf file : {e}")
            raise CustomException(e, sys) 
        
    elif filename.name.endwith(".txt"):     
        txt_file = filename.read().decode("utf_8")
        logging.info("Successfully Read the text file")
        return txt_file     
    
    else:
        # logging.info(f"Unspported file format only pdf and text file supported : {e}")
        raise CustomException("Unspported file format only pdf and text file supported", sys) 
        

def get_table_data(quiz_str):
    try:
        logging.info("Getting Quiz convert into table data format.")
        quiz_dict = json.loads(quiz_str)
        quiz_table_data = []
        for key, value in quiz_dict.items():
            mcq = value["mcq"]
            option = "||".join(
                [
                    f"{option}-> {option_value}" for option , option_value in value["option"].items()
                ]
            )
            correct = value["correct"]
            quiz_table_data.append({"MCQ": mcq, "Chioces": option, "Correct": correct})
        logging.info("Successfully Quiz convert into table data format.")
        return quiz_table_data
        
    except Exception as e:
        logging.info(f"An exception has occurred : {e}")
        raise CustomException(e, sys) 

