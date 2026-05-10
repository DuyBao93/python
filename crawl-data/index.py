import requests
import time
import os
from datetime import datetime
import pytz
from bs4 import BeautifulSoup
from termcolor import colored

tzVN = pytz.timezone('Asia/Ho_Chi_Minh') 

def split_space(val):
    words = val.split()
    return (" ".join(words))