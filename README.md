# Panopto Delete Users Tool

This is a Python Tkinter GUI application to merge user files and delete users via the Panopto API.

---

## Requirements

- Python 3.7 or higher
- The following Python packages:
  - `zeep`
  - `pandas`
  - `tkinter` (usually included with Python)
  - `hashlib` (standard Python library)
  - `openpyxl` (if working with Excel `.xlsx` files)

---

## Setup Instructions

1. **Clone or download this repository**  
   Ensure all files (`main.py`, `config.py`, and utility modules) are in the same folder.

2. **Create a virtual environment (optional but recommended)**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate

3. **Install dependencies**

    ```bash
    pip install zeep pandas openpyxl # or pip3 if using Python 3.x

4. **Configure credentials**
    Edit `config.py` with your Panopto API credentials:

    ```python
    userkey = "your_userkey" # admin's username 
    password = "your_password" # admin's password
    applicationkey = "your_applicationkey" # available through "Identity Providers" on Panopto
    servername = "your_servername" # in this case, "gettysburg.hosted.panopto.com"

5. **Run the application**

    ```python
    python3 main.py

- Once it runs, it launches an application that enables you to browse files on your computer 
- Put your Excel or .csv files into the boxes
- Click "Merge Files" to map users' emails with IDs
- After merging, it will export another .csv file that contains only email and IDs in the current folder
- Click "Delete Users" to delete users on Panopto
    - It will prompt out a window showing emails that will be deleted
    - Click "Delete" to proceed and "Cancel" to not proceed