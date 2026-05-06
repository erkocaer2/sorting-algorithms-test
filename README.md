\# Sorting Algorithms \& Automated Unit Testing



This repository contains basic sorting algorithms in Python. It also uses GitHub Actions for automatic unit testing.



\##  Project Structure



The project has these main files:



\*   \*\*`sorting\_algorithms.py`\*\*: The main module with basic sorting algorithms (like Bubble Sort).

\*   \*\*`main.py`\*\*: The driver code to run and test the algorithms manually in the terminal.

\*   \*\*`ds.py`\*\*: Contains basic data structures (like Stack) to use with algorithms.

\*   \*\*`tests/test\_sorting.py`\*\*: Contains unit tests using the `unittest` module. It checks if the algorithms give the correct results.



\##  Continuous Integration (CI) - GitHub Actions



This project uses \*\*GitHub Actions\*\* for a Continuous Integration (CI) process. This keeps the code correct and high quality.



Because of the workflow in the `.github/workflows/python-tests.yml` file, when you `push` or make a `pull\_request` to the `main` branch:

1\. It opens an Ubuntu virtual server.

2\. It sets up Python 3.10.

3\. It runs all unit tests in the `tests` folder automatically.



You can see the test results quickly in the "Actions" tab of the project.





