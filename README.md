# Data Structures and Algorithms Assignment

This project contains three Python programs for the assignment:

- `src/q1_pharmacy_hash_table.py` - Pharmacy inventory using a hash table with linear probing.
- `src/q2_transaction_divide_conquer.py` - Transaction sorting/searching using merge sort, binary search, and linear search.
- `src/q3_factorial_threading.py` - Factorial timing experiment with and without multithreading.

## How to Run

If Python is installed normally:

```powershell
python .\src\q1_pharmacy_hash_table.py --demo
python .\src\q2_transaction_divide_conquer.py --demo
python .\src\q3_factorial_threading.py --demo
```

On this Codex machine, Python was available at:

```powershell
C:\Users\JL\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe
```

Interactive menus:

```powershell
python .\src\q1_pharmacy_hash_table.py
python .\src\q2_transaction_divide_conquer.py
```

## Evidence Pack

Run this after running the demos if you want to regenerate screenshots:

```powershell
python .\tools\make_evidence.py
```

Generated screenshots and output files are placed in `evidence/`.

## GitHub Submission

Create a GitHub repository, then push this folder:

```powershell
git init
git add .
git commit -m "Complete DSA assignment programs"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
git push -u origin main
```

Replace the remote URL with your own GitHub repository URL.
