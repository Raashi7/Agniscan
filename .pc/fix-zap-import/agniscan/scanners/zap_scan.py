import time
import subprocess
import requests
from zapv2 import ZAPv2

ZAP_HOST = "127.0.0.1"
ZAP_PORT = "8090"
ZAP_API = f"http://{ZAP_HOST}:{ZAP_PORT}"


def is_zap_running():
    try:
        r = requests.get(f"{ZAP_API}/JSON/core/view/version/", timeout=5)
        return r.status_code == 200
    except:
        return False


def start_zap():

    if is_zap_running():
        print("[AgniScan] ZAP already running")
        return True

    print("[AgniScan] Starting ZAP daemon...")

    subprocess.Popen([
        "zaproxy",
        "-daemon",
        "-host", ZAP_HOST,
        "-port", ZAP_PORT,
        "-config", "api.disablekey=true"
    ])

    print("[AgniScan] Waiting for ZAP to initialize...")

    for _ in range(40):

        if is_zap_running():
            print("[AgniScan] ZAP started successfully")
            return True

        time.sleep(3)

    print("[AgniScan] ZAP failed to start")
    return False


def run_zap(target):

    if not target.startswith("http"):
        target = "http://" + target

    print(f"[AgniScan] Target: {target}")

    if not start_zap():
        return

    zap = ZAPv2(
        apikey='',
        proxies={
            'http': f'http://{ZAP_HOST}:{ZAP_PORT}',
            'https': f'http://{ZAP_HOST}:{ZAP_PORT}'
        }
    )

    print("[AgniScan] ZAP Version:", zap.core.version)

    # Access target so it appears in Sites Tree
    print("[AgniScan] Accessing target")

    try:
        zap.urlopen(target)
    except:
        pass

    time.sleep(5)

    # -------------------
    # Spider Scan
    # -------------------

    print("[AgniScan] Starting Spider Scan")

    spider_id = zap.spider.scan(target)

    while True:

        status = zap.spider.status(spider_id)

        if not status.isdigit():
            break

        progress = int(status)

        print(f"Spider progress: {progress}%")

        if progress >= 100:
            break

        time.sleep(2)

    print("[AgniScan] Spider completed")

    time.sleep(10)

    # -------------------
    # Active Scan
    # -------------------

    print("[AgniScan] Starting Active Scan")

    scan_id = zap.ascan.scan(target)

    if scan_id == "does_not_exist" or scan_id is None:
        print("[AgniScan] Active scan failed to start")
        return

    while True:

        status = zap.ascan.status(scan_id)

        if not status.isdigit():
            print("[AgniScan] Scan status error:", status)
            break

        progress = int(status)

        print(f"Active scan progress: {progress}%")

        if progress >= 100:
            break

        time.sleep(5)

    print("[AgniScan] Active scan completed")

    # -------------------
    # Alerts
    # -------------------

    print("\n[AgniScan] Vulnerabilities Found\n")

    alerts = zap.core.alerts(baseurl=target)

    if not alerts:
        print("No vulnerabilities detected")
        return

    for alert in alerts:

        print("Name:", alert.get("alert"))
        print("Risk:", alert.get("risk"))
        print("URL:", alert.get("url"))
        print("Description:", alert.get("description"))
        print("-" * 60)
