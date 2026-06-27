# Advanced Algorithm Assignment

This repository contains three Python programs for the assignment.

## Files

```text
advanced-algorithm-assignment/
|-- q1_pharmacy_hash_table.py
|-- q2_transaction_divide_conquer.py
|-- q3_factorial_threading.py
|-- .gitignore
`-- README.md
```

## Question 1

`q1_pharmacy_hash_table.py`

Pharmacy inventory system using a hash table with linear probing. It includes product records, display, insert/update, search, and a search performance comparison against a one-dimensional array.

Run program:

```powershell
python .\q1_pharmacy_hash_table.py
```

## Question 2

`q2_transaction_divide_conquer.py`

Transaction system using Merge Sort, Binary Search, and Linear Search. It includes mandatory menu features and optional features such as inserting transactions, sorting by amount, counting recursive calls, and showing a complexity table.

Run program:

```powershell
python .\q2_transaction_divide_conquer.py
```

## Question 3

`q3_factorial_threading.py`

Factorial timing experiment comparing multithreaded execution and sequential execution for `50!`, `100!`, and `200!`.

Run program:

```powershell
python .\q3_factorial_threading.py
```

## Requirements

- Python 3.10 or newer
- No external Python packages are required

## Quick Check

```powershell
python -m compileall .\q1_pharmacy_hash_table.py .\q2_transaction_divide_conquer.py .\q3_factorial_threading.py
```
