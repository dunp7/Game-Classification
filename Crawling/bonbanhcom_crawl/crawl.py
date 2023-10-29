from Crawl_tool import Crawl_tool
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
import time
import csv
import re

class Crawling_tool(Crawl_tool):
    def __init__(self):
        super().__init__()
