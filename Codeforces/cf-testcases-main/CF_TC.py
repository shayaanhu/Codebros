from selenium import webdriver

# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.options import Options

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from selenium.webdriver.support.ui import Select

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import sys
# shim missing stdlib distutils → setuptools._distutils
import setuptools._distutils as _distutils_pkg
import setuptools._distutils.version as _distutils_version
sys.modules['distutils'] = _distutils_pkg
sys.modules['distutils.version'] = _distutils_version

import undetected_chromedriver as uc
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


import requests, json

import requests, json
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

# For terminal beatify
from rich.console import Console

console = Console()

_cf_session = requests.Session()
_retry_strategy = Retry(
    total=5,
    backoff_factor=1,
    status_forcelist=[429, 500, 502, 503, 504],
    allowed_methods=["GET"]
)
_cf_session.mount("https://", HTTPAdapter(max_retries=_retry_strategy))



class CF_TC:
    def __init__(self, base_url="https://codeforces.com/"):
        options = uc.ChromeOptions()
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--window-size=1200,800")
        options.headless = True

        # point at the ChromeDriver that matches your installed Chrome
        service = Service(ChromeDriverManager().install())
        self.driver = uc.Chrome(service=service, options=options)

        self.wait = WebDriverWait(self.driver, 30)
        self.base_url = base_url

    def _getSubmissionID(self, contest_id, problem_index):
        status_url = f"{self.base_url}contest/{contest_id}/status"
        self.driver.get(status_url)

        # wait up to 60s for the real dropdown to load (skip CF challenge)
        try:
            self.wait.until(EC.presence_of_element_located((By.ID, "problemIndex")))
        except:
            return (None, "Cloudflare challenge not passed / status page not ready")

        # now filter by problem
        problem_dropdown = self.driver.find_element(By.ID, "problemIndex")
        Select(problem_dropdown).select_by_value(problem_index)

        # filter by verdict
        self.wait.until(EC.presence_of_element_located((By.ID, "verdictName")))
        verdict_dropdown = self.driver.find_element(By.ID, "verdictName")
        Select(verdict_dropdown).select_by_value("OK")

        # click apply if needed
        if self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//input[@type='submit' and (@value='Go' or @value='Apply')]")
        )):
            self.driver.find_element(
                By.XPATH, "//input[@type='submit' and (@value='Go' or @value='Apply')]"
            ).click()

        # grab first submission ID
        sub_xpath = "//table[contains(@class,'status-frame-datatable')]//tr[2]/td[1]/a"
        self.wait.until(EC.presence_of_element_located((By.XPATH, sub_xpath)))
        link = self.driver.find_element(By.XPATH, sub_xpath)
        return (True, link.get_attribute("href").split("/")[-1])

    # def _getSubmissionID(self, contest_id, problem_index):
    #     # Get to the contest submission page
    #     self.driver.get(f"{self.base_url}contest/{contest_id}/status")

    #     # # applying filters for the problem and verdict to be `accepted`
    #     # if self.wait_till_load('//*[@id="frameProblemIndex"]'):
    #     #     select = Select(
    #     #         self.driver.find_element(By.XPATH, '//*[@id="frameProblemIndex"]')
    #     #     )

    #     #     select.select_by_index(ord(problem_index) - ord("A") + 1)

    #     if self.wait_till_load('//*[@id="problemIndex"]'):
    #         select = Select(self.driver.find_element(By.ID, "problemIndex"))
    #         select.select_by_value(problem_index)
    #     else:
    #         return (None, "Error while filtering problem index")

    #     if self.wait_till_load('//*[@id="verdictName"]', delay = 5):
    #         verdict = Select(
    #             # self.driver.find_element(By.XPATH, '//*[@id="verdictName"]')
    #             self.driver.find_element(By.ID, "verdictName")
    #         )

    #         verdict.select_by_index(1)

    #         if self.wait_till_load(
    #             "/html/body/div[6]/div[4]/div[1]/div[4]/div[2]/form/div[2]/input[1]"
    #         ):
    #             apply_btn = self.driver.find_element(
    #                 By.XPATH,
    #                 "/html/body/div[6]/div[4]/div[1]/div[4]/div[2]/form/div[2]/input[1]",
    #             )
    #             apply_btn.click()
    #     else:
    #         return (None, "Error while filtering problem verdict")

    #     if self.wait_till_load(
    #         "/html/body/div[6]/div[4]/div[2]/div[2]/div[6]/table/tbody/tr[2]/td[1]/a"
    #     ):
    #         content = self.driver.find_element(
    #             By.XPATH,
    #             "/html/body/div[6]/div[4]/div[2]/div[2]/div[6]/table/tbody/tr[2]/td[1]/a",
    #         )
    #         return (True, content.text)

    #     else:
    #         return (None, "Error while finding Submission ID ")

    # def _getSubmissionID(self, contest_id, problem_index):
    #     """
    #     Navigate to the contest status page, filter by problem_index and Accepted verdict,
    #     and return the latest accepted submission ID for that problem.
    #     """
    #     # 1) Open the status page
    #     self.driver.get(f"{self.base_url}contest/{contest_id}/status")
    #     print(self.driver.page_source[:2000])

    #     # 2) Filter by problem index
    #     if not self.wait_till_load("//select[@id='problemIndex']", delay=10):
    #         return (None, "Error while filtering problem index")
    #     problem_dropdown = self.driver.find_element(By.ID, "problemIndex")
    #     Select(problem_dropdown).select_by_value(problem_index)

    #     # 3) Filter by verdict = Accepted
    #     if not self.wait_till_load("//select[@id='verdictName']", delay=10):
    #         return (None, "Error while filtering problem verdict")
    #     verdict_dropdown = self.driver.find_element(By.ID, "verdictName")
    #     Select(verdict_dropdown).select_by_value("OK")

    #     # 4) Click the “Go”/apply button if it exists
    #     if self.wait_till_load(
    #         "//input[@type='submit' and (@value='Go' or @value='Apply')]", delay=5
    #     ):
    #         apply_btn = self.driver.find_element(
    #             By.XPATH, "//input[@type='submit' and (@value='Go' or @value='Apply')]"
    #         )
    #         apply_btn.click()

    #     # 5) Wait for the filtered table and grab the first submission link
    #     #    Note: row[1] is the header, row[2] is the first data row
    #     sub_link_xpath = "//table[contains(@class,'status-frame-datatable')]//tr[2]/td[1]/a"
    #     if not self.wait_till_load(sub_link_xpath, delay=10):
    #         return (None, "Error while finding Submission ID")
    #     link = self.driver.find_element(By.XPATH, sub_link_xpath)
    #     return

    # def _isProblemExists(self, contest_id, problem_num):
    #     url = f"{self.base_url}api/contest.standings?contestId={contest_id}&from=1&count=1"
    #     r = requests.get(url)
    #     r = r.json()
    #     # r = json.loads(r)

    #     if r["status"] != "OK":
    #         x = str(
    #             input("Codeforces API is down.\nDo you still want to continue (y/n): ")
    #         )
    #         if x == "n":
    #             return (None, "Codeforces API is down")

    #     for i in r["result"]["problems"]:
    #         if str(problem_num) == i["index"]:
    #             return (True, "Problem found")

    #     return (None, "Problem does not exists")

    #     # https://codeforces.com/api/contest.standings?contestId=566&from=1&count=1

        # filepath: ...\cf-testcases-main\CF_TC.py
    def _isProblemExists(self, contest_id, problem_num):
        url = f"{self.base_url}api/contest.standings?contestId={contest_id}&from=1&count=1"
        try:
            # use our retrying session here
            resp = _cf_session.get(url, timeout=10)
            resp.raise_for_status()
            data = resp.json()
        except requests.RequestException as e:
            return (None, f"HTTP error: {e}")
        except ValueError:
            return (None, "Invalid JSON from Codeforces API")

        if data.get("status") != "OK":
            return (None, f"API returned status: {data.get('status')}")
        for p in data["result"]["problems"]:
            if str(problem_num) == p.get("index"):
                return (True, "Problem found")
        return (None, "Problem does not exist")


    def get_testcases(self, contest_id, problem_num):
        problem_exist = self._isProblemExists(contest_id, problem_num)
        if not problem_exist[0]:
            return problem_exist

        console.log("Found the problem")

        submission_id = self._getSubmissionID(contest_id, problem_num)

        if not submission_id[0]:
            return submission_id

        self.driver.get(
            f"https://codeforces.com/contest/{contest_id}/submission/{submission_id[1]}"
        )

        if self.wait_till_load("/html/body/div[6]/div[4]/div/div[4]/div[2]/a", 3):
            click_btn = self.driver.find_element(
                By.XPATH, "/html/body/div[6]/div[4]/div/div[4]/div[2]/a"
            )

            click_btn.click()

        if self.wait_till_load("/html/body/div[6]/div[4]/div/div[4]/div[3]", 3):
            input = self.driver.find_elements(By.CLASS_NAME, "input")
            output = self.driver.find_elements(By.CLASS_NAME, "output")

            tc = []
            for i in range(len(input)):
                tc.append((input[i].text, output[i].text))
            tc = tc[1:]
            console.log(f"Total test cases found : {len(tc)}")
            return (True, tc)

        return (None, "Error while finding test cases")

    def wait_till_load(self, xpath_value, delay=3):
        try:
            myElem = WebDriverWait(self.driver, delay).until(
                EC.presence_of_element_located((By.XPATH, xpath_value))
            )
            # print("Page is ready!")
            return 1
        except TimeoutException:
            # print("Loading took too much time!")
            return 0
