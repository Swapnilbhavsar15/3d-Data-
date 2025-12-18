# 3D Point Cloud Analysis: "Smart Segmentation"

**Two-Word Summary:** robust metrics.

This tool processes large-scale 3D scan data (`.ply`), automatically segments the dominant architectural structures, and calculates room height by intelligently handling coordinate system orientation and clutter.

---

## 🛠️ Setup & Installation

**Prerequisites:** Python 3.8+ (Linux/Ubuntu recommended for heavy 3D processing)

### 1. System Dependencies (Linux/Codespaces)
To prevent Open3D crashes on headless servers (like GitHub Codespaces or CI/CD pipelines), install the OpenGL drivers first:
```bash
sudo apt-get update
sudo apt-get install -y libgl1 libgomp1

### 2. Python Dependancies
Install the necessary computational libraries:
```bash
pip install -r requirements.txt

### 3. Run the Tool
The tool can be used by running the main file.
```bash 
python main.py