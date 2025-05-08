import requests
from concurrent.futures import ThreadPoolExecutor

def check_username_on_site(site_url, username):
    try:
        url = site_url.format(username=username)
        res = requests.get(url, timeout=5)
        if res.status_code == 200 and username in res.text:
            return (site_url, True)
    except:
        pass
    return (site_url, False)

def run_checks(username, sites, threads=100):
    with ThreadPoolExecutor(max_workers=threads) as executor:
        futures = [executor.submit(check_username_on_site, site, username) for site in sites]
        return [f.result() for f in futures]
