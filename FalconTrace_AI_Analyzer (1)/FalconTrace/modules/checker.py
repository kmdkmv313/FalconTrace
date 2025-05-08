import requests
from concurrent.futures import ThreadPoolExecutor
from modules.ai_analyzer import analyze_page_content

PROXIES = {
    'http': 'http://your-proxy:port',
    'https': 'http://your-proxy:port'
}

def check_username_on_site(site_url, username):
    try:
        url = site_url.format(username=username)
        res = requests.get(url, timeout=5, proxies=PROXIES)
        if res.status_code == 200:
            analysis = analyze_page_content(res.text)
            return (site_url, True, analysis)
    except:
        pass
    return (site_url, False, "⚠️ No Response")

def run_checks(username, sites, threads=100):
    with ThreadPoolExecutor(max_workers=threads) as executor:
        futures = [executor.submit(check_username_on_site, site, username) for site in sites]
        return [f.result() for f in futures]
