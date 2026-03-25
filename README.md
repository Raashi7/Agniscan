# 🔥 AgniScan CLI

AgniScan is a **Security Scanning CLI Tool** that integrates both:

* 🔍 **SAST** (Static Application Security Testing)
* 🌐 **DAST** (Dynamic Application Security Testing)

It helps identify vulnerabilities in **source code** as well as **live web applications**.

---

## 🚀 Features

* ✅ SAST scanning using secure coding analysis tools
* ✅ DAST pipeline with multiple recon & scanning tools
* ✅ Easy-to-use CLI interface
* ✅ Supports file, folder, and ZIP scanning
* ✅ Automated workflow for web security testing

---

## 🛠️ Installation & Setup

Follow these steps to install and run AgniScan:

```bash
# Clone the repository
git clone https://github.com/Raashi7/Agniscan

# Navigate into the project directory
cd Agniscan

# Install virtual environment package
sudo apt install python3-venv -y

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install ZAP Proxy (for DAST)
sudo apt install zaproxy -y

# Install AgniScan
pip install .

# Verify installation
agniscan --help
```

---

## ✅ Requirements

* Python 3.x
* pip
* Virtual Environment (venv)
* ZAP Proxy

---

## ⚡ Usage

### 🔍 SAST (Static Application Security Testing)

Scan a local file, folder, or ZIP:

```bash
agniscan sast <target_path>
```

#### 📌 Examples

```bash
agniscan sast test.py
agniscan sast ./project_folder
agniscan sast Downloads/project.zip
```

---

### 🌐 DAST (Dynamic Application Security Testing)

Scan a live web application:

```bash
agniscan dast <target_url>
```

#### 📌 Examples

```bash
agniscan dast http://testphp.vulnweb.com
agniscan dast https://example.com
```

---

## 📊 DAST Workflow

AgniScan performs multiple steps in the DAST pipeline:

1. Subdomain Discovery
2. Port Scanning
3. Service Detection
4. Vulnerability Scanning
5. Web Scanning (ZAP)

---

## 📌 Help Command

```bash
agniscan --help
```


## 📄 License

This project is licensed under the MIT License.

