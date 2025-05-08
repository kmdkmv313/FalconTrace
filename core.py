from modules.checker import run_checks
from modules.report_generator import generate_html_report

with open("modules/sites_list.txt") as f:
    sites = [line.strip() for line in f]

username = input("Enter username: ")
results = run_checks(username, sites)
generate_html_report(results, username)
