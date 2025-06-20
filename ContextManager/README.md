# ContextManager Example

This example demonstrates how to use Python's `contextvars` module together with
an asynchronous context manager to manage request-scoped data. The pattern is
useful in real-world, production-grade applications that handle concurrent tasks.

## Running the example

Execute the `main.py` script:

```bash
python -m context_manager.main
```

You should see output similar to:

```
task-1: request_id=req-42
task-2: request_id=req-42
```

All concurrent tasks share the same request identifier via the context manager.
