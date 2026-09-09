"""
==========================================================
AI ROUTER
==========================================================

Central location for every AI request made by the platform.

Current Provider:
    - OpenAI

Future Providers:
    - Anthropic Claude
    - Google Gemini
    - Grok
    - DeepSeek
    - Local Models

Nothing outside this file should know which provider
is currently being used.
"""

import os
import time

from providers import get_provider_adapter
# ---------------------------------------------------------
# CONFIGURATION
# ---------------------------------------------------------

DEFAULT_PROVIDER = (
    os.getenv(
        "DEFAULT_PROVIDER",
        "openai",
    )
    .strip()
    .lower()
)
# ---------------------------------------------------------
# REQUEST LOGGING
# ---------------------------------------------------------

_REQUEST_LOG = []

_ROUTER_USAGE = {
    "requests": 0,
    "successful_requests": 0,
    "failed_requests": 0,
    "prompt_tokens": 0,
    "completion_tokens": 0,
    "total_tokens": 0,
}


def get_request_log():
    """
    Return a copy of the current request log.
    """

    return list(_REQUEST_LOG)


def clear_request_log():
    """
    Clear the request log and usage counters.
    """

    _REQUEST_LOG.clear()

    for key in _ROUTER_USAGE:
        _ROUTER_USAGE[key] = 0


def get_router_usage():
    """
    Return router usage statistics.
    """

    usage = dict(_ROUTER_USAGE)

    usage.setdefault(
        "estimated_cost",
        0.0,
    )

    return usage


def reset_router_usage():
    """
    Reset router usage counters.
    """

    for key in _ROUTER_USAGE:

        if isinstance(
            _ROUTER_USAGE[key],
            float,
        ):
            _ROUTER_USAGE[key] = 0.0

        else:
            _ROUTER_USAGE[key] = 0

def log_request(
    provider,
    model,
    duration_seconds,
    success,
    error=None,
    prompt_tokens=0,
    completion_tokens=0,
    estimated_cost=0.0,
):
    """
    Record metadata for a completed AI request.
    """

    total_tokens = (
        prompt_tokens
        + completion_tokens
    )

    _REQUEST_LOG.append(
        {
            "timestamp": time.time(),
            "provider": provider,
            "model": model,
            "duration_seconds": round(
                duration_seconds,
                3,
            ),
            "success": success,
            "error": error,
            "prompt_tokens": prompt_tokens,
            "completion_tokens": completion_tokens,
            "total_tokens": total_tokens,
            "estimated_cost": estimated_cost,
        }
    )

    _ROUTER_USAGE["requests"] += 1

    if success:
        _ROUTER_USAGE[
            "successful_requests"
        ] += 1
    else:
        _ROUTER_USAGE[
            "failed_requests"
        ] += 1

    _ROUTER_USAGE[
        "prompt_tokens"
    ] += prompt_tokens

    _ROUTER_USAGE[
        "completion_tokens"
    ] += completion_tokens

    _ROUTER_USAGE[
        "total_tokens"
    ] += total_tokens

    _ROUTER_USAGE.setdefault(
        "estimated_cost",
        0.0,
    )

    _ROUTER_USAGE[
        "estimated_cost"
    ] += estimated_cost
def get_router_statistics():
    """
    Return router statistics.
    """

    total_requests = (
        _ROUTER_USAGE["requests"]
    )

    successful_requests = (
        _ROUTER_USAGE[
            "successful_requests"
        ]
    )

    failed_requests = (
        _ROUTER_USAGE[
            "failed_requests"
        ]
    )

    if total_requests:

        success_rate = round(
            (
                successful_requests
                / total_requests
            )
            * 100,
            1,
        )

    else:

        success_rate = 100.0

    return {
        **dict(_ROUTER_USAGE),
        "success_rate": success_rate,
    }
# ---------------------------------------------------------
# PROVIDER MANAGEMENT
# ---------------------------------------------------------

from providers import (
    get_provider_adapter,
    get_provider_metadata,
    get_registered_providers,
    is_provider_enabled,
    provider_supports,
)


_current_provider = DEFAULT_PROVIDER


def get_current_provider():
    """
    Return the currently selected provider.
    """

    return _current_provider


def set_current_provider(
    provider_name,
):
    """
    Select the active provider.
    """

    global _current_provider

    provider_name = (
        provider_name.strip()
        .lower()
    )

    if provider_name not in (
        get_registered_providers()
    ):
        raise RuntimeError(
            f"Unknown provider "
            f"'{provider_name}'."
        )

    if not is_provider_enabled(
        provider_name
    ):
        raise RuntimeError(
            f"Provider '{provider_name}' "
            "is disabled."
        )

    _current_provider = provider_name


def get_active_provider():
    """
    Return metadata for the current provider.
    """

    return get_provider_metadata(
        _current_provider
    )


def validate_provider():
    """
    Validate the current provider.
    """

    provider = get_active_provider()

    if not is_provider_enabled(
        _current_provider
    ):
        raise RuntimeError(
            f"Provider "
            f"'{_current_provider}' "
            "is currently disabled."
        )

    return provider


def get_provider_info():
    """
    Return information about the
    active provider.
    """

    provider = get_active_provider()

    return {
        "name": _current_provider,
        "display_name": provider[
            "display_name"
        ],
        "model": provider.get(
            "model"
        ),
        "enabled": provider[
            "enabled"
        ],
    }


def get_request_options():
    """
    Return request options for the
    active provider.
    """

    provider = get_active_provider()

    return dict(
        provider.get(
            "request_options",
            {},
        )
    )
# ---------------------------------------------------------
# MAIN GENERATE FUNCTION
# ---------------------------------------------------------

def generate(
    messages,
    temperature=None,
    max_tokens=None,
):
    """
    Central AI generation entry point.

    Every text-generation request for the Novelist passes
    through this function.
    """

    provider = validate_provider()

    if not provider_supports(
        DEFAULT_PROVIDER,
        "chat",
    ):
        raise RuntimeError(
            f"Provider '{DEFAULT_PROVIDER}' "
            "does not support chat generation."
        )

    adapter = get_provider_adapter(
        DEFAULT_PROVIDER
    )

    request_options = get_request_options()

    if (
        temperature is not None
        and "temperature"
        in request_options
    ):
        request_options["temperature"] = (
            temperature
        )

    if max_tokens is not None:
        request_options[
            "max_completion_tokens"
        ] = max_tokens

    try:

        result = adapter.generate(
            model=provider["model"],
            messages=messages,
            request_options=request_options,
        )

        log_request(
            provider=DEFAULT_PROVIDER,
            model=provider["model"],
            duration_seconds=result["duration"],
            success=True,
        )

        return result["content"]

    except Exception as error:

        log_request(
            provider=DEFAULT_PROVIDER,
            model=provider["model"],
            duration_seconds=0,
            success=False,
            error=str(error),
        )

        raise RuntimeError(
            f"AI Router Error: {error}"
        ) from error
# ---------------------------------------------------------
# PLACEHOLDERS
# ---------------------------------------------------------

def stream(*args, **kwargs):
    raise NotImplementedError


def embedding(*args, **kwargs):
    raise NotImplementedError


def image(*args, **kwargs):
    raise NotImplementedError


def get_router_status():
    """
    Return the complete router status.
    """

    return {
        "provider": get_provider_info(),
        "statistics": get_router_statistics(),
        "usage": get_router_usage(),
    }


def health_check():
    """
    Backwards-compatible router health check.
    """

    status = get_router_status()

    return {
        "provider": status[
            "provider"
        ]["name"],
        "display_name": status[
            "provider"
        ]["display_name"],
        "model": status[
            "provider"
        ]["model"],
        "enabled": status[
            "provider"
        ]["enabled"],
        "supported_providers": (
            get_registered_providers()
        ),
        "statistics": status[
            "statistics"
        ],
        "usage": status[
            "usage"
        ],
    }