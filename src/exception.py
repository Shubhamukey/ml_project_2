import sys
import logging
import os
from datetime import datetime

def error_message_detail(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occurred in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error))

    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message

if __name__ == "__main__":
    # Create logs directory if it doesn't exist
    logs_dir = "logs"
    os.makedirs(logs_dir, exist_ok=True)

    # Set up logging
    log_file = "{0}.log".format(datetime.now().strftime('%m_%d_%Y_%H_%M_%S'))
    log_file_path = os.path.join(logs_dir, log_file)
    logging.basicConfig(
        filename=log_file_path,
        format="[%(asctime)s] %(levelname)s %(name)s - %(message)s",
        level=logging.INFO
    )

    try:
        a = 1 / 0
    except Exception as e:
        logging.info('Divided by Zero Error ohhh ohhhh')
        raise CustomException(e, sys)




