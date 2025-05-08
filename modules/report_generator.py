def generate_html_report(results, username):
    with open(f"{username}_report.html", "w") as f:
        f.write("<h1>FalconTrace OSINT Report</h1>")
        for site, found in results:
            status = "✅ Found" if found else "❌ Not Found"
            f.write(f"<p>{site} : {status}</p>")
