import os
import constants
from openai import OpenAI
from icecream import ic 
import time

os.environ["OPENAI_API_KEY"] = constants.OPENAI_APIKEY
client = OpenAI()



# MCQ Generator Assistant
assistant_id = 'asst_1MbhtKBV5G9Pi5LCu2Dk8kCM'



