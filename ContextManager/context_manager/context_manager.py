"""Asynchronous context manager using contextvars."""

import contextvars
from contextlib import asynccontextmanager

# Context variable to store a request id
request_id_var = contextvars.ContextVar('request_id', default=None)

@asynccontextmanager
async def request_context(request_id: str):
    """Context manager that sets the current request id.

    Args:
        request_id: Unique identifier for the current request.
    """
    token = request_id_var.set(request_id)
    try:
        yield
    finally:
        request_id_var.reset(token)
