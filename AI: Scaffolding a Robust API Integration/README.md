# AI: Scaffolding a Robust API Integration

## Task Overview

This task demonstrates the use of AI and Contextual Prompting to improve an existing Python sentiment-analysis tool. The objective was to refactor the `analyze_sentiment` function so that it securely handles API authentication and provides more comprehensive error handling.

## AI Tool Used

AI tool: ChatGPT

The Contextual Prompting technique was used by providing the AI with the complete original `sentiment_analyzer.py` code and then giving specific instructions for the required improvements.

## Initial Code

The file `sentiment_analyzer_initial.py` contains the original version of the sentiment-analysis program before AI-assisted refinement.

The original program sends a sentence to the Text Processing API and maps the API response labels to `positive`, `negative`, or `neutral`.

## Refactored Code

The file `sentiment_analyzer.py` contains the AI-refactored version of the program.

The main improvements include:

* Importing the `os` module.
* Reading the API key from the `TEXT_PROCESSING_API_KEY` environment variable.
* Using the standard `Authorization: Bearer <key>` format for authentication.
* Avoiding hard-coded API credentials.
* Adding specific handling for `requests.exceptions.Timeout`.
* Adding specific handling for `requests.exceptions.ConnectionError`.
* Providing distinct and informative error messages for timeout and connection failures.
* Preserving the existing HTTP error, request error, and invalid-response handling.
* Preserving the original sentiment-label mapping and command-line interface.

## Security

The API key is not stored directly in the Python source code. Instead, it is retrieved from the `TEXT_PROCESSING_API_KEY` environment variable. This is a safer approach because credentials can be supplied separately from the application code and can be changed without modifying the source file.

## Error Handling

The refined implementation handles timeout and connection errors separately. A timeout produces a message indicating that the API request timed out, while a connection error indicates that the API could not be reached. More general request and HTTP errors are also retained.

## Contextual Prompting

Contextual Prompting was important because the AI was given the complete existing application before being asked to modify it. This allowed the AI to understand the existing API request, response processing, sentiment mapping, error handling, and command-line interface.

The detailed instructions ensured that the requested security and robustness improvements were incorporated without unnecessarily changing the application's existing behavior.

## Files

* `sentiment_analyzer_initial.py` — Original code before AI refinement.
* `sentiment_analyzer.py` — Refactored code generated with AI assistance.
* `README.md` — Documentation explaining the task, AI tool, code changes, security improvements, and error handling.

## Conclusion

The task demonstrates how Contextual Prompting can be used as part of a software development workflow to guide an AI toward producing code that satisfies specific functional, security, and robustness requirements.
