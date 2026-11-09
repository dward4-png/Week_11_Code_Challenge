# CIS 105 - Dictionaries and Data Structures: Quiz and Code Challenge

## Make This Repo Yours

1. Click the **Fork** button at the top right of this page. This creates your own copy of the repository under your GitHub account.
2. In your fork, click on `README.md`, then click the pencil icon to edit it.
3. Fill in your information below and answer every quiz question in this file, right where it says **Your answer:**.
4. Commit your changes (the green **Commit changes** button at the bottom of the edit page).
5. Complete the code challenge in the file `gradebook_challenge.py` in this same repository. You can edit it in the browser or download it and work in your usual editor, then upload the finished file.
6. When everything is done, copy the web address (URL) of your forked repository and submit that link on Moodle.

Name: Dylan Ward
Section: CIS 105-01
Date: 11/9/26

---

## Part 1: Quiz (50 points, 5 points each)

Answer each question in your own words or with the exact output, as asked. Write your answer on the line under each question.

**1.** A dictionary stores data as key-value pairs. Write one line of Python that creates a dictionary named `student` with the keys `"name"` and `"major"` and values of your choosing.

Your answer: student = {"name:", "Dylan", "major:", "Cybersecurity"

**2.** What is the output of this code?

```python
grades = {"quiz1": 85, "quiz2": 92, "quiz3": 78}
print(grades["quiz2"])
```

Your answer: 92 

**3.** What is the difference between `grades["quiz4"]` and `grades.get("quiz4")` when the key `"quiz4"` does not exist in the dictionary?

Your answer: grades{"quiz4"] gives an error because the key doesnt exist.  grades.get("quiz4") returns with none which is also a error.

**4.** Write the line of code that adds a new key `"quiz4"` with the value 88 to the `grades` dictionary above. Then write the line that changes `"quiz1"` to 90.

Your answer: grades["quiz4"] = 88
            grades["quiz5"] = 90

**5.** What do the dictionary methods `.keys()`, `.values()`, and `.items()` each return?

Your answer: returns all keys, returns all values, and returns keys and values together

**6.** In one or two sentences each, explain the main difference between a list, a tuple, and a set. When would you choose each one?

Your answer: A list is ordered and can be changed. A tuple is ordered but cannot be changed. A set stores unique values and does not allow duplicates. I would use a list for items I need to change, a tuple for information that stays the same, and a set when I want to avoid duplicates.

**7.** True or false, and explain why: in Python, the expression `"quiz1" in grades` checks whether `"quiz1"` is one of the values in the dictionary.

Your answer: False this checks if quiz1 is a key in the directory not a value

**8.** What is the output of this code?

```python
student = {"name": "Alex", "courses": {"current": "CIS 105", "credits": 3}}
print(student["courses"]["current"])
```

Your answer: CIS 105

**9.** Name two different ways to remove the key `"quiz3"` from the `grades` dictionary. What is one difference between them?

Your answer: del grades["quiz3"]

**10.** What does `len(grades)` return for the dictionary in Question 2, and what exactly is it counting?

Your answer: grades.pop("quiz3")

---

## Part 2: Code Challenge (50 points)

Open `gradebook_challenge.py` in this repository. You will build a small grade book program that stores student names as dictionary keys and each student's list of test scores as the value.

The file contains starter code with five functions to complete where you see `# TODO`:

1. `add_student(book, name)` - adds a new student with an empty score list. If the student is already in the grade book, print a message saying so and change nothing.
2. `add_grade(book, name, grade)` - adds a score to a student's list. If the student is not in the grade book yet, add the student first, then the score.
3. `student_average(book, name)` - returns the average of a student's scores. Use `.get()` so the function returns `None` instead of crashing if the student is not found.
4. `top_student(book)` - returns the name of the student with the highest average score.
5. `print_report(book)` - prints every student, their scores, and their average, one student per line, using a loop over `.items()`.

The bottom of the file has test code that is already written for you. Do not change the test code. When your functions are correct, running the file produces exactly this output:

```
Alex: [90, 85, 95] Average: 90.0
Jordan: [70, 80] Average: 75.0
Taylor: [100, 95, 90, 85] Average: 92.5
Top student: Taylor
```

### Rules

- Work only inside the five TODO functions. Do not change the test code at the bottom of the file.
- Use a dictionary as the main data structure. Solutions that store the grade book as separate variables will not receive credit.
- Your code must run with no errors from start to finish.

### How You Are Graded

- Quiz answers complete and correct: 50 points
- Each challenge function working correctly: 8 points each (40 points)
- Code runs cleanly and matches the expected output: 10 points

### Submitting

Submit the URL of your forked repository on Moodle. Make sure your repository is public, or I cannot see it to grade it.
