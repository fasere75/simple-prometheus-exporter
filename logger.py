import logging
import datetime
import random
from time import sleep

FORMAT = '%(asctime)-20s %(message)5s'
logging.basicConfig (
    format=FORMAT, 
    level = logging.INFO,
    handlers = [
        logging.FileHandler("app.log"),
        logging.StreamHandler()
    ]
)

APP_LOG =  [
    "application_error Invalid entry",
    "user_activity admin login",
    "application_event restart",
    "user_actitivy admin login",
    "application_error OOM",
    "application_event memory_claim"
    
]
def mylogger ():
    while True:
        logging.info ( random.choice(APP_LOG))
        sleep (random.randrange(1,5))
   
if __name__ == "__main__":
    mylogger()