# 0. AI: SQL to ORM Refactoring and Security Analysis

## Objective

This task demonstrates the use of an AI assistant to refactor procedural Python database code using MySQL Connector and raw SQL into a modern, object-oriented solution using SQLAlchemy ORM.

The task also analyzes the security, abstraction, professionalism, and maintainability benefits of using an ORM.

## Files

### `initial_code.py`

Contains the original procedural Python example using `mysql.connector` and a parameterized SQL `INSERT` statement.

### `orm_refactored.py`

Contains the refactored SQLAlchemy ORM implementation. It defines a declarative `User` model and demonstrates:

- Database engine configuration
- ORM table creation
- Creating a user
- Querying a user
- Updating a user
- Deleting a user
- Listing users
- Transaction handling
- Error handling
- Environment-based database configuration

## AI-Assisted Refactoring

The AI assistant was instructed to convert the procedural database operations into SQLAlchemy ORM code and provide a detailed security and professional analysis.

The prompt specifically required the AI to define the `User` declarative model, create the database table, add and query users through an ORM Session, demonstrate CRUD operations, explain parameter binding and SQL injection protection, and discuss abstraction and maintainability.

## Security Analysis

The original example already uses parameterized SQL, which helps protect against SQL injection because user-supplied values are passed separately from the SQL statement.

The SQLAlchemy ORM provides a higher-level abstraction in which application code works with Python objects and ORM expressions rather than manually constructing SQL strings. SQLAlchemy also uses bound parameters when generating SQL, reducing the need for unsafe string concatenation.

The refactored solution additionally improves credential management by obtaining the database connection string from an environment variable instead of requiring a real password to be stored directly in source code.

SQLAlchemy transaction handling also provides a structured way to commit successful operations and roll back failed operations, helping maintain database consistency.

## Abstraction and Maintainability

ORM reduces the amount of repetitive SQL that developers must write and maintain. Instead of manually constructing SQL statements for every operation, developers work with the `User` Python class and its attributes. This makes the application code easier to understand and keeps database-related behavior organized around meaningful objects.

As a project grows, this object-centric structure makes changes easier to manage. For example, adding a field to the `User` model provides a clear central representation of that field in application code. ORM expressions are also less error-prone than repeatedly writing SQL strings because table and column references are represented directly through Python model attributes.

## AI Tool

ChatGPT was used as the AI assistant for the SQL-to-ORM refactoring and security analysis.

## Educational Purpose

This repository folder is part of an academic exercise demonstrating responsible use of AI-assisted software engineering techniques.
