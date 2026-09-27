/**
 * Handles queue-related notifications and warnings.
 * Responsibility: Console logging and alerting.
 */
class QueueLogger {
  static logQueueStart(queueName) {
    console.log(`Starting queue ${queueName}.`);
  }

  static logHighPriorityWarning(queueName, priority) {
    if (priority > 9) {
      console.warn(`High priority task added to ${queueName}.`);
    }
  }
}

/**
 * Manages queue storage and task processing status.
 * Responsibility: Pure task queuing and execution triggers.
 */
class TaskQueue {
  constructor(name, logger = QueueLogger) {
    this.queueName = name;
    this.tasks = [];
    this.isProcessing = false;
    this.logger = logger;
  }

  /**
   * Adds a new task function to the queue.
   * @param {Function} taskFn - The task execution function
   * @param {number} priority - Task priority level
   */
  addTask(taskFn, priority) {
    if (typeof taskFn !== 'function') {
      throw new TypeError('Task must be a function.');
    }

    // 1. Add task to array
    const task = { taskFn, priority, timestamp: Date.now() };
    this.tasks.push(task);

    // 2. Delegate notification to external logger
    this.logger.logHighPriorityWarning(this.queueName, priority);

    // 3. Delegate start logic
    if (this.shouldStartProcessing()) {
      this.logger.logQueueStart(this.queueName);
      this._startProcessing();
    }
  }

  shouldStartProcessing() {
    return this.tasks.length === 1 && !this.isProcessing;
  }

  _startProcessing() {
    this.isProcessing = true;
  }
}

module.exports = { TaskQueue, QueueLogger };
