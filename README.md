##  Quiz Paper and MCQ Generator System
This project creates a web application using Streamlit to generate MCQs (Multiple Choice Questions) from uploaded text or PDF documents. It leverages LangChain, a natural language processing (NLP) framework, and OpenAI's large language model (LLM) to process text and create relevant MCQs.
Components:


## 1.   User Interface (UI):
* Streamlit is used to create a user-friendly interface with the following features:
*  Upload a PDF or text file containing the source material.
* Specify the desired number of MCQs.
*  Enter the subject name for context.
* Set the complexity level of the questions (e.g., Simple, Medium).
*  Generate MCQs and view them in a table format.
*  Download the generated MCQs as a CSV file for further editing.
* Download the MCQs as a PDF file for printing or sharing.


## 2.  MCQ Generation Logic:

* The application utilizes the following functionalities:
* Text Extraction: The uploaded file (PDF or text) is processed to extract the text content.
* MCQ Generation with LangChain: LangChain's LLMChains are employed to interact with OpenAI's LLM. The extracted text, along with the user-specified number of MCQs, subject, and complexity level, are fed into the LLMChain. The LLM then generates the MCQs using its knowledge and understanding of language.
* Data Processing: The generated MCQs are further processed to convert them into a structured format suitable for displaying as a table and generating a PDF.


##  Technical Stack:
* Programming Language: Python
* Web Framework: Streamlit
*  NLP Framework: LangChain
* Large Language Model: OpenAI (through LangChain)
* Data Processing Libraries: pandas
* PDF Generation: reportlab
* Exception Handling: Custom Exception class


##  Benefits:
* Automatic MCQ generation: Saves time and effort compared to manual creation.
* Customizable: Users can define the number, subject, and complexity level of MCQs.
* Streamlined workflow: Integrates text extraction, MCQ generation, and output formatting.
* Efficient download options: Generated MCQs are downloadable in CSV and PDF formats.


first login to the AWS: https://aws.amazon.com/console/

search about the EC2

you need to config the UBUNTU Machine

launch the instance

update the machine:

sudo apt update

sudo apt-get update

sudo apt upgrade -y

sudo apt install git curl unzip tar make sudo vim wget -y

git clone "Your-repository"

sudo apt install python3-pip

pip3 install -r requirements.txt

python3 -m streamlit run StreamlitAPP.py

if you want to add openai api key
create .env file in your server touch .env
vi .env #press insert #copy your api key and paste it there #press and then :wq and hit enter

go with security and add the inbound rule add the port 8501
