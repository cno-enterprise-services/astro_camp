# Lesson 0: Introduction to Python for Complete Beginners
A beginner-friendly **Lesson 0** to help complete beginners get up to speed with Python before diving into further lessons.

Welcome to Lesson 0! If you're new to Python, this lesson will introduce you to the basics of Python programming. By the end of this lesson, you'll have the foundational knowledge needed to start building a game with Pygame.

---

## Learning Objectives
- Understand what Python is and how to run Python code
- Learn basic Python syntax and concepts
- Write your first Python program
- Understand variables, data types, loops, and functions

---

## Step 1: Installing Python

### What is Python?
Python is a beginner-friendly programming language that's widely used for web development, data analysis, artificial intelligence, and game development.

### Install Python
1. Go to the [Python website](https://www.python.org/).
2. Download the latest version of Python for your operating system.
3. During installation:
   - Check the box that says **"Add Python to PATH"**.
   - Complete the installation.

To verify the installation, open your terminal or command prompt and type:
```
python --version
```
You should see the installed version of Python.

> You may have to type ```python3``` instead of ```python``` on some systems.

---

## Step 2: Writing Your First Program

### Using an IDE or Text Editor
You can write Python code in any text editor (e.g., VS Code, PyCharm) or use an online editor like [Replit](https://replit.com/).

### Your First Program
Create a new file called `lesson0.py` and write the following code:

```
print("Hello, Mars!")
```

Run the program by typing:
```
python lesson0.py
```

You should see:
```
Hello, Mars!
```

---

## Step 3: Understanding Variables and Data Types

### Variables
Variables store information that your program can use later.

Example:
```
name = "Mars Rover"
speed = 10
print("The", name, "moves at", speed, "km/h.")
```

Output:
```
The Mars Rover moves at 10 km/h.
```

### Data Types
Python has several data types:
- **Strings**: Text (e.g., `"Hello"`)
- **Integers**: Whole numbers (e.g., `10`)
- **Floats**: Decimal numbers (e.g., `3.14`)
- **Booleans**: True/False values (e.g., `True`)

---

## Step 4: Using Loops

Loops allow you to repeat actions multiple times.

### For Loop Example:
```
for i in range(5):
    print("Step", i)
```

Output:
```
Step 0
Step 1
Step 2
Step 3
Step 4
```

### While Loop Example:
```
count = 0
while count < 5:
    print("Count is", count)
    count += 1
```

Output:
```
Count is 0
Count is 1
Count is 2
Count is 3
Count is 4
```

---

## Step 5: Writing Functions

Functions are reusable blocks of code that perform specific tasks.

Example:
```
def greet(name):
    print("Hello,", name)

greet("Mars Rover")
greet("Martian")
```

Output:
```
Hello, Mars Rover
Hello, Martian
```

---

## Step 6: Importing Libraries

Python has many libraries that add extra functionality. For example:

```
import math

print(math.sqrt(16))  # Prints the square root of 16
print(math.pi)        # Prints the value of pi
```

Output:
```
4.0
3.141592653589793
```

Pygame is also a library that you'll import in future lessons.

---

## Challenges for Lesson 0

1. **Print Your Own Message**  
   Modify the `print` statement to display your own custom message.

2. **Create a Simple Calculator**  
   Write a program that adds two numbers together.
   ```
   num1 = int(input("Enter first number: "))
   num2 = int(input("Enter second number: "))
   print("The sum is:", num1 + num2)
   ```

3. **Write a Loop**  
   Write a loop that prints numbers from `1` to `10`.

4. **Write a Function**  
   Create a function called `square` that takes a number as input and returns its square.

---

## Summary of Lesson 0

In this lesson, you learned:
1. How to install and run Python.
2. Basic syntax like `print`, variables, loops, and functions.
3. How to import libraries for additional functionality.

Now that you're familiar with Python basics, you're ready to move on to **Lesson 1**, where you'll create your first game window using Pygame!
