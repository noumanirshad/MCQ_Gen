import os
import sys
import logging
from datetime import datetime

logging_str = "\n['Date & time': %(asctime)s,  'Level' :  %(levelname)s, 'file': %(module)s, \n'message': %(message)s]\n"
log_dir = "logs"
Log_file = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
log_filepath = os.path.join(log_dir, Log_file)
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("MCQ_Generator")