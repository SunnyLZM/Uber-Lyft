# SQL & Pandas

## Introduction

In this assignment, you will benchmark some common data queries using both SQL and Pandas using a TDD approach.


**For the autograder, you must create a git *tag* for each question that labels the commit which represents your solution. For the tag name, use the format 1.x.y where x is the question number and y is the attempt number. The auto grader will choose the highest grade from the tags that match this format**

!!! info "Grading your unit tests"

    Some of the questions in this assignment ask you to write unit tests. Since "testing the test" would be complicated, here is how we will grade these questions:

    1. You will receive full credit for your **function implementation** if it passes the test you wrote, no matter how complete or incomplete the test is, as long as you write the test first. If you have done one cycle of red-green-refactor, you may continue with more cycles until your test covers all the desired behavior of the function.
    2. Your function will then be tested against a different battery of tests that is not provided to you. Your grade for the tests you write will be determined by how many of these secret tests you pass. **You may only submit code in a passing 🟢 state once per cycle.** Then, the autograder must receive another 🔴 commit before you may continue. If you receive the same test failure twice in a row from the autograder, or if you fail more test cases than in your previous submission (this is called a *regression*), the autograder will be turned off until the submission deadline for that question. Thus, you still may receive full credit after the deadline but will not have the benefit of the autograder's feedback.

🟢 and 🔴 circles indicate the status of the checks you need for credit for each question.

Each question is worth 10 points each.

## Basic Unit Tests and Queries

1. Examine the provided test in `tests/test_hw1.py` and its Pandas implementation `filter_after_cutoff_age` that filters your generated dataset to include people who are 18 or older. Refactor the query to use SQL instead.🟢

2. Now, examine the SQL query and test for `avg_age_per_state` that calculates the mean age of people for each state. Refactor the query to use Pandas instead.🟢

3. Write a test for a function `large_states_adult_age` which will use the data in `data/state_populations.csv` to calculate the mean age of adults you generate in states with over 5 million people. 🔴

4. First, implement this function in Pandas, performing the filter *after* the join.🟢

5. Refactor the function to perform the filter *before* the join.🟢

6. Finally, refactor the function to use SQL for the entire query. In other words, do not use any of the previous implementations for this step.🟢

## Data Generation & Benchmarking

We will use the [Faker](https://faker.readthedocs.io/en/master/) library to generate fake data for our benchmarking. Faker is a Python library that generates fake data for a variety of data types, including names, addresses, phone numbers, and more. It is useful for generating fake data for testing and benchmarking purposes.

7. (#7) Write a test for a function `generate_people` that generates *n* fake records for a "Person" table. This function should include columns for first name, last name, age, US State, and a random sentence.🔴

8. (# 8) Implement this function using the [*faker* library](https://faker.readthedocs.io/en/master/).🟢

~~9. Write a test for a function `query_runtime` that uses `generate_people` to profile the query performance runtime of your functions as a function of n. The output of `query_runtime`should fit the data schema for the input of the provided `benchmark` function 🔴.~~

~~10. Implement this function and observe the results from the provided `benchmark` function.~~
