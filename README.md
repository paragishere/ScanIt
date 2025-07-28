# 🛡️ ScanIt

A lightweight and modular **Web Vulnerability Scanner** written in Python that detects common web application flaws like SQL Injection, XSS, insecure headers, and exposed admin panels.

---

##  Features

- SQL Injection Detection (Error-based, Time-based)
- ⚔Cross Site Scripting (XSS) Scanner
- HTTP Security Headers Analyzer
- Admin Panel Exposure Detection
- Modular Codebase for Future Expansion
- Output-ready structure for report saving


---

## 📦 Installation for linux/macOS

```bash
git clone https://github.com/paragishere/ScanIt.git
cd ScanIt

sudo apt install python3-venv
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt


```
## 📦 Installation for windows

```bash
git clone https://github.com/paragishere/ScanIt.git
cd ScanIt

python -m venv venv                # Create virtual environment
venv\Scripts\activate              # Activate the environment
pip install -r requirements.txt

```
## Usage 
```bash
python scanner.py https://example.com

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.

