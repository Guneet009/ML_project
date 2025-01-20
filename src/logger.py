import logging
import os

from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(logs_path,exist_ok=True)

'''
os.getcwd() gets the current working directory (where the script is being run).
os.path.join() combines the current directory with the logs folder and the generated LOG_FILE name. 
For example, the path might look like C:/Users/YourName/your_project/logs/01_20_2025_14_30_45.log.

os.makedirs() creates the necessary directories if they don’t already exist. 
The exist_ok=True argument ensures that it won't raise an error if the logs directory already exists.
This ensures that the logs directory exists before attempting to write logs.
'''

LOG_FILE_PATH = os.path.join(logs_path,LOG_FILE)

'''
This line creates the full path to the log file by combining the logs_path (directory path) with the LOG_FILE (log filename).
The final path might look something like: C:/Users/YourName/your_project/logs/01_20_2025_14_30_45.log.
'''


logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

'''
Summary
The code sets up a logging system where logs are stored in a file with a timestamped name, allowing you to track logs over time.
The logs are saved in a logs directory in the current working directory.
The log format includes the timestamp, line number, logger name, log level, and the log message.
The INFO logging level is configured, meaning all log messages of level INFO or higher will be recorded.
'''

# if __name__=="__main__":
#     logging.info('Logging has started')