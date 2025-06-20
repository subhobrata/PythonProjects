"""Entry point demonstrating use of the asynchronous request context."""

import asyncio
from .context_manager import request_context
from .async_tasks import process_item

async def main():
    # Simulate handling a single request with id "req-42"
    async with request_context("req-42"):
        await asyncio.gather(
            process_item("task-1"),
            process_item("task-2"),
        )

if __name__ == "__main__":
    asyncio.run(main())
