import subprocess


def generate_allure_report():
    allure_results_dir = "./allure-results"
    behave_command = f"behave -f allure_behave.formatter:AllureFormatter -o {allure_results_dir}"
    subprocess.run(behave_command, shell=True, check=True)
    allure_report_dir = "./allure-report"
    subprocess.run(f"allure serve {allure_results_dir} -o {allure_report_dir}", shell=True, check=True, timeout=10)


if __name__ == "__main__":
    generate_allure_report()