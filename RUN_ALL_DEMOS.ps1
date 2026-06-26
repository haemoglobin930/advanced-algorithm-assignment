$ErrorActionPreference = "Stop"

Write-Host "Running Question 1 demo..." -ForegroundColor Cyan
python .\src\q1_pharmacy_hash_table.py --demo

Write-Host "`nRunning Question 2 demo..." -ForegroundColor Cyan
python .\src\q2_transaction_divide_conquer.py --demo

Write-Host "`nRunning Question 3 demo..." -ForegroundColor Cyan
python .\src\q3_factorial_threading.py --demo

Write-Host "`nAll demos completed." -ForegroundColor Green
