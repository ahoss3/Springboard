# Spring Board Mini Project 1

This project simulates a Banking System with Python.

## Data Model
### Bank
* Each bank is associated with a unique id
### Customers
* Customer is one of core entities in the banking system. 
* Each Customer entity represents a customer of a given bank.
### Employees
* Employee represents an employee tied to a certain bank with personal information.
### Bank Accounts
* `Accounts` represents an abstract bank account. One account could be saving, checking, credit card, or loan, each with additional functionality
* `Accounts` are tied to banks and customers via bank_id and cust_id, respectively