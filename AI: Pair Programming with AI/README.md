# Task Queue AI Pair Programming Audit

## Overview
This repository contains the legacy implementation and refactored code for a JavaScript `TaskQueue` class, audited with AI assistance for Single Responsibility Principle (SRP) violations and scope/closure traps.

---

## 1. Prompts Used

### Prompt 1: Scope & Closures Audit
```text
Act as a Senior JavaScript Developer. I am reviewing a legacy task queue implementation in JavaScript.

Code:
class TaskQueue {
  constructor(name) {
    this.queueName = name;
    this.tasks = [];
    this.isProcessing = false;
  }

  addTask(taskFn, priority) {
    if (!taskFn || typeof taskFn !== 'function') {
      console.error('Task must be a function.');
      return;
    }
    this.tasks.push({ taskFn, priority, timestamp: Date.now() });

    if (this.tasks.length === 1) {
      console.log(`Starting queue ${this.queueName}.`);
      this._startProcessing();
    }

    function notify() { 
      if (priority > 9) {
        console.warn(`High priority task added to ${name}.`);
      }
    }
    notify(); 
  }

  _startProcessing() {
    this.isProcessing = true;
  }
}

Please analyze the addTask method:
1. Explain the scope of the notify function and what variables it "closes over."
2. Identify any variables that should be block-scoped (using let or const) but are not, and why this matters for predictable code.
3. Explain how closures are created in this specific context and why referencing 'name' instead of 'this.queueName' causes issues.
