/**
 * task_queue_clean.js
 * Refactored TaskQueue with separated responsibilities.
 */

class NotificationService {
  static notifyIfHighPriority(queueName, priority) {
    if (priority > 9) {
      console.warn(`High priority task added to ${queueName}.`);
    }
  }
}

class QueueProcessor {
  static checkAndStart(queue) {
    if (queue.tasks.length === 1 && !queue.isProcessing) {
      console.log(`Starting queue ${queue.queueName}.`);
      queue._startProcessing();
    }
  }
}

class TaskQueue {
  constructor(name) {
    this.queueName = name;
    this.tasks = [];
    this.isProcessing = false;
  }

  addTask(taskFn, priority) {
    if (!taskFn || typeof taskFn !== 'function') {
      console.error('Task must be a function.');
      return null;
    }

    const task = {
      taskFn,
      priority,
      timestamp: Date.now()
    };

    this.tasks.push(task);
    return task;
  }

  _startProcessing() {
    this.isProcessing = true;
    // ... logic to process tasks ...
  }
}

class TaskQueueManager {
  constructor(queueName) {
    this.queue = new TaskQueue(queueName);
  }

  addTask(taskFn, priority) {
    const task = this.queue.addTask(taskFn, priority);

    if (task) {
      NotificationService.notifyIfHighPriority(
        this.queue.queueName,
        priority
      );
      QueueProcessor.checkAndStart(this.queue);
    }

    return task;
  }
}

module.exports = {
  TaskQueue,
  TaskQueueManager,
  NotificationService,
  QueueProcessor
};
