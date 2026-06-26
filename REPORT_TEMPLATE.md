# Assignment Report Template

Important: write the final explanations in your own words. The assignment brief says AI tools should not write the report content. Use this file as a checklist and fill it with your own explanations after studying the code.

## Cover Page

- Module / assignment title
- Student name and ID
- GitHub source code link

## Table of Contents

Add page numbers after exporting to PDF.

## Question 1: Hashing

### i. Hash Table Bucket Structure

Insert screenshot:

- `evidence/q1_bucket_structure.png`

Points to explain in your own words:

- The hash table uses a fixed-size Python list called `buckets`.
- Each bucket stores either `None` or one `Medicine` object.
- This matches open addressing with linear probing because collided items are placed in the next available slot.
- A list is simple, direct, memory-efficient for this task, and gives constant-time index access.

### ii. Product Entity Class

Insert screenshot:

- `evidence/q1_product_entity.png`

Points to explain in your own words:

- `product_id` is a string because IDs such as `M001` contain letters and leading zeroes.
- `name`, `category`, and `expiry_date` are strings for descriptive product information.
- `price` is a float because it stores decimal currency values.
- `quantity` is an integer because stock count is a whole number.

### iii. Search Performance Experiment

Insert screenshots:

- `evidence/q1_experiment_code.png`
- `evidence/q1_output.png`

Points to include:

- Same records are inserted into both the hash table and a one-dimensional list.
- Existing and non-existing keys are searched repeatedly.
- Hash table search uses hashing plus linear probing.
- Array search checks items one by one.
- Compare total and average time from your own generated output.
- Explain whether the hash table was faster and why.

## Question 2: Divide and Conquer Algorithm

### i. Mandatory Features

Insert screenshots:

- `evidence/q2_merge_sort.png`
- `evidence/q2_binary_search.png`
- `evidence/q2_menu_mandatory.png`
- `evidence/q2_output.png`

Explain in your own words:

- Display all transactions.
- Merge Sort recursively divides the list, sorts smaller lists, and merges them.
- Binary Search works only after sorting by transaction ID.
- Linear Search checks each record and is included for comparison.

### ii. Extra Features

Insert screenshots:

- `evidence/q2_extra_features.png`

Implemented optional features:

- Insert transaction dynamically.
- Sort by amount.
- Count recursive calls during Merge Sort.
- Display time complexity table.

### iii. Output Screenshots

Use:

- `evidence/q2_output.png`

Explain which test data shows before sorting, after sorting, existing search, non-existing search, and optional features.

## Question 3: Concurrent Process

### i. Factorial Function and Big-O

Insert screenshot:

- `evidence/q3_factorial_function.png`

Points to explain:

- The loop multiplies from 2 to `n`.
- The number of loop iterations grows linearly as `n` increases.
- Therefore the time complexity is `O(n)`.

### ii. Threaded vs Sequential Experiment

Insert screenshots:

- `evidence/q3_output.png`

Points to include:

- State the threaded average time and sequential average time from your output.
- Compare whether multithreading shortened the time.
- Mention that small CPU-bound factorial calculations may not benefit from Python threads.

### iii. Multithreading Code

Insert screenshot:

- `evidence/q3_threading_code.png`

Explain:

- One thread is created for each factorial number: 50, 100, and 200.
- Threads are started and then joined.
- Total time is measured from the earliest thread start to the latest thread finish.

### iv. Discussion

Write this in your own words:

- Python threads are concurrent, but CPU-bound Python code is limited by the Global Interpreter Lock.
- Multithreading can improve performance for I/O-bound tasks, such as downloading files, reading from network APIs, or waiting for database responses.

## Question 4: Challenges Faced and Personal Reflection

Write no more than 2 pages in your own words. Possible points:

- Understanding linear probing.
- Making sure binary search is used only after sorting.
- Measuring program time consistently.
- Learning about Python threads and why they may not speed up CPU-bound work.
- Preparing for VIVA by tracing the code step by step.

## References

- Python Software Foundation. Python documentation: `time`, `threading`, and `dataclasses`.
- Course lecture notes on hashing, divide and conquer, and time complexity.
