# Pharmacy DSA Assignment

GitHub repository: <https://github.com/haemoglobin930/pharmacy-dsa-assignment>

This repository contains the source code and evidence pack for the Data Structures and Algorithms assignment. It includes three Python programs:

- `src/q1_pharmacy_hash_table.py` - Pharmacy inventory using a hash table with linear probing.
- `src/q2_transaction_divide_conquer.py` - Transaction sorting/searching using merge sort, binary search, and linear search.
- `src/q3_factorial_threading.py` - Factorial timing experiment with and without multithreading.

## Project Structure

```text
pharmacy-dsa-assignment/
|-- .github/workflows/python-check.yml
|-- evidence/
|   |-- q1_*.png and q1_*.txt
|   |-- q2_*.png and q2_*.txt
|   `-- q3_*.png and q3_*.txt
|-- src/
|   |-- q1_pharmacy_hash_table.py
|   |-- q2_transaction_divide_conquer.py
|   `-- q3_factorial_threading.py
|-- tools/
|   `-- make_evidence.py
|-- REPORT_TEMPLATE.md
|-- RUN_ALL_DEMOS.ps1
|-- requirements.txt
`-- README.md
```

## Requirements

- Python 3.10 or newer
- Pillow, only needed if regenerating screenshot evidence with `tools/make_evidence.py`

Install the optional evidence dependency:

```powershell
python -m pip install -r requirements.txt
```

## How to Run the Programs

If Python is installed normally:

```powershell
python .\src\q1_pharmacy_hash_table.py --demo
python .\src\q2_transaction_divide_conquer.py --demo
python .\src\q3_factorial_threading.py --demo
```

To run all demo outputs at once on Windows PowerShell:

```powershell
.\RUN_ALL_DEMOS.ps1
```

Interactive menus:

```powershell
python .\src\q1_pharmacy_hash_table.py
python .\src\q2_transaction_divide_conquer.py
```

Question 3 is an experiment program and runs its 10-round timing comparison directly.

## Evidence Pack

The `evidence/` folder contains ready-to-use code screenshots and output screenshots for the report. To regenerate them:

```powershell
python .\tools\make_evidence.py
```

Generated screenshots and output text files are saved back into `evidence/`.

## Verification

Compile all Python files:

```powershell
python -m compileall .\src .\tools
```

GitHub Actions also runs a basic check on every push to confirm that the Python files compile and the demo programs execute.

## Report Support

Use `REPORT_TEMPLATE.md` as a checklist for placing screenshots and writing your own explanation. The final report wording should be written personally so you can explain it confidently during VIVA.
