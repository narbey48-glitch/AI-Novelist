"""
==========================================================
OPENAI PROVIDER
==========================================================

Handles all communication with the OpenAI API.

The AI Router should never make OpenAI API calls directly.
"""

import time

from openai import OpenAI


_client = None


CAPABILITIES = {

    "chat": True,

    "stream": False,

    "embeddings": False,

    "images": False,

    "audio": False,

    "structured_output": True,

    "tool_calling": True,

    "vision": True,
}


def get_capabilities():
    """
    Return the capabilities supported by this provider.
    """

    return dict(CAPABILITIES)


def supports(
    capability: str,
):
    """
    Determine whether this provider supports
    a requested capability.
    """

    return CAPABILITIES.get(
        capability,
        False,
    )


def get_client():
    """
    Lazily create a single OpenAI client instance.
    """

    global _client

    if _client is None:
        _client = OpenAI()

    return _client


def generate(
    *,
    model,
    messages,
    request_options,
):
    """
    Generate a chat completion using OpenAI.
    """

    client = get_client()

    #
    # Work on a copy so we never modify the
    # caller's dictionary.
    #
    options = dict(request_options)

    #
    # GPT-4o currently ignores/rejects custom
    # temperature values through this API.
    #
    options.pop(
        "temperature",
        None,
    )

    start_time = time.perf_counter()

    response = client.chat.completions.create(
        model=model,
        messages=messages,
        **options,
    )

    duration = (
        time.perf_counter()
        - start_time
    )

    return {
        "content": (
            response.choices[0]
            .message.content
        ),
        "duration": duration,
    }
def client_initialized():
    """
    Returns True once the OpenAI client
    has been created.
    """

    return _client is not None