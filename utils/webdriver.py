from selenium import webdriver
import subprocess


def initialize_webdriver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(60)
    driver.maximize_window()
    return driver


# def generate_allure_report():
#     print("Generating Allure report...")
#     allure_results_dir = "./allure-results"
#     behave_command = f"behave -f allure_behave.formatter:AllureFormatter -o {allure_results_dir}"
#     subprocess.run(behave_command, shell=True, check=True, timeout=15)
#     allure_report_dir = "./allure-report"
#     subprocess.run(f"allure serve {allure_results_dir} -o {allure_report_dir}", shell=True, check=True, timeout=10)


