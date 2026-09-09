"""
==========================================================
PROVIDER REGISTRY
==========================================================

Maintains the registry of available AI provider adapters.
"""

from . import openai_provider

import os


OPENAI_MODEL = os.getenv(
    "OPENAI_MODEL",
    "gpt-4o",
).strip()




_PROVIDER_REGISTRY = {

    "openai": {
            "adapter": openai_provider,
            "enabled": True,
            "display_name": "OpenAI",
            "model": OPENAI_MODEL,
            "request_options": {
                "temperature": 0.7,
                "max_completion_tokens": 4000,
            },
        },
    
        "claude": {
        "adapter": None,
        "enabled": False,
        "display_name": "Anthropic Claude",
        "model": None,
        "request_options": {},
    },

    "gemini": {
        "adapter": None,
        "enabled": False,
        "display_name": "Google Gemini",
        "model": None,
        "request_options": {},
    },

    "grok": {
        "adapter": None,
        "enabled": False,
        "display_name": "xAI Grok",
        "model": None,
        "request_options": {},
    },

    "deepseek": {
        "adapter": None,
        "enabled": False,
        "display_name": "DeepSeek",
        "model": None,
        "request_options": {},
    },

    "local": {
        "adapter": None,
        "enabled": False,
        "display_name": "Local Model",
        "model": None,
        "request_options": {},
    },
}

def get_provider_adapter(provider_name: str):
    """
    Return the provider adapter for the requested provider.
    """

    provider = get_provider_metadata(
        provider_name
    )

    adapter = provider["adapter"]

    if adapter is None:

        raise RuntimeError(
            f"Provider '{provider_name}' has not yet "
            f"been implemented."
        )

    return adapter


def get_registered_providers():
    """
    Return a sorted list of registered providers.
    """

    return sorted(
        _PROVIDER_REGISTRY.keys()
    )


def get_enabled_providers():
    """
    Return enabled providers.
    """

    return sorted(
        provider_name
        for provider_name, provider
        in _PROVIDER_REGISTRY.items()
        if provider["enabled"]
    )


def get_disabled_providers():
    """
    Return disabled providers.
    """

    return sorted(
        provider_name
        for provider_name, provider
        in _PROVIDER_REGISTRY.items()
        if not provider["enabled"]
    )


def get_implemented_providers():
    """
    Return providers with implemented adapters.
    """

    return sorted(
        provider_name
        for provider_name, provider
        in _PROVIDER_REGISTRY.items()
        if provider["adapter"] is not None
    )


def get_unimplemented_providers():
    """
    Return providers awaiting implementation.
    """

    return sorted(
        provider_name
        for provider_name, provider
        in _PROVIDER_REGISTRY.items()
        if provider["adapter"] is None
    )


def provider_exists(
    provider_name: str,
):
    """
    Determine whether a provider exists.
    """

    return (
        provider_name.lower()
        in _PROVIDER_REGISTRY
    )


def get_provider_metadata(
    provider_name: str,
):
    """
    Return provider metadata.
    """

    provider_key = provider_name.lower()

    try:

        return dict(
            _PROVIDER_REGISTRY[
                provider_key
            ]
        )

    except KeyError as error:

        raise RuntimeError(
            f"No provider adapter registered for "
            f"'{provider_name}'."
        ) from error
# ==========================================================
# PROVIDER STATUS & CAPABILITY HELPERS
# ==========================================================

def is_provider_enabled(
    provider_name: str,
):
    """
    Return True if the provider is enabled.
    """

    return get_provider_metadata(
        provider_name
    )["enabled"]


def is_provider_implemented(
    provider_name: str,
):
    """
    Return True if the provider has an adapter.
    """

    return (
        get_provider_metadata(
            provider_name
        )["adapter"]
        is not None
    )


def get_provider_display_name(
    provider_name: str,
):
    """
    Return the human-readable provider name.
    """

    return get_provider_metadata(
        provider_name
    )["display_name"]


def provider_supports(
    provider_name: str,
    capability: str,
):
    """
    Return True if the provider supports
    the requested capability.
    """

    adapter = get_provider_adapter(
        provider_name
    )

    if hasattr(
        adapter,
        "supports",
    ):
        return adapter.supports(
            capability
        )

    return False


def get_provider_capabilities(
    provider_name: str,
):
    """
    Return the provider capability dictionary.
    """

    adapter = get_provider_adapter(
        provider_name
    )

    if hasattr(
        adapter,
        "get_capabilities",
    ):
        return adapter.get_capabilities()

    return {}


def get_provider_summary():
    """
    Return summary information for every
    registered provider.
    """

    summary = []

    for provider_name in get_registered_providers():

        metadata = get_provider_metadata(
            provider_name
        )

        summary.append(
            {
                "name": provider_name,
                "display_name": metadata[
                    "display_name"
                ],
                "enabled": metadata[
                    "enabled"
                ],
                "implemented": (
                    metadata["adapter"]
                    is not None
                ),
                "model": metadata.get(
                    "model"
                ),
                "capabilities": (
                    get_provider_capabilities(
                        provider_name
                    )
                    if metadata["adapter"]
                    is not None
                    else {}
                ),
            }
        )

    return summary


def get_provider_health():
    """
    Return diagnostic information for every
    registered provider.
    """

    health = {}

    for provider_name in get_registered_providers():

        metadata = get_provider_metadata(
            provider_name
        )

        implemented = (
            metadata["adapter"]
            is not None
        )

        enabled = metadata[
            "enabled"
        ]

        available = (
            enabled
            and implemented
        )

        if implemented:

            capabilities = (
                get_provider_capabilities(
                    provider_name
                )
            )

        else:

            capabilities = {}

        if available:

            status = "READY"

        elif implemented:

            status = "DISABLED"

        else:

            status = "NOT IMPLEMENTED"

        health[
            provider_name
        ] = {
            "display_name": metadata[
                "display_name"
            ],
            "enabled": enabled,
            "implemented": implemented,
            "available": available,
            "model": metadata.get(
                "model"
            ),
            "request_options": dict(
                metadata.get(
                    "request_options",
                    {},
                )
            ),
            "capabilities": capabilities,
            "status": status,

            #
            # Reserved diagnostics for future
            # monitoring.
            #
            "statistics": {
                "last_error": None,
                "last_success": None,
                "request_count": 0,
                "average_latency": None,
                "estimated_cost": 0.0,
            },
        }

    return health

def is_provider_available(
    provider_name: str,
):
    """
    Return True if a provider can
    currently be used.
    """

    metadata = get_provider_metadata(
        provider_name
    )

    return (
        metadata["enabled"]
        and metadata["adapter"]
        is not None
    )


def get_provider_configuration(
    provider_name: str,
):
    """
    Return the runtime configuration for
    a provider.
    """

    metadata = get_provider_metadata(
        provider_name
    )

    return {
        "name": provider_name.lower(),
        "display_name": metadata[
            "display_name"
        ],
        "enabled": metadata[
            "enabled"
        ],
        "implemented": (
            metadata["adapter"]
            is not None
        ),
        "available": (
            metadata["enabled"]
            and metadata["adapter"]
            is not None
        ),
        "model": metadata.get(
            "model"
        ),
        "request_options": dict(
            metadata.get(
                "request_options",
                {},
            )
        ),
    }