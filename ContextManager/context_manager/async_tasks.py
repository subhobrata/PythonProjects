"""Example asynchronous tasks that use the request context."""

import asyncio
from .context_manager import request_id_var

async def process_item(name: str, delay: float = 0.1) -> None:
    """Simulate processing that relies on the request id from context."""
    await asyncio.sleep(delay)
    request_id = request_id_var.get()
    print(f"{name}: request_id={request_id}")
