# SQL vs Pandas Benchmarking

## Introduction

In this assignment, you will benchmark some common data queries using both SQL and Pandas using a TDD approach.


**For each question, create a git *tag* that labels the commit which represents your solution. Use the format 1.x where x is the question number.**


1. Examine the provided test and SQL query `get_adults` that filters your generated dataset to include people who are 18 or older. Refactor the query to use Pandas instead.

2. Now, examine the function and test for `avg_age_per_state` that calculates the mean age of people for each state. Refactor the query to use SQL instead.

3. Write a test for a function `large_states_adult_age` that calculates the mean age of adults in states with over 5 million people. Write the test such that this function takes the output from the previous two functions as parameters.

4. First, implement this function in Pandas, performing the filter _after_ the join.

5. Refactor the function to perform the filter _before_ the join.

6. Finally, refactor the function to use SQL for the entire query. More specifically, you will not use the implementations you wrote for problems 1 and 2.

## Data Generation & benchmarking

We will use the [Faker](https://faker.readthedocs.io/en/master/) library to generate fake data for our benchmarking. Faker is a Python library that generates fake data for a variety of data types, including names, addresses, phone numbers, and more. It is useful for generating fake data for testing and benchmarking purposes.

7. Write a test for a function `generate_people` that generates _n_ fake records for a "Person" table. This function should include columns for first name, last name, age, US State, and a random sentence.

8. Implement this function using the _faker_ library.

9. Write a test for a function `query_profile` that uses `generate_people` to profile the query performance as a function of n.

10. Implement this function and observe the results from the `benchmark` function.
