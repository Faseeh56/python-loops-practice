# 🐍 Python Loops Practice

> Hands-on Python loop practice as part of my **AI Engineering learning journey**.

This repository contains my practical work from **Python Class 3**, where I focused on understanding and applying **loops, repetition, conditions, and basic data processing**.

Rather than learning Python as a programming language for its own sake, this practice is part of building the Python foundation required for my future work in **Data Science, Machine Learning, and AI Engineering**.

---

## 🎯 What This Repository Is About

The main goal of this repository is to move from:

```text
Understanding a concept
        ↓
Writing the code
        ↓
Running the program
        ↓
Testing different inputs
        ↓
Understanding the result
```

The exercises are intentionally small and beginner-friendly, but each one introduces a practical way of thinking about loops.

---

## 🧠 Concepts Practiced

This repository focuses on:

* `for` loops
* `range()`
* Loop variables
* User input with `input()`
* Type conversion with `int()`
* Conditional statements with `if`
* Comparison operators
* Modulo operator `%`
* Logical operator `and`
* Iterating through lists
* Filtering values
* Counting values using a counter
* Basic data processing

---

## 🚀 Practice Missions

### 01 — Robot Steps 🤖

**File:** `01_Robot_Steps.py`

A simple robot simulation that asks the user how many steps the robot should take and uses a `for` loop to generate each step.

**Concepts:**

* User input
* `int()`
* `for` loop
* `range()`
* Loop variable
* f-strings

Example idea:

```text
Enter the number of steps the robot should take: 5

Step 1: The robot has taken a step.
Step 2: The robot has taken a step.
Step 3: The robot has taken a step.
...
```

This was my starting point for understanding how a loop can automate repetitive actions.

---

### 02 — Secret Number Scanner 🔎

**File:** `02_Secret_Number_Scanner.py`

A simple number scanner that examines a range of numbers and identifies numbers that satisfy multiple conditions.

The program checks whether a number is:

* Even
* Greater than 10

**Concepts:**

```text
for loop
+
range()
+
if
+
%
+
and
```

Example:

```text
Enter a number to stop at: 20

12 is an even number greater than 10.
14 is an even number greater than 10.
16 is an even number greater than 10.
18 is an even number greater than 10.
```

This exercise introduced the idea of combining **iteration with decision-making**.

---

### 03 — Power-Up Pattern ⚡

**File:** `03_Power_Up_Pattern.py`

This program generates a multiplication-based pattern using a base number and a user-defined stopping value.

Example:

```text
Enter a base number: 5
Enter the number to stop at: 6

5
10
15
20
25
```

**Concepts:**

* User input
* `for` loops
* `range()`
* Multiplication
* Loop-controlled patterns

The important idea here is recognizing that repetitive numerical patterns can be generated automatically instead of manually writing every result.

---

### 04 — Score Filter 🎯

**File:** `04_Score_Filter.py`

This exercise introduces loops with a collection of values.

The program works with a list of scores:

```python
scores = [33, 45, 67, 89, 12, 55, 78, 90, 23, 44]
```

It then loops through the scores and identifies values above the selected threshold.

**Concepts:**

* Lists
* Iterating through a list
* `for`
* `if`
* Comparison operators
* Basic filtering

This is an important step toward **data processing**, because the same general pattern is used when examining values inside larger datasets.

---

### 05 — Mini Data Analyzer 📊

**File:** `05_Mini_Data_Analyzer.py`

The final exercise takes the loop concept into a small data-processing scenario.

The program works with temperature data:

```python
temperatures = [31, 34, 29, 36, 33, 27, 38, 35, 30, 32]
```

It processes the values to identify:

* All temperatures
* Temperatures `35` or above
* Number of temperatures `35` or above
* Number of temperatures below `30`

**Concepts:**

* Lists
* `for` loops
* Conditions
* Counters
* Filtering
* Basic data analysis

This exercise represents the direction I want to take with Python:

```text
Python
   ↓
Process Data
   ↓
Understand Data
   ↓
Machine Learning
   ↓
AI Engineering
```

---

## 📂 Repository Structure

```text
python-loops-practice/
│
├── Problems/
│
├── output_screen_shots/
│
├── 01_Robot_Steps.py
├── 02_Secret_Number_Scanner.py
├── 03_Power_Up_Pattern.py
├── 04_Score_Filter.py
└── 05_Mini_Data_Analyzer.py
```

The `Problems` folder contains the practice/problem material, while `output_screen_shots` contains screenshots of program outputs.

---

## 🛠️ How to Run

Make sure Python is installed on your system.

Clone the repository:

```bash
git clone https://github.com/Faseeh56/python-loops-practice.git
```

Move into the repository:

```bash
cd python-loops-practice
```

Run any program with:

```bash
python 01_Robot_Steps.py
```

For example:

```bash
python 05_Mini_Data_Analyzer.py
```

You can also open the `.py` files in **VS Code** or another Python-compatible editor and run them there.

---

## 💡 What I Learned

Through these exercises, I practiced an important programming pattern:

```text
Take multiple values
       ↓
Loop through them
       ↓
Check / process each value
       ↓
Produce useful information
```

The most important takeaway is not memorizing the syntax of a `for` loop.

It is learning to recognize situations where I can say:

> **"This task is repetitive — I can make Python do it for me."**

---

## 🤖 Why Loops Matter for AI Engineering

Loops may look simple, but the underlying idea is extremely important.

In AI and Data Science, we constantly work with collections of information:

```text
Rows
Records
Images
Features
Predictions
Measurements
Samples
```

The specific tools will become much more powerful later, especially with **NumPy** and **Pandas**, but the basic programming mindset remains:

```text
Data
 ↓
Iteration / Processing
 ↓
Transformation
 ↓
Useful Result
```

This repository is one of the first steps toward that way of thinking.

---

## 📈 Learning Progress

### Python Foundation

* [x] Variables & basic syntax
* [x] User input
* [x] Basic operators
* [x] Conditional logic
* [x] `for` loops
* [x] `range()`
* [x] Loop + conditions
* [x] Looping through lists
* [x] Basic filtering
* [x] Basic data processing

### Coming Next

The Python journey will gradually move toward concepts that are more directly useful for AI Engineering:

```text
Loops
  ↓
Collections
  ↓
Functions
  ↓
Data Structures
  ↓
Files / JSON
  ↓
NumPy
  ↓
Pandas
  ↓
Data Analysis
  ↓
Machine Learning
  ↓
AI
```

---

## 🎓 Learning Philosophy

This repository follows a simple approach:

> **Learn → Practice → Build → Explain**

I am not trying to become a professional Python developer through this series.

The objective is to learn **enough Python, deeply enough**, to confidently use it as a tool for:

* Data Science
* Machine Learning
* Artificial Intelligence
* Automation
* AI Engineering

---

## 👨‍💻 Author

**Faseeh Qamar**

Computer Science Student | AI Engineering Journey

GitHub: **[@Faseeh56](https://github.com/Faseeh56)**

---

⭐ This repository is part of my ongoing **AI Series learning journey**.
