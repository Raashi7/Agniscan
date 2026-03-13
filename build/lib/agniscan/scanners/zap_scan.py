import time
import subprocess
import requests

try:
    from zapv2 import ZAPv2
except ImportError:
    print("[!] ZAP Python API not installed.")
    print("[!] Install it using: sudo apt install python3-zapv2")
    ZAPv2 = None


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

    if ZAPv2 is None:
        print("[!] ZAP dependency missing. Skipping ZAP scan.")
        return

    print("[+] Running ZAP scan on:", target)

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

    # Access target
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

        status = int(zap.spider.status(spider_id))

        print(f"[Spider] Progress: {status}%")

        if status >= 100:
            break

        time.sleep(2)

    print("[AgniScan] Spider scan completed")

    # -------------------
    # Active Scan
    # -------------------

    print("[AgniScan] Starting Active Scan")

    scan_id = zap.ascan.scan(target)

    while True:

        status = int(zap.ascan.status(scan_id))

        print(f"[Active Scan] Progress: {status}%")

        if status >= 100:
            break

        time.sleep(5)

    print("[AgniScan] Active scan completed")

    # -------------------
    # Alerts
    # -------------------

    alerts = zap.core.alerts()

    print(f"[AgniScan] Total Alerts Found: {len(alerts)}")

    for alert in alerts[:10]:
        print(f"[{alert['risk']}] {alert['alert']} -> {alert['url']}")
