# AI: Pair Programming with AI

## Overview

This task demonstrates the use of AI-assisted code analysis and refactoring to identify and address structural problems in a JavaScript class.

The exercise focuses on the Single Responsibility Principle (SRP), scope and closures, and improving code modularity and maintainability through structured prompting.

## Files

### 1. task_queue_legacy.js

This file contains the original TaskQueue implementation provided for the exercise. It intentionally contains SRP violations and scope/closure issues for analysis.

### 2. task_queue_clean.js

This file contains the refactored TaskQueue implementation after applying the AI-assisted analysis and refactoring process.

The refactoring separates task management from logging and scheduling responsibilities and addresses the scope/closure concerns identified during the audit.

## AI Tool Used

Gemini was used as an AI pair programmer to:

- Audit the legacy JavaScript code for scope and closure behavior.
- Identify Single Responsibility Principle violations.
- Suggest a refactored implementation.
- Review the final implementation for correctness.

## Learning Focus

The task focuses on using structured prompting to understand code structure rather than simply asking AI to fix code. It demonstrates how AI pattern matching can help identify structural problems such as SRP violations, scope issues, and closure behavior.

## Reflection

LLMs are pattern-matching engines rather than code executors, so their usefulness depends on asking focused questions about the structure and behavior of code. In this exercise, auditing the `notify` closure and the SRP violations helped me understand why the original `addTask` method mixed responsibilities, instead of simply accepting an AI-generated fix without understanding the underlying problems.
