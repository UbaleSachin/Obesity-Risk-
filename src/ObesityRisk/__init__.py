import os
import sys
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

log_file = 'Log'
logfile_path = os.path.join(log_file, 'Running_logs.log')
os.makedirs(log_file, exist_ok=True)


logging.basicConfig(

    level = logging.INFO,
    format = logging_str,
    
    handlers = [
        logging.FileHandler(logfile_path),
        logging.StreamHandler(sys.stdout)
    ]

)

logger = logging.getLogger('ObesityRisk')
