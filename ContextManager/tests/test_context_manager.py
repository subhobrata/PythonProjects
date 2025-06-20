import sys
import asyncio
import pytest

sys.path.append('ContextManager')
from context_manager import request_context, request_id_var
from context_manager.async_tasks import process_item

@pytest.mark.asyncio
async def test_request_context_sets_variable(capsys):
    assert request_id_var.get() is None
    async with request_context('test-1'):
        await process_item('unit')
        assert request_id_var.get() == 'test-1'
    assert request_id_var.get() is None
