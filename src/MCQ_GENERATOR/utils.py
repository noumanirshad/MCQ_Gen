import traceback
import os
import PyPDF2
from Exception.logger import logging
from Exception.exception import CustomException
import sys
import json



def read_file(filename):
    if filename.name.endswith('.pdf'):
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
        
    elif filename.name.endswith(".txt"):     
        txt_file = filename.read().decode("utf_8")
        logging.info("Successfully Read the text file")
        return txt_file     
    
    else:
        # logging.info(f"Unspported file format only pdf and text file supported : {e}")
        raise CustomException("Unspported file format only pdf and text file supported", sys) 
        

def get_table_data(quiz_str):
    try:
        # convert the quiz from a str to dict
        logging.info("Getting Quiz convert into table data format.")
        # Correcting the malformed JSON by replacing single quotes with double quotes
        quiz_dict = json.loads(quiz_str.replace("'", "\""))
        quiz_table_data = []

        # iterate over the quiz dictionary and extract the required information
        for key, value in quiz_dict.items():
            mcq = value["mcq"]
            options = " || ".join([f"{option}->{option_value}" for option, option_value in value["options"].items()])
            correct = value["correct"]
            quiz_table_data.append({"MCQ": mcq, "Choices": options, "Correct": correct})

        logging.info("Successfully Quiz convert into table data format.")
        return quiz_table_data

    except json.JSONDecodeError as e:
        # JSONDecodeError will occur if the provided JSON is malformed
        logging.error(f"JSON decoding error: {e}")
        raise CustomException("Malformed JSON provided.", sys)
    except KeyError as e:
        # KeyError will occur if required keys are missing in the JSON structure
        logging.error(f"KeyError: {e}")
        raise CustomException("Required keys are missing in the JSON structure.", sys)
    except Exception as e:
        # Catching other exceptions
        logging.error(f"An exception has occurred : {e}")
        raise CustomException(e, sys)

