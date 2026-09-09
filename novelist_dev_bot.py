# ============================================================
# NOVELIST DEVELOPMENT BOT
# Dependency-Aware Read-Only Development Model
# ============================================================

import ast
import os
import re
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI


# ============================================================
# ENVIRONMENT
# ============================================================

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL = os.getenv("OPENAI_MODEL")

if not OPENAI_API_KEY:
    raise RuntimeError(
        "OPENAI_API_KEY was not found in the .env file."
    )

if not OPENAI_MODEL:
    raise RuntimeError(
        "OPENAI_MODEL was not found in the .env file."
    )


# ============================================================
# PROJECT LOCATION
# ============================================================

PROJECT_ROOT = Path(__file__).resolve().parent


# ============================================================
# OPENAI CLIENT
# ============================================================

client = OpenAI(api_key=OPENAI_API_KEY)


# ============================================================
# DEVELOPMENT BOT IDENTITY
# ============================================================

PROJECT_IDENTITY = {

    "project_name": "AI Novelist",

    "project_version": "0.30.0",

    "current_task": 31,

    "current_subtask": "31A",

    "current_milestone": (
        "Development Bot Intelligence Layer"
    ),

    "architecture_phase": (
        "Foundation Complete"
    ),

    "router_version": (
        "Router v1"
    ),
}


def get_project_identity():
    """
    Return the current project identity.
    """

    return dict(
        PROJECT_IDENTITY
    )


def get_project_version():
    """
    Return the current project version.
    """

    return PROJECT_IDENTITY[
        "project_version"
    ]


def get_current_task():
    """
    Return the active task.
    """

    return (
        PROJECT_IDENTITY[
            "current_task"
        ],
        PROJECT_IDENTITY[
            "current_subtask"
        ],
    )


def get_current_milestone():
    """
    Return the current milestone.
    """

    return PROJECT_IDENTITY[
        "current_milestone"
    ]


DEVELOPMENT_BOT_CAPABILITIES = {

    "project_analysis": True,

    "project_structure": True,

    "project_index": True,

    "target_discovery": True,

    "dependency_analysis": True,

    "reverse_dependency_analysis": True,

    "safe_file_reading": True,

    "implementation": False,

    "automatic_file_modification": False,

    "automatic_project_changes": False,
}


def get_bot_capabilities():
    """
    Return Development Bot capabilities.
    """

    return dict(
        DEVELOPMENT_BOT_CAPABILITIES
    )


def can_perform(
    capability: str,
):
    """
    Return True if the Development Bot
    supports the requested capability.
    """

    return (
        DEVELOPMENT_BOT_CAPABILITIES.get(
            capability,
            False,
        )
    )


DEVELOPMENT_BOT_STATE = {

    "mode": "READ_ONLY",

    "implementation_enabled": False,

    "automatic_changes": False,

    "testing_enabled": False,

    "approval_required": True,
}


def get_bot_state():
    """
    Return the current Development Bot state.
    """

    return dict(
        DEVELOPMENT_BOT_STATE
    )


def get_current_mode():
    """
    Return the current operating mode.
    """

    return DEVELOPMENT_BOT_STATE[
        "mode"
    ]


def is_read_only():
    """
    Return True when the bot is operating
    in read-only mode.
    """

    return (
        DEVELOPMENT_BOT_STATE[
            "mode"
        ]
        == "READ_ONLY"
    )


PROJECT_FEATURES = {

    "ai_router": "Complete",

    "provider_registry": "Complete",

    "development_bot": "In Development",

    "story_architect": "Complete",

    "character_engine": "Complete",

    "world_builder": "Complete",

    "timeline_builder": "Complete",

    "chapter_planner": "Complete",

    "chapter_writer": "Complete",

    "editor_analyzer": "Complete",

    "specialist_bot_system": "Planned",

    "publishing_system": "Planned",

    "marketplace": "Planned",
}


def get_project_features():
    """
    Return the current project feature map.
    """

    return dict(
        PROJECT_FEATURES
    )


def get_feature_status(
    feature_name: str,
):
    """
    Return the status of a single feature.
    """

    return PROJECT_FEATURES.get(
        feature_name,
        "Unknown",
    )


PROJECT_MILESTONES = {

    "foundation": "Complete",

    "ai_router": "Complete",

    "development_bot": "In Progress",

    "specialist_bot_framework": "Planned",

    "commercial_platform": "Planned",

    "internal_alpha": "Future",

    "closed_beta": "Future",

    "public_release": "Future",
}


def get_project_milestones():
    """
    Return all project milestones.
    """

    return dict(
        PROJECT_MILESTONES
    )


def get_milestone_status(
    milestone_name: str,
):
    """
    Return the status of a project milestone.
    """

    return PROJECT_MILESTONES.get(
        milestone_name,
        "Unknown",
    )


PROJECT_STATISTICS = {

    "completed_major_tasks": 30,

    "current_major_task": 31,

    "completed_subtasks": 5,

    "supported_ai_providers": 6,

    "implemented_ai_providers": 1,

    "development_stage": (
        "Development Bot Intelligence"
    ),
}


def get_project_statistics():
    """
    Return overall project statistics.
    """

    return dict(
        PROJECT_STATISTICS
    )


def get_project_statistic(
    statistic_name: str,
):
    """
    Return a single project statistic.
    """

    return PROJECT_STATISTICS.get(
        statistic_name
    )


DEVELOPMENT_BOT_COMMANDS = {

    "structure": "Project Structure",

    "project-files": "Project File List",

    "index": "Project Index",

    "index-analyze": "Project Analysis",

    "find": "Target Discovery",

    "source": "Target Source",

    "deps": "Dependency Analysis",

    "callers": "Reverse Dependency Analysis",

    "project": "Project Status",

    "help": "Available Commands",
}


def get_available_commands():
    """
    Return all registered Development Bot commands.
    """

    return dict(
        DEVELOPMENT_BOT_COMMANDS
    )


def command_exists(
    command_name: str,
):
    """
    Return True if a command is registered.
    """

    return (
        command_name
        in DEVELOPMENT_BOT_COMMANDS
    )


DEVELOPMENT_BOT_COMMAND_CATEGORIES = {

    "Project": [
        "structure",
        "project-files",
        "project",
    ],

    "Analysis": [
        "index",
        "index-analyze",
    ],

    "Discovery": [
        "find",
        "source",
    ],

    "Dependencies": [
        "deps",
        "callers",
    ],

    "System": [
        "help",
    ],
}


def get_command_categories():
    """
    Return all command categories.
    """

    return {
        category: list(commands)
        for category, commands
        in DEVELOPMENT_BOT_COMMAND_CATEGORIES.items()
    }


def get_commands_for_category(
    category_name: str,
):
    """
    Return all commands within a category.
    """

    return list(
        DEVELOPMENT_BOT_COMMAND_CATEGORIES.get(
            category_name,
            [],
        )
    )


DEVELOPMENT_BOT_COMMAND_HELP = {

    "structure":
        "Display the project folder structure.",

    "project-files":
        "List approved project Python files.",

    "project":
        "Display current project status.",

    "index":
        "Build the project index.",

    "index-analyze":
        "Analyze the indexed project.",

    "find":
        "Locate functions or classes.",

    "source":
        "Display source for a selected target.",

    "deps":
        "Show direct internal dependencies.",

    "callers":
        "Show reverse dependencies.",

    "help":
        "Display available Development Bot commands.",
}


def get_command_help():
    """
    Return the Development Bot help registry.
    """

    return dict(
        DEVELOPMENT_BOT_COMMAND_HELP
    )


def get_command_description(
    command_name: str,
):
    """
    Return the description for a command.
    """

    return DEVELOPMENT_BOT_COMMAND_HELP.get(
        command_name,
        "Unknown command.",
    )


DEVELOPMENT_BOT_COMMAND_ALIASES = {

    "status": "project",

    "files": "project-files",

    "search": "find",

    "dependencies": "deps",

    "reverse-dependencies": "callers",

    "commands": "help",
}


def get_command_aliases():
    """
    Return all registered command aliases.
    """

    return dict(
        DEVELOPMENT_BOT_COMMAND_ALIASES
    )


def resolve_command(
    command_name: str,
):
    """
    Resolve a command alias to its
    canonical Development Bot command.
    """

    command_name = command_name.strip()

    if command_exists(
        command_name
    ):
        return command_name

    return DEVELOPMENT_BOT_COMMAND_ALIASES.get(
        command_name,
        command_name,
    )


DEVELOPMENT_BOT_COMMAND_PERMISSIONS = {

    "structure": True,

    "project-files": True,

    "project": True,

    "index": True,

    "index-analyze": True,

    "find": True,

    "source": True,

    "deps": True,

    "callers": True,

    "help": True,
}


def get_command_permissions():
    """
    Return the Development Bot
    command permissions.
    """

    return dict(
        DEVELOPMENT_BOT_COMMAND_PERMISSIONS
    )


def is_command_permitted(
    command_name: str,
):
    """
    Return True if a command is
    currently permitted.
    """

    command_name = resolve_command(
        command_name
    )

    return DEVELOPMENT_BOT_COMMAND_PERMISSIONS.get(
        command_name,
        False,
    )


DEVELOPMENT_BOT_COMMAND_METADATA = {

    "structure": {
        "category": "Project",
        "read_only": True,
    },

    "project-files": {
        "category": "Project",
        "read_only": True,
    },

    "project": {
        "category": "Project",
        "read_only": True,
    },

    "index": {
        "category": "Analysis",
        "read_only": True,
    },

    "index-analyze": {
        "category": "Analysis",
        "read_only": True,
    },

    "find": {
        "category": "Discovery",
        "read_only": True,
    },

    "source": {
        "category": "Discovery",
        "read_only": True,
    },

    "deps": {
        "category": "Dependencies",
        "read_only": True,
    },

    "callers": {
        "category": "Dependencies",
        "read_only": True,
    },

    "help": {
        "category": "System",
        "read_only": True,
    },
}


def get_command_metadata():
    """
    Return metadata for all commands.
    """

    return dict(
        DEVELOPMENT_BOT_COMMAND_METADATA
    )


def get_metadata_for_command(
    command_name: str,
):
    """
    Return metadata for a single command.
    """

    command_name = resolve_command(
        command_name
    )

    return DEVELOPMENT_BOT_COMMAND_METADATA.get(
        command_name,
        {},
    )


def validate_command(
    command_name: str,
):
    """
    Validate a Development Bot command.
    """

    resolved_command = resolve_command(
        command_name
    )

    exists = command_exists(
        resolved_command
    )

    return {
        "requested": command_name,
        "resolved": resolved_command,
        "exists": exists,
        "permitted": (
            is_command_permitted(
                resolved_command
            )
            if exists
            else False
        ),
        "metadata": (
            get_metadata_for_command(
                resolved_command
            )
            if exists
            else {}
        ),
        "description": (
            get_command_description(
                resolved_command
            )
            if exists
            else "Unknown command."
        ),
    }


def get_command_summary():
    """
    Return a complete summary of every
    registered Development Bot command.
    """

    summary = {}

    for command in get_available_commands():

        summary[command] = {
            "description": (
                get_command_description(
                    command
                )
            ),
            "category": (
                get_metadata_for_command(
                    command
                ).get(
                    "category",
                    "Unknown",
                )
            ),
            "permitted": (
                is_command_permitted(
                    command
                )
            ),
            "read_only": (
                get_metadata_for_command(
                    command
                ).get(
                    "read_only",
                    False,
                )
            ),
        }

    return summary


PROJECT_CONTEXT = {

    "active_project": "AI Novelist",

    "current_major_task": 31,

    "current_subtask": "31O",

    "current_focus": (
        "Development Bot Intelligence Layer"
    ),

    "operating_mode": (
        get_current_mode()
    ),
}


def get_project_context():
    """
    Return the current project context.
    """

    return dict(
        PROJECT_CONTEXT
    )


def update_project_context(
    key,
    value,
):
    """
    Update a single project context value.
    """

    if key in PROJECT_CONTEXT:

        PROJECT_CONTEXT[key] = value


DEVELOPMENT_SESSION = {

    "active": True,

    "major_task": 31,

    "current_subtask": "31P",

    "mode": get_current_mode(),

    "changes_pending": True,

    "level_1_tests_passed": 15,
}


def get_development_session():
    """
    Return the current development session.
    """

    return dict(
        DEVELOPMENT_SESSION
    )


def update_development_session(
    key,
    value,
):
    """
    Update a development session value.
    """

    if key in DEVELOPMENT_SESSION:

        DEVELOPMENT_SESSION[key] = value


DEVELOPMENT_CHECKPOINTS = {

    "last_completed_major_task": 30,

    "current_major_task": 31,

    "current_subtask": "31Q",

    "last_verified_subtask": "31P",

    "router_complete": True,

    "development_bot_phase": (
        "Intelligence Layer"
    ),
}


def get_development_checkpoints():
    """
    Return development checkpoints.
    """

    return dict(
        DEVELOPMENT_CHECKPOINTS
    )


def update_development_checkpoint(
    key,
    value,
):
    """
    Update a development checkpoint.
    """

    if key in DEVELOPMENT_CHECKPOINTS:

        DEVELOPMENT_CHECKPOINTS[key] = value


def get_last_verified_subtask():
    """
    Return the last verified subtask.
    """

    return DEVELOPMENT_CHECKPOINTS[
        "last_verified_subtask"
    ]


DEVELOPMENT_HEALTH = {

    "project_status": "Healthy",

    "level_1_tests": "Passing",

    "current_major_task": 31,

    "current_subtask": "31R",

    "architecture_status": (
        "Stable"
    ),

    "ready_for_next_task": True,
}


def get_development_health():
    """
    Return the current development health.
    """

    return dict(
        DEVELOPMENT_HEALTH
    )


def update_development_health(
    key,
    value,
):
    """
    Update a development health value.
    """

    if key in DEVELOPMENT_HEALTH:

        DEVELOPMENT_HEALTH[key] = value


def is_project_healthy():
    """
    Return True when the project is
    considered healthy.
    """

    return (
        DEVELOPMENT_HEALTH[
            "project_status"
        ]
        == "Healthy"
    )


DEVELOPMENT_PRIORITIES = {

    "highest_priority": (
        "Development Bot Intelligence"
    ),

    "current_major_task": 31,

    "current_subtask": "31S",

    "next_major_task": 32,

    "launch_priority": (
        "Continue platform development"
    ),

    "commercial_focus": (
        "Build MVP"
    ),
}


def get_development_priorities():
    """
    Return the current development
    priorities.
    """

    return dict(
        DEVELOPMENT_PRIORITIES
    )


def get_highest_priority():
    """
    Return the highest development
    priority.
    """

    return DEVELOPMENT_PRIORITIES[
        "highest_priority"
    ]


def update_development_priority(
    key,
    value,
):
    """
    Update a development priority.
    """

    if key in DEVELOPMENT_PRIORITIES:

        DEVELOPMENT_PRIORITIES[key] = value


DEVELOPMENT_GOALS = {

    "primary_goal": (
        "Build the world's leading AI-assisted novel development platform"
    ),

    "current_focus": (
        "Development Bot Intelligence Layer"
    ),

    "next_focus": (
        "Advanced reasoning and project analysis"
    ),

    "long_term_target": (
        "Specialist Bot Ecosystem"
    ),

    "commercial_target": (
        "Launch AI Novelist MVP"
    ),
}


def get_development_goals():
    """
    Return the Development Bot goals.
    """

    return dict(
        DEVELOPMENT_GOALS
    )


def get_primary_goal():
    """
    Return the primary development goal.
    """

    return DEVELOPMENT_GOALS[
        "primary_goal"
    ]


def update_development_goal(
    key,
    value,
):
    """
    Update a development goal.
    """

    if key in DEVELOPMENT_GOALS:

        DEVELOPMENT_GOALS[key] = value
# ============================================================
# DEVELOPMENT ANALYSIS PROFILES
# ============================================================

DEVELOPMENT_ANALYSIS_PROFILES = {

    "architecture": {
        "enabled": True,
        "priority": 10,
        "description": (
            "Evaluate software architecture, modularity, "
            "layer separation and long-term scalability."
        ),
    },

    "code_quality": {
        "enabled": True,
        "priority": 10,
        "description": (
            "Review readability, maintainability, "
            "consistency and code organization."
        ),
    },

    "dependencies": {
        "enabled": True,
        "priority": 9,
        "description": (
            "Inspect internal dependencies and identify "
            "tight coupling or circular references."
        ),
    },

    "performance": {
        "enabled": True,
        "priority": 8,
        "description": (
            "Identify unnecessary processing, repeated work "
            "and potential performance improvements."
        ),
    },

    "reliability": {
        "enabled": True,
        "priority": 10,
        "description": (
            "Check for robustness, defensive coding and "
            "failure handling."
        ),
    },

    "extensibility": {
        "enabled": True,
        "priority": 9,
        "description": (
            "Evaluate how easily future features can be added."
        ),
    },

    "ai_integration": {
        "enabled": True,
        "priority": 10,
        "description": (
            "Review AI routing, provider abstraction and "
            "future multi-model compatibility."
        ),
    },
}


def get_analysis_profiles():
    """
    Return every registered Development Analysis Profile.
    """

    return dict(DEVELOPMENT_ANALYSIS_PROFILES)


def get_analysis_profile(profile_name):
    """
    Return one analysis profile.
    """

    return DEVELOPMENT_ANALYSIS_PROFILES.get(profile_name)


def analysis_profile_exists(profile_name):
    """
    Return True if the requested profile exists.
    """

    return profile_name in DEVELOPMENT_ANALYSIS_PROFILES


def get_enabled_analysis_profiles():
    """
    Return only enabled analysis profiles.
    """

    return {
        name: profile
        for name, profile
        in DEVELOPMENT_ANALYSIS_PROFILES.items()
        if profile["enabled"]
    }  
# ============================================================
# DEVELOPMENT ANALYSIS REPORT TEMPLATE
# ============================================================

DEVELOPMENT_ANALYSIS_TEMPLATE = {

    "target": None,

    "analysis_profile": None,

    "status": "Not Started",

    "findings": [],

    "risks": [],

    "recommendations": [],

    "confidence": 0,

    "summary": "",
}


def create_analysis_report(
    target,
    profile,
):
    """
    Create a new Development Bot analysis report.
    """

    report = dict(
        DEVELOPMENT_ANALYSIS_TEMPLATE
    )

    report["target"] = target

    report["analysis_profile"] = profile

    report["status"] = "Created"

    return report  
def add_finding(
    report,
    finding,
):
    """
    Add a finding to an analysis report.
    """

    report["findings"].append(finding)


def add_risk(
    report,
    risk,
):
    """
    Add a risk to an analysis report.
    """

    report["risks"].append(risk)


def add_recommendation(
    report,
    recommendation,
):
    """
    Add a recommendation to an analysis report.
    """

    report["recommendations"].append(
        recommendation
    )


def finalize_analysis_report(
    report,
    summary,
    confidence,
):
    """
    Finalize an analysis report.
    """

    report["summary"] = summary

    report["confidence"] = confidence

    report["status"] = "Completed"

    return report  
# ============================================================
# DEVELOPMENT ANALYSIS SEVERITY
# ============================================================

DEVELOPMENT_ANALYSIS_SEVERITY = {

    "critical": 5,

    "high": 4,

    "medium": 3,

    "low": 2,

    "info": 1,
}


def get_analysis_severity():
    """
    Return the standard analysis severity levels.
    """

    return dict(
        DEVELOPMENT_ANALYSIS_SEVERITY
    )


def severity_exists(
    severity_name,
):
    """
    Return True if the severity exists.
    """

    return (
        severity_name.lower()
        in DEVELOPMENT_ANALYSIS_SEVERITY
    )


def get_severity_score(
    severity_name,
):
    """
    Return the numeric score for a severity.
    """

    return DEVELOPMENT_ANALYSIS_SEVERITY.get(
        severity_name.lower(),
        0,
    )  
# ============================================================
# DEVELOPMENT ANALYSIS CONFIDENCE
# ============================================================

DEVELOPMENT_ANALYSIS_CONFIDENCE = {

    "confirmed": 100,

    "very_high": 90,

    "high": 75,

    "medium": 50,

    "low": 25,

    "unknown": 0,
}


def get_analysis_confidence():
    """
    Return the standard confidence levels.
    """

    return dict(
        DEVELOPMENT_ANALYSIS_CONFIDENCE
    )


def confidence_exists(
    confidence_name,
):
    """
    Return True if a confidence level exists.
    """

    return (
        confidence_name.lower()
        in DEVELOPMENT_ANALYSIS_CONFIDENCE
    )


def get_confidence_score(
    confidence_name,
):
    """
    Return the numeric score for a confidence level.
    """

    return DEVELOPMENT_ANALYSIS_CONFIDENCE.get(
        confidence_name.lower(),
        0,
    )
# ============================================================
# DEVELOPMENT ANALYSIS EVIDENCE
# ============================================================

DEVELOPMENT_ANALYSIS_EVIDENCE = {

    "confirmed": (
        "Supported directly by inspected source code."
    ),

    "inferred": (
        "Reasonable conclusion based on available evidence."
    ),

    "possible": (
        "Potential issue requiring further verification."
    ),

    "unknown": (
        "Insufficient evidence to determine."
    ),
}


def get_analysis_evidence():
    """
    Return the standard evidence classifications.
    """

    return dict(
        DEVELOPMENT_ANALYSIS_EVIDENCE
    )


def evidence_exists(
    evidence_name,
):
    """
    Return True if an evidence level exists.
    """

    return (
        evidence_name.lower()
        in DEVELOPMENT_ANALYSIS_EVIDENCE
    )


def get_evidence_description(
    evidence_name,
):
    """
    Return the description for an evidence level.
    """

    return DEVELOPMENT_ANALYSIS_EVIDENCE.get(
        evidence_name.lower(),
        "Unknown evidence classification.",
    )
DEVELOPMENT_BOT_INSTRUCTIONS = f"""
You are the Novelist Development Bot.

Project:
    {PROJECT_IDENTITY["project_name"]}

Version:
    {PROJECT_IDENTITY["project_version"]}

Current Development Task:
    {PROJECT_IDENTITY["current_task"]}

Current Subtask:
    {PROJECT_IDENTITY["current_subtask"]}

Current Milestone:
    {PROJECT_IDENTITY["current_milestone"]}

Architecture Phase:
    {PROJECT_IDENTITY["architecture_phase"]}

Your job is to help design, test, improve, debug and develop an
AI-powered professional novel-writing application.

You are NOT the novel-writing model itself.

You are the development intelligence responsible for improving
the Novelist system.

CORE RESPONSIBILITIES:

1. Analyze software architecture.
2. Identify bugs, weaknesses and conflicts.
3. Recommend improvements.
4. Design new Novelist features.
5. Help test existing features.
6. Review prompts and AI behaviour.
7. Detect inconsistencies between modules.
8. Improve story quality and system reliability.
9. Explain proposed changes clearly.
10. Work through development tasks in a controlled sequence.

DEVELOPMENT RULES:

- Work on one numbered development task at a time.
- Do not jump ahead to unrelated tasks.
- Never claim a code change has been made unless it has.
- Never silently modify project files.
- Separate analysis from implementation.
- Explain why a proposed change is useful.
- Protect existing working functionality.
- Prefer small, testable improvements over uncontrolled rewrites.
- Identify dependencies before recommending major changes.
- Flag uncertainty rather than pretending something is confirmed.
- Treat existing working code as valuable.
- Clearly distinguish confirmed findings from recommendations.
- Do not invent functions, imports, classes or modules that are
  not present in supplied project context.
- When targeted source code is supplied, base conclusions on that
  source code.
- When dependency source code is supplied, analyze how the target
  and dependencies interact.
- If more source code is required to confirm something, say so.

CURRENT ACCESS LEVEL:

READ / REASON / RECOMMEND ONLY.

You may inspect:
- project structure
- project index information
- approved Python files
- targeted functions
- targeted classes
- direct internal dependencies
- limited project source context

You currently do NOT have authorization to automatically modify,
delete, rename or overwrite project files.

LONG-TERM OBJECTIVE:

Help develop the Novelist into a sophisticated AI-assisted
professional fiction development, writing, editing and publishing
platform.
"""
# ============================================================
# SAFETY SETTINGS
# ============================================================

ALLOWED_FILE_EXTENSIONS = {
    ".py",
}

BLOCKED_FILENAMES = {
    ".env",
}

IGNORED_FOLDERS = {
    ".git",
    ".venv",
    "venv",
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
    ".idea",
    ".vscode",
    "node_modules",
}

IGNORED_PROJECT_FILES = {
    "novelist_dev_bot.py",
    "app_v1_backup.py",
    "app_v1_1_backup.py",
    "app_v1_2_backup.py",
}

MAX_FILE_CHARACTERS = 25000
MAX_PROJECT_CHARACTERS = 80000
MAX_TARGET_CHARACTERS = 30000
MAX_DEPENDENCY_CHARACTERS = 60000


# ============================================================
# SAFE FILE ACCESS
# ============================================================

def get_safe_project_file(filename: str) -> Path | None:
    requested_path = (PROJECT_ROOT / filename).resolve()

    try:
        requested_path.relative_to(PROJECT_ROOT)
    except ValueError:
        return None

    if not requested_path.exists():
        return None

    if not requested_path.is_file():
        return None

    if requested_path.name in BLOCKED_FILENAMES:
        return None

    if requested_path.suffix.lower() not in ALLOWED_FILE_EXTENSIONS:
        return None

    return requested_path


def read_project_file(filename: str) -> str:
    safe_path = get_safe_project_file(filename)

    if safe_path is None:
        return (
            "File access denied or file not found. "
            "Only Python files inside the Novelist project may be read."
        )

    try:
        content = safe_path.read_text(
            encoding="utf-8",
            errors="replace",
        )
    except Exception as error:
        return f"Could not read file: {error}"

    if len(content) > MAX_FILE_CHARACTERS:
        return (
            content[:MAX_FILE_CHARACTERS]
            + "\n\n"
            + "[FILE TRUNCATED BY SAFETY LIMIT]"
        )

    return content
# ============================================================
# PROJECT ANALYSIS CACHE
# ============================================================

_PROJECT_PYTHON_FILES_CACHE = None


def clear_project_analysis_cache():
    """
    Clear cached project-analysis information.

    This allows the bot to refresh its view after project
    files have changed.
    """

    global _PROJECT_PYTHON_FILES_CACHE

    _PROJECT_PYTHON_FILES_CACHE = None


def get_cached_project_python_files():
    """
    Return the active Python project files using an
    in-memory cache after the first project scan.
    """

    global _PROJECT_PYTHON_FILES_CACHE

    if _PROJECT_PYTHON_FILES_CACHE is None:

        _PROJECT_PYTHON_FILES_CACHE = (
            get_project_python_files()
        )

    return list(
        _PROJECT_PYTHON_FILES_CACHE
    )

# ============================================================
# CACHED PYTHON SOURCE AND AST
# ============================================================

_PROJECT_SOURCE_CACHE = {}
_PROJECT_AST_CACHE = {}


def get_cached_python_source(
    path: Path,
) -> str:
    """
    Read Python source once and reuse it during the
    current development-bot session.
    """

    cache_key = str(
        path.resolve()
    )

    if cache_key not in _PROJECT_SOURCE_CACHE:

        _PROJECT_SOURCE_CACHE[
            cache_key
        ] = path.read_text(
            encoding="utf-8",
            errors="replace",
        )

    return _PROJECT_SOURCE_CACHE[
        cache_key
    ]


def get_cached_python_ast(
    path: Path,
):
    """
    Parse a Python file once and reuse its AST during the
    current development-bot session.
    """

    cache_key = str(
        path.resolve()
    )

    if cache_key not in _PROJECT_AST_CACHE:

        source = get_cached_python_source(
            path
        )

        _PROJECT_AST_CACHE[
            cache_key
        ] = ast.parse(
            source
        )

    return _PROJECT_AST_CACHE[
        cache_key
    ]
# ============================================================
# PROJECT FILE DISCOVERY
# ============================================================

def get_project_python_files() -> list[Path]:
    python_files = []

    for path in PROJECT_ROOT.rglob("*.py"):

        if any(
            folder in path.parts
            for folder in IGNORED_FOLDERS
        ):
            continue

        if path.name in IGNORED_PROJECT_FILES:
            continue

        python_files.append(path)

    return sorted(
        python_files,
        key=lambda item: str(
            item.relative_to(PROJECT_ROOT)
        ).lower(),
    )


def get_project_python_file_list() -> str:
    python_files = get_project_python_files()

    if not python_files:
        return "No approved Python files were detected."

    return "\n".join(
        f"- {path.relative_to(PROJECT_ROOT)}"
        for path in python_files
    )


# ============================================================
# PROJECT STRUCTURE
# ============================================================

def get_project_structure() -> str:
    project_lines = []

    for root, dirs, files in os.walk(PROJECT_ROOT):

        dirs[:] = [
            directory
            for directory in dirs
            if directory not in IGNORED_FOLDERS
        ]

        current_root = Path(root)

        try:
            relative_root = current_root.relative_to(PROJECT_ROOT)
        except ValueError:
            continue

        depth = len(relative_root.parts)

        if str(relative_root) == ".":
            folder_name = PROJECT_ROOT.name
        else:
            folder_name = relative_root.name

        indent = "    " * depth

        project_lines.append(
            f"{indent}[Folder] {folder_name}"
        )

        file_indent = "    " * (depth + 1)

        for filename in sorted(files):

            if filename == ".env":
                continue

            if filename.endswith(".pyc"):
                continue

            project_lines.append(
                f"{file_indent}- {filename}"
            )

    return "\n".join(project_lines)


# ============================================================
# PYTHON STRUCTURE ANALYSIS
# ============================================================

def analyze_python_structure(path: Path) -> dict:
    result = {
        "imports": [],
        "functions": [],
        "classes": [],
        "error": None,
    }

    try:
        source = path.read_text(
            encoding="utf-8",
            errors="replace",
        )

        tree = ast.parse(source)

    except Exception as error:
        result["error"] = str(error)
        return result

    for node in tree.body:

        if isinstance(node, ast.Import):

            for alias in node.names:
                result["imports"].append(alias.name)

        elif isinstance(node, ast.ImportFrom):

            module_name = node.module or ""

            for alias in node.names:

                if module_name:
                    import_name = (
                        f"{module_name}.{alias.name}"
                    )
                else:
                    import_name = alias.name

                result["imports"].append(import_name)

        elif isinstance(
            node,
            (ast.FunctionDef, ast.AsyncFunctionDef),
        ):
            result["functions"].append(node.name)

        elif isinstance(node, ast.ClassDef):
            result["classes"].append(node.name)

    return result


# ============================================================
# PROJECT INDEX
# ============================================================

def build_project_index() -> str:
    python_files = get_project_python_files()

    if not python_files:
        return "No Python files available for indexing."

    index_parts = []

    for path in python_files:

        relative_path = path.relative_to(PROJECT_ROOT)

        structure = analyze_python_structure(path)

        index_parts.append("=" * 60)
        index_parts.append(
            f"FILE: {relative_path}"
        )

        if structure["error"]:

            index_parts.append(
                f"PARSE ERROR: {structure['error']}"
            )

            continue

        index_parts.append("")
        index_parts.append("IMPORTS:")

        if structure["imports"]:
            for item in structure["imports"]:
                index_parts.append(
                    f"  - {item}"
                )
        else:
            index_parts.append("  None")

        index_parts.append("")
        index_parts.append("FUNCTIONS:")

        if structure["functions"]:
            for item in structure["functions"]:
                index_parts.append(
                    f"  - {item}"
                )
        else:
            index_parts.append("  None")

        index_parts.append("")
        index_parts.append("CLASSES:")

        if structure["classes"]:
            for item in structure["classes"]:
                index_parts.append(
                    f"  - {item}"
                )
        else:
            index_parts.append("  None")

        index_parts.append("")

    return "\n".join(index_parts)


# ============================================================
# TARGET DISCOVERY
# ============================================================

def find_code_targets(target_name: str) -> list[dict]:
    matches = []

    target_name = target_name.strip()

    if not target_name:
        return matches

    for path in get_project_python_files():

        try:
            source = path.read_text(
                encoding="utf-8",
                errors="replace",
            )

            tree = ast.parse(source)

        except Exception:
            continue

        for node in ast.walk(tree):

            if isinstance(
                node,
                (
                    ast.FunctionDef,
                    ast.AsyncFunctionDef,
                    ast.ClassDef,
                ),
            ):

                if node.name != target_name:
                    continue

                if isinstance(node, ast.ClassDef):
                    target_type = "class"
                else:
                    target_type = "function"

                matches.append(
                    {
                        "file": str(
                            path.relative_to(PROJECT_ROOT)
                        ),
                        "name": node.name,
                        "type": target_type,
                        "line_start": node.lineno,
                        "line_end": getattr(
                            node,
                            "end_lineno",
                            node.lineno,
                        ),
                    }
                )

    return matches


def format_target_matches(target_name: str) -> str:
    matches = find_code_targets(target_name)

    if not matches:
        return (
            f"No function or class named "
            f"'{target_name}' was found."
        )

    lines = []

    for match in matches:

        lines.append(
            f"{match['type'].upper()}: "
            f"{match['name']}"
        )

        lines.append(
            f"  File: {match['file']}"
        )

        lines.append(
            f"  Lines: "
            f"{match['line_start']}-"
            f"{match['line_end']}"
        )

        lines.append("")

    return "\n".join(lines)


# ============================================================
# SOURCE EXTRACTION
# ============================================================

def extract_source_lines(
    filename: str,
    line_start: int,
    line_end: int,
) -> str:

    safe_path = get_safe_project_file(filename)

    if safe_path is None:
        return "File access denied or file not found."

    try:

        source_lines = safe_path.read_text(
            encoding="utf-8",
            errors="replace",
        ).splitlines()

    except Exception as error:
        return f"Could not read file: {error}"

    start_index = max(
        line_start - 1,
        0,
    )

    end_index = min(
        line_end,
        len(source_lines),
    )

    selected_lines = source_lines[
        start_index:end_index
    ]

    numbered_lines = []

    for line_number, line in enumerate(
        selected_lines,
        start=line_start,
    ):

        numbered_lines.append(
            f"{line_number:>5}: {line}"
        )

    content = "\n".join(numbered_lines)

    if len(content) > MAX_TARGET_CHARACTERS:

        content = (
            content[:MAX_TARGET_CHARACTERS]
            + "\n\n"
            + "[TARGET SOURCE TRUNCATED]"
        )

    return content


def get_target_source(target_name: str) -> str:
    matches = find_code_targets(target_name)

    if not matches:
        return (
            f"No function or class named "
            f"'{target_name}' was found."
        )

    source_parts = []

    for match in matches:

        source = extract_source_lines(
            filename=match["file"],
            line_start=match["line_start"],
            line_end=match["line_end"],
        )

        source_parts.append(
            f"""
============================================================
TARGET: {match['name']}
TYPE: {match['type']}
FILE: {match['file']}
LINES: {match['line_start']}-{match['line_end']}
============================================================

{source}
"""
        )

    return "\n".join(source_parts)


# ============================================================
# DEPENDENCY DISCOVERY
# ============================================================

def get_called_function_names(
    target_name: str,
) -> list[str]:
    """
    Find function calls made directly inside a named target.
    """

    matches = find_code_targets(target_name)

    if not matches:
        return []

    called_names = set()

    for match in matches:

        safe_path = get_safe_project_file(
            match["file"]
        )

        if safe_path is None:
            continue

        try:

            source = safe_path.read_text(
                encoding="utf-8",
                errors="replace",
            )

            tree = ast.parse(source)

        except Exception:
            continue

        for node in ast.walk(tree):

            if not isinstance(
                node,
                (
                    ast.FunctionDef,
                    ast.AsyncFunctionDef,
                    ast.ClassDef,
                ),
            ):
                continue

            if node.name != target_name:
                continue

            for child in ast.walk(node):

                if not isinstance(
                    child,
                    ast.Call,
                ):
                    continue

                if isinstance(
                    child.func,
                    ast.Name,
                ):
                    called_names.add(
                        child.func.id
                    )

                elif isinstance(
                    child.func,
                    ast.Attribute,
                ):
                    called_names.add(
                        child.func.attr
                    )

    return sorted(called_names)


def get_internal_dependencies(
    target_name: str,
) -> list[str]:
    """
    Return only called functions/classes that also exist
    inside the Novelist project.

    Uses cached project AST data so the project does not
    need to be repeatedly rescanned for every dependency.
    """

    called_names = get_called_function_names(
        target_name
    )

    if not called_names:
        return []

    project_targets = set()

    for path in get_cached_project_python_files():

        try:

            tree = get_cached_python_ast(
                path
            )

        except Exception:
            continue

        for node in ast.walk(tree):

            if isinstance(
                node,
                (
                    ast.FunctionDef,
                    ast.AsyncFunctionDef,
                    ast.ClassDef,
                ),
            ):

                project_targets.add(
                    node.name
                )

    internal_dependencies = [
        called_name
        for called_name in called_names
        if called_name in project_targets
    ]

    return sorted(
        set(internal_dependencies)
    )

def format_dependencies(
    target_name: str,
) -> str:

    dependencies = get_internal_dependencies(
        target_name
    )

    if not dependencies:
        return (
            f"No direct internal dependencies were found "
            f"for '{target_name}'."
        )

    lines = [
        f"Direct internal dependencies for '{target_name}':",
        "",
    ]

    for dependency in dependencies:
        lines.append(
            f"- {dependency}"
        )

    return "\n".join(lines)

# ============================================================
# REVERSE DEPENDENCY DISCOVERY
# ============================================================

def get_reverse_dependencies(
    target_name: str,
) -> list[dict]:
    """
    Find internal project functions/classes that directly
    call the supplied target.

    Uses cached source and AST data to avoid repeatedly
    reading and parsing the same project files.
    """

    callers = []

    for path in get_cached_project_python_files():

        try:

            source = get_cached_python_source(
                path
            )

            tree = get_cached_python_ast(
                path
            )

        except Exception:
            continue

        relative_file = str(
            path.relative_to(PROJECT_ROOT)
        )

        for node in ast.walk(tree):

            if not isinstance(
                node,
                (
                    ast.FunctionDef,
                    ast.AsyncFunctionDef,
                    ast.ClassDef,
                ),
            ):
                continue

            found_call = False

            for child in ast.walk(node):

                if not isinstance(
                    child,
                    ast.Call,
                ):
                    continue

                called_name = None

                if isinstance(
                    child.func,
                    ast.Name,
                ):

                    called_name = (
                        child.func.id
                    )

                elif isinstance(
                    child.func,
                    ast.Attribute,
                ):

                    called_name = (
                        child.func.attr
                    )

                if called_name == target_name:

                    found_call = True
                    break

            if not found_call:
                continue

            callers.append(
                {
                    "caller": node.name,
                    "type": (
                        "class"
                        if isinstance(
                            node,
                            ast.ClassDef,
                        )
                        else "function"
                    ),
                    "file": relative_file,
                    "line_start": node.lineno,
                    "line_end": getattr(
                        node,
                        "end_lineno",
                        node.lineno,
                    ),
                }
            )

    callers.sort(
        key=lambda item: (
            item["file"].lower(),
            item["line_start"],
            item["caller"].lower(),
        )
    )

    return callers
def format_reverse_dependencies(
    target_name: str,
) -> str:
    """
    Format callers of a selected function or class.
    """

    matches = get_reverse_dependencies(
        target_name
    )

    if not matches:
        return (
            f"No internal callers were found "
            f"for '{target_name}'."
        )

    lines = [
        f"Internal callers of '{target_name}':",
        "",
    ]

    for match in matches:

        lines.append(
            f"- {match['caller']} "
            f"({match['type']})"
        )

        lines.append(
            f"  File: {match['file']}"
        )

        lines.append(
            f"  Lines: "
            f"{match['line_start']}-"
            f"{match['line_end']}"
        )

        lines.append("")

    return "\n".join(lines)


def build_reverse_dependency_context(
    target_name: str,
) -> str:
    """
    Build source context for the selected target plus its
    direct internal callers.
    """

    target_source = get_target_source(
        target_name
    )

    if target_source.startswith(
        "No function or class"
    ):
        return target_source

    callers = get_reverse_dependencies(
        target_name
    )

    parts = []

    parts.append(
        """
############################################################
SELECTED TARGET
############################################################
"""
    )

    parts.append(target_source)

    if not callers:

        parts.append(
            "\nNo direct internal callers were found."
        )

        return "\n".join(parts)

    parts.append(
        """
############################################################
DIRECT INTERNAL CALLERS
############################################################
"""
    )

    total_characters = len(
        target_source
    )

    for caller in callers:

        caller_source = extract_source_lines(
            filename=caller["file"],
            line_start=caller["line_start"],
            line_end=caller["line_end"],
        )

        remaining = (
            MAX_DEPENDENCY_CHARACTERS
            - total_characters
        )

        if remaining <= 0:

            parts.append(
                "\n[REVERSE DEPENDENCY CONTEXT LIMIT REACHED]"
            )
            break

        if len(caller_source) > remaining:

            caller_source = (
                caller_source[:remaining]
                + "\n\n"
                + "[CALLER SOURCE TRUNCATED]"
            )

        parts.append(
            f"""
============================================================
CALLER: {caller['caller']}
TYPE: {caller['type']}
FILE: {caller['file']}
LINES: {caller['line_start']}-{caller['line_end']}
============================================================

{caller_source}
"""
        )

        total_characters += len(
            caller_source
        )

    return "\n".join(parts)


def analyze_reverse_dependencies(
    target_name: str,
    user_request: str,
) -> str:
    """
    Analyze the likely impact of changing a selected target
    by inspecting its direct internal callers.
    """

    reverse_context = (
        build_reverse_dependency_context(
            target_name
        )
    )

    if reverse_context.startswith(
        "No function or class"
    ):
        return reverse_context

    development_context = f"""
CURRENT NOVELIST PROJECT INDEX:

{build_project_index()}

TARGET AND REVERSE DEPENDENCY SOURCE:

{reverse_context}

USER DEVELOPMENT REQUEST:

{user_request}

REVERSE DEPENDENCY ANALYSIS RULES:

- Treat the selected target as the function or class being considered
  for change.
- Identify every supplied direct caller.
- Explain how each caller depends on the target.
- Identify visible assumptions callers make about parameters,
  return values, exceptions or side effects.
- Identify likely breakage risks if the target changes.
- Do not claim indirect effects unless supported by supplied source.
- Clearly separate confirmed impact from possible impact.
- If deeper inspection is required, identify the next function or
  module that should be inspected.
- Do not modify project files.
"""

    try:

        response = client.responses.create(
            model=OPENAI_MODEL,
            instructions=DEVELOPMENT_BOT_INSTRUCTIONS,
            input=development_context,
        )

        return response.output_text

    except Exception as error:

        return (
            f"Development Bot Error: {error}"
        )
# ============================================================
# DEPENDENCY SOURCE CONTEXT
# ============================================================

def build_dependency_context(
    target_name: str,
) -> str:
    """
    Retrieve target source plus one level of direct
    internal dependency source.
    """

    target_source = get_target_source(
        target_name
    )

    if target_source.startswith(
        "No function or class"
    ):
        return target_source

    dependencies = get_internal_dependencies(
        target_name
    )

    parts = []

    parts.append(
        """
############################################################
PRIMARY TARGET
############################################################
"""
    )

    parts.append(target_source)

    if not dependencies:

        parts.append(
            "\nNo direct internal dependencies were found."
        )

        return "\n".join(parts)

    parts.append(
        """
############################################################
DIRECT INTERNAL DEPENDENCIES
############################################################
"""
    )

    total_characters = len(target_source)

    for dependency in dependencies:

        dependency_source = get_target_source(
            dependency
        )

        remaining = (
            MAX_DEPENDENCY_CHARACTERS
            - total_characters
        )

        if remaining <= 0:

            parts.append(
                "\n[DEPENDENCY CONTEXT LIMIT REACHED]"
            )

            break

        if len(dependency_source) > remaining:

            dependency_source = (
                dependency_source[:remaining]
                + "\n\n"
                + "[DEPENDENCY SOURCE TRUNCATED]"
            )

        parts.append(dependency_source)

        total_characters += len(
            dependency_source
        )

    return "\n".join(parts)


# ============================================================
# TARGETED AI ANALYSIS
# ============================================================

def analyze_code_target(
    target_name: str,
    user_request: str,
) -> str:

    target_source = get_target_source(
        target_name
    )

    if target_source.startswith(
        "No function or class"
    ):
        return target_source

    development_context = f"""
CURRENT NOVELIST PROJECT INDEX:

{build_project_index()}

TARGETED SOURCE CODE:

{target_source}

USER DEVELOPMENT REQUEST:

{user_request}

TARGETED ANALYSIS RULES:

- Focus primarily on the supplied target source.
- Use the project index only for architectural context.
- Do not invent implementation details from other functions.
- Identify dependencies visible in the target.
- Identify potential bugs or weaknesses visible in the target.
- If another function must be inspected to confirm something,
  identify that function by name.
- Do not modify project files.
"""

    try:

        response = client.responses.create(
            model=OPENAI_MODEL,
            instructions=DEVELOPMENT_BOT_INSTRUCTIONS,
            input=development_context,
        )

        return response.output_text

    except Exception as error:

        return (
            f"Development Bot Error: {error}"
        )


# ============================================================
# DEPENDENCY-AWARE AI ANALYSIS
# ============================================================

def analyze_target_with_dependencies(
    target_name: str,
    user_request: str,
) -> str:
    """
    Analyze a target with one level of direct internal
    dependency source.
    """

    dependency_context = build_dependency_context(
        target_name
    )

    if dependency_context.startswith(
        "No function or class"
    ):
        return dependency_context

    development_context = f"""
CURRENT NOVELIST PROJECT INDEX:

{build_project_index()}

TARGET AND DEPENDENCY SOURCE:

{dependency_context}

USER DEVELOPMENT REQUEST:

{user_request}

DEPENDENCY ANALYSIS RULES:

- Treat the PRIMARY TARGET as the main focus.
- Analyze direct internal dependencies only where they affect
  the target.
- Trace visible data flow between the target and its dependencies.
- Identify assumptions the target makes about dependency outputs.
- Identify error propagation risks.
- Identify duplicated or conflicting logic if visible.
- Do not invent behavior outside the supplied source.
- Clearly separate confirmed findings from recommendations.
- If deeper dependencies are required, identify them by name.
- Do not modify project files.
"""

    try:

        response = client.responses.create(
            model=OPENAI_MODEL,
            instructions=DEVELOPMENT_BOT_INSTRUCTIONS,
            input=development_context,
        )

        return response.output_text

    except Exception as error:

        return (
            f"Development Bot Error: {error}"
        )


# ============================================================
# PROJECT CODE CONTEXT
# ============================================================

def build_project_code_context() -> str:
    combined_parts = []
    total_characters = 0

    for path in get_project_python_files():

        relative_path = path.relative_to(
            PROJECT_ROOT
        )

        try:

            content = path.read_text(
                encoding="utf-8",
                errors="replace",
            )

        except Exception as error:

            combined_parts.append(
                f"""
============================================================
FILE: {relative_path}
============================================================

Could not read file: {error}
"""
            )

            continue

        if len(content) > MAX_FILE_CHARACTERS:

            content = (
                content[:MAX_FILE_CHARACTERS]
                + "\n\n"
                + "[FILE TRUNCATED BY PER-FILE SAFETY LIMIT]"
            )

        remaining = (
            MAX_PROJECT_CHARACTERS
            - total_characters
        )

        if remaining <= 0:

            combined_parts.append(
                "\n[PROJECT-WIDE SAFETY LIMIT REACHED]\n"
            )

            break

        if len(content) > remaining:

            content = (
                content[:remaining]
                + "\n\n"
                + "[FILE TRUNCATED BY PROJECT LIMIT]"
            )

        combined_parts.append(
            f"""
============================================================
FILE: {relative_path}
============================================================

{content}
"""
        )

        total_characters += len(content)

    return "\n".join(combined_parts)


# ============================================================
# INDEX-BASED ANALYSIS
# ============================================================

def analyze_project_index(
    user_request: str,
) -> str:

    development_context = f"""
CURRENT NOVELIST PROJECT STRUCTURE:

{get_project_structure()}

PROJECT INDEX:

{build_project_index()}

USER DEVELOPMENT REQUEST:

{user_request}

INDEX ANALYSIS RULES:

- Base your answer only on the index information supplied.
- Use imports to identify likely module dependencies.
- Use functions and classes to identify module responsibilities.
- Do not pretend to know internal function logic from the index.
- Clearly say when raw source inspection would be required.
"""

    try:

        response = client.responses.create(
            model=OPENAI_MODEL,
            instructions=DEVELOPMENT_BOT_INSTRUCTIONS,
            input=development_context,
        )

        return response.output_text

    except Exception as error:

        return (
            f"Development Bot Error: {error}"
        )


# ============================================================
# PROJECT-WIDE RAW CODE ANALYSIS
# ============================================================

def analyze_entire_project(
    user_request: str,
) -> str:

    development_context = f"""
CURRENT NOVELIST PROJECT STRUCTURE:

{get_project_structure()}

PROJECT INDEX:

{build_project_index()}

PROJECT SOURCE CODE:

{build_project_code_context()}

USER DEVELOPMENT REQUEST:

{user_request}
"""

    try:

        response = client.responses.create(
            model=OPENAI_MODEL,
            instructions=DEVELOPMENT_BOT_INSTRUCTIONS,
            input=development_context,
        )

        return response.output_text

    except Exception as error:

        return (
            f"Development Bot Error: {error}"
        )


# ============================================================
# SINGLE FILE ANALYSIS
# ============================================================

def analyze_project_file(
    filename: str,
    user_request: str,
) -> str:

    file_content = read_project_file(
        filename
    )

    development_context = f"""
SELECTED FILE:

{filename}

FILE CONTENT:

{file_content}

USER DEVELOPMENT REQUEST:

{user_request}
"""

    try:

        response = client.responses.create(
            model=OPENAI_MODEL,
            instructions=DEVELOPMENT_BOT_INSTRUCTIONS,
            input=development_context,
        )

        return response.output_text

    except Exception as error:

        return (
            f"Development Bot Error: {error}"
        )


# ============================================================
# DISPLAY HELPERS
# ============================================================

def display_project_structure():

    print()
    print("=" * 60)
    print("NOVELIST PROJECT STRUCTURE")
    print("=" * 60)
    print(get_project_structure())
    print("=" * 60)


def display_project_files():

    print()
    print("=" * 60)
    print("PROJECT-WIDE ANALYSIS FILES")
    print("=" * 60)
    print(get_project_python_file_list())
    print("=" * 60)


def display_project_index():

    print()
    print("=" * 60)
    print("NOVELIST PROJECT INDEX")
    print("=" * 60)
    print(build_project_index())
    print("=" * 60)


def display_file(filename: str):

    print()
    print("=" * 60)
    print(
        f"READ-ONLY FILE: {filename}"
    )
    print("=" * 60)
    print(read_project_file(filename))
    print("=" * 60)


def display_target(target_name: str):

    print()
    print("=" * 60)
    print(
        f"CODE TARGET: {target_name}"
    )
    print("=" * 60)
    print(
        format_target_matches(
            target_name
        )
    )
    print("=" * 60)


def display_target_source(
    target_name: str,
):

    print()
    print("=" * 60)
    print(
        f"TARGET SOURCE: {target_name}"
    )
    print("=" * 60)
    print(
        get_target_source(
            target_name
        )
    )
    print("=" * 60)


def display_dependencies(
    target_name: str,
):

    print()
    print("=" * 60)
    print(
        f"DEPENDENCIES: {target_name}"
    )
    print("=" * 60)
    print(
        format_dependencies(
            target_name
        )
    )
    print("=" * 60)


# ============================================================
# GENERAL BOT ENGINE
# ============================================================

def ask_development_bot(
    user_request: str,
) -> str:

    development_context = f"""
CURRENT NOVELIST PROJECT STRUCTURE:

{get_project_structure()}

PROJECT INDEX:

{build_project_index()}

USER DEVELOPMENT REQUEST:

{user_request}
"""

    try:

        response = client.responses.create(
            model=OPENAI_MODEL,
            instructions=DEVELOPMENT_BOT_INSTRUCTIONS,
            input=development_context,
        )

        return response.output_text

    except Exception as error:

        return (
            f"Development Bot Error: {error}"
        )
# ============================================================
# DEEP DEPENDENCY TRACING
# ============================================================

MAX_DEPENDENCY_DEPTH = 3


def build_dependency_tree(
    target_name: str,
    max_depth: int = MAX_DEPENDENCY_DEPTH,
) -> dict:
    """
    Build a recursive tree of internal project dependencies.

    The tree follows function/class calls downward while
    preventing circular dependency loops.
    """

    def trace_target(
        current_target: str,
        depth: int,
        path: tuple,
    ) -> dict:

        node = {
            "name": current_target,
            "depth": depth,
            "dependencies": [],
        }

        if depth >= max_depth:
            return node

        dependencies = get_internal_dependencies(
            current_target
        )

        for dependency in dependencies:

            dependency_name = dependency

            # Prevent circular recursion within the
            # current dependency path.
            if dependency_name in path:

                node["dependencies"].append(
                    {
                        "name": dependency_name,
                        "depth": depth + 1,
                        "circular": True,
                        "dependencies": [],
                    }
                )

                continue

            child = trace_target(
                dependency_name,
                depth + 1,
                path + (dependency_name,),
            )

            node["dependencies"].append(
                child
            )

        return node

    return trace_target(
        target_name,
        0,
        (target_name,),
    )


def format_dependency_tree(
    target_name: str,
    max_depth: int = MAX_DEPENDENCY_DEPTH,
) -> str:
    """
    Format the recursive dependency tree for terminal display.
    """

    matches = find_code_targets(
        target_name
    )

    if not matches:

        return (
            f"No function or class named "
            f"'{target_name}' was found."
        )

    tree = build_dependency_tree(
        target_name,
        max_depth,
    )

    lines = [
        f"Dependency tree for '{target_name}':",
        "",
    ]

    def add_node(
        node: dict,
        prefix: str = "",
    ):

        name = node["name"]
        depth = node["depth"]

        if depth == 0:

            lines.append(name)

        else:

            circular = node.get(
                "circular",
                False,
            )

            marker = " [CIRCULAR]" if circular else ""

            lines.append(
                f"{prefix}└── {name}{marker}"
            )

        children = node.get(
            "dependencies",
            [],
        )

        for child in children:

            child_prefix = (
                prefix + "    "
            )

            add_node(
                child,
                child_prefix,
            )

    add_node(tree)

    lines.append("")
    lines.append(
        f"Maximum trace depth: {max_depth}"
    )

    return "\n".join(lines)
# ============================================================
# DEEP REVERSE DEPENDENCY TRACING
# ============================================================

MAX_CALLER_DEPTH = 3


def build_caller_tree(
    target_name: str,
    max_depth: int = MAX_CALLER_DEPTH,
) -> dict:
    """
    Build a recursive tree of internal project callers.

    The tree follows callers upward while preventing
    circular recursion.
    """

    def trace_target(
        current_target: str,
        depth: int,
        path: tuple,
    ) -> dict:

        node = {
            "name": current_target,
            "depth": depth,
            "callers": [],
        }

        if depth >= max_depth:
            return node

        callers = get_reverse_dependencies(
            current_target
        )

        for caller in callers:

            caller_name = caller["caller"]

            if caller_name in path:

                node["callers"].append(
                    {
                        "name": caller_name,
                        "file": caller["file"],
                        "depth": depth + 1,
                        "circular": True,
                        "callers": [],
                    }
                )

                continue

            child = trace_target(
                caller_name,
                depth + 1,
                path + (caller_name,),
            )

            child["file"] = caller["file"]

            node["callers"].append(
                child
            )

        return node

    return trace_target(
        target_name,
        0,
        (target_name,),
    )


def format_caller_tree(
    target_name: str,
    max_depth: int = MAX_CALLER_DEPTH,
) -> str:
    """
    Format the recursive caller tree for terminal display.
    """

    matches = find_code_targets(
        target_name
    )

    if not matches:

        return (
            f"No function or class named "
            f"'{target_name}' was found."
        )

    tree = build_caller_tree(
        target_name,
        max_depth,
    )

    lines = [
        f"Caller tree for '{target_name}':",
        "",
    ]

    def add_node(
        node: dict,
        prefix: str = "",
    ):

        name = node["name"]
        depth = node["depth"]

        if depth == 0:

            lines.append(name)

        else:

            file_name = node.get(
                "file",
                "unknown",
            )

            circular = node.get(
                "circular",
                False,
            )

            marker = (
                " [CIRCULAR]"
                if circular
                else ""
            )

            lines.append(
                f"{prefix}└── "
                f"{name} "
                f"[{file_name}]"
                f"{marker}"
            )

        children = node.get(
            "callers",
            [],
        )

        for child in children:

            add_node(
                child,
                prefix + "    ",
            )

    add_node(tree)

    lines.append("")
    lines.append(
        f"Maximum caller depth: {max_depth}"
    )

    return "\n".join(lines)
# ============================================================
# SMART CODE CONTEXT SELECTION
# ============================================================

import tokenize
from io import StringIO


def normalize_search_terms(
    search_text: str,
) -> list[str]:
    """
    Convert a development request into useful search terms.
    """

    raw_terms = re.findall(
        r"[A-Za-z_][A-Za-z0-9_]*",
        search_text.lower(),
    )

    ignored_terms = {
        "a",
        "an",
        "and",
        "are",
        "as",
        "at",
        "be",
        "better",
        "by",
        "change",
        "code",
        "for",
        "from",
        "function",
        "i",
        "in",
        "improve",
        "is",
        "it",
        "make",
        "of",
        "on",
        "or",
        "project",
        "the",
        "this",
        "to",
        "with",
    }

    terms = []

    for term in raw_terms:

        if term in ignored_terms:
            continue

        if len(term) < 3:
            continue

        if term not in terms:
            terms.append(term)

    return terms


def score_code_target_for_request(
    target_name: str,
    filename: str,
    source: str,
    search_terms: list[str],
) -> int:
    """
    Score a code target against a development request.

    Higher scores indicate a stronger likely relationship.
    """

    score = 0

    target_lower = target_name.lower()
    filename_lower = filename.lower()
    source_lower = source.lower()

    for term in search_terms:

        if term == target_lower:
            score += 20

        elif term in target_lower:
            score += 10

        if term in filename_lower:
            score += 5

        source_occurrences = (
            source_lower.count(term)
        )

        score += min(
            source_occurrences,
            5,
        )

    return score


def find_relevant_code_targets(
    development_request: str,
    max_results: int = 8,
) -> list[dict]:
    """
    Find likely relevant functions/classes for a development
    request using lightweight local source scoring.
    """

    search_terms = normalize_search_terms(
        development_request
    )

    if not search_terms:
        return []

    results = []

    for path in get_cached_project_python_files():

        try:

            source = path.read_text(
                encoding="utf-8",
                errors="replace",
            )

            tree = ast.parse(source)

        except Exception:
            continue

        relative_file = str(
            path.relative_to(PROJECT_ROOT)
        )

        for node in ast.walk(tree):

            if not isinstance(
                node,
                (
                    ast.FunctionDef,
                    ast.AsyncFunctionDef,
                    ast.ClassDef,
                ),
            ):
                continue

            line_start = node.lineno

            line_end = getattr(
                node,
                "end_lineno",
                node.lineno,
            )

            source_lines = source.splitlines()

            target_source = "\n".join(
                source_lines[
                    line_start - 1:line_end
                ]
            )

            score = score_code_target_for_request(
                target_name=node.name,
                filename=relative_file,
                source=target_source,
                search_terms=search_terms,
            )

            if score <= 0:
                continue

            results.append(
                {
                    "name": node.name,
                    "file": relative_file,
                    "type": (
                        "class"
                        if isinstance(
                            node,
                            ast.ClassDef,
                        )
                        else "function"
                    ),
                    "line_start": line_start,
                    "line_end": line_end,
                    "score": score,
                }
            )

    results.sort(
        key=lambda item: (
            -item["score"],
            item["file"].lower(),
            item["line_start"],
        )
    )

    return results[:max_results]


def format_relevant_code_targets(
    development_request: str,
) -> str:
    """
    Format smart code-selection results for terminal display.
    """

    terms = normalize_search_terms(
        development_request
    )

    results = find_relevant_code_targets(
        development_request
    )

    lines = [
        "Smart code context search",
        "",
        "Search terms:",
        ", ".join(terms) if terms else "None",
        "",
    ]

    if not results:

        lines.append(
            "No relevant code targets were found."
        )

        return "\n".join(lines)

    lines.append(
        "Likely relevant code targets:"
    )

    lines.append("")

    for number, result in enumerate(
        results,
        start=1,
    ):

        lines.append(
            f"{number}. {result['name']}"
        )

        lines.append(
            f"   Type: {result['type']}"
        )

        lines.append(
            f"   File: {result['file']}"
        )

        lines.append(
            f"   Lines: "
            f"{result['line_start']}-"
            f"{result['line_end']}"
        )

        lines.append(
            f"   Relevance score: "
            f"{result['score']}"
        )

        lines.append("")

    return "\n".join(lines)
# ============================================================
# SMART DEVELOPMENT REQUEST INSPECTION
# ============================================================

MAX_SMART_INSPECTION_TARGETS = 3
MAX_SMART_INSPECTION_CHARACTERS = 50000


def build_smart_inspection_context(
    development_request: str,
) -> str:
    """
    Build focused source context for a plain-English
    development request.

    Relevant targets are selected using the local smart
    context search before any AI reasoning is performed.
    """

    matches = find_relevant_code_targets(
        development_request,
        max_results=MAX_SMART_INSPECTION_TARGETS,
    )

    if not matches:

        return (
            "No relevant code targets were found for "
            "the development request."
        )

    sections = [
        "DEVELOPMENT REQUEST",
        development_request,
        "",
        "AUTOMATICALLY SELECTED TARGETS",
        "",
    ]

    for number, match in enumerate(
        matches,
        start=1,
    ):

        sections.extend(
            [
                (
                    f"{number}. {match['name']} "
                    f"({match['type']})"
                ),
                f"File: {match['file']}",
                (
                    f"Lines: "
                    f"{match['line_start']}-"
                    f"{match['line_end']}"
                ),
                (
                    f"Relevance score: "
                    f"{match['score']}"
                ),
                "",
            ]
        )

        source_result = get_target_source(
            match["name"]
        )

        sections.extend(
            [
                "SOURCE",
                source_result,
                "",
                "DIRECT DEPENDENCIES",
                format_dependencies(
                    match["name"]
                ),
                "",
                "DIRECT CALLERS",
                format_reverse_dependencies(
                    match["name"]
                ),
                "",
                "-" * 60,
                "",
            ]
        )

    context = "\n".join(sections)

    if len(context) > MAX_SMART_INSPECTION_CHARACTERS:

        context = context[
            :MAX_SMART_INSPECTION_CHARACTERS
        ]

        context += (
            "\n\n"
            "[SMART INSPECTION CONTEXT TRUNCATED]"
        )

    return context


def inspect_development_request(
    development_request: str,
) -> str:
    """
    Inspect a plain-English development request and identify
    the most likely code area before change planning.
    """

    context = build_smart_inspection_context(
        development_request
    )

    prompt = f"""
You are inspecting an existing Python/Streamlit AI Novelist
project.

The user has supplied a development request.

Your job is NOT to modify code.

Your job is to determine where the requested change most
likely belongs and whether enough evidence exists to begin
formal change planning.

DEVELOPMENT REQUEST:

{development_request}

PROJECT EVIDENCE:

{context}

Use only the supplied project evidence.

Return exactly these sections:

1. REQUEST INTERPRETATION

Explain what the development request appears to require.

2. PRIMARY TARGET

Identify the strongest likely function or class and file.

3. SUPPORTING TARGETS

List other relevant functions/classes that may participate.

4. CURRENT CODE FLOW

Explain the relevant confirmed flow through the selected
code.

5. DEPENDENCY IMPACT

Explain confirmed downstream dependencies.

6. CALLER IMPACT

Explain confirmed upstream callers.

7. EVIDENCE GAPS

State anything that still needs inspection.

8. RECOMMENDED NEXT TARGET

State the exact function or class that should be used for
the next planning step.

9. INSPECTION STATUS

End this section with exactly one of:

READY FOR CHANGE PLANNING

or

MORE INSPECTION REQUIRED

Rules:

- Do not invent project behavior.
- Separate confirmed evidence from assumptions.
- Prefer the minimum relevant code surface.
- Do not suggest implementation code.
- Do not modify files.
- If evidence is incomplete, choose MORE INSPECTION REQUIRED.
- If multiple targets are relevant, identify one primary target.
- The recommended next target must be an actual target found
  in the supplied evidence.

End the entire response with exactly:

NO FILES WERE MODIFIED
"""

    response = client.responses.create(
        model=OPENAI_MODEL,
        input=prompt,
    )

    return response.output_text
# ============================================================
# AUTOMATIC CHANGE TARGET SELECTION
# ============================================================

MAX_AUTO_TARGET_CANDIDATES = 5


def select_change_target(
    development_request: str,
) -> dict | None:
    """
    Select the strongest likely code target for a
    plain-English development request.

    Selection combines text relevance with confirmed
    project dependency and caller relationships.
    """

    candidates = find_relevant_code_targets(
        development_request,
        max_results=MAX_AUTO_TARGET_CANDIDATES,
    )

    if not candidates:
        return None

    ranked_candidates = []

    for candidate in candidates:

        target_name = candidate["name"]

        dependencies = get_internal_dependencies(
            target_name
        )

        callers = get_reverse_dependencies(
            target_name
        )

        dependency_bonus = min(
            len(dependencies),
            5,
        )

        caller_bonus = min(
            len(callers) * 2,
            6,
        )

        final_score = (
            candidate["score"]
            + dependency_bonus
            + caller_bonus
        )

        ranked_candidate = dict(candidate)

        ranked_candidate[
            "dependency_count"
        ] = len(dependencies)

        ranked_candidate[
            "caller_count"
        ] = len(callers)

        ranked_candidate[
            "final_score"
        ] = final_score

        ranked_candidates.append(
            ranked_candidate
        )

    ranked_candidates.sort(
        key=lambda item: (
            -item["final_score"],
            -item["score"],
            item["file"].lower(),
            item["line_start"],
        )
    )

    top_candidate = ranked_candidates[0]

    return {
        "name": top_candidate["name"],
        "file": top_candidate["file"],
        "type": top_candidate["type"],
        "line_start": top_candidate["line_start"],
        "line_end": top_candidate["line_end"],
        "score": top_candidate["score"],
        "final_score": top_candidate["final_score"],
        "dependency_count": top_candidate[
            "dependency_count"
        ],
        "caller_count": top_candidate[
            "caller_count"
        ],
        "candidate_count": len(
            ranked_candidates
        ),
    }

def format_selected_change_target(
    development_request: str,
) -> str:
    """
    Format the automatically selected change target.
    """

    target = select_change_target(
        development_request
    )

    if target is None:

        return (
            "No suitable change target was found "
            "for the development request."
        )

    lines = [
        "Automatic change target selection",
        "",
        f"Request: {development_request}",
        "",
        f"Selected target: {target['name']}",
        f"Type: {target['type']}",
        f"File: {target['file']}",
        (
            f"Lines: "
            f"{target['line_start']}-"
            f"{target['line_end']}"
        ),
        f"Relevance score: {target['score']}",
        (
            f"Candidates considered: "
            f"{target['candidate_count']}"
        ),
    ]

    return "\n".join(lines)
# ============================================================
# SAFE CHANGE PLANNING
# ============================================================

MAX_CHANGE_PLAN_CHARACTERS = 90000


def build_change_plan_context(
    target_name: str,
) -> str:
    """
    Build a controlled context containing:

    - selected target
    - direct internal dependencies
    - direct internal callers

    This is used to reason about a proposed change
    without modifying any project files.
    """

    target_source = get_target_source(
        target_name
    )

    if target_source.startswith(
        "No function or class"
    ):
        return target_source

    forward_context = build_dependency_context(
        target_name
    )

    reverse_context = (
        build_reverse_dependency_context(
            target_name
        )
    )

    sections = [
        """
############################################################
CHANGE PLANNING TARGET
############################################################
""",
        target_source,
        """
############################################################
FORWARD DEPENDENCY CONTEXT
############################################################
""",
        forward_context,
        """
############################################################
REVERSE DEPENDENCY CONTEXT
############################################################
""",
        reverse_context,
    ]

    combined_context = "\n".join(
        sections
    )

    if len(combined_context) > MAX_CHANGE_PLAN_CHARACTERS:

        combined_context = (
            combined_context[
                :MAX_CHANGE_PLAN_CHARACTERS
            ]
            + "\n\n"
            + "[CHANGE PLAN CONTEXT TRUNCATED]"
        )

    return combined_context


def analyze_change_plan(
    target_name: str,
    requested_change: str,
) -> str:
    """
    Produce a safe implementation plan for a proposed
    code change.

    No project files are modified.
    """

    change_context = (
        build_change_plan_context(
            target_name
        )
    )

    if change_context.startswith(
        "No function or class"
    ):
        return change_context

    development_context = f"""
CURRENT NOVELIST PROJECT INDEX:

{build_project_index()}

PROPOSED CHANGE TARGET:

{target_name}

REQUESTED CHANGE:

{requested_change}

AVAILABLE SOURCE CONTEXT:

{change_context}

CHANGE PLANNING RULES:

You are preparing a development plan only.

DO NOT modify code.

DO NOT claim that a change has been implemented.

Use only behavior that can be confirmed from the supplied
project source and index.

Evaluate the proposed change in this order:

1. CURRENT BEHAVIOR
Explain what the target currently does based only on supplied
source.

2. REQUESTED CHANGE
Explain exactly what behavior would need to change.

3. DIRECT DEPENDENCIES
Identify internal functions or classes used by the target that
could affect implementation.

4. DIRECT CALLERS
Identify confirmed project code that depends directly on the
target.

5. CHANGE IMPACT
Explain what existing behavior could be affected.

Separate:

CONFIRMED IMPACT

from:

POSSIBLE IMPACT

6. FILES LIKELY TO REQUIRE CHANGES
List only files supported by supplied evidence.

Do not include unrelated project files simply because they
exist in the project index.

7. IMPLEMENTATION PLAN
Create a numbered implementation plan.

Prefer the smallest reliable change.

Do not recommend broad refactoring unless required.

8. SAFETY CHECKS
Identify behavior that must remain unchanged.

9. TEST PLAN
Give specific tests that should be run after implementation.

10. IMPLEMENTATION READINESS
Finish with exactly one of:

READY FOR IMPLEMENTATION

or

MORE INSPECTION REQUIRED

If more inspection is required, identify exactly which
function, class or file should be inspected next and why.

IMPORTANT:

The Development Bot currently has READ / REASON / RECOMMEND
permission only.

It must never state or imply that it has edited project files.
"""

    try:

        response = client.responses.create(
            model=OPENAI_MODEL,
            instructions=DEVELOPMENT_BOT_INSTRUCTIONS,
            input=development_context,
        )

        return response.output_text

    except Exception as error:

        return (
            f"Development Bot Error: {error}"
        )
    # ============================================================
# AUTOMATIC SAFE CHANGE PLANNING
# ============================================================


def automatically_plan_change(
    development_request: str,
) -> str:
    """
    Automatically select the strongest likely code target
    and pass it into the existing safe change planner.

    No files are modified.
    """

    selected_target = select_change_target(
        development_request
    )

    if selected_target is None:

        return (
            "AUTOMATIC CHANGE PLAN\n\n"
            "No suitable code target was found.\n\n"
            "MORE INSPECTION REQUIRED\n\n"
            "NO FILES WERE MODIFIED"
        )

    target_name = selected_target["name"]

    change_plan = analyze_change_plan(
        target_name,
        development_request,
    )

    header = "\n".join(
        [
            "AUTOMATIC TARGET SELECTION",
            "",
            f"Selected target: {target_name}",
            (
                f"File: "
                f"{selected_target['file']}"
            ),
            (
                f"Relevance score: "
                f"{selected_target['score']}"
            ),
            (
                f"Final selection score: "
                f"{selected_target['final_score']}"
            ),
            (
                f"Direct dependencies: "
                f"{selected_target['dependency_count']}"
            ),
            (
                f"Direct callers: "
                f"{selected_target['caller_count']}"
            ),
            "",
            "=" * 60,
            "",
        ]
    )

    return (
        header
        + change_plan
        + "\n\nNO FILES WERE MODIFIED"
    )
# ============================================================
# SAFE PROPOSAL VALIDATION
# ============================================================


def extract_proposal_section(
    proposal: str,
    section_heading: str,
    next_heading: str,
) -> str:
    """
    Extract text between two proposal section headings.
    """

    start_marker = section_heading
    end_marker = next_heading

    start_index = proposal.find(
        start_marker
    )

    if start_index == -1:
        return ""

    start_index += len(
        start_marker
    )

    end_index = proposal.find(
        end_marker,
        start_index,
    )

    if end_index == -1:
        return ""

    return proposal[
        start_index:end_index
    ].strip()


def validate_code_proposal(
    proposal: str,
) -> tuple[bool, str]:
    """
    Validate that a READY proposal has a replacement boundary
    that matches the replacement code it provides.

    This performs local structural checks only.
    No files are modified.
    """

    if (
        "PROPOSAL STATUS: READY"
        not in proposal
    ):

        return (
            False,
            "Proposal is not marked READY.",
        )

    boundary_section = extract_proposal_section(
        proposal,
        "D. REPLACEMENT BOUNDARY",
        "E. COMPLETE REPLACEMENT CODE",
    )

    code_section = extract_proposal_section(
        proposal,
        "E. COMPLETE REPLACEMENT CODE",
        "F. WHY THIS CHANGE SHOULD WORK",
    )

    if not boundary_section:

        return (
            False,
            "Replacement boundary is missing.",
        )

    if not code_section:

        return (
            False,
            "Replacement code is missing.",
        )

    allowed_boundaries = [
        "DOCSTRING ONLY",
        "SINGLE STATEMENT",
        "LOGICAL BLOCK",
        "FUNCTION BODY ONLY",
        "ENTIRE FUNCTION",
        "ENTIRE CLASS",
        "COMPLETE SECTION",
        "ENTIRE FILE",
    ]

    selected_boundary = None

    for boundary in allowed_boundaries:

        if boundary in boundary_section:

            selected_boundary = boundary
            break

    if selected_boundary is None:

        return (
            False,
            "Replacement boundary type is invalid.",
        )

    code_text = code_section.strip()

    if code_text.startswith("```python"):

        code_text = code_text[
            len("```python"):
        ].strip()

    elif code_text.startswith("```"):

        code_text = code_text[
            len("```"):
        ].strip()

    if code_text.endswith("```"):

        code_text = code_text[
            :-3
        ].strip()

    if not code_text:

        return (
            False,
            "Replacement code is empty.",
        )

    if selected_boundary == "DOCSTRING ONLY":

        stripped_code = code_text.lstrip()

        if not (
            stripped_code.startswith('"""')
            or stripped_code.startswith("'''")
        ):

            return (
                False,
                (
                    "DOCSTRING ONLY proposal does not "
                    "begin with a docstring."
                ),
            )

        if (
            "\ndef " in code_text
            or "\nclass " in code_text
            or code_text.startswith("def ")
            or code_text.startswith("class ")
        ):

            return (
                False,
                (
                    "DOCSTRING ONLY proposal contains "
                    "function or class code."
                ),
            )

    if selected_boundary == "ENTIRE FUNCTION":

        if not (
            code_text.lstrip().startswith(
                "def "
            )
            or code_text.lstrip().startswith(
                "async def "
            )
        ):

            return (
                False,
                (
                    "ENTIRE FUNCTION proposal does not "
                    "contain a complete function definition."
                ),
            )

    if selected_boundary == "ENTIRE CLASS":

        if not code_text.lstrip().startswith(
            "class "
        ):

            return (
                False,
                (
                    "ENTIRE CLASS proposal does not "
                    "contain a complete class definition."
                ),
            )

    return (
        True,
        (
            f"Proposal validation passed: "
            f"{selected_boundary}"
        ),
    )
# ============================================================
# CHANGE APPROVAL STATE
# ============================================================


_PENDING_CHANGE_APPROVAL = None


def clear_pending_change():
    """
    Clear any development change currently waiting for
    explicit user approval.
    """

    global _PENDING_CHANGE_APPROVAL
    _PENDING_CHANGE_APPROVAL = None


def set_pending_change(
    target_name: str,
    development_request: str,
    proposal: str,
):
    """
    Store a proposed development change as structured
    pending approval data.

    A snapshot of the target source is also stored so the
    project state can be verified again before any future
    implementation attempt.

    This does not modify any project file.
    """

    global _PENDING_CHANGE_APPROVAL

    boundary_section = extract_proposal_section(
        proposal,
        "D. REPLACEMENT BOUNDARY",
        "E. COMPLETE REPLACEMENT CODE",
    )

    code_section = extract_proposal_section(
        proposal,
        "E. COMPLETE REPLACEMENT CODE",
        "F. WHY THIS CHANGE SHOULD WORK",
    )

    affected_files_section = extract_proposal_section(
        proposal,
        "C. CONFIRMED AFFECTED FILES",
        "D. REPLACEMENT BOUNDARY",
    )

    allowed_boundaries = [
        "DOCSTRING ONLY",
        "SINGLE STATEMENT",
        "LOGICAL BLOCK",
        "FUNCTION BODY ONLY",
        "ENTIRE FUNCTION",
        "ENTIRE CLASS",
        "COMPLETE SECTION",
        "ENTIRE FILE",
    ]

    selected_boundary = None

    for boundary in allowed_boundaries:

        if boundary in boundary_section:

            selected_boundary = boundary
            break

    replacement_code = (
        code_section.strip()
    )

    if replacement_code.startswith(
        "```python"
    ):

        replacement_code = (
            replacement_code[
                len("```python"):
            ].strip()
        )

    elif replacement_code.startswith(
        "```"
    ):

        replacement_code = (
            replacement_code[
                len("```"):
            ].strip()
        )

    if replacement_code.endswith(
        "```"
    ):

        replacement_code = (
            replacement_code[:-3]
            .strip()
        )

    affected_files = []

    for line in affected_files_section.splitlines():

        cleaned_line = (
            line.strip()
        )

        if cleaned_line.startswith("-"):

            file_name = (
                cleaned_line[1:]
                .strip()
            )

            file_name = (
                file_name
                .strip("`")
                .strip()
            )

            if file_name:

                affected_files.append(
                    file_name
                )

    target_source_snapshot = (
        get_target_source(
            target_name
        )
    )

    _PENDING_CHANGE_APPROVAL = {
        "target_name": target_name,
        "development_request": development_request,
        "proposal": proposal,
        "boundary_type": selected_boundary,
        "replacement_code": replacement_code,
        "affected_files": affected_files,
        "target_source_snapshot": target_source_snapshot,
        "approved": False,
        "backup_path": None,
        "implemented": False,
        "implemented_file": None,

        # Task 25 — SINGLE STATEMENT safety data.
        #
        # These values remain empty until the user explicitly
        # selects an existing statement from the target.
        "statement_index": None,
        "statement_source": None,
        "statement_start_line": None,
        "statement_end_line": None,
    }


def get_pending_change():
    """
    Return the current pending change object.
    """

    return _PENDING_CHANGE_APPROVAL


def approve_pending_change() -> str:
    """
    Approve the current pending change.

    Approval alone never modifies source files.
    """

    global _PENDING_CHANGE_APPROVAL

    if _PENDING_CHANGE_APPROVAL is None:

        return (
            "There is no pending change to approve."
        )

    boundary_type = (
        _PENDING_CHANGE_APPROVAL.get(
            "boundary_type"
        )
    )

    if boundary_type == "SINGLE STATEMENT":

        statement_index = (
            _PENDING_CHANGE_APPROVAL.get(
                "statement_index"
            )
        )

        statement_source = (
            _PENDING_CHANGE_APPROVAL.get(
                "statement_source"
            )
        )

        if (
            statement_index is None
            or not statement_source
        ):

            return (
                "SINGLE STATEMENT change cannot be approved yet.\n"
                "An exact existing statement must first be selected."
            )

    _PENDING_CHANGE_APPROVAL[
        "approved"
    ] = True

    target_name = (
        _PENDING_CHANGE_APPROVAL[
            "target_name"
        ]
    )

    return (
        f"Change approved for '{target_name}'.\n"
        "No files have been modified."
    )


def reject_pending_change() -> str:
    """
    Reject and clear the current pending change.
    """

    global _PENDING_CHANGE_APPROVAL

    if _PENDING_CHANGE_APPROVAL is None:

        return (
            "There is no pending change to reject."
        )

    target_name = (
        _PENDING_CHANGE_APPROVAL[
            "target_name"
        ]
    )

    _PENDING_CHANGE_APPROVAL = None

    return (
        f"Change rejected for '{target_name}'.\n"
        "Pending change cleared.\n"
        "No files have been modified."
    )


def validate_pending_change_state() -> tuple[bool, str]:
    """
    Validate that the currently approved pending change still
    matches the source state from which it was proposed.

    This function is read-only.
    """

    pending_change = (
        get_pending_change()
    )

    if pending_change is None:

        return (
            False,
            "There is no pending change to validate.",
        )

    if not pending_change.get(
        "approved",
        False,
    ):

        return (
            False,
            "Pending change has not been approved.",
        )

    target_name = (
        pending_change.get(
            "target_name"
        )
    )

    if not target_name:

        return (
            False,
            "Pending change has no target name.",
        )

    boundary_type = (
        pending_change.get(
            "boundary_type"
        )
    )

    if not boundary_type:

        return (
            False,
            "Pending change has no replacement boundary.",
        )

    replacement_code = (
        pending_change.get(
            "replacement_code",
            "",
        )
    )

    if not replacement_code.strip():

        return (
            False,
            "Pending change has no replacement code.",
        )

    affected_files = (
        pending_change.get(
            "affected_files",
            [],
        )
    )

    if not affected_files:

        return (
            False,
            "Pending change has no affected file.",
        )

    if len(affected_files) != 1:

        return (
            False,
            (
                "Pending change affects more than one file. "
                "Automatic implementation is not yet allowed."
            ),
        )

    original_source = (
        pending_change.get(
            "target_source_snapshot"
        )
    )

    if not original_source:

        return (
            False,
            "Original target source snapshot is missing.",
        )

    current_source = (
        get_target_source(
            target_name
        )
    )

    if current_source.startswith(
        "No function or class"
    ):

        return (
            False,
            (
                "The target can no longer be found in "
                "the current project source."
            ),
        )

    if current_source != original_source:

        return (
            False,
            (
                "Current source no longer matches the "
                "source used to create this proposal. "
                "The proposal must be regenerated."
            ),
        )

    if boundary_type == "SINGLE STATEMENT":

        statement_index = (
            pending_change.get(
                "statement_index"
            )
        )

        statement_source = (
            pending_change.get(
                "statement_source"
            )
        )

        statement_start_line = (
            pending_change.get(
                "statement_start_line"
            )
        )

        statement_end_line = (
            pending_change.get(
                "statement_end_line"
            )
        )

        if statement_index is None:

            return (
                False,
                (
                    "SINGLE STATEMENT change has no "
                    "selected statement."
                ),
            )

        if not statement_source:

            return (
                False,
                (
                    "SINGLE STATEMENT change has no "
                    "stored statement source."
                ),
            )

        if (
            statement_start_line is None
            or statement_end_line is None
        ):

            return (
                False,
                (
                    "SINGLE STATEMENT change has no "
                    "verified statement boundaries."
                ),
            )

    return (
        True,
        (
            "Pre-implementation validation passed. "
            "The approved proposal still matches the "
            "current project source."
        ),
    )


def get_target_top_level_statements(
    target_name: str,
):
    """
    Return the top-level executable statements inside a
    uniquely named function, async function, or class.

    Existing docstrings are excluded from the selectable list.

    This function is read-only.
    """

    matches = (
        find_code_targets(
            target_name
        )
    )

    if not matches:

        return (
            False,
            [],
            (
                f"Target '{target_name}' "
                "was not found."
            ),
        )

    exact_matches = []

    for match in matches:

        if match.get(
            "name"
        ) == target_name:

            exact_matches.append(
                match
            )

    if len(exact_matches) != 1:

        return (
            False,
            [],
            (
                f"Target '{target_name}' "
                "is not uniquely identifiable."
            ),
        )

    file_name = (
        exact_matches[0].get(
            "file"
        )
    )

    if not file_name:

        return (
            False,
            [],
            (
                "Target result does not contain "
                "a source file."
            ),
        )

    file_path = (
        PROJECT_ROOT
        / file_name
    ).resolve()

    if not file_path.exists():

        return (
            False,
            [],
            (
                f"Target file does not exist: "
                f"{file_name}"
            ),
        )

    try:

        source_text = (
            file_path.read_text(
                encoding="utf-8"
            )
        )

        source_tree = (
            ast.parse(
                source_text
            )
        )

    except Exception as error:

        return (
            False,
            [],
            (
                "Could not parse target source: "
                f"{error}"
            ),
        )

    target_nodes = []

    for node in ast.walk(
        source_tree
    ):

        if isinstance(
            node,
            (
                ast.FunctionDef,
                ast.AsyncFunctionDef,
                ast.ClassDef,
            ),
        ):

            if node.name == target_name:

                target_nodes.append(
                    node
                )

    if len(target_nodes) != 1:

        return (
            False,
            [],
            (
                f"Target '{target_name}' "
                "is not unique in the source file."
            ),
        )

    target_node = (
        target_nodes[0]
    )

    source_lines = (
        source_text.splitlines(
            keepends=True
        )
    )

    selectable_statements = []

    for body_index, statement in enumerate(
        target_node.body
    ):

        is_docstring = (
            body_index == 0
            and isinstance(
                statement,
                ast.Expr,
            )
            and isinstance(
                statement.value,
                ast.Constant,
            )
            and isinstance(
                statement.value.value,
                str,
            )
        )

        if is_docstring:

            continue

        if (
            statement.lineno is None
            or statement.end_lineno is None
        ):

            continue

        start_index = (
            statement.lineno - 1
        )

        end_index = (
            statement.end_lineno
        )

        statement_source = "".join(
            source_lines[
                start_index:end_index
            ]
        )

        selectable_statements.append(
            {
                "selection_number": (
                    len(
                        selectable_statements
                    )
                    + 1
                ),
                "body_index": body_index,
                "node_type": (
                    type(statement).__name__
                ),
                "start_line": (
                    statement.lineno
                ),
                "end_line": (
                    statement.end_lineno
                ),
                "source": (
                    statement_source
                ),
                "file": file_name,
            }
        )

    if not selectable_statements:

        return (
            False,
            [],
            (
                f"Target '{target_name}' "
                "contains no selectable statements."
            ),
        )

    return (
        True,
        selectable_statements,
        (
            f"Found "
            f"{len(selectable_statements)} "
            "selectable top-level statements."
        ),
    )


def format_target_statements(
    target_name: str,
) -> str:
    """
    Produce a numbered, read-only view of selectable
    top-level statements inside the requested target.
    """

    success, statements, message = (
        get_target_top_level_statements(
            target_name
        )
    )

    if not success:

        return message

    output_lines = [
        (
            f"SELECTABLE STATEMENTS — "
            f"{target_name}"
        ),
        "",
    ]

    for statement in statements:

        output_lines.append(
            (
                f"[{statement['selection_number']}] "
                f"{statement['node_type']} "
                f"— lines "
                f"{statement['start_line']}"
                f"-"
                f"{statement['end_line']}"
            )
        )

        output_lines.append(
            statement[
                "source"
            ].rstrip()
        )

        output_lines.append(
            "-" * 60
        )

    return "\n".join(
        output_lines
    )


def select_pending_statement(
    selection_number: int,
) -> tuple[bool, str]:
    """
    Explicitly select one existing top-level statement as the
    only legal replacement target for a pending
    SINGLE STATEMENT proposal.

    This function is read-only.
    """

    global _PENDING_CHANGE_APPROVAL

    pending_change = (
        get_pending_change()
    )

    if pending_change is None:

        return (
            False,
            "There is no pending change.",
        )

    if pending_change.get(
        "boundary_type"
    ) != "SINGLE STATEMENT":

        return (
            False,
            (
                "The pending change is not a "
                "SINGLE STATEMENT proposal."
            ),
        )

    if pending_change.get(
        "approved",
        False,
    ):

        return (
            False,
            (
                "The pending change is already approved. "
                "Reject it and create a new proposal before "
                "changing the selected statement."
            ),
        )

    target_name = (
        pending_change.get(
            "target_name"
        )
    )

    success, statements, message = (
        get_target_top_level_statements(
            target_name
        )
    )

    if not success:

        return (
            False,
            message,
        )

    selected_statement = None

    for statement in statements:

        if (
            statement[
                "selection_number"
            ]
            == selection_number
        ):

            selected_statement = (
                statement
            )

            break

    if selected_statement is None:

        return (
            False,
            (
                f"Statement selection "
                f"{selection_number} "
                "does not exist."
            ),
        )

    current_target_source = (
        get_target_source(
            target_name
        )
    )

    original_target_source = (
        pending_change.get(
            "target_source_snapshot"
        )
    )

    if (
        current_target_source
        != original_target_source
    ):

        return (
            False,
            (
                "Current target source no longer matches "
                "the proposal snapshot. Selection blocked."
            ),
        )

    _PENDING_CHANGE_APPROVAL[
        "statement_index"
    ] = selection_number

    _PENDING_CHANGE_APPROVAL[
        "statement_source"
    ] = selected_statement[
        "source"
    ]

    _PENDING_CHANGE_APPROVAL[
        "statement_start_line"
    ] = selected_statement[
        "start_line"
    ]

    _PENDING_CHANGE_APPROVAL[
        "statement_end_line"
    ] = selected_statement[
        "end_line"
    ]

    return (
        True,
        (
            f"Statement {selection_number} selected "
            f"for '{target_name}'.\n"
            f"Lines: "
            f"{selected_statement['start_line']}"
            f"-"
            f"{selected_statement['end_line']}\n"
            "No files have been modified."
        ),
    )


# ============================================================
# BACKUP AND ROLLBACK PREPARATION
# ============================================================


BACKUP_FOLDER_NAME = ".novelist_dev_backups"


def get_backup_folder() -> Path:
    """
    Return the controlled development backup folder.

    The folder is located inside the Novelist project root.
    """

    return (
        PROJECT_ROOT
        / BACKUP_FOLDER_NAME
    )


def get_pending_change_file_path():
    """
    Resolve and validate the single source file associated
    with the current pending change.

    This function is read-only.
    """

    pending_change = get_pending_change()

    if pending_change is None:

        return (
            None,
            "There is no pending change.",
        )

    affected_files = pending_change.get(
        "affected_files",
        [],
    )

    if len(affected_files) != 1:

        return (
            None,
            (
                "Exactly one affected file is required "
                "before backup, rollback, or implementation."
            ),
        )

    file_name = affected_files[0]

    file_path = (
        PROJECT_ROOT
        / file_name
    ).resolve()

    project_root = (
        PROJECT_ROOT.resolve()
    )

    try:

        file_path.relative_to(
            project_root
        )

    except ValueError:

        return (
            None,
            (
                "Affected file is outside the "
                "Novelist project root."
            ),
        )

    if not file_path.exists():

        return (
            None,
            (
                f"Affected file does not exist: "
                f"{file_name}"
            ),
        )

    if not file_path.is_file():

        return (
            None,
            (
                f"Affected path is not a file: "
                f"{file_name}"
            ),
        )

    if file_path.suffix.lower() not in (
        ALLOWED_FILE_EXTENSIONS
    ):

        return (
            None,
            (
                f"File type is not permitted: "
                f"{file_path.suffix}"
            ),
        )

    if file_path.name in BLOCKED_FILENAMES:

        return (
            None,
            (
                f"File is blocked from development "
                f"operations: {file_path.name}"
            ),
        )

    return (
        file_path,
        "Affected file validated.",
    )


def create_pending_change_backup() -> tuple[bool, str]:
    """
    Create a timestamped backup of the affected source file.

    This function does not modify the original source file.
    """

    global _PENDING_CHANGE_APPROVAL

    validation_passed, validation_message = (
        validate_pending_change_state()
    )

    if not validation_passed:

        return (
            False,
            validation_message,
        )

    file_path, file_message = (
        get_pending_change_file_path()
    )

    if file_path is None:

        return (
            False,
            file_message,
        )

    try:

        from datetime import datetime

        backup_folder = get_backup_folder()

        backup_folder.mkdir(
            parents=True,
            exist_ok=True,
        )

        timestamp = datetime.now().strftime(
            "%Y%m%d_%H%M%S_%f"
        )

        backup_file_name = (
            f"{file_path.stem}"
            f"__{timestamp}"
            f"{file_path.suffix}.bak"
        )

        backup_path = (
            backup_folder
            / backup_file_name
        )

        original_bytes = (
            file_path.read_bytes()
        )

        backup_path.write_bytes(
            original_bytes
        )

        if not backup_path.exists():

            return (
                False,
                "Backup file was not created.",
            )

        backup_bytes = (
            backup_path.read_bytes()
        )

        if backup_bytes != original_bytes:

            backup_path.unlink(
                missing_ok=True
            )

            return (
                False,
                (
                    "Backup verification failed. "
                    "Backup was removed."
                ),
            )

        _PENDING_CHANGE_APPROVAL[
            "backup_path"
        ] = str(
            backup_path
        )

        return (
            True,
            (
                "Backup created and verified: "
                f"{backup_path.name}"
            ),
        )

    except Exception as error:

        return (
            False,
            (
                "Backup creation failed: "
                f"{error}"
            ),
        )


def validate_pending_backup() -> tuple[bool, str]:
    """
    Verify that the pending change has a valid backup file
    inside the controlled backup folder.

    This function is read-only.
    """

    pending_change = get_pending_change()

    if pending_change is None:

        return (
            False,
            "There is no pending change.",
        )

    backup_path_value = pending_change.get(
        "backup_path"
    )

    if not backup_path_value:

        return (
            False,
            "No backup has been recorded for this change.",
        )

    backup_path = Path(
        backup_path_value
    ).resolve()

    backup_folder = (
        get_backup_folder()
        .resolve()
    )

    try:

        backup_path.relative_to(
            backup_folder
        )

    except ValueError:

        return (
            False,
            (
                "Recorded backup is outside the "
                "controlled backup folder."
            ),
        )

    if not backup_path.exists():

        return (
            False,
            "Recorded backup file does not exist.",
        )

    if not backup_path.is_file():

        return (
            False,
            "Recorded backup path is not a file.",
        )

    if backup_path.suffix.lower() != ".bak":

        return (
            False,
            "Recorded backup does not have a .bak extension.",
        )

    return (
        True,
        "Recorded backup is valid.",
    )


def validate_backup_matches_current_source() -> tuple[bool, str]:
    """
    Confirm that the verified backup still exactly matches
    the current affected source file before implementation.

    This prevents implementation from starting if the source
    changed after the backup was created.

    This function is read-only.
    """

    backup_valid, backup_message = (
        validate_pending_backup()
    )

    if not backup_valid:

        return (
            False,
            backup_message,
        )

    file_path, file_message = (
        get_pending_change_file_path()
    )

    if file_path is None:

        return (
            False,
            file_message,
        )

    pending_change = get_pending_change()

    backup_path = Path(
        pending_change[
            "backup_path"
        ]
    ).resolve()

    try:

        current_bytes = (
            file_path.read_bytes()
        )

        backup_bytes = (
            backup_path.read_bytes()
        )

    except Exception as error:

        return (
            False,
            (
                "Could not compare backup with current "
                f"source: {error}"
            ),
        )

    if current_bytes != backup_bytes:

        return (
            False,
            (
                "Current source does not match the "
                "verified backup. Implementation blocked."
            ),
        )

    return (
        True,
        (
            "Verified backup exactly matches the "
            "current source file."
        ),
    )


def validate_implementation_readiness() -> tuple[bool, str]:
    """
    Perform the final safety checks required before any
    approved source-code implementation may occur.

    This function is read-only.
    """

    pending_change = get_pending_change()

    if pending_change is None:

        return (
            False,
            "There is no pending change to implement.",
        )

    if not pending_change.get(
        "approved",
        False,
    ):

        return (
            False,
            "Pending change has not been approved.",
        )

    validation_passed, validation_message = (
        validate_pending_change_state()
    )

    if not validation_passed:

        return (
            False,
            validation_message,
        )

    backup_valid, backup_message = (
        validate_pending_backup()
    )

    if not backup_valid:

        return (
            False,
            backup_message,
        )

    backup_matches, backup_match_message = (
        validate_backup_matches_current_source()
    )

    if not backup_matches:

        return (
            False,
            backup_match_message,
        )

    boundary_type = pending_change.get(
        "boundary_type"
    )

    if boundary_type not in {
        "DOCSTRING ONLY",
        "SINGLE STATEMENT",
    }:

        return (
            False,
            (
                "Automatic implementation is currently "
                "restricted to DOCSTRING ONLY and "
                "SINGLE STATEMENT changes."
            ),
        )

    replacement_code = pending_change.get(
        "replacement_code",
        "",
    )

    if not replacement_code.strip():

        return (
            False,
            "Pending change has no replacement code.",
        )

    if boundary_type == "SINGLE STATEMENT":

        if pending_change.get("statement_index") is None:

            return (
                False,
                "SINGLE STATEMENT change has no selected statement.",
            )

        if not pending_change.get("statement_source"):

            return (
                False,
                "SINGLE STATEMENT change has no stored statement source.",
            )

        if pending_change.get("statement_start_line") is None:

            return (
                False,
                "SINGLE STATEMENT change has no stored start line.",
            )

        if pending_change.get("statement_end_line") is None:

            return (
                False,
                "SINGLE STATEMENT change has no stored end line.",
            )

        replacement_valid, replacement_message = (
            validate_single_statement_replacement(
                replacement_code
            )
        )

        if not replacement_valid:

            return (
                False,
                replacement_message,
            )

    return (
        True,
        (
            "Implementation safety gate passed. "
            "The approved change is ready for the "
            "controlled write engine."
        ),
    )


def get_target_ast_node_in_file(
    file_path: Path,
    target_name: str,
):
    """
    Locate a uniquely named function, async function,
    or class inside the specified Python source file.

    This function is read-only.
    """

    try:

        source_text = file_path.read_text(
            encoding="utf-8"
        )

        source_tree = ast.parse(
            source_text
        )

    except Exception as error:

        return (
            None,
            None,
            (
                "Could not parse affected source file: "
                f"{error}"
            ),
        )

    matches = []

    for node in ast.walk(
        source_tree
    ):

        if isinstance(
            node,
            (
                ast.FunctionDef,
                ast.AsyncFunctionDef,
                ast.ClassDef,
            ),
        ):

            if node.name == target_name:

                matches.append(
                    node
                )

    if not matches:

        return (
            None,
            source_text,
            (
                f"Target '{target_name}' was not found "
                f"in {file_path.name}."
            ),
        )

    if len(matches) != 1:

        return (
            None,
            source_text,
            (
                f"Target '{target_name}' is not unique "
                f"in {file_path.name}. Implementation blocked."
            ),
        )

    return (
        matches[0],
        source_text,
        "Target located.",
    )


def build_docstring_replacement_source():
    """
    Build a complete updated source file for a validated
    DOCSTRING ONLY pending change.

    If the target already has a docstring, it is replaced.

    If the target has no docstring, a new docstring is safely
    inserted as the first statement inside the target body.

    No file is written by this function.
    """

    pending_change = get_pending_change()

    if pending_change is None:

        return (
            False,
            None,
            None,
            "There is no pending change.",
        )

    if pending_change.get(
        "boundary_type"
    ) != "DOCSTRING ONLY":

        return (
            False,
            None,
            None,
            (
                "Controlled write engine currently supports "
                "DOCSTRING ONLY changes."
            ),
        )

    file_path, file_message = (
        get_pending_change_file_path()
    )

    if file_path is None:

        return (
            False,
            None,
            None,
            file_message,
        )

    target_name = pending_change.get(
        "target_name"
    )

    replacement_code = pending_change.get(
        "replacement_code",
        "",
    ).strip()

    if not (
        replacement_code.startswith('"""')
        or
        replacement_code.startswith("'''")
    ):

        return (
            False,
            None,
            None,
            (
                "DOCSTRING ONLY replacement does not begin "
                "with a valid triple-quoted string."
            ),
        )

    target_node, source_text, target_message = (
        get_target_ast_node_in_file(
            file_path,
            target_name,
        )
    )

    if target_node is None:

        return (
            False,
            None,
            None,
            target_message,
        )

    if not isinstance(
        target_node,
        (
            ast.FunctionDef,
            ast.AsyncFunctionDef,
            ast.ClassDef,
        ),
    ):

        return (
            False,
            None,
            None,
            (
                "Target type does not support controlled "
                "docstring implementation."
            ),
        )

    if not target_node.body:

        return (
            False,
            None,
            None,
            (
                f"Target '{target_name}' has no body. "
                "Implementation blocked."
            ),
        )

    source_lines = source_text.splitlines(
        keepends=True
    )

    first_statement = (
        target_node.body[0]
    )

    if first_statement.lineno is None:

        return (
            False,
            None,
            None,
            (
                "Python AST did not provide reliable "
                "target-body line boundaries."
            ),
        )

    first_statement_index = (
        first_statement.lineno - 1
    )

    first_statement_line = (
        source_lines[
            first_statement_index
        ]
    )

    indentation = (
        first_statement_line[
            :len(first_statement_line)
            - len(first_statement_line.lstrip())
        ]
    )

    if not indentation:

        return (
            False,
            None,
            None,
            (
                "Could not determine safe target-body "
                "indentation. Implementation blocked."
            ),
        )

    replacement_lines = (
        replacement_code.splitlines()
    )

    if not replacement_lines:

        return (
            False,
            None,
            None,
            "Replacement docstring is empty.",
        )

    normalized_replacement_lines = []

    for line_number, line in enumerate(
        replacement_lines
    ):

        if line_number == 0:

            normalized_replacement_lines.append(
                indentation
                + line.lstrip()
                + "\n"
            )

        else:

            if line.strip():

                normalized_replacement_lines.append(
                    indentation
                    + line.lstrip()
                    + "\n"
                )

            else:

                normalized_replacement_lines.append(
                    "\n"
                )

    is_existing_docstring = (
        isinstance(
            first_statement,
            ast.Expr,
        )
        and isinstance(
            first_statement.value,
            ast.Constant,
        )
        and isinstance(
            first_statement.value.value,
            str,
        )
    )

    if is_existing_docstring:

        if first_statement.end_lineno is None:

            return (
                False,
                None,
                None,
                (
                    "Python AST did not provide reliable "
                    "existing-docstring boundaries."
                ),
            )

        start_index = (
            first_statement.lineno - 1
        )

        end_index = (
            first_statement.end_lineno
        )

        updated_lines = (
            source_lines[:start_index]
            + normalized_replacement_lines
            + source_lines[end_index:]
        )

        operation_message = (
            "Existing docstring replacement"
        )

    else:

        insertion_index = (
            first_statement.lineno - 1
        )

        updated_lines = (
            source_lines[:insertion_index]
            + normalized_replacement_lines
            + source_lines[insertion_index:]
        )

        operation_message = (
            "New docstring insertion"
        )

    updated_source = "".join(
        updated_lines
    )

    try:

        updated_tree = ast.parse(
            updated_source
        )

    except SyntaxError as error:

        return (
            False,
            None,
            None,
            (
                "Proposed source failed Python syntax "
                f"validation: {error}"
            ),
        )

    updated_matches = []

    for node in ast.walk(
        updated_tree
    ):

        if isinstance(
            node,
            (
                ast.FunctionDef,
                ast.AsyncFunctionDef,
                ast.ClassDef,
            ),
        ):

            if node.name == target_name:

                updated_matches.append(
                    node
                )

    if len(updated_matches) != 1:

        return (
            False,
            None,
            None,
            (
                "Post-build target validation failed. "
                "Implementation blocked."
            ),
        )

    updated_target = (
        updated_matches[0]
    )

    updated_docstring = ast.get_docstring(
        updated_target,
        clean=False,
    )

    if updated_docstring is None:

        return (
            False,
            None,
            None,
            (
                "Post-build validation could not confirm "
                "the target docstring."
            ),
        )

    return (
        True,
        file_path,
        updated_source,
        (
            f"{operation_message} built and "
            "syntax validated."
        ),
    )



SIMPLE_STATEMENT_AST_TYPES = (
    ast.Assign,
    ast.AnnAssign,
    ast.AugAssign,
    ast.Expr,
    ast.Return,
    ast.Raise,
    ast.Assert,
    ast.Delete,
    ast.Pass,
)


def is_docstring_statement(statement) -> bool:
    """
    Return True when the AST statement is a Python docstring.

    This helper is read-only.
    """

    return (
        isinstance(statement, ast.Expr)
        and isinstance(statement.value, ast.Constant)
        and isinstance(statement.value.value, str)
    )


def validate_single_statement_replacement(
    replacement_code: str,
) -> tuple[bool, str]:
    """
    Validate that replacement code contains exactly one simple
    Python statement suitable for the first SINGLE STATEMENT
    controlled-write boundary.

    Compound statements, imports, definitions, and multiple
    statements are intentionally rejected.

    This function is read-only.
    """

    cleaned_code = (
        replacement_code
        or ""
    ).strip()

    if not cleaned_code:

        return (
            False,
            "SINGLE STATEMENT replacement is empty.",
        )

    try:

        replacement_tree = ast.parse(
            cleaned_code
        )

    except SyntaxError as error:

        return (
            False,
            (
                "SINGLE STATEMENT replacement failed "
                f"Python syntax validation: {error}"
            ),
        )

    if len(replacement_tree.body) != 1:

        return (
            False,
            (
                "SINGLE STATEMENT replacement must contain "
                "exactly one Python statement."
            ),
        )

    replacement_statement = (
        replacement_tree.body[0]
    )

    if not isinstance(
        replacement_statement,
        SIMPLE_STATEMENT_AST_TYPES,
    ):

        return (
            False,
            (
                "SINGLE STATEMENT replacement must be a simple "
                "statement. Compound statements, imports, "
                "definitions, and control-flow blocks are not "
                "enabled for automatic implementation."
            ),
        )

    return (
        True,
        (
            "SINGLE STATEMENT replacement contains exactly "
            "one supported simple Python statement."
        ),
    )


def normalize_statement_source_for_comparison(
    source_text: str,
) -> str:
    """
    Normalize statement source only for exact-selection safety
    comparisons while preserving statement content.

    This function is read-only.
    """

    lines = (
        source_text
        or ""
    ).strip().splitlines()

    if not lines:

        return ""

    nonblank_lines = [
        line
        for line in lines
        if line.strip()
    ]

    if not nonblank_lines:

        return ""

    indentation_values = [
        len(line) - len(line.lstrip())
        for line in nonblank_lines
    ]

    common_indentation = min(
        indentation_values
    )

    normalized_lines = []

    for line in lines:

        if line.strip():

            normalized_lines.append(
                line[common_indentation:].rstrip()
            )

        else:

            normalized_lines.append("")

    return "\n".join(
        normalized_lines
    ).strip()


def build_single_statement_replacement_source():
    """
    Build a complete updated source file for a validated
    SINGLE STATEMENT pending change.

    The selected original statement is re-located using the
    stored target, line range, and source snapshot before any
    replacement is built.

    Only supported simple top-level statements inside the
    selected function/class body are eligible.

    No file is written by this function.
    """

    pending_change = get_pending_change()

    if pending_change is None:

        return (
            False,
            None,
            None,
            "There is no pending change.",
        )

    if pending_change.get(
        "boundary_type"
    ) != "SINGLE STATEMENT":

        return (
            False,
            None,
            None,
            (
                "SINGLE STATEMENT source builder received "
                "a different replacement boundary."
            ),
        )

    file_path, file_message = (
        get_pending_change_file_path()
    )

    if file_path is None:

        return (
            False,
            None,
            None,
            file_message,
        )

    target_name = pending_change.get(
        "target_name"
    )

    selected_source = pending_change.get(
        "statement_source",
        "",
    )

    selected_start_line = pending_change.get(
        "statement_start_line"
    )

    selected_end_line = pending_change.get(
        "statement_end_line"
    )

    replacement_code = pending_change.get(
        "replacement_code",
        "",
    ).strip()

    replacement_valid, replacement_message = (
        validate_single_statement_replacement(
            replacement_code
        )
    )

    if not replacement_valid:

        return (
            False,
            None,
            None,
            replacement_message,
        )

    target_node, source_text, target_message = (
        get_target_ast_node_in_file(
            file_path,
            target_name,
        )
    )

    if target_node is None:

        return (
            False,
            None,
            None,
            target_message,
        )

    if not isinstance(
        target_node,
        (
            ast.FunctionDef,
            ast.AsyncFunctionDef,
            ast.ClassDef,
        ),
    ):

        return (
            False,
            None,
            None,
            (
                "Target type does not support controlled "
                "SINGLE STATEMENT implementation."
            ),
        )

    matching_statements = []

    for statement in target_node.body:

        if is_docstring_statement(
            statement
        ):

            continue

        if (
            statement.lineno == selected_start_line
            and statement.end_lineno == selected_end_line
        ):

            matching_statements.append(
                statement
            )

    if len(matching_statements) != 1:

        return (
            False,
            None,
            None,
            (
                "The previously selected statement could not "
                "be uniquely re-located at its stored line range. "
                "Implementation blocked."
            ),
        )

    selected_statement = (
        matching_statements[0]
    )

    if not isinstance(
        selected_statement,
        SIMPLE_STATEMENT_AST_TYPES,
    ):

        return (
            False,
            None,
            None,
            (
                "The selected original statement is not a "
                "supported simple statement. Compound statements, "
                "imports, definitions, and control-flow blocks are "
                "not enabled for automatic implementation."
            ),
        )

    if (
        selected_statement.lineno is None
        or selected_statement.end_lineno is None
    ):

        return (
            False,
            None,
            None,
            (
                "Python AST did not provide reliable selected-"
                "statement line boundaries."
            ),
        )

    source_lines = source_text.splitlines(
        keepends=True
    )

    start_index = (
        selected_statement.lineno - 1
    )

    end_index = (
        selected_statement.end_lineno
    )

    current_statement_source = "".join(
        source_lines[
            start_index:end_index
        ]
    )

    normalized_current_source = (
        normalize_statement_source_for_comparison(
            current_statement_source
        )
    )

    normalized_selected_source = (
        normalize_statement_source_for_comparison(
            selected_source
        )
    )

    if (
        not normalized_selected_source
        or normalized_current_source
        != normalized_selected_source
    ):

        return (
            False,
            None,
            None,
            (
                "The selected statement source no longer exactly "
                "matches the stored selection. Implementation "
                "blocked."
            ),
        )

    original_first_line = (
        source_lines[
            start_index
        ]
    )

    indentation = (
        original_first_line[
            :len(original_first_line)
            - len(original_first_line.lstrip())
        ]
    )

    replacement_lines = (
        replacement_code.splitlines()
    )

    if not replacement_lines:

        return (
            False,
            None,
            None,
            "SINGLE STATEMENT replacement is empty.",
        )

    replacement_source_lines = []

    for line in replacement_lines:

        if line.strip():

            replacement_source_lines.append(
                indentation
                + line.lstrip()
                + "\n"
            )

        else:

            replacement_source_lines.append(
                "\n"
            )

    updated_lines = (
        source_lines[:start_index]
        + replacement_source_lines
        + source_lines[end_index:]
    )

    updated_source = "".join(
        updated_lines
    )

    try:

        updated_tree = ast.parse(
            updated_source
        )

    except SyntaxError as error:

        return (
            False,
            None,
            None,
            (
                "Proposed SINGLE STATEMENT source failed "
                f"Python syntax validation: {error}"
            ),
        )

    updated_matches = []

    for node in ast.walk(
        updated_tree
    ):

        if isinstance(
            node,
            (
                ast.FunctionDef,
                ast.AsyncFunctionDef,
                ast.ClassDef,
            ),
        ):

            if node.name == target_name:

                updated_matches.append(
                    node
                )

    if len(updated_matches) != 1:

        return (
            False,
            None,
            None,
            (
                "Post-build target validation failed. "
                "Implementation blocked."
            ),
        )

    updated_target = (
        updated_matches[0]
    )

    updated_statement_matches = []

    for statement in updated_target.body:

        if is_docstring_statement(
            statement
        ):

            continue

        statement_source = ast.get_source_segment(
            updated_source,
            statement,
        )

        if statement_source is None:

            continue

        if (
            normalize_statement_source_for_comparison(
                statement_source
            )
            == normalize_statement_source_for_comparison(
                replacement_code
            )
        ):

            updated_statement_matches.append(
                statement
            )

    if not updated_statement_matches:

        return (
            False,
            None,
            None,
            (
                "Post-build validation could not confirm the "
                "replacement statement inside the target."
            ),
        )

    return (
        True,
        file_path,
        updated_source,
        (
            "SINGLE STATEMENT replacement source built, "
            "re-located, and syntax validated."
        ),
    )


def normalize_logical_block_source_for_comparison(
    source: str,
) -> str:
    """
    Normalize a complete logical block for source-comparison checks.

    Leading/trailing blank lines are removed and common indentation
    is stripped without changing relative indentation inside the block.
    """

    source = (
        source
        or ""
    ).strip("\n")

    if not source.strip():

        return ""

    lines = source.splitlines()

    non_blank_indents = [
        len(line) - len(line.lstrip())
        for line in lines
        if line.strip()
    ]

    common_indent = (
        min(non_blank_indents)
        if non_blank_indents
        else 0
    )

    normalized_lines = [
        (
            line[common_indent:].rstrip()
            if line.strip()
            else ""
        )
        for line in lines
    ]

    return "\n".join(
        normalized_lines
    ).strip()


def get_logical_block_ast_signature(
    source: str,
) -> str | None:
    """
    Return a stable AST signature for exactly one supported
    logical-block statement.
    """

    try:

        tree = ast.parse(
            source
        )

    except SyntaxError:

        return None

    if len(tree.body) != 1:

        return None

    node = tree.body[0]

    if not isinstance(
        node,
        LOGICAL_BLOCK_AST_TYPES,
    ):

        return None

    return ast.dump(
        node,
        include_attributes=False,
    )


def find_matching_logical_block_in_target(
    target_node,
    source_text: str,
    expected_start_line: int,
    expected_type: str,
    expected_signature: str,
):
    """
    Find the exact written logical block inside one target using
    stored start-line/type metadata plus the replacement AST signature.

    Nested function/class scopes are excluded.
    """

    matches = []

    def visit_statement(statement):

        if isinstance(
            statement,
            (
                ast.FunctionDef,
                ast.AsyncFunctionDef,
                ast.ClassDef,
            ),
        ):

            return

        if (
            isinstance(
                statement,
                LOGICAL_BLOCK_AST_TYPES,
            )
            and getattr(
                statement,
                "lineno",
                None,
            )
            == expected_start_line
            and type(
                statement
            ).__name__
            == expected_type
        ):

            statement_source = (
                ast.get_source_segment(
                    source_text,
                    statement,
                )
                or ""
            )

            signature = (
                get_logical_block_ast_signature(
                    normalize_logical_block_source_for_comparison(
                        statement_source
                    )
                )
            )

            if signature == expected_signature:

                matches.append(
                    statement
                )

        child_groups = []

        if isinstance(
            statement,
            ast.If,
        ):

            child_groups.extend(
                [
                    statement.body,
                    statement.orelse,
                ]
            )

        elif isinstance(
            statement,
            (
                ast.For,
                ast.AsyncFor,
                ast.While,
            ),
        ):

            child_groups.extend(
                [
                    statement.body,
                    statement.orelse,
                ]
            )

        elif isinstance(
            statement,
            ast.Try,
        ):

            child_groups.extend(
                [
                    statement.body,
                    statement.orelse,
                    statement.finalbody,
                ]
            )

            for handler in statement.handlers:

                child_groups.append(
                    handler.body
                )

        elif isinstance(
            statement,
            (
                ast.With,
                ast.AsyncWith,
            ),
        ):

            child_groups.append(
                statement.body
            )

        elif isinstance(
            statement,
            ast.Match,
        ):

            for case in statement.cases:

                child_groups.append(
                    case.body
                )

        else:

            for field_name in (
                "body",
                "orelse",
                "finalbody",
            ):

                possible_group = getattr(
                    statement,
                    field_name,
                    None,
                )

                if isinstance(
                    possible_group,
                    list,
                ):

                    child_groups.append(
                        possible_group
                    )

        for child_group in child_groups:

            for child_statement in child_group:

                if isinstance(
                    child_statement,
                    ast.stmt,
                ):

                    visit_statement(
                        child_statement
                    )

    for statement in getattr(
        target_node,
        "body",
        [],
    ):

        if isinstance(
            statement,
            ast.stmt,
        ):

            visit_statement(
                statement
            )

    return matches


def build_logical_block_replacement_source():
    """
    Build a complete updated source file for one fully validated
    LOGICAL BLOCK pending change.

    This function does not write the project file.
    """

    readiness_passed, readiness_message = (
        validate_pending_logical_block_readiness()
    )

    if not readiness_passed:

        return (
            False,
            None,
            None,
            readiness_message,
        )

    pending_change = get_pending_change()

    if (
        pending_change is None
        or pending_change.get(
            "boundary_type"
        )
        != "LOGICAL BLOCK"
    ):

        return (
            False,
            None,
            None,
            (
                "LOGICAL BLOCK source builder received "
                "a different replacement boundary."
            ),
        )

    file_path, file_message = (
        get_pending_change_file_path()
    )

    if file_path is None:

        return (
            False,
            None,
            None,
            file_message,
        )

    target_name = pending_change.get(
        "target_name"
    )

    selected_start_line = pending_change.get(
        "block_start_line"
    )

    selected_end_line = pending_change.get(
        "block_end_line"
    )

    selected_type = pending_change.get(
        "block_type"
    )

    selected_source = (
        pending_change.get(
            "block_source",
            ""
        )
        or ""
    )

    replacement_code = (
        pending_change.get(
            "replacement_code",
            ""
        )
        or ""
    ).strip()

    try:

        replacement_tree = ast.parse(
            replacement_code
        )

    except SyntaxError as error:

        return (
            False,
            None,
            None,
            (
                "LOGICAL BLOCK replacement is not valid Python: "
                f"{error}"
            ),
        )

    if len(
        replacement_tree.body
    ) != 1:

        return (
            False,
            None,
            None,
            (
                "LOGICAL BLOCK replacement must contain exactly "
                "one complete Python statement."
            ),
        )

    replacement_node = (
        replacement_tree.body[0]
    )

    if not isinstance(
        replacement_node,
        LOGICAL_BLOCK_AST_TYPES,
    ):

        return (
            False,
            None,
            None,
            (
                "LOGICAL BLOCK replacement is not a supported "
                "logical-block AST type."
            ),
        )

    replacement_type = type(
        replacement_node
    ).__name__

    if replacement_type != selected_type:

        return (
            False,
            None,
            None,
            (
                "LOGICAL BLOCK replacement type does not match "
                "the stored source block type."
            ),
        )

    replacement_signature = ast.dump(
        replacement_node,
        include_attributes=False,
    )

    target_node, source_text, target_message = (
        get_target_ast_node_in_file(
            file_path,
            target_name,
        )
    )

    if target_node is None:

        return (
            False,
            None,
            None,
            target_message,
        )

    current_matches = []

    for statement in ast.walk(
        target_node
    ):

        if isinstance(
            statement,
            (
                ast.FunctionDef,
                ast.AsyncFunctionDef,
                ast.ClassDef,
            ),
        ) and statement is not target_node:

            continue

        if (
            isinstance(
                statement,
                LOGICAL_BLOCK_AST_TYPES,
            )
            and getattr(
                statement,
                "lineno",
                None,
            )
            == selected_start_line
            and getattr(
                statement,
                "end_lineno",
                None,
            )
            == selected_end_line
            and type(
                statement
            ).__name__
            == selected_type
        ):

            statement_source = (
                ast.get_source_segment(
                    source_text,
                    statement,
                )
                or ""
            ).strip()

            if statement_source == selected_source.strip():

                current_matches.append(
                    statement
                )

    if len(current_matches) != 1:

        return (
            False,
            None,
            None,
            (
                "The previously selected LOGICAL BLOCK could not "
                "be uniquely re-located at its stored line range "
                "with its stored source. Implementation blocked."
            ),
        )

    source_lines = source_text.splitlines(
        keepends=True
    )

    start_index = (
        selected_start_line - 1
    )

    end_index = (
        selected_end_line
    )

    if (
        start_index < 0
        or end_index > len(source_lines)
        or start_index >= end_index
    ):

        return (
            False,
            None,
            None,
            (
                "Stored LOGICAL BLOCK line boundaries are invalid."
            ),
        )

    original_first_line = (
        source_lines[
            start_index
        ]
    )

    base_indentation = (
        original_first_line[
            :len(original_first_line)
            - len(original_first_line.lstrip())
        ]
    )

    replacement_lines = (
        replacement_code.splitlines()
    )

    if not replacement_lines:

        return (
            False,
            None,
            None,
            "LOGICAL BLOCK replacement is empty.",
        )

    non_blank_indents = [
        len(line) - len(line.lstrip())
        for line in replacement_lines
        if line.strip()
    ]

    common_indent = (
        min(non_blank_indents)
        if non_blank_indents
        else 0
    )

    replacement_source_lines = []

    for line in replacement_lines:

        if line.strip():

            relative_line = (
                line[common_indent:]
            )

            replacement_source_lines.append(
                base_indentation
                + relative_line.rstrip()
                + "\n"
            )

        else:

            replacement_source_lines.append(
                "\n"
            )

    updated_lines = (
        source_lines[:start_index]
        + replacement_source_lines
        + source_lines[end_index:]
    )

    updated_source = "".join(
        updated_lines
    )

    try:

        updated_tree = ast.parse(
            updated_source
        )

    except SyntaxError as error:

        return (
            False,
            None,
            None,
            (
                "Proposed LOGICAL BLOCK source failed "
                f"Python syntax validation: {error}"
            ),
        )

    updated_matches = []

    for node in ast.walk(
        updated_tree
    ):

        if isinstance(
            node,
            (
                ast.FunctionDef,
                ast.AsyncFunctionDef,
                ast.ClassDef,
            ),
        ) and node.name == target_name:

            updated_matches.append(
                node
            )

    if len(updated_matches) != 1:

        return (
            False,
            None,
            None,
            (
                "Post-build target validation failed. "
                "Implementation blocked."
            ),
        )

    replacement_matches = (
        find_matching_logical_block_in_target(
            updated_matches[0],
            updated_source,
            selected_start_line,
            selected_type,
            replacement_signature,
        )
    )

    if len(replacement_matches) != 1:

        return (
            False,
            None,
            None,
            (
                "Post-build validation could not uniquely confirm "
                "the replacement LOGICAL BLOCK inside the target."
            ),
        )

    return (
        True,
        file_path,
        updated_source,
        (
            "LOGICAL BLOCK replacement source built, "
            "re-located, and syntax validated."
        ),
    )



def implement_pending_change() -> tuple[bool, str]:
    """
    Apply an explicitly approved and fully validated
    DOCSTRING ONLY, SINGLE STATEMENT, or LOGICAL BLOCK change
    to the affected
    Python file.

    The write occurs only after:
    - explicit approval
    - source-state validation
    - verified backup creation
    - backup/current-source equality
    - replacement-boundary validation
    - exact statement re-location for SINGLE STATEMENT
    - exact source-backed block re-location for LOGICAL BLOCK
    - Python syntax validation

    If post-write verification fails, rollback is attempted.
    """

    global _PENDING_CHANGE_APPROVAL

    pending_change = get_pending_change()

    if (
        pending_change is not None
        and pending_change.get(
            "boundary_type"
        )
        == "LOGICAL BLOCK"
    ):

        readiness_passed, readiness_message = (
            validate_pending_logical_block_readiness()
        )

    else:

        readiness_passed, readiness_message = (
            validate_implementation_readiness()
        )

    if not readiness_passed:

        return (
            False,
            readiness_message,
        )

    pending_change = get_pending_change()

    boundary_type = pending_change.get(
        "boundary_type"
    )

    if boundary_type == "DOCSTRING ONLY":

        build_passed, file_path, updated_source, build_message = (
            build_docstring_replacement_source()
        )

    elif boundary_type == "SINGLE STATEMENT":

        build_passed, file_path, updated_source, build_message = (
            build_single_statement_replacement_source()
        )

    elif boundary_type == "LOGICAL BLOCK":

        build_passed, file_path, updated_source, build_message = (
            build_logical_block_replacement_source()
        )

    else:

        return (
            False,
            (
                "Automatic implementation is currently "
                "restricted to DOCSTRING ONLY, "
                "SINGLE STATEMENT, and LOGICAL BLOCK changes."
            ),
        )

    if not build_passed:

        return (
            False,
            build_message,
        )

    backup_path = Path(
        pending_change[
            "backup_path"
        ]
    ).resolve()

    temporary_path = (
        file_path.parent
        / (
            f".{file_path.name}"
            ".novelist_dev_temp"
        )
    )

    try:

        original_bytes = (
            file_path.read_bytes()
        )

        backup_bytes = (
            backup_path.read_bytes()
        )

        if original_bytes != backup_bytes:

            return (
                False,
                (
                    "Source changed after backup validation. "
                    "Implementation blocked."
                ),
            )

        updated_bytes = (
            updated_source.encode(
                "utf-8"
            )
        )

        if updated_bytes == original_bytes:

            return (
                False,
                (
                    "Proposed implementation would not "
                    "change the source file."
                ),
            )

        temporary_path.write_bytes(
            updated_bytes
        )

        temporary_bytes = (
            temporary_path.read_bytes()
        )

        if temporary_bytes != updated_bytes:

            temporary_path.unlink(
                missing_ok=True
            )

            return (
                False,
                (
                    "Temporary implementation file failed "
                    "verification. Source was not modified."
                ),
            )

        try:

            temporary_source = (
                temporary_bytes.decode(
                    "utf-8"
                )
            )

            temporary_tree = ast.parse(
                temporary_source
            )

        except SyntaxError as error:

            temporary_path.unlink(
                missing_ok=True
            )

            return (
                False,
                (
                    "Temporary implementation failed "
                    f"syntax validation: {error}"
                ),
            )

        target_name = pending_change.get(
            "target_name"
        )

        temporary_matches = []

        for node in ast.walk(
            temporary_tree
        ):

            if isinstance(
                node,
                (
                    ast.FunctionDef,
                    ast.AsyncFunctionDef,
                    ast.ClassDef,
                ),
            ):

                if node.name == target_name:

                    temporary_matches.append(
                        node
                    )

        if len(temporary_matches) != 1:

            temporary_path.unlink(
                missing_ok=True
            )

            return (
                False,
                (
                    "Temporary implementation could not "
                    "uniquely confirm the target."
                ),
            )

        temporary_target = (
            temporary_matches[0]
        )

        if boundary_type == "DOCSTRING ONLY":

            temporary_docstring = ast.get_docstring(
                temporary_target,
                clean=False,
            )

            if temporary_docstring is None:

                temporary_path.unlink(
                    missing_ok=True
                )

                return (
                    False,
                    (
                        "Temporary implementation could not "
                        "confirm the target docstring."
                    ),
                )

        elif boundary_type == "SINGLE STATEMENT":

            replacement_code = pending_change.get(
                "replacement_code",
                "",
            )

            normalized_replacement = (
                normalize_statement_source_for_comparison(
                    replacement_code
                )
            )

            temporary_statement_found = False

            for statement in temporary_target.body:

                if is_docstring_statement(
                    statement
                ):

                    continue

                statement_source = ast.get_source_segment(
                    temporary_source,
                    statement,
                )

                if statement_source is None:

                    continue

                if (
                    normalize_statement_source_for_comparison(
                        statement_source
                    )
                    == normalized_replacement
                ):

                    temporary_statement_found = True
                    break

            if not temporary_statement_found:

                temporary_path.unlink(
                    missing_ok=True
                )

                return (
                    False,
                    (
                        "Temporary implementation could not "
                        "confirm the replacement statement "
                        "inside the selected target."
                    ),
                )

        elif boundary_type == "LOGICAL BLOCK":

            replacement_code = pending_change.get(
                "replacement_code",
                "",
            )

            replacement_signature = (
                get_logical_block_ast_signature(
                    replacement_code
                )
            )

            if replacement_signature is None:

                temporary_path.unlink(
                    missing_ok=True
                )

                return (
                    False,
                    (
                        "Temporary implementation could not "
                        "validate the replacement LOGICAL BLOCK."
                    ),
                )

            temporary_block_matches = (
                find_matching_logical_block_in_target(
                    temporary_target,
                    temporary_source,
                    pending_change.get(
                        "block_start_line"
                    ),
                    pending_change.get(
                        "block_type"
                    ),
                    replacement_signature,
                )
            )

            if len(temporary_block_matches) != 1:

                temporary_path.unlink(
                    missing_ok=True
                )

                return (
                    False,
                    (
                        "Temporary implementation could not "
                        "uniquely confirm the replacement "
                        "LOGICAL BLOCK inside the selected target."
                    ),
                )

        os.replace(
            temporary_path,
            file_path,
        )

        written_bytes = (
            file_path.read_bytes()
        )

        if written_bytes != updated_bytes:

            rollback_completed, rollback_message = (
                rollback_pending_change_backup()
            )

            return (
                False,
                (
                    "Post-write verification failed. "
                    f"Rollback result: {rollback_message} "
                    f"Rollback successful: {rollback_completed}"
                ),
            )

        try:

            written_source = (
                written_bytes.decode(
                    "utf-8"
                )
            )

            written_tree = ast.parse(
                written_source
            )

        except SyntaxError as error:

            rollback_completed, rollback_message = (
                rollback_pending_change_backup()
            )

            return (
                False,
                (
                    "Written source failed syntax validation: "
                    f"{error}. "
                    f"Rollback result: {rollback_message} "
                    f"Rollback successful: {rollback_completed}"
                ),
            )

        written_matches = []

        for node in ast.walk(
            written_tree
        ):

            if isinstance(
                node,
                (
                    ast.FunctionDef,
                    ast.AsyncFunctionDef,
                    ast.ClassDef,
                ),
            ):

                if node.name == target_name:

                    written_matches.append(
                        node
                    )

        if len(written_matches) != 1:

            rollback_completed, rollback_message = (
                rollback_pending_change_backup()
            )

            return (
                False,
                (
                    "Written source target verification failed. "
                    f"Rollback result: {rollback_message} "
                    f"Rollback successful: {rollback_completed}"
                ),
            )

        written_target = (
            written_matches[0]
        )

        if boundary_type == "DOCSTRING ONLY":

            written_docstring = ast.get_docstring(
                written_target,
                clean=False,
            )

            if written_docstring is None:

                rollback_completed, rollback_message = (
                    rollback_pending_change_backup()
                )

                return (
                    False,
                    (
                        "Written source docstring verification failed. "
                        f"Rollback result: {rollback_message} "
                        f"Rollback successful: {rollback_completed}"
                    ),
                )

        elif boundary_type == "SINGLE STATEMENT":

            normalized_replacement = (
                normalize_statement_source_for_comparison(
                    pending_change.get(
                        "replacement_code",
                        "",
                    )
                )
            )

            written_statement_found = False

            for statement in written_target.body:

                if is_docstring_statement(
                    statement
                ):

                    continue

                statement_source = ast.get_source_segment(
                    written_source,
                    statement,
                )

                if statement_source is None:

                    continue

                if (
                    normalize_statement_source_for_comparison(
                        statement_source
                    )
                    == normalized_replacement
                ):

                    written_statement_found = True
                    break

            if not written_statement_found:

                rollback_completed, rollback_message = (
                    rollback_pending_change_backup()
                )

                return (
                    False,
                    (
                        "Written source SINGLE STATEMENT "
                        "verification failed. "
                        f"Rollback result: {rollback_message} "
                        f"Rollback successful: {rollback_completed}"
                    ),
                )

        elif boundary_type == "LOGICAL BLOCK":

            replacement_signature = (
                get_logical_block_ast_signature(
                    pending_change.get(
                        "replacement_code",
                        "",
                    )
                )
            )

            written_block_matches = []

            if replacement_signature is not None:

                written_block_matches = (
                    find_matching_logical_block_in_target(
                        written_target,
                        written_source,
                        pending_change.get(
                            "block_start_line"
                        ),
                        pending_change.get(
                            "block_type"
                        ),
                        replacement_signature,
                    )
                )

            if len(written_block_matches) != 1:

                rollback_completed, rollback_message = (
                    rollback_pending_change_backup()
                )

                return (
                    False,
                    (
                        "Written source LOGICAL BLOCK "
                        "verification failed. "
                        f"Rollback result: {rollback_message} "
                        f"Rollback successful: {rollback_completed}"
                    ),
                )

        clear_project_analysis_cache()

        _PENDING_CHANGE_APPROVAL[
            "implemented"
        ] = True

        _PENDING_CHANGE_APPROVAL[
            "implemented_file"
        ] = str(
            file_path
        )

        return (
            True,
            (
                f"Approved {boundary_type} change implemented "
                f"and verified in {file_path.name}. "
                "Verified backup remains available for rollback."
            ),
        )

    except Exception as error:

        temporary_path.unlink(
            missing_ok=True
        )

        try:

            current_bytes = (
                file_path.read_bytes()
            )

            backup_bytes = (
                backup_path.read_bytes()
            )

            if current_bytes != backup_bytes:

                rollback_completed, rollback_message = (
                    rollback_pending_change_backup()
                )

                return (
                    False,
                    (
                        "Implementation failed after source "
                        f"modification: {error}. "
                        f"Rollback result: {rollback_message} "
                        f"Rollback successful: {rollback_completed}"
                    ),
                )

        except Exception:

            pass

        return (
            False,
            (
                "Implementation failed before completion: "
                f"{error}"
            ),
        )


def rollback_pending_change_backup() -> tuple[bool, str]:
    """
    Restore the affected source file from the verified
    backup associated with the current pending change.

    This operation overwrites the affected source file
    with the previously verified backup contents.
    """

    backup_valid, backup_message = (
        validate_pending_backup()
    )

    if not backup_valid:

        return (
            False,
            backup_message,
        )

    file_path, file_message = (
        get_pending_change_file_path()
    )

    if file_path is None:

        return (
            False,
            file_message,
        )

    pending_change = get_pending_change()

    backup_path = Path(
        pending_change[
            "backup_path"
        ]
    ).resolve()

    try:

        backup_bytes = (
            backup_path.read_bytes()
        )

        if not backup_bytes:

            return (
                False,
                "Backup file is empty.",
            )

        file_path.write_bytes(
            backup_bytes
        )

        restored_bytes = (
            file_path.read_bytes()
        )

        if restored_bytes != backup_bytes:

            return (
                False,
                (
                    "Rollback verification failed. "
                    "Restored source does not match backup."
                ),
            )

        clear_project_analysis_cache()

        if pending_change is not None:

            pending_change[
                "implemented"
            ] = False

        return (
            True,
            (
                "Rollback completed and verified for "
                f"{file_path.name}."
            ),
        )

    except Exception as error:

        return (
            False,
            (
                "Rollback failed: "
                f"{error}"
            ),
        )



# ============================================================
# IMPLEMENTATION AUDIT LOGGING
# ============================================================


AUDIT_FOLDER_NAME = ".novelist_dev_audit"
AUDIT_LOG_FILE_NAME = "implementation_audit.jsonl"


def get_audit_log_folder() -> Path:
    """
    Return the controlled audit-log folder inside the project root.

    This function is read-only and does not create the folder.
    """

    return (
        PROJECT_ROOT
        / AUDIT_FOLDER_NAME
    )


def get_audit_log_path() -> Path:
    """
    Return the controlled append-only implementation audit-log path.

    This function is read-only and does not create the file.
    """

    return (
        get_audit_log_folder()
        / AUDIT_LOG_FILE_NAME
    )


def build_audit_event_record(
    event_type: str,
    success=None,
    message: str = "",
    details=None,
) -> dict:
    """
    Build a structured audit record from the current pending change.

    Building the record does not write anything to disk.
    """

    from datetime import datetime, timezone

    pending_change = get_pending_change()

    if pending_change is None:

        pending_snapshot = None

    else:

        backup_path_value = pending_change.get(
            "backup_path"
        )

        backup_file_name = None

        if backup_path_value:

            try:

                backup_file_name = Path(
                    backup_path_value
                ).name

            except Exception:

                backup_file_name = str(
                    backup_path_value
                )

        pending_snapshot = {
            "target_name": pending_change.get(
                "target_name"
            ),
            "development_request": pending_change.get(
                "development_request"
            ),
            "boundary_type": pending_change.get(
                "boundary_type"
            ),
            "affected_files": list(
                pending_change.get(
                    "affected_files",
                    [],
                )
            ),
            "approved": bool(
                pending_change.get(
                    "approved",
                    False,
                )
            ),
            "implemented": bool(
                pending_change.get(
                    "implemented",
                    False,
                )
            ),
            "backup_file": backup_file_name,
            "statement_index": pending_change.get(
                "statement_index"
            ),
            "statement_start_line": pending_change.get(
                "statement_start_line"
            ),
            "statement_end_line": pending_change.get(
                "statement_end_line"
            ),
            "statement_source": pending_change.get(
                "statement_source"
            ),
            "replacement_code": pending_change.get(
                "replacement_code"
            ),
        }

    record = {
        "timestamp_utc": datetime.now(
            timezone.utc
        ).isoformat(),
        "event_type": str(
            event_type
        ).strip(),
        "success": success,
        "message": str(
            message
        ),
        "pending_change": pending_snapshot,
        "details": details or {},
    }

    return record


def append_audit_event(
    event_type: str,
    success=None,
    message: str = "",
    details=None,
) -> tuple[bool, str]:
    """
    Append one structured JSON record to the controlled audit log.

    Existing audit records are never rewritten by this function.
    """

    import json

    if not str(
        event_type
    ).strip():

        return (
            False,
            "Audit event type is required.",
        )

    audit_folder = (
        get_audit_log_folder()
        .resolve()
    )

    audit_path = (
        get_audit_log_path()
        .resolve()
    )

    project_root = (
        PROJECT_ROOT.resolve()
    )

    try:

        audit_folder.relative_to(
            project_root
        )

        audit_path.relative_to(
            audit_folder
        )

    except ValueError:

        return (
            False,
            (
                "Audit log path is outside the controlled "
                "Novelist project location."
            ),
        )

    try:

        audit_folder.mkdir(
            parents=True,
            exist_ok=True,
        )

        record = build_audit_event_record(
            event_type=event_type,
            success=success,
            message=message,
            details=details,
        )

        serialized_record = json.dumps(
            record,
            ensure_ascii=False,
            separators=(
                ",",
                ":",
            ),
        )

        with audit_path.open(
            "a",
            encoding="utf-8",
            newline="\n",
        ) as audit_file:

            audit_file.write(
                serialized_record
                + "\n"
            )

            audit_file.flush()

            os.fsync(
                audit_file.fileno()
            )

        return (
            True,
            (
                "Audit event recorded: "
                f"{record['event_type']}"
            ),
        )

    except Exception as error:

        return (
            False,
            (
                "Audit logging failed: "
                f"{error}"
            ),
        )


# Preserve the proven approval function, then wrap it with
# append-only audit logging without changing approval behavior.
_APPROVE_PENDING_CHANGE_CORE = approve_pending_change


def approve_pending_change():
    """
    Run the existing approval gate and record the result in the
    implementation audit log.

    Audit-log failure never changes the approval result.
    """

    result = _APPROVE_PENDING_CHANGE_CORE()

    pending_change = get_pending_change()

    approval_succeeded = bool(
        pending_change
        and pending_change.get(
            "approved",
            False,
        )
    )

    event_type = (
        "CHANGE_APPROVED"
        if approval_succeeded
        else "CHANGE_APPROVAL_BLOCKED"
    )

    append_audit_event(
        event_type=event_type,
        success=approval_succeeded,
        message=str(result),
        details={
            "action": "approve",
        },
    )

    return result


# Preserve the proven backup function, then wrap it with
# append-only audit logging without changing backup behavior.
_CREATE_PENDING_CHANGE_BACKUP_CORE = create_pending_change_backup


def create_pending_change_backup() -> tuple[bool, str]:
    """
    Run the existing backup gate and record the result in the
    implementation audit log.

    Audit-log failure never changes the backup result.
    """

    backup_succeeded, backup_message = (
        _CREATE_PENDING_CHANGE_BACKUP_CORE()
    )

    event_type = (
        "BACKUP_CREATED"
        if backup_succeeded
        else "BACKUP_CREATION_BLOCKED"
    )

    append_audit_event(
        event_type=event_type,
        success=backup_succeeded,
        message=backup_message,
        details={
            "action": "backup",
        },
    )

    return (
        backup_succeeded,
        backup_message,
    )


# Preserve the proven implementation function, then wrap it with
# append-only audit logging and automatic post-change verification.
_IMPLEMENT_PENDING_CHANGE_CORE = implement_pending_change


def implement_pending_change() -> tuple[bool, str]:
    """
    Run the existing controlled implementation engine.

    After a successful write:
    1. Validate syntax across all active project Python files.
    2. Execute the controlled project unittest suite.
    3. Report implementation success only when both checks pass.
    4. Keep the verified backup available for manual rollback if
       post-change verification fails.

    Audit-log failure never changes the implementation result.
    """

    implementation_succeeded, implementation_message = (
        _IMPLEMENT_PENDING_CHANGE_CORE()
    )

    if not implementation_succeeded:

        append_audit_event(
            event_type="IMPLEMENTATION_BLOCKED",
            success=False,
            message=implementation_message,
            details={
                "action": "implement",
                "post_change_verification_run": False,
            },
        )

        return (
            False,
            implementation_message,
        )

    syntax_passed, syntax_message = (
        run_project_syntax_validation()
    )

    unit_tests_passed = False
    unit_tests_message = (
        "Unit tests were not executed because "
        "project syntax validation failed."
    )

    if syntax_passed:

        unit_tests_passed, unit_tests_message = (
            run_project_unit_tests()
        )

    verification_passed = bool(
        syntax_passed
        and unit_tests_passed
    )

    pending_change = get_pending_change()

    if pending_change is not None:

        pending_change[
            "post_implementation_syntax_passed"
        ] = syntax_passed

        pending_change[
            "post_implementation_unit_tests_passed"
        ] = unit_tests_passed

        pending_change[
            "post_implementation_verification_passed"
        ] = verification_passed

    verification_message = "\n".join(
        [
            implementation_message,
            "",
            "POST-IMPLEMENTATION VERIFICATION",
            "",
            syntax_message,
            "",
            (
                "Syntax Validation Passed: "
                f"{syntax_passed}"
            ),
            "",
            unit_tests_message,
            "",
            (
                "Unit Tests Passed: "
                f"{unit_tests_passed}"
            ),
            "",
            (
                "Post-Implementation Verification: "
                + (
                    "PASSED"
                    if verification_passed
                    else "FAILED"
                )
            ),
        ]
    )

    if verification_passed:

        append_audit_event(
            event_type="IMPLEMENTATION_COMPLETED",
            success=True,
            message=verification_message,
            details={
                "action": "implement",
                "post_change_verification_run": True,
                "syntax_validation_passed": True,
                "unit_tests_passed": True,
                "post_change_verification_passed": True,
            },
        )

        append_audit_event(
            event_type="POST_IMPLEMENTATION_VERIFICATION_PASSED",
            success=True,
            message=(
                "Automatic post-implementation syntax validation "
                "and unit tests passed."
            ),
            details={
                "action": "post_implementation_verification",
                "syntax_validation_passed": True,
                "unit_tests_passed": True,
            },
        )

        return (
            True,
            verification_message,
        )

    verification_failure_message = "\n".join(
        [
            verification_message,
            "",
            (
                "The approved change was written, but automatic "
                "post-implementation verification failed."
            ),
            (
                "Automatic rollback will now restore the verified "
                "pre-change backup."
            ),
        ]
    )

    append_audit_event(
        event_type="IMPLEMENTATION_VERIFICATION_FAILED",
        success=False,
        message=verification_failure_message,
        details={
            "action": "implement",
            "post_change_verification_run": True,
            "syntax_validation_passed": syntax_passed,
            "unit_tests_passed": unit_tests_passed,
            "post_change_verification_passed": False,
            "automatic_rollback_requested": True,
        },
    )

    rollback_succeeded, rollback_message = (
        rollback_pending_change_backup()
    )

    rollback_syntax_passed = False
    rollback_unit_tests_passed = False

    rollback_syntax_message = (
        "Rollback syntax verification was not executed."
    )

    rollback_unit_tests_message = (
        "Rollback unit tests were not executed."
    )

    if rollback_succeeded:

        rollback_syntax_passed, rollback_syntax_message = (
            run_project_syntax_validation()
        )

        if rollback_syntax_passed:

            (
                rollback_unit_tests_passed,
                rollback_unit_tests_message,
            ) = run_project_unit_tests()

        else:

            rollback_unit_tests_message = (
                "Rollback unit tests were not executed because "
                "post-rollback syntax validation failed."
            )

    rollback_verification_passed = bool(
        rollback_succeeded
        and rollback_syntax_passed
        and rollback_unit_tests_passed
    )

    if pending_change is not None:

        pending_change[
            "automatic_rollback_attempted"
        ] = True

        pending_change[
            "automatic_rollback_succeeded"
        ] = rollback_succeeded

        pending_change[
            "post_rollback_syntax_passed"
        ] = rollback_syntax_passed

        pending_change[
            "post_rollback_unit_tests_passed"
        ] = rollback_unit_tests_passed

        pending_change[
            "post_rollback_verification_passed"
        ] = rollback_verification_passed

    rollback_summary = "\n".join(
        [
            verification_failure_message,
            "",
            "AUTOMATIC ROLLBACK",
            "",
            rollback_message,
            "",
            (
                "Rollback Completed: "
                f"{rollback_succeeded}"
            ),
            "",
            "POST-ROLLBACK VERIFICATION",
            "",
            rollback_syntax_message,
            "",
            (
                "Rollback Syntax Validation Passed: "
                f"{rollback_syntax_passed}"
            ),
            "",
            rollback_unit_tests_message,
            "",
            (
                "Rollback Unit Tests Passed: "
                f"{rollback_unit_tests_passed}"
            ),
            "",
            (
                "Post-Rollback Verification: "
                + (
                    "PASSED"
                    if rollback_verification_passed
                    else "FAILED"
                )
            ),
        ]
    )

    append_audit_event(
        event_type=(
            "AUTOMATIC_ROLLBACK_VERIFIED"
            if rollback_verification_passed
            else "AUTOMATIC_ROLLBACK_FAILED"
        ),
        success=rollback_verification_passed,
        message=rollback_summary,
        details={
            "action": "automatic_rollback_after_verification_failure",
            "rollback_succeeded": rollback_succeeded,
            "rollback_syntax_validation_passed": rollback_syntax_passed,
            "rollback_unit_tests_passed": rollback_unit_tests_passed,
            "post_rollback_verification_passed": (
                rollback_verification_passed
            ),
        },
    )

    if rollback_verification_passed:

        final_message = "\n".join(
            [
                rollback_summary,
                "",
                (
                    "The failed implementation was automatically "
                    "rolled back and the restored project passed "
                    "syntax validation and unit tests."
                ),
                (
                    "Implementation remains FAILED because the "
                    "proposed change did not pass verification."
                ),
            ]
        )

    else:

        final_message = "\n".join(
            [
                rollback_summary,
                "",
                (
                    "CRITICAL: automatic rollback or post-rollback "
                    "verification did not complete successfully."
                ),
                (
                    "Do not treat the project as verified until the "
                    "rollback state is inspected manually."
                ),
            ]
        )

    return (
        False,
        final_message,
    )


# Preserve the proven rollback function, then wrap it with
# append-only audit logging without changing rollback behavior.
_ROLLBACK_PENDING_CHANGE_BACKUP_CORE = rollback_pending_change_backup


def rollback_pending_change_backup() -> tuple[bool, str]:
    """
    Run the existing verified rollback engine and record the result
    in the implementation audit log.

    Audit-log failure never changes the rollback result.
    """

    rollback_succeeded, rollback_message = (
        _ROLLBACK_PENDING_CHANGE_BACKUP_CORE()
    )

    event_type = (
        "ROLLBACK_COMPLETED"
        if rollback_succeeded
        else "ROLLBACK_BLOCKED"
    )

    append_audit_event(
        event_type=event_type,
        success=rollback_succeeded,
        message=rollback_message,
        details={
            "action": "rollback",
        },
    )

    return (
        rollback_succeeded,
        rollback_message,
    )


def read_audit_events(
    limit: int = 25,
) -> tuple[bool, str]:
    """
    Read and format the most recent implementation audit events.

    This function is read-only.
    """

    import json

    audit_path = get_audit_log_path()

    if not audit_path.exists():

        return (
            True,
            "No implementation audit events have been recorded yet.",
        )

    if not audit_path.is_file():

        return (
            False,
            "Implementation audit path is not a file.",
        )

    try:

        raw_lines = audit_path.read_text(
            encoding="utf-8"
        ).splitlines()

        requested_limit = max(
            1,
            min(
                int(limit),
                100,
            ),
        )

        selected_lines = raw_lines[
            -requested_limit:
        ]

        if not selected_lines:

            return (
                True,
                "No implementation audit events have been recorded yet.",
            )

        formatted_events = []

        for raw_line in selected_lines:

            if not raw_line.strip():
                continue

            record = json.loads(
                raw_line
            )

            pending_snapshot = (
                record.get(
                    "pending_change"
                )
                or {}
            )

            formatted_events.append(
                " | ".join(
                    [
                        str(
                            record.get(
                                "timestamp_utc",
                                "",
                            )
                        ),
                        str(
                            record.get(
                                "event_type",
                                "",
                            )
                        ),
                        (
                            "success="
                            + str(
                                record.get(
                                    "success"
                                )
                            )
                        ),
                        (
                            "target="
                            + str(
                                pending_snapshot.get(
                                    "target_name"
                                )
                            )
                        ),
                        (
                            "boundary="
                            + str(
                                pending_snapshot.get(
                                    "boundary_type"
                                )
                            )
                        ),
                        str(
                            record.get(
                                "message",
                                "",
                            )
                        ),
                    ]
                )
            )

        return (
            True,
            "\n".join(
                formatted_events
            ),
        )

    except Exception as error:

        return (
            False,
            (
                "Could not read implementation audit log: "
                f"{error}"
            ),
        )


# ============================================================
# AUTOMATED TEST RUNNER
# ============================================================


TEST_FILE_PATTERNS = (
    "test_",
    "_test.py",
)


def get_project_test_files() -> list[Path]:
    """
    Return active project Python files that look like test modules.

    Discovery is read-only. No tests are executed by this function.
    """

    test_files = []

    for file_path in get_cached_project_python_files():

        file_name = file_path.name.lower()

        is_test_file = (
            file_name.startswith(
                TEST_FILE_PATTERNS[0]
            )
            or file_name.endswith(
                TEST_FILE_PATTERNS[1]
            )
        )

        if is_test_file:
            test_files.append(
                file_path
            )

    return sorted(
        test_files,
        key=lambda path: str(
            path.relative_to(
                PROJECT_ROOT
            )
        ).lower(),
    )


def format_project_test_files() -> str:
    """
    Format discovered project test files for terminal display.
    """

    test_files = get_project_test_files()

    if not test_files:
        return (
            "No project test files were discovered.\n"
            "Expected names such as test_example.py or example_test.py."
        )

    lines = [
        "DISCOVERED PROJECT TEST FILES",
        "",
    ]

    for index, file_path in enumerate(
        test_files,
        start=1,
    ):
        lines.append(
            f"[{index}] "
            + str(
                file_path.relative_to(
                    PROJECT_ROOT
                )
            )
        )

    return "\n".join(
        lines
    )


def run_project_syntax_validation() -> tuple[bool, str]:
    """
    Parse every active project Python file with Python's AST parser.

    This is a read-only validation pass. It does not execute application
    code, call external APIs, create bytecode, or modify project files.
    """

    python_files = get_cached_project_python_files()

    if not python_files:
        return (
            False,
            "No active project Python files were found to validate.",
        )

    passed_files = []
    failed_files = []

    for file_path in python_files:

        relative_path = str(
            file_path.relative_to(
                PROJECT_ROOT
            )
        )

        try:
            source_text = get_cached_python_source(
                file_path
            )

            ast.parse(
                source_text,
                filename=relative_path,
            )

            passed_files.append(
                relative_path
            )

        except SyntaxError as error:

            failed_files.append(
                (
                    relative_path,
                    (
                        f"line {error.lineno}: "
                        f"{error.msg}"
                    ),
                )
            )

        except Exception as error:

            failed_files.append(
                (
                    relative_path,
                    str(error),
                )
            )

    lines = [
        "PROJECT SYNTAX VALIDATION",
        "",
        (
            "Files Checked: "
            f"{len(python_files)}"
        ),
        (
            "Passed: "
            f"{len(passed_files)}"
        ),
        (
            "Failed: "
            f"{len(failed_files)}"
        ),
    ]

    if failed_files:

        lines.extend(
            [
                "",
                "FAILURES",
            ]
        )

        for relative_path, error_message in failed_files:
            lines.append(
                f"- {relative_path}: {error_message}"
            )

        return (
            False,
            "\n".join(
                lines
            ),
        )

    lines.extend(
        [
            "",
            "All active project Python files parsed successfully.",
            "No project files were modified.",
        ]
    )

    return (
        True,
        "\n".join(
            lines
        ),
    )

def clear_loaded_project_modules_for_tests() -> list[str]:
    """
    Remove already-loaded project modules from sys.modules so each
    controlled test run imports the current source from disk.

    The Development Bot module itself is never removed.
    """

    import importlib
    import sys

    removed_modules = []

    dev_bot_file = Path(__file__).resolve()

    for module_name, module in list(
        sys.modules.items()
    ):

        module_file = getattr(
            module,
            "__file__",
            None,
        )

        if not module_file:

            continue

        try:

            module_path = Path(
                module_file
            ).resolve()

        except (
            OSError,
            RuntimeError,
            TypeError,
        ):

            continue

        if module_path == dev_bot_file:

            continue

        try:

            module_path.relative_to(
                PROJECT_ROOT
            )

        except ValueError:

            continue

        sys.modules.pop(
            module_name,
            None,
        )

        removed_modules.append(
            module_name
        )

    importlib.invalidate_caches()

    return removed_modules


def run_project_unit_tests() -> tuple[bool, str]:
    """
    Execute only discovered project unittest test modules.

    The runner:
    - uses Python's built-in unittest framework
    - does not accept arbitrary shell commands
    - runs only files returned by get_project_test_files()
    - reloads project modules from current source on every run
    - temporarily disables .pyc bytecode creation
    - captures unittest output for controlled terminal reporting
    """

    import importlib.util
    import io
    import sys
    import unittest

    test_files = get_project_test_files()

    if not test_files:

        return (
            False,
            (
                "No project test files were discovered.\n"
                "No unit tests were executed."
            ),
        )

    original_dont_write_bytecode = (
        sys.dont_write_bytecode
    )

    loaded_modules = []

    try:

        sys.dont_write_bytecode = True

        clear_loaded_project_modules_for_tests()

        loader = unittest.TestLoader()
        combined_suite = unittest.TestSuite()

        import_failures = []

        for index, file_path in enumerate(
            test_files,
            start=1,
        ):

            relative_path = str(
                file_path.relative_to(
                    PROJECT_ROOT
                )
            )

            module_name = (
                "_novelist_dev_test_"
                f"{index}"
            )

            try:

                spec = (
                    importlib.util.spec_from_file_location(
                        module_name,
                        file_path,
                    )
                )

                if (
                    spec is None
                    or spec.loader is None
                ):

                    import_failures.append(
                        (
                            relative_path,
                            "Could not create a Python import specification.",
                        )
                    )

                    continue

                module = (
                    importlib.util.module_from_spec(
                        spec
                    )
                )

                sys.modules[
                    module_name
                ] = module

                loaded_modules.append(
                    module_name
                )

                spec.loader.exec_module(
                    module
                )

                module_suite = (
                    loader.loadTestsFromModule(
                        module
                    )
                )

                combined_suite.addTests(
                    module_suite
                )

            except Exception as error:

                import_failures.append(
                    (
                        relative_path,
                        (
                            f"{type(error).__name__}: "
                            f"{error}"
                        ),
                    )
                )

        discovered_test_count = (
            combined_suite.countTestCases()
        )

        if import_failures:

            lines = [
                "PROJECT UNIT TEST EXECUTION",
                "",
                (
                    "Test Files Discovered: "
                    f"{len(test_files)}"
                ),
                (
                    "Tests Loaded: "
                    f"{discovered_test_count}"
                ),
                (
                    "Import Failures: "
                    f"{len(import_failures)}"
                ),
                "",
                "IMPORT FAILURES",
            ]

            for (
                relative_path,
                error_message,
            ) in import_failures:

                lines.append(
                    f"- {relative_path}: "
                    f"{error_message}"
                )

            lines.extend(
                [
                    "",
                    "Unit test execution was blocked because "
                    "one or more test modules could not be imported.",
                    "No project source files were intentionally modified "
                    "by the Development Bot test runner.",
                ]
            )

            return (
                False,
                "\n".join(
                    lines
                ),
            )

        if discovered_test_count == 0:

            return (
                False,
                (
                    "PROJECT UNIT TEST EXECUTION\n\n"
                    f"Test Files Discovered: {len(test_files)}\n"
                    "Tests Loaded: 0\n\n"
                    "No unittest test cases were found.\n"
                    "No project source files were intentionally modified "
                    "by the Development Bot test runner."
                ),
            )

        output_buffer = (
            io.StringIO()
        )

        runner = unittest.TextTestRunner(
            stream=output_buffer,
            verbosity=2,
        )

        result = runner.run(
            combined_suite
        )

        runner_output = (
            output_buffer.getvalue().strip()
        )

        lines = [
            "PROJECT UNIT TEST EXECUTION",
            "",
            (
                "Test Files Discovered: "
                f"{len(test_files)}"
            ),
            (
                "Tests Run: "
                f"{result.testsRun}"
            ),
            (
                "Failures: "
                f"{len(result.failures)}"
            ),
            (
                "Errors: "
                f"{len(result.errors)}"
            ),
            (
                "Skipped: "
                f"{len(result.skipped)}"
            ),
            "",
            "UNITTEST OUTPUT",
            runner_output,
            "",
            (
                "Overall Result: "
                + (
                    "PASSED"
                    if result.wasSuccessful()
                    else "FAILED"
                )
            ),
            (
                "No project source files were intentionally modified "
                "by the Development Bot test runner."
            ),
        ]

        return (
            result.wasSuccessful(),
            "\n".join(
                lines
            ),
        )

    except Exception as error:

        return (
            False,
            (
                "PROJECT UNIT TEST EXECUTION\n\n"
                "Controlled unit test execution failed unexpectedly: "
                f"{type(error).__name__}: {error}\n"
                "No arbitrary shell command was executed."
            ),
        )

    finally:

        sys.dont_write_bytecode = (
            original_dont_write_bytecode
        )

        for module_name in loaded_modules:

            sys.modules.pop(
                module_name,
                None,
            )

        clear_loaded_project_modules_for_tests()


# ============================================================
# SAFE CODE PROPOSAL
# ============================================================

MAX_CODE_PROPOSAL_CHARACTERS = 90000


def get_unique_proposal_target(
    target_name: str,
):
    """
    Resolve one unique project function/class target.

    Returns:
        (file_path, source_text, target_node, error_message)
    """

    matches = []

    for file_path in get_cached_project_python_files():

        try:

            source_tree = get_cached_python_ast(
                file_path
            )

        except Exception:

            continue

        for node in ast.walk(source_tree):

            if isinstance(
                node,
                (
                    ast.FunctionDef,
                    ast.AsyncFunctionDef,
                    ast.ClassDef,
                ),
            ) and node.name == target_name:

                matches.append(
                    (
                        file_path,
                        node,
                    )
                )

    if not matches:

        return (
            None,
            None,
            None,
            (
                f"Target '{target_name}' was not found "
                "in active project Python files."
            ),
        )

    if len(matches) != 1:

        return (
            None,
            None,
            None,
            (
                f"Target '{target_name}' is not unique "
                "across active project Python files."
            ),
        )

    file_path, target_node = matches[0]

    try:

        source_text = get_cached_python_source(
            file_path
        )

    except Exception as error:

        return (
            None,
            None,
            None,
            f"Could not read target source: {error}",
        )

    return (
        file_path,
        source_text,
        target_node,
        None,
    )


def get_executable_top_level_statements(
    target_node,
) -> list:
    """
    Return top-level executable statements, excluding a
    function/class docstring.
    """

    statements = []

    for statement in getattr(
        target_node,
        "body",
        [],
    ):

        is_docstring = (
            isinstance(
                statement,
                ast.Expr,
            )
            and isinstance(
                getattr(
                    statement,
                    "value",
                    None,
                ),
                ast.Constant,
            )
            and isinstance(
                statement.value.value,
                str,
            )
        )

        if is_docstring:
            continue

        statements.append(
            statement
        )

    return statements


def collect_exit_paths_from_statement(
    statement,
    source_text: str,
) -> list[dict]:
    """
    Collect deterministic return/raise paths inside one
    top-level statement.

    Nested function/class/lambda bodies are deliberately
    excluded because their exits do not exit the outer target.
    """

    paths = []

    def source_for(node) -> str:

        return (
            ast.get_source_segment(
                source_text,
                node,
            )
            or ast.dump(
                node,
                include_attributes=False,
            )
        ).strip()

    def walk_node(
        node,
        conditions: list[str],
    ) -> None:

        if isinstance(
            node,
            (
                ast.FunctionDef,
                ast.AsyncFunctionDef,
                ast.ClassDef,
                ast.Lambda,
            ),
        ):

            return

        if isinstance(
            node,
            ast.Return,
        ):

            paths.append(
                {
                    "exit_type": "return",
                    "line": getattr(
                        node,
                        "lineno",
                        None,
                    ),
                    "conditions": list(
                        conditions
                    ),
                    "source": source_for(
                        node
                    ),
                }
            )

            return

        if isinstance(
            node,
            ast.Raise,
        ):

            paths.append(
                {
                    "exit_type": "raise",
                    "line": getattr(
                        node,
                        "lineno",
                        None,
                    ),
                    "conditions": list(
                        conditions
                    ),
                    "source": source_for(
                        node
                    ),
                }
            )

            return

        if isinstance(
            node,
            ast.If,
        ):

            condition = source_for(
                node.test
            )

            for child in node.body:

                walk_node(
                    child,
                    conditions
                    + [condition],
                )

            for child in node.orelse:

                walk_node(
                    child,
                    conditions
                    + [f"NOT ({condition})"],
                )

            return

        if isinstance(
            node,
            ast.For,
        ):

            loop_source = (
                f"for {source_for(node.target)} "
                f"in {source_for(node.iter)}"
            )

            for child in node.body:

                walk_node(
                    child,
                    conditions
                    + [loop_source],
                )

            for child in node.orelse:

                walk_node(
                    child,
                    conditions
                    + [
                        (
                            "loop completes without "
                            "an earlier exit"
                        )
                    ],
                )

            return

        if isinstance(
            node,
            ast.While,
        ):

            condition = source_for(
                node.test
            )

            for child in node.body:

                walk_node(
                    child,
                    conditions
                    + [f"while {condition}"],
                )

            for child in node.orelse:

                walk_node(
                    child,
                    conditions
                    + [
                        (
                            "while loop completes "
                            "without an earlier exit"
                        )
                    ],
                )

            return

        if isinstance(
            node,
            ast.Try,
        ):

            for child in node.body:

                walk_node(
                    child,
                    conditions
                    + ["try body"],
                )

            for handler in node.handlers:

                handler_name = (
                    source_for(
                        handler.type
                    )
                    if handler.type
                    is not None
                    else "Exception"
                )

                for child in handler.body:

                    walk_node(
                        child,
                        conditions
                        + [
                            (
                                "exception handler "
                                f"{handler_name}"
                            )
                        ],
                    )

            for child in node.orelse:

                walk_node(
                    child,
                    conditions
                    + ["try else"],
                )

            for child in node.finalbody:

                walk_node(
                    child,
                    conditions
                    + ["finally"],
                )

            return

        for child in ast.iter_child_nodes(
            node
        ):

            walk_node(
                child,
                conditions,
            )

    walk_node(
        statement,
        [],
    )

    return paths


def build_target_control_flow_facts(
    target_name: str,
) -> str:
    """
    Build deterministic AST-derived execution facts.

    These facts are source data, not AI interpretation.
    """

    (
        file_path,
        source_text,
        target_node,
        error_message,
    ) = get_unique_proposal_target(
        target_name
    )

    if error_message:

        return (
            "CONTROL-FLOW FACTS UNAVAILABLE:\n"
            f"{error_message}"
        )

    statements = (
        get_executable_top_level_statements(
            target_node
        )
    )

    lines = [
        "DETERMINISTIC CONTROL-FLOW FACTS",
        f"File: {file_path.name}",
        f"Target: {target_name}",
        "",
        "Top-level execution order:",
    ]

    for index, statement in enumerate(
        statements,
        start=1,
    ):

        statement_source = (
            ast.get_source_segment(
                source_text,
                statement,
            )
            or ast.dump(
                statement,
                include_attributes=False,
            )
        ).strip()

        first_line = (
            statement_source
            .splitlines()[0]
        )

        lines.append(
            (
                f"[{index}] "
                f"{type(statement).__name__} "
                f"lines "
                f"{getattr(statement, 'lineno', '?')}-"
                f"{getattr(statement, 'end_lineno', '?')}: "
                f"{first_line}"
            )
        )

        exits = (
            collect_exit_paths_from_statement(
                statement,
                source_text,
            )
        )

        for exit_path in exits:

            if exit_path["conditions"]:

                condition_text = " AND ".join(
                    exit_path["conditions"]
                )

            else:

                condition_text = (
                    "top-level statement reached"
                )

            lines.append(
                (
                    "    EXIT: WHEN "
                    f"{condition_text} "
                    "THEN "
                    f"{exit_path['source']}"
                )
            )

    if statements:

        final_statement = statements[-1]

        final_source = (
            ast.get_source_segment(
                source_text,
                final_statement,
            )
            or ast.dump(
                final_statement,
                include_attributes=False,
            )
        ).strip()

        lines.extend(
            [
                "",
                (
                    "FINAL TOP-LEVEL STATEMENT: "
                    f"{final_source}"
                ),
                (
                    "HARD RULE: Any return or raise in an "
                    "earlier top-level statement exits before "
                    "the final statement and cannot be changed "
                    "by replacing only the final statement."
                ),
            ]
        )

    return "\n".join(
        lines
    )


def extract_proposal_replacement_code(
    proposal: str,
) -> str:
    """
    Extract the best valid Python replacement from Section E.

    Candidate ranking is boundary-aware:
    - LOGICAL BLOCK prefers supported compound statements.
    - SINGLE STATEMENT prefers substantive simple statements
      over placeholder/pass candidates.

    Handles fenced/unfenced code and mixed prose.
    """

    section = extract_proposal_section(
        proposal,
        "E. COMPLETE REPLACEMENT CODE",
        "F. WHY THIS CHANGE SHOULD WORK",
    )

    section = (
        section or ""
    ).strip()

    if not section:
        return ""

    boundary_section = extract_proposal_section(
        proposal,
        "D. REPLACEMENT BOUNDARY",
        "E. COMPLETE REPLACEMENT CODE",
    ).upper()

    candidates = []

    for fenced_match in re.finditer(
        r"```(?:python)?\s*\n?(.*?)```",
        section,
        flags=re.IGNORECASE | re.DOTALL,
    ):
        fenced_code = (
            fenced_match.group(1)
        ).strip()
        if fenced_code:
            candidates.append(fenced_code)

    fence_stripped = re.sub(
        r"^\s*```(?:python)?\s*",
        "",
        section,
        flags=re.IGNORECASE,
    )
    fence_stripped = re.sub(
        r"\s*```\s*$",
        "",
        fence_stripped,
    ).strip()
    if fence_stripped:
        candidates.append(fence_stripped)

    lines = section.splitlines()

    for start_index in range(len(lines)):
        for end_index in range(
            len(lines),
            start_index,
            -1,
        ):
            candidate = "\n".join(
                lines[start_index:end_index]
            ).strip()
            if candidate:
                candidates.append(candidate)

    seen = set()
    parsed_candidates = []

    for candidate in candidates:
        normalized = candidate.strip()

        normalized = re.sub(
            r"^\s*```(?:python)?\s*",
            "",
            normalized,
            flags=re.IGNORECASE,
        )
        normalized = re.sub(
            r"\s*```\s*$",
            "",
            normalized,
        ).strip()

        if (
            not normalized
            or normalized in seen
        ):
            continue

        seen.add(normalized)

        try:
            parsed = ast.parse(normalized)
        except SyntaxError:
            continue

        if len(parsed.body) != 1:
            continue

        statement = parsed.body[0]

        if (
            isinstance(statement, ast.Expr)
            and isinstance(
                statement.value,
                ast.Constant,
            )
            and isinstance(
                statement.value.value,
                str,
            )
        ):
            continue

        parsed_candidates.append(
            (
                normalized,
                statement,
            )
        )

    if not parsed_candidates:
        return section

    logical_types = globals().get(
        "LOGICAL_BLOCK_AST_TYPES",
        (
            ast.If,
            ast.For,
            ast.AsyncFor,
            ast.While,
            ast.Try,
            ast.With,
            ast.AsyncWith,
            ast.Match,
        ),
    )

    if "LOGICAL BLOCK" in boundary_section:
        logical_candidates = [
            item
            for item in parsed_candidates
            if isinstance(
                item[1],
                logical_types,
            )
        ]

        if logical_candidates:
            # Prefer the longest complete logical block.
            logical_candidates.sort(
                key=lambda item: len(item[0]),
                reverse=True,
            )
            return logical_candidates[0][0]

    if "SINGLE STATEMENT" in boundary_section:
        simple_candidates = [
            item
            for item in parsed_candidates
            if not isinstance(
                item[1],
                logical_types,
            )
        ]

        if simple_candidates:
            # De-prioritize placeholder pass statements.
            substantive = [
                item
                for item in simple_candidates
                if not isinstance(
                    item[1],
                    ast.Pass,
                )
            ]

            if substantive:
                substantive.sort(
                    key=lambda item: len(item[0]),
                    reverse=True,
                )
                return substantive[0][0]

            return simple_candidates[0][0]

    return parsed_candidates[0][0]

def get_single_statement_replacement_target(
    target_name: str,
    replacement_code: str,
):
    """
    Deterministically identify which top-level source statement
    a SINGLE STATEMENT replacement can safely correspond to.

    The match is based on AST statement type, not AI prose.

    Returns:
        (
            file_path,
            source_text,
            target_node,
            original_statement,
            earlier_exit_paths,
            error_message,
        )
    """

    try:

        replacement_tree = ast.parse(
            replacement_code
        )

    except SyntaxError as error:

        return (
            None,
            None,
            None,
            None,
            [],
            (
                "Replacement code is not valid Python: "
                f"{error}"
            ),
        )

    if len(replacement_tree.body) != 1:

        return (
            None,
            None,
            None,
            None,
            [],
            (
                "SINGLE STATEMENT replacement must "
                "contain exactly one Python statement."
            ),
        )

    replacement_statement = (
        replacement_tree.body[0]
    )

    (
        file_path,
        source_text,
        target_node,
        error_message,
    ) = get_unique_proposal_target(
        target_name
    )

    if error_message:

        return (
            None,
            None,
            None,
            None,
            [],
            error_message,
        )

    statements = (
        get_executable_top_level_statements(
            target_node
        )
    )

    matching_statements = [
        statement
        for statement in statements
        if type(statement)
        is type(replacement_statement)
    ]

    if len(matching_statements) != 1:

        return (
            None,
            None,
            None,
            None,
            [],
            (
                "The intended SINGLE STATEMENT source "
                "location is ambiguous. "
                f"Found {len(matching_statements)} top-level "
                f"{type(replacement_statement).__name__} "
                "statements in the target."
            ),
        )

    original_statement = (
        matching_statements[0]
    )

    statement_index = statements.index(
        original_statement
    )

    earlier_exit_paths = []

    for earlier_statement in statements[
        :statement_index
    ]:

        earlier_exit_paths.extend(
            collect_exit_paths_from_statement(
                earlier_statement,
                source_text,
            )
        )

    return (
        file_path,
        source_text,
        target_node,
        original_statement,
        earlier_exit_paths,
        None,
    )


def describe_deterministic_exit_path(
    exit_path: dict,
) -> str:
    """
    Render one source-derived earlier exit without interpreting
    AI-generated prose.
    """

    conditions = exit_path.get(
        "conditions",
        [],
    )

    source = exit_path.get(
        "source",
        "",
    )

    if conditions:

        condition_text = " AND ".join(
            conditions
        )

    else:

        condition_text = (
            "the earlier statement is reached"
        )

    # Deterministic Python truthiness explanation for a direct
    # `not variable` guard. This is language semantics, not AI
    # inference.
    if (
        len(conditions) == 1
        and conditions[0].startswith(
            "not "
        )
    ):

        variable_name = (
            conditions[0][4:]
            .strip()
        )

        condition_text += (
            f" (that is, `{variable_name}` is falsy; "
            "for ordinary plan text this includes "
            "None or an empty string)"
        )

    return (
        f"WHEN {condition_text} "
        f"THEN {source}"
    )


def build_deterministic_single_statement_proposal(
    target_name: str,
    requested_change: str,
    raw_proposal: str,
) -> str:
    """
    Rebuild a SINGLE STATEMENT READY proposal from AST facts.

    AI prose is not used to decide which earlier paths change.
    Earlier exits and required regression checks come directly
    from the source tree.
    """

    replacement_code = (
        extract_proposal_replacement_code(
            raw_proposal
        )
    )

    if not replacement_code:

        return (
            "PROPOSAL STATUS: MORE INSPECTION REQUIRED\n\n"
            "A. WHY THE CURRENT SOURCE IS INSUFFICIENT\n\n"
            "The generated proposal did not contain a valid "
            "Section E SINGLE STATEMENT replacement.\n\n"
            "B. EXACT NEXT INSPECTION REQUIRED\n\n"
            "Regenerate the proposal with exactly one Python "
            "statement in Section E.\n\n"
            "C. WHAT MUST BE CONFIRMED\n\n"
            "Confirm the exact source statement that the "
            "replacement is intended to replace.\n\n"
            "NO FILES WERE MODIFIED"
        )

    (
        file_path,
        source_text,
        target_node,
        original_statement,
        earlier_exit_paths,
        error_message,
    ) = get_single_statement_replacement_target(
        target_name,
        replacement_code,
    )

    if error_message:

        return (
            "PROPOSAL STATUS: MORE INSPECTION REQUIRED\n\n"
            "A. WHY THE CURRENT SOURCE IS INSUFFICIENT\n\n"
            f"{error_message}\n\n"
            "B. EXACT NEXT INSPECTION REQUIRED\n\n"
            "Select or inspect the exact top-level statement "
            "that should be replaced before implementation.\n\n"
            "C. WHAT MUST BE CONFIRMED\n\n"
            "Confirm one unambiguous existing source statement "
            "for the proposed SINGLE STATEMENT replacement.\n\n"
            "NO FILES WERE MODIFIED"
        )

    original_source = (
        ast.get_source_segment(
            source_text,
            original_statement,
        )
        or ast.dump(
            original_statement,
            include_attributes=False,
        )
    ).strip()

    start_line = getattr(
        original_statement,
        "lineno",
        None,
    )

    end_line = getattr(
        original_statement,
        "end_lineno",
        start_line,
    )

    earlier_exit_lines = []

    for exit_path in earlier_exit_paths:

        earlier_exit_lines.append(
            "- UNCHANGED EARLIER EXIT: "
            + describe_deterministic_exit_path(
                exit_path
            )
        )

    if not earlier_exit_lines:

        earlier_exit_lines.append(
            "- No earlier return/raise paths were detected "
            "before this statement."
        )

    required_tests = []

    test_number = 1

    for exit_path in earlier_exit_paths:

        required_tests.append(
            (
                f"{test_number}. Regression test the unchanged "
                "earlier exit: "
                f"{describe_deterministic_exit_path(exit_path)}."
            )
        )

        test_number += 1

    required_tests.append(
        (
            f"{test_number}. Test an execution path that reaches "
            f"line {start_line}; it must execute the proposed "
            f"replacement `{replacement_code}`."
        )
    )

    test_number += 1

    required_tests.append(
        (
            f"{test_number}. Test existing successful paths "
            "that return before the replacement and confirm "
            "their existing return values remain unchanged."
        )
    )

    affected_path_text = "\n".join(
        earlier_exit_lines
    )

    tests_text = "\n".join(
        required_tests
    )

    return f"""PROPOSAL STATUS: READY

A. CONFIRMED PROBLEM MECHANISM

The exact source statement selected for replacement is:

`{original_source}`

at {file_path.name} lines {start_line}-{end_line}.

This statement executes only when control reaches that source
location. Any return or raise that occurs earlier exits the
target before this statement and is therefore outside this
replacement's effect.

B. CHANGE SUMMARY

Requested change:

{requested_change}

Proposed SINGLE STATEMENT replacement:

`{replacement_code}`

C. CONFIRMED AFFECTED FILES

- {file_path.name}

D. REPLACEMENT BOUNDARY

SINGLE STATEMENT

Exact existing source boundary:
- Start line: {start_line}
- End line: {end_line}
- Existing statement: `{original_source}`

E. COMPLETE REPLACEMENT CODE

```python
{replacement_code}
```

F. WHY THIS CHANGE SHOULD WORK

Only execution paths that actually reach lines {start_line}-{end_line}
can execute the replacement.

Deterministic earlier-exit analysis:

{affected_path_text}

Therefore, none of the earlier exits listed above are changed by
this SINGLE STATEMENT replacement.

G. WHY THIS IS SAFE

The replacement boundary is one uniquely identified top-level
{type(original_statement).__name__} statement. The function
signature, earlier guards, earlier returns/raises, dependencies,
and callers are not included in the replacement boundary.

The proposal's path-impact claims above are generated directly
from the Python AST rather than inferred from AI wording.

H. REQUIRED TESTS

{tests_text}

NO FILES WERE MODIFIED"""


def validate_source_grounded_proposal(
    proposal: str,
    target_name: str,
) -> tuple[bool, str]:
    """
    Validate that a READY SINGLE STATEMENT proposal can be
    grounded to one exact source statement.

    This validator does not interpret English claims.
    """

    if not proposal.startswith(
        "PROPOSAL STATUS: READY"
    ):

        return (
            False,
            "Proposal is not READY.",
        )

    if (
        "D. REPLACEMENT BOUNDARY"
        in proposal
        and "SINGLE STATEMENT"
        in proposal
    ):

        replacement_code = (
            extract_proposal_replacement_code(
                proposal
            )
        )

        (
            _file_path,
            _source_text,
            _target_node,
            _original_statement,
            _earlier_exit_paths,
            error_message,
        ) = get_single_statement_replacement_target(
            target_name,
            replacement_code,
        )

        if error_message:

            return (
                False,
                error_message,
            )

    return (
        True,
        (
            "Proposal passed deterministic "
            "source-grounding validation."
        ),
    )


# ------------------------------------------------------------
# WHOLE FUNCTION DISCOVERY — READ ONLY
# ------------------------------------------------------------

FUNCTION_AST_TYPES = (
    ast.FunctionDef,
    ast.AsyncFunctionDef,
)


def get_target_functions(
    target_name: str,
) -> list[dict]:
    """
    Return every complete source-backed Python function matching
    target_name across the active project.

    Read-only. No pending change is created and no project file is
    modified.
    """

    target_name = (target_name or "").strip()

    if not target_name:
        return []

    matches = []

    for path in get_project_python_files():

        try:
            source = path.read_text(
                encoding="utf-8",
                errors="replace",
            )
            tree = ast.parse(source)
        except Exception:
            continue

        source_lines = source.splitlines()
        parent_map = {}

        for parent in ast.walk(tree):
            for child in ast.iter_child_nodes(parent):
                parent_map[child] = parent

        for node in ast.walk(tree):

            if not isinstance(node, FUNCTION_AST_TYPES):
                continue

            if node.name != target_name:
                continue

            start_line = node.lineno
            end_line = getattr(
                node,
                "end_lineno",
                node.lineno,
            )

            function_source = "\n".join(
                source_lines[
                    start_line - 1:end_line
                ]
            )

            nesting_depth = 0
            current_parent = parent_map.get(node)
            parent_type = None
            parent_line = None

            if current_parent is not None:
                parent_type = type(
                    current_parent
                ).__name__
                parent_line = getattr(
                    current_parent,
                    "lineno",
                    None,
                )

            while current_parent is not None:
                if isinstance(
                    current_parent,
                    (
                        ast.FunctionDef,
                        ast.AsyncFunctionDef,
                        ast.ClassDef,
                    ),
                ):
                    nesting_depth += 1

                current_parent = parent_map.get(
                    current_parent
                )

            matches.append(
                {
                    "name": node.name,
                    "node_type": type(node).__name__,
                    "file": str(
                        path.relative_to(PROJECT_ROOT)
                    ),
                    "start_line": start_line,
                    "end_line": end_line,
                    "source": function_source,
                    "nesting_depth": nesting_depth,
                    "parent_type": parent_type,
                    "parent_line": parent_line,
                }
            )

    matches.sort(
        key=lambda item: (
            item["file"].lower(),
            item["start_line"],
            item["node_type"],
        )
    )

    for index, match in enumerate(
        matches,
        start=1,
    ):
        match["selection_number"] = index

    return matches


def format_target_functions(
    target_name: str,
) -> str:
    """Format complete matching functions for terminal review."""

    functions = get_target_functions(
        target_name
    )

    if not functions:
        return (
            "No complete Python function named "
            f"'{target_name}' was found."
        )

    lines = [
        f"Selectable whole functions for '{target_name}':",
        "",
    ]

    for function in functions:
        lines.extend(
            [
                (
                    f"{function['selection_number']}. "
                    f"{function['node_type']}"
                ),
                f"   File: {function['file']}",
                (
                    "   Lines: "
                    f"{function['start_line']}-"
                    f"{function['end_line']}"
                ),
                (
                    "   Nesting Depth: "
                    f"{function['nesting_depth']}"
                ),
                (
                    "   Parent: "
                    f"{function['parent_type'] or 'Module'}"
                    + (
                        f" at line {function['parent_line']}"
                        if function['parent_line']
                        else ""
                    )
                ),
                "",
            ]
        )

    lines.extend(
        [
            "Read-only discovery only.",
            "No pending change was created.",
            "No files were modified.",
        ]
    )

    return "\n".join(lines)


def select_target_function(
    target_name: str,
    selection_number: int,
) -> tuple[bool, str, dict | None]:
    """
    Select one exact whole function from live source.

    Read-only. This does not store pending-change metadata and does
    not enable WHOLE FUNCTION implementation.
    """

    functions = get_target_functions(
        target_name
    )

    if not functions:
        return (
            False,
            (
                "No complete Python function named "
                f"'{target_name}' was found."
            ),
            None,
        )

    if (
        selection_number < 1
        or selection_number > len(functions)
    ):
        return (
            False,
            (
                "Whole function selection is out of range. "
                f"Choose 1-{len(functions)}."
            ),
            None,
        )

    selected = functions[
        selection_number - 1
    ]

    message = "\n".join(
        [
            "Whole function selected from live source.",
            f"Target: {selected['name']}",
            (
                "Selection: "
                f"{selected['selection_number']}"
            ),
            f"Type: {selected['node_type']}",
            f"File: {selected['file']}",
            (
                "Lines: "
                f"{selected['start_line']}-"
                f"{selected['end_line']}"
            ),
            (
                "Nesting Depth: "
                f"{selected['nesting_depth']}"
            ),
            "",
            "Read-only selection only.",
            "No pending change was created.",
            "No files were modified.",
        ]
    )

    return (
        True,
        message,
        selected,
    )


# ------------------------------------------------------------
# LOGICAL BLOCK DISCOVERY — READ ONLY
# ------------------------------------------------------------

LOGICAL_BLOCK_AST_TYPES = (
    ast.If,
    ast.For,
    ast.AsyncFor,
    ast.While,
    ast.Try,
    ast.With,
    ast.AsyncWith,
    ast.Match,
)


def get_target_logical_blocks(
    target_name: str,
) -> list[dict]:
    """
    Discover source-backed logical blocks inside one unique target.

    Read-only:
    - does not modify files
    - does not modify pending-change state
    - does not approve or implement anything

    Nested function/class/lambda bodies are excluded because they
    are separate execution scopes.
    """

    (
        file_path,
        source_text,
        target_node,
        error_message,
    ) = get_unique_proposal_target(
        target_name
    )

    if error_message:

        return []

    discovered_blocks = []

    def source_for(node) -> str:

        return (
            ast.get_source_segment(
                source_text,
                node,
            )
            or ""
        ).strip()

    def visit_statement(
        statement,
        parent_type: str,
        parent_line,
        depth: int,
    ) -> None:

        if isinstance(
            statement,
            (
                ast.FunctionDef,
                ast.AsyncFunctionDef,
                ast.ClassDef,
            ),
        ):

            return

        if isinstance(
            statement,
            LOGICAL_BLOCK_AST_TYPES,
        ):

            block_source = source_for(
                statement
            )

            if (
                block_source
                and getattr(
                    statement,
                    "lineno",
                    None,
                )
                and getattr(
                    statement,
                    "end_lineno",
                    None,
                )
            ):

                discovered_blocks.append(
                    {
                        "selection_number": 0,
                        "node_type": type(
                            statement
                        ).__name__,
                        "start_line": (
                            statement.lineno
                        ),
                        "end_line": (
                            statement.end_lineno
                        ),
                        "source": block_source,
                        "parent_type": (
                            parent_type
                        ),
                        "parent_line": (
                            parent_line
                        ),
                        "nesting_depth": (
                            depth
                        ),
                        "file": (
                            file_path.name
                        ),
                    }
                )

        child_groups = []

        if isinstance(
            statement,
            ast.If,
        ):

            child_groups.extend(
                [
                    statement.body,
                    statement.orelse,
                ]
            )

        elif isinstance(
            statement,
            (
                ast.For,
                ast.AsyncFor,
                ast.While,
            ),
        ):

            child_groups.extend(
                [
                    statement.body,
                    statement.orelse,
                ]
            )

        elif isinstance(
            statement,
            ast.Try,
        ):

            child_groups.extend(
                [
                    statement.body,
                    statement.orelse,
                    statement.finalbody,
                ]
            )

            for handler in (
                statement.handlers
            ):

                child_groups.append(
                    handler.body
                )

        elif isinstance(
            statement,
            (
                ast.With,
                ast.AsyncWith,
            ),
        ):

            child_groups.append(
                statement.body
            )

        elif isinstance(
            statement,
            ast.Match,
        ):

            for case in statement.cases:

                child_groups.append(
                    case.body
                )

        else:

            for field_name in (
                "body",
                "orelse",
                "finalbody",
            ):

                possible_group = getattr(
                    statement,
                    field_name,
                    None,
                )

                if isinstance(
                    possible_group,
                    list,
                ):

                    child_groups.append(
                        possible_group
                    )

        for child_group in child_groups:

            for child_statement in (
                child_group
            ):

                if isinstance(
                    child_statement,
                    ast.stmt,
                ):

                    visit_statement(
                        child_statement,
                        type(
                            statement
                        ).__name__,
                        getattr(
                            statement,
                            "lineno",
                            None,
                        ),
                        depth + 1,
                    )

    for top_level_statement in getattr(
        target_node,
        "body",
        [],
    ):

        visit_statement(
            top_level_statement,
            type(
                target_node
            ).__name__,
            getattr(
                target_node,
                "lineno",
                None,
            ),
            0,
        )

    discovered_blocks.sort(
        key=lambda item: (
            item["start_line"],
            item["end_line"],
            item["nesting_depth"],
            item["node_type"],
        )
    )

    for selection_number, block in enumerate(
        discovered_blocks,
        start=1,
    ):

        block["selection_number"] = (
            selection_number
        )

    return discovered_blocks


def format_target_logical_blocks(
    target_name: str,
) -> str:
    """
    Format selectable logical blocks for terminal display.

    Read-only.
    """

    blocks = get_target_logical_blocks(
        target_name
    )

    if not blocks:

        return (
            f"No selectable logical blocks were found "
            f"for '{target_name}'."
        )

    lines = [
        (
            "SELECTABLE LOGICAL BLOCKS: "
            f"{target_name}"
        ),
        "",
    ]

    for block in blocks:

        source_lines = (
            block["source"]
            .splitlines()
        )

        first_line = (
            source_lines[0].strip()
            if source_lines
            else ""
        )

        lines.append(
            (
                f"[{block['selection_number']}] "
                f"{block['node_type']} "
                f"lines "
                f"{block['start_line']}-"
                f"{block['end_line']} "
                f"depth={block['nesting_depth']}"
            )
        )

        lines.append(
            (
                "    Parent: "
                f"{block['parent_type']} "
                f"line "
                f"{block['parent_line']}"
            )
        )

        lines.append(
            (
                "    Starts: "
                f"{first_line}"
            )
        )

    lines.extend(
        [
            "",
            (
                "READ ONLY: no logical block "
                "has been selected for implementation."
            ),
        ]
    )

    return "\n".join(
        lines
    )


def select_target_logical_block(
    target_name: str,
    selection_number: int,
) -> tuple[bool, str, dict | None]:
    """
    Resolve one logical-block selection by its displayed number.

    This is a read-only selection helper. It returns exact source
    metadata but does not store pending state and cannot approve,
    back up, write, or implement anything.
    """

    if not isinstance(
        selection_number,
        int,
    ):

        return (
            False,
            (
                "Logical block selection must "
                "be a whole number."
            ),
            None,
        )

    if selection_number < 1:

        return (
            False,
            (
                "Logical block selection must "
                "be 1 or greater."
            ),
            None,
        )

    blocks = get_target_logical_blocks(
        target_name
    )

    if not blocks:

        return (
            False,
            (
                f"No selectable logical blocks "
                f"were found for '{target_name}'."
            ),
            None,
        )

    selected_block = next(
        (
            block
            for block in blocks
            if block[
                "selection_number"
            ]
            == selection_number
        ),
        None,
    )

    if selected_block is None:

        return (
            False,
            (
                "Logical block selection "
                f"{selection_number} is out of range. "
                f"Valid selections are 1-{len(blocks)}."
            ),
            None,
        )

    message = "\n".join(
        [
            (
                "Logical block selected "
                "for read-only inspection."
            ),
            (
                f"Target: {target_name}"
            ),
            (
                "Selection: "
                f"{selected_block['selection_number']}"
            ),
            (
                "Type: "
                f"{selected_block['node_type']}"
            ),
            (
                "File: "
                f"{selected_block['file']}"
            ),
            (
                "Lines: "
                f"{selected_block['start_line']}-"
                f"{selected_block['end_line']}"
            ),
            (
                "Nesting Depth: "
                f"{selected_block['nesting_depth']}"
            ),
            "",
            "Selected Logical Block:",
            selected_block["source"],
            "",
            (
                "READ ONLY: nothing was stored, "
                "approved, backed up, or modified."
            ),
        ]
    )

    return (
        True,
        message,
        dict(
            selected_block
        ),
    )

def select_pending_logical_block(
    selection_number: int,
) -> tuple[bool, str]:
    """
    Attach one exact source-backed logical block to a pending
    LOGICAL BLOCK proposal.

    This function does NOT:
    - approve the pending change
    - create a backup
    - modify project source

    It only records deterministic source metadata in pending state.
    """

    global _PENDING_CHANGE_APPROVAL

    pending_change = get_pending_change()

    if pending_change is None:

        return (
            False,
            "There is no pending change.",
        )

    if pending_change.get(
        "boundary_type"
    ) != "LOGICAL BLOCK":

        return (
            False,
            (
                "The pending change is not a "
                "LOGICAL BLOCK proposal."
            ),
        )

    if pending_change.get(
        "approved",
        False,
    ):

        return (
            False,
            (
                "The pending change is already approved. "
                "Logical block selection is locked."
            ),
        )

    if pending_change.get(
        "implemented",
        False,
    ):

        return (
            False,
            (
                "The pending change has already been implemented. "
                "Logical block selection is locked."
            ),
        )

    target_name = pending_change.get(
        "target_name"
    )

    if not target_name:

        return (
            False,
            (
                "Pending change does not contain "
                "a valid target name."
            ),
        )

    replacement_code = pending_change.get(
        "replacement_code",
        "",
    )

    if not str(
        replacement_code
    ).strip():

        return (
            False,
            (
                "Pending LOGICAL BLOCK proposal does not "
                "contain replacement code."
            ),
        )

    try:

        replacement_tree = ast.parse(
            replacement_code
        )

    except SyntaxError as error:

        return (
            False,
            (
                "Pending LOGICAL BLOCK replacement is "
                "not valid Python: "
                f"{error}"
            ),
        )

    if len(
        replacement_tree.body
    ) != 1:

        return (
            False,
            (
                "LOGICAL BLOCK replacement must contain "
                "exactly one complete Python statement."
            ),
        )

    replacement_node = (
        replacement_tree.body[0]
    )

    if not isinstance(
        replacement_node,
        LOGICAL_BLOCK_AST_TYPES,
    ):

        return (
            False,
            (
                "LOGICAL BLOCK replacement must be one "
                "complete supported compound block."
            ),
        )

    selection_passed, selection_message, selected_block = (
        select_target_logical_block(
            target_name,
            selection_number,
        )
    )

    if (
        not selection_passed
        or selected_block is None
    ):

        return (
            False,
            selection_message,
        )

    replacement_type = type(
        replacement_node
    ).__name__

    if (
        selected_block.get(
            "node_type"
        )
        != replacement_type
    ):

        return (
            False,
            (
                "Selected source block type does not match "
                "the proposed replacement block type. "
                f"Selected: {selected_block.get('node_type')}. "
                f"Replacement: {replacement_type}."
            ),
        )

    _PENDING_CHANGE_APPROVAL.update(
        {
            "block_index": (
                selected_block[
                    "selection_number"
                ]
            ),
            "block_type": (
                selected_block[
                    "node_type"
                ]
            ),
            "block_start_line": (
                selected_block[
                    "start_line"
                ]
            ),
            "block_end_line": (
                selected_block[
                    "end_line"
                ]
            ),
            "block_source": (
                selected_block[
                    "source"
                ]
            ),
            "block_nesting_depth": (
                selected_block[
                    "nesting_depth"
                ]
            ),
            "block_parent_type": (
                selected_block[
                    "parent_type"
                ]
            ),
            "block_parent_line": (
                selected_block[
                    "parent_line"
                ]
            ),
            "block_file": (
                selected_block[
                    "file"
                ]
            ),
            # Keep SINGLE STATEMENT metadata mutually exclusive.
            "statement_index": None,
            "statement_start_line": None,
            "statement_end_line": None,
            "statement_source": None,
        }
    )

    return (
        True,
        "\n".join(
            [
                (
                    "Pending LOGICAL BLOCK selection stored."
                ),
                (
                    f"Target: {target_name}"
                ),
                (
                    "Selection: "
                    f"{selected_block['selection_number']}"
                ),
                (
                    "Type: "
                    f"{selected_block['node_type']}"
                ),
                (
                    "File: "
                    f"{selected_block['file']}"
                ),
                (
                    "Lines: "
                    f"{selected_block['start_line']}-"
                    f"{selected_block['end_line']}"
                ),
                (
                    "Nesting Depth: "
                    f"{selected_block['nesting_depth']}"
                ),
                "",
                (
                    "LOGICAL BLOCK selection is stored and ready for the approval, backup, readiness, and controlled implementation workflow."
                ),
                (
                    "No files were modified."
                ),
            ]
        ),
    )


def validate_pending_logical_block_readiness() -> tuple[bool, str]:
    """
    Read-only Task 29C readiness validation for a pending LOGICAL BLOCK.

    Confirms:
    - one pending LOGICAL BLOCK change exists
    - the exact block selection metadata is present
    - the pending change is approved
    - the replacement is exactly one supported logical block
    - replacement AST type matches the stored source block type
    - the live source block still exactly matches the stored snapshot
    - the recorded file/lines/type still match the live block
    - a valid verified backup exists and still matches current source

    This function does not modify project files.
    """

    pending_change = get_pending_change()

    if pending_change is None:

        return (
            False,
            "There is no pending change.",
        )

    if (
        pending_change.get(
            "boundary_type"
        )
        != "LOGICAL BLOCK"
    ):

        return (
            False,
            (
                "Pending change boundary is not "
                "LOGICAL BLOCK."
            ),
        )

    required_fields = (
        "target_name",
        "replacement_code",
        "block_index",
        "block_type",
        "block_start_line",
        "block_end_line",
        "block_source",
        "block_file",
    )

    missing_fields = [
        field
        for field in required_fields
        if pending_change.get(
            field
        ) in (
            None,
            "",
        )
    ]

    if missing_fields:

        return (
            False,
            (
                "Pending LOGICAL BLOCK metadata is incomplete. "
                "Missing: "
                + ", ".join(
                    missing_fields
                )
            ),
        )

    if not pending_change.get(
        "approved",
        False,
    ):

        return (
            False,
            (
                "Pending LOGICAL BLOCK change has not "
                "been approved."
            ),
        )

    replacement_code = (
        pending_change.get(
            "replacement_code",
            ""
        )
        or ""
    ).strip()

    try:

        replacement_tree = ast.parse(
            replacement_code
        )

    except SyntaxError as error:

        return (
            False,
            (
                "Pending LOGICAL BLOCK replacement "
                "is not valid Python: "
                f"{error}"
            ),
        )

    if len(
        replacement_tree.body
    ) != 1:

        return (
            False,
            (
                "Pending LOGICAL BLOCK replacement must "
                "contain exactly one complete Python statement."
            ),
        )

    replacement_node = (
        replacement_tree.body[0]
    )

    if not isinstance(
        replacement_node,
        LOGICAL_BLOCK_AST_TYPES,
    ):

        return (
            False,
            (
                "Pending LOGICAL BLOCK replacement is not "
                "one supported logical-block AST type."
            ),
        )

    replacement_type = type(
        replacement_node
    ).__name__

    stored_block_type = (
        pending_change.get(
            "block_type"
        )
    )

    if (
        replacement_type
        != stored_block_type
    ):

        return (
            False,
            (
                "Pending replacement type no longer matches "
                "the stored source block type. "
                f"Replacement: {replacement_type}; "
                f"stored source: {stored_block_type}."
            ),
        )

    target_name = (
        pending_change.get(
            "target_name"
        )
    )

    selection_number = (
        pending_change.get(
            "block_index"
        )
    )

    selected, select_message, live_block = (
        select_target_logical_block(
            target_name,
            selection_number,
        )
    )

    if (
        not selected
        or live_block is None
    ):

        return (
            False,
            (
                "Stored logical block can no longer be "
                "resolved from live source: "
                f"{select_message}"
            ),
        )

    stored_source = (
        pending_change.get(
            "block_source",
            ""
        )
        or ""
    )

    live_source = (
        live_block.get(
            "source",
            ""
        )
        or ""
    )

    if (
        live_source
        != stored_source
    ):

        return (
            False,
            (
                "Stored logical block source no longer "
                "matches the live source. Re-propose and "
                "re-select the block before implementation."
            ),
        )

    live_checks = (
        (
            "block_type",
            "node_type",
            "type",
        ),
        (
            "block_start_line",
            "start_line",
            "start line",
        ),
        (
            "block_end_line",
            "end_line",
            "end line",
        ),
        (
            "block_file",
            "file",
            "file",
        ),
    )

    for (
        pending_key,
        live_key,
        label,
    ) in live_checks:

        if (
            pending_change.get(
                pending_key
            )
            != live_block.get(
                live_key
            )
        ):

            return (
                False,
                (
                    "Stored logical block "
                    f"{label} no longer matches live source."
                ),
            )

    backup_valid, backup_message = (
        validate_pending_backup()
    )

    if not backup_valid:

        return (
            False,
            backup_message,
        )

    backup_matches, backup_match_message = (
        validate_backup_matches_current_source()
    )

    if not backup_matches:

        return (
            False,
            backup_match_message,
        )

    return (
        True,
        (
            "LOGICAL BLOCK readiness passed. "
            "The exact approved block, replacement, live source, "
            "and verified backup are consistent. "
            "The change is ready for controlled LOGICAL BLOCK implementation."
        ),
    )

def get_logical_block_replacement_target(
    target_name: str,
    replacement_code: str,
    requested_change: str = "",
) -> tuple[bool, str, dict | None]:
    """
    Deterministically identify the intended source logical block.

    Priority:
    1. Match source block header text against the development request.
    2. If no request-text match exists, fall back to AST-type matching.

    Read-only.
    """

    replacement_code = (
        replacement_code or ""
    ).strip()

    if not replacement_code:

        return (
            False,
            "LOGICAL BLOCK replacement code is empty.",
            None,
        )

    try:

        replacement_tree = ast.parse(
            replacement_code
        )

    except SyntaxError as error:

        return (
            False,
            (
                "Replacement code is not valid Python: "
                f"{error}"
            ),
            None,
        )

    if len(
        replacement_tree.body
    ) != 1:

        return (
            False,
            (
                "LOGICAL BLOCK replacement must contain "
                "exactly one complete Python statement."
            ),
            None,
        )

    replacement_node = (
        replacement_tree.body[0]
    )

    if not isinstance(
        replacement_node,
        LOGICAL_BLOCK_AST_TYPES,
    ):

        return (
            False,
            (
                "Replacement is not one supported "
                "logical-block AST type."
            ),
            None,
        )

    blocks = get_target_logical_blocks(
        target_name
    )

    if not blocks:

        return (
            False,
            "No selectable logical blocks were found.",
            None,
        )

    request_text = (
        requested_change or ""
    ).lower()

    # --------------------------------------------------------
    # REQUEST-TEXT SOURCE MATCH
    # --------------------------------------------------------

    request_matches = []

    for block in blocks:

        source_text = (
            block.get(
                "source",
                "",
            )
            or ""
        ).strip()

        if not source_text:
            continue

        header_line = (
            source_text.splitlines()[0]
            .strip()
            .lower()
        )

        # Exact/near-exact header phrase match.
        normalized_header = re.sub(
            r"\s+",
            " ",
            header_line,
        )

        normalized_request = re.sub(
            r"\s+",
            " ",
            request_text,
        )

        header_without_colon = (
            normalized_header.rstrip(":")
        )

        if (
            header_without_colon
            and header_without_colon
            in normalized_request
        ):

            request_matches.append(
                block
            )

    if len(
        request_matches
    ) == 1:

        selected_block = (
            request_matches[0]
        )

        selected_type = (
            selected_block.get(
                "node_type"
            )
        )

        replacement_type = type(
            replacement_node
        ).__name__

        if (
            selected_type
            != replacement_type
        ):

            return (
                False,
                (
                    "The requested source block is "
                    f"'{selected_type}', but the proposed replacement "
                    f"is '{replacement_type}'. "
                    "The model proposed the wrong logical-block level."
                ),
                selected_block,
            )

        return (
            True,
            (
                "Unique requested logical block identified "
                "from source header text."
            ),
            selected_block,
        )

    if len(
        request_matches
    ) > 1:

        return (
            False,
            (
                "Multiple logical blocks matched the request text. "
                "Select the exact block before proposal storage."
            ),
            None,
        )

    # --------------------------------------------------------
    # FALLBACK: AST-TYPE MATCH
    # --------------------------------------------------------

    replacement_type = type(
        replacement_node
    ).__name__

    type_matches = [
        block
        for block in blocks
        if block.get("node_type")
        == replacement_type
    ]

    if not type_matches:

        return (
            False,
            (
                "No source logical block of matching type "
                f"'{replacement_type}' was found."
            ),
            None,
        )

    if len(
        type_matches
    ) != 1:

        return (
            False,
            (
                "Multiple source logical blocks match the replacement "
                f"type '{replacement_type}'. Select the exact block "
                "before proposal storage."
            ),
            None,
        )

    return (
        True,
        "Unique logical-block source target identified by AST type.",
        type_matches[0],
    )

def promote_inner_logical_block_replacement(
    selected_block: dict,
    replacement_code: str,
) -> tuple[bool, str, str]:
    """
    Promote a valid inner logical-block replacement back into the
    exact selected outer logical block.

    Example:
    requested source = outer For
    model replacement = inner If
    result = complete For block with only that If replaced

    Read-only.
    """

    selected_source = (
        selected_block.get(
            "source",
            "",
        )
        or ""
    )

    if not selected_source.strip():

        return (
            False,
            "Selected logical block has no source text.",
            "",
        )

    replacement_code = (
        replacement_code or ""
    ).strip()

    if not replacement_code:

        return (
            False,
            "Replacement code is empty.",
            "",
        )

    import textwrap

    try:

        outer_source = textwrap.dedent(
            selected_source
        )

        outer_tree = ast.parse(
            outer_source
        )

        replacement_tree = ast.parse(
            replacement_code
        )

    except SyntaxError as error:

        return (
            False,
            (
                "Could not parse logical-block promotion source: "
                f"{error}"
            ),
            "",
        )

    if (
        len(outer_tree.body) != 1
        or len(replacement_tree.body) != 1
    ):

        return (
            False,
            (
                "Logical-block promotion requires one outer "
                "statement and one replacement statement."
            ),
            "",
        )

    outer_node = (
        outer_tree.body[0]
    )

    replacement_node = (
        replacement_tree.body[0]
    )

    replacement_type = type(
        replacement_node
    )

    replacement_header = (
        replacement_code
        .splitlines()[0]
        .strip()
        .rstrip(":")
    )

    descendant_matches = []

    for node in ast.walk(
        outer_node
    ):

        if node is outer_node:
            continue

        if not isinstance(
            node,
            replacement_type,
        ):
            continue

        node_line = ast.get_source_segment(
            outer_source,
            node,
        )

        if not node_line:
            continue

        node_header = (
            node_line
            .splitlines()[0]
            .strip()
            .rstrip(":")
        )

        if (
            node_header
            == replacement_header
        ):

            descendant_matches.append(
                node
            )

    if len(
        descendant_matches
    ) != 1:

        return (
            False,
            (
                "Could not uniquely promote the model's inner "
                "logical block into the requested outer block."
            ),
            "",
        )

    inner_node = (
        descendant_matches[0]
    )

    outer_lines = (
        outer_source.splitlines()
    )

    start_index = (
        inner_node.lineno - 1
    )

    end_index = (
        inner_node.end_lineno
    )

    original_line = (
        outer_lines[start_index]
    )

    indentation = (
        original_line[
            :len(original_line)
            - len(original_line.lstrip())
        ]
    )

    promoted_lines = []

    for line in replacement_code.splitlines():

        if line.strip():

            promoted_lines.append(
                indentation + line
            )

        else:

            promoted_lines.append(
                ""
            )

    promoted_source = "\n".join(
        outer_lines[:start_index]
        + promoted_lines
        + outer_lines[end_index:]
    )

    try:

        promoted_tree = ast.parse(
            promoted_source
        )

    except SyntaxError as error:

        return (
            False,
            (
                "Promoted logical block failed syntax validation: "
                f"{error}"
            ),
            "",
        )

    if len(
        promoted_tree.body
    ) != 1:

        return (
            False,
            (
                "Promoted source is not exactly one complete "
                "logical block."
            ),
            "",
        )

    promoted_node = (
        promoted_tree.body[0]
    )

    expected_type = (
        selected_block.get(
            "node_type"
        )
    )

    if (
        type(promoted_node).__name__
        != expected_type
    ):

        return (
            False,
            (
                "Promoted source does not preserve the requested "
                f"outer block type '{expected_type}'."
            ),
            "",
        )

    return (
        True,
        (
            "Inner logical-block replacement promoted into "
            "the exact requested outer block."
        ),
        promoted_source.strip(),
    )

def validate_requested_exception_change(
    requested_change: str,
    replacement_code: str,
) -> tuple[bool, str]:
    """
    Validate explicit named-exception requirements from the request.
    """

    requested_exceptions = []

    for name in re.findall(
        r"\b[A-Z][A-Za-z0-9_]*Error\b",
        requested_change or "",
    ):
        if name not in requested_exceptions:
            requested_exceptions.append(name)

    if len(requested_exceptions) < 2:
        return (
            True,
            "No multi-exception semantic constraint detected.",
        )

    try:
        tree = ast.parse(replacement_code or "")
    except SyntaxError as error:
        return (
            False,
            (
                "Replacement code is not valid Python during "
                f"semantic validation: {error}"
            ),
        )

    caught_names = set()

    for node in ast.walk(tree):
        if not isinstance(node, ast.ExceptHandler):
            continue

        handler_type = node.type

        if isinstance(handler_type, ast.Name):
            caught_names.add(handler_type.id)

        elif isinstance(handler_type, ast.Tuple):
            for item in handler_type.elts:
                if isinstance(item, ast.Name):
                    caught_names.add(item.id)

    missing = [
        name
        for name in requested_exceptions
        if name not in caught_names
    ]

    if missing:
        return (
            False,
            (
                "Replacement does not satisfy the requested "
                "exception handling change. Missing: "
                + ", ".join(missing)
            ),
        )

    return (
        True,
        (
            "Replacement satisfies requested exception names: "
            + ", ".join(requested_exceptions)
        ),
    )


def apply_requested_exception_change(
    requested_change: str,
    replacement_code: str,
) -> tuple[bool, str, str]:
    """
    Deterministically add explicitly requested exception names to one
    existing named except handler.
    """

    requested_exceptions = []

    for name in re.findall(
        r"\b[A-Z][A-Za-z0-9_]*Error\b",
        requested_change or "",
    ):
        if name not in requested_exceptions:
            requested_exceptions.append(name)

    if len(requested_exceptions) < 2:
        return (
            False,
            "No deterministic multi-exception change requested.",
            replacement_code,
        )

    try:
        tree = ast.parse(replacement_code or "")
    except SyntaxError as error:
        return (
            False,
            (
                "Replacement code is not valid Python during "
                f"exception correction: {error}"
            ),
            replacement_code,
        )

    handlers = [
        node
        for node in ast.walk(tree)
        if isinstance(node, ast.ExceptHandler)
        and node.type is not None
    ]

    if len(handlers) != 1:
        return (
            False,
            (
                "Deterministic exception correction requires "
                "exactly one except handler."
            ),
            replacement_code,
        )

    handler = handlers[0]
    existing_names = []

    if isinstance(handler.type, ast.Name):
        existing_names = [handler.type.id]

    elif isinstance(handler.type, ast.Tuple):
        existing_names = [
            item.id
            for item in handler.type.elts
            if isinstance(item, ast.Name)
        ]

    if not existing_names:
        return (
            False,
            (
                "Existing except handler type is not a supported "
                "named exception form."
            ),
            replacement_code,
        )

    merged = []

    for name in existing_names + requested_exceptions:
        if name not in merged:
            merged.append(name)

    if len(merged) == 1:
        new_type = ast.Name(
            id=merged[0],
            ctx=ast.Load(),
        )
    else:
        new_type = ast.Tuple(
            elts=[
                ast.Name(
                    id=name,
                    ctx=ast.Load(),
                )
                for name in merged
            ],
            ctx=ast.Load(),
        )

    handler.type = new_type
    ast.fix_missing_locations(tree)

    corrected = ast.unparse(tree)

    ok, message = validate_requested_exception_change(
        requested_change,
        corrected,
    )

    if not ok:
        return (
            False,
            message,
            replacement_code,
        )

    return (
        True,
        (
            "Explicit requested exception names were "
            "deterministically applied."
        ),
        corrected,
    )

def build_deterministic_logical_block_proposal(
    target_name: str,
    requested_change: str,
    raw_proposal: str,
) -> str:
    """
    Rebuild a LOGICAL BLOCK proposal from deterministic source facts.

    For explicit multi-exception requests, the exact requested source
    block is used as the replacement baseline and modified
    deterministically. The model's replacement code is not trusted for
    that semantic change.

    For other logical-block requests, the model may still suggest
    replacement code, but source identity and block metadata remain
    Python/AST-grounded.
    """

    requested_exceptions = []

    for name in re.findall(
        r"\b[A-Z][A-Za-z0-9_]*Error\b",
        requested_change or "",
    ):
        if name not in requested_exceptions:
            requested_exceptions.append(
                name
            )

    # --------------------------------------------------------
    # DETERMINISTIC SOURCE-FIRST PATH FOR EXCEPTION CHANGES
    # --------------------------------------------------------

    if len(
        requested_exceptions
    ) >= 2:

        blocks = get_target_logical_blocks(
            target_name
        )

        request_text = (
            requested_change or ""
        ).lower()

        normalized_request = re.sub(
            r"\s+",
            " ",
            request_text,
        )

        request_matches = []

        for block in blocks:

            source_text = (
                block.get(
                    "source",
                    "",
                )
                or ""
            ).strip()

            if not source_text:
                continue

            header_line = (
                source_text
                .splitlines()[0]
                .strip()
                .lower()
            )

            normalized_header = re.sub(
                r"\s+",
                " ",
                header_line,
            ).rstrip(":")

            if (
                normalized_header
                and normalized_header
                in normalized_request
            ):

                request_matches.append(
                    block
                )

        if len(
            request_matches
        ) != 1:

            return (
                "PROPOSAL STATUS: MORE INSPECTION REQUIRED\n\n"
                "A. WHY THE CURRENT SOURCE IS INSUFFICIENT\n\n"
                "The requested logical block could not be uniquely "
                "identified from source header text.\n\n"
                "B. EXACT NEXT INSPECTION REQUIRED\n\n"
                "Use blocks <function_or_class> and select-block "
                "<function_or_class> | <number> to identify the exact "
                "logical block before proposal storage.\n\n"
                "C. WHAT MUST BE CONFIRMED\n\n"
                "Confirm one exact source-backed logical block.\n\n"
                "NO FILES WERE MODIFIED"
            )

        selected_block = (
            request_matches[0]
        )

        replacement_code = (
            selected_block.get(
                "source",
                "",
            )
            or ""
        ).strip()

        (
            corrected,
            correction_message,
            corrected_code,
        ) = apply_requested_exception_change(
            requested_change,
            replacement_code,
        )

        if not corrected:

            return (
                "PROPOSAL STATUS: MORE INSPECTION REQUIRED\n\n"
                "A. WHY THE CURRENT SOURCE IS INSUFFICIENT\n\n"
                f"{correction_message}\n\n"
                "B. EXACT NEXT INSPECTION REQUIRED\n\n"
                "Inspect the selected source block's exception "
                "handlers before proposal storage.\n\n"
                "C. WHAT MUST BE CONFIRMED\n\n"
                "Confirm one supported named except handler can be "
                "modified deterministically.\n\n"
                "NO FILES WERE MODIFIED"
            )

        replacement_code = (
            corrected_code
        )

        semantic_ok, semantic_message = (
            validate_requested_exception_change(
                requested_change,
                replacement_code,
            )
        )

        if not semantic_ok:

            return (
                "PROPOSAL STATUS: MORE INSPECTION REQUIRED\n\n"
                "A. WHY THE CURRENT SOURCE IS INSUFFICIENT\n\n"
                f"{semantic_message}\n\n"
                "B. EXACT NEXT INSPECTION REQUIRED\n\n"
                "Inspect the deterministic exception transformation.\n\n"
                "C. WHAT MUST BE CONFIRMED\n\n"
                "Confirm every requested exception name is present.\n\n"
                "NO FILES WERE MODIFIED"
            )

        file_name = selected_block[
            "file"
        ]
        start_line = selected_block[
            "start_line"
        ]
        end_line = selected_block[
            "end_line"
        ]
        block_type = selected_block[
            "node_type"
        ]
        source_code = selected_block[
            "source"
        ]

        return f"""PROPOSAL STATUS: READY

A. CONFIRMED PROBLEM MECHANISM

The requested change targets one complete source-backed logical block.

Target:
{target_name}

Source block type:
{block_type}

Source file:
{file_name}

Source lines:
{start_line}-{end_line}

Existing source block:

```python
{source_code}
```

B. CHANGE SUMMARY

{requested_change}

C. CONFIRMED AFFECTED FILES

- {file_name}

D. REPLACEMENT BOUNDARY

LOGICAL BLOCK

E. COMPLETE REPLACEMENT CODE

```python
{replacement_code}
```

F. WHY THIS CHANGE SHOULD WORK

The replacement was generated deterministically from the exact selected
source block. The requested exception names were applied directly to the
existing except handler using Python AST.

G. WHY THIS IS SAFE

- The proposal is grounded to one exact source-backed logical block.
- The model's replacement code was not used for this exception change.
- No project file has been modified.
- Approval is still required.
- Backup is still required.
- Controlled implementation remains blocked until the exact block is stored, approved, backed up, and passes readiness validation.
- This proposal stores metadata only; it does not modify project files.

H. REQUIRED TESTS

1. Confirm the replacement still contains the original logical block.
2. Confirm every explicitly requested exception name is present.
3. Store the exact pending block only after reviewing the proposal.
4. After review, follow the controlled workflow: store-block, approve, backup, readiness, then implement.

NO FILES WERE MODIFIED"""

    # --------------------------------------------------------
    # GENERAL LOGICAL-BLOCK PATH
    # --------------------------------------------------------

    replacement_code = (
        extract_proposal_replacement_code(
            raw_proposal
        )
    )

    (
        matched,
        match_message,
        selected_block,
    ) = get_logical_block_replacement_target(
        target_name,
        replacement_code,
        requested_change,
    )

    if (
        not matched
        and selected_block is not None
    ):

        (
            promoted,
            promotion_message,
            promoted_code,
        ) = promote_inner_logical_block_replacement(
            selected_block,
            replacement_code,
        )

        if promoted:

            replacement_code = (
                promoted_code
            )

            (
                matched,
                match_message,
                selected_block,
            ) = get_logical_block_replacement_target(
                target_name,
                replacement_code,
                requested_change,
            )

    if (
        not matched
        or selected_block is None
    ):

        return (
            "PROPOSAL STATUS: MORE INSPECTION REQUIRED\n\n"
            "A. WHY THE CURRENT SOURCE IS INSUFFICIENT\n\n"
            f"{match_message}\n\n"
            "B. EXACT NEXT INSPECTION REQUIRED\n\n"
            "Use blocks <function_or_class> and select-block "
            "<function_or_class> | <number> to identify the exact "
            "logical block before proposal storage.\n\n"
            "C. WHAT MUST BE CONFIRMED\n\n"
            "Confirm one exact source-backed logical block for "
            "the proposed replacement.\n\n"
            "NO FILES WERE MODIFIED"
        )

    file_name = selected_block[
        "file"
    ]
    start_line = selected_block[
        "start_line"
    ]
    end_line = selected_block[
        "end_line"
    ]
    block_type = selected_block[
        "node_type"
    ]
    source_code = selected_block[
        "source"
    ]

    return f"""PROPOSAL STATUS: READY

A. CONFIRMED PROBLEM MECHANISM

The requested change targets one complete source-backed logical block.

Target:
{target_name}

Source block type:
{block_type}

Source file:
{file_name}

Source lines:
{start_line}-{end_line}

Existing source block:

```python
{source_code}
```

B. CHANGE SUMMARY

{requested_change}

C. CONFIRMED AFFECTED FILES

- {file_name}

D. REPLACEMENT BOUNDARY

LOGICAL BLOCK

E. COMPLETE REPLACEMENT CODE

```python
{replacement_code}
```

F. WHY THIS CHANGE SHOULD WORK

The replacement is one complete Python logical block whose AST type
matches the unique source block type '{block_type}' identified above.

G. WHY THIS IS SAFE

- The proposal is grounded to one exact source-backed logical block.
- No project file has been modified.
- Approval is still required.
- Backup is still required.
- Controlled implementation remains blocked until the exact block is stored, approved, backed up, and passes readiness validation.
- This proposal stores metadata only; it does not modify project files.

H. REQUIRED TESTS

1. Re-run blocks {target_name}.
2. Confirm the intended block still resolves to lines {start_line}-{end_line}.
3. Store the exact pending block only after reviewing the proposal.
4. After review, follow the controlled workflow: store-block, approve, backup, readiness, then implement.

NO FILES WERE MODIFIED"""

def validate_logical_block_proposal(
    proposal: str,
    target_name: str,
) -> tuple[bool, str]:
    """
    Validate that a READY LOGICAL BLOCK proposal resolves
    deterministically to one exact source logical block.
    """

    if not proposal.startswith(
        "PROPOSAL STATUS: READY"
    ):

        return (
            False,
            "Proposal is not READY.",
        )

    boundary_section = extract_proposal_section(
        proposal,
        "D. REPLACEMENT BOUNDARY",
        "E. COMPLETE REPLACEMENT CODE",
    ).upper()

    if "LOGICAL BLOCK" not in boundary_section:

        return (
            False,
            "Proposal is not a LOGICAL BLOCK proposal.",
        )

    replacement_code = (
        extract_proposal_replacement_code(
            proposal
        )
    )

    requested_change = extract_proposal_section(
        proposal,
        "B. CHANGE SUMMARY",
        "C. CONFIRMED AFFECTED FILES",
    )

    semantic_ok, semantic_message = (
        validate_requested_exception_change(
            requested_change,
            replacement_code,
        )
    )

    if not semantic_ok:
        return (
            False,
            semantic_message,
        )

    matched, message, _block = (
        get_logical_block_replacement_target(
            target_name,
            replacement_code,
            requested_change,
        )
    )

    return (
        matched,
        message,
    )

def build_code_proposal_context(
    target_name: str,
) -> str:
    """
    Build controlled source context for proposal generation.
    """

    target_source = get_target_source(
        target_name
    )

    if target_source.startswith(
        "No function or class"
    ):

        return target_source

    control_flow_facts = (
        build_target_control_flow_facts(
            target_name
        )
    )

    forward_context = (
        build_dependency_context(
            target_name
        )
    )

    reverse_context = (
        build_reverse_dependency_context(
            target_name
        )
    )

    combined_context = f"""
############################################################
TARGET SOURCE
############################################################

{target_source}

############################################################
DETERMINISTIC CONTROL FLOW FACTS
############################################################

{control_flow_facts}

############################################################
DIRECT DEPENDENCIES
############################################################

{forward_context}

############################################################
DIRECT CALLERS
############################################################

{reverse_context}
"""

    if (
        len(combined_context)
        > MAX_CODE_PROPOSAL_CHARACTERS
    ):

        combined_context = (
            combined_context[
                :MAX_CODE_PROPOSAL_CHARACTERS
            ]
            + "\n\n"
            + "[CODE PROPOSAL CONTEXT TRUNCATED]"
        )

    return combined_context


def generate_code_proposal(
    target_name: str,
    requested_change: str,
) -> str:
    """
    Generate a source-grounded code proposal.

    SINGLE STATEMENT and LOGICAL BLOCK proposals are
    deterministically rebuilt from source/AST facts.
    """

    proposal_context = (
        build_code_proposal_context(
            target_name
        )
    )

    if proposal_context.startswith(
        "No function or class"
    ):

        return proposal_context

    development_context = f"""
CURRENT NOVELIST PROJECT INDEX:

{build_project_index()}

TARGET:

{target_name}

REQUESTED CHANGE:

{requested_change}

SOURCE CONTEXT:

{proposal_context}

You are preparing proposed code only.

YOU DO NOT HAVE PERMISSION TO MODIFY PROJECT FILES.

Use only source-supported code.
Prefer the smallest safe replacement boundary.

Allowed proposal boundaries for this stage:

- SINGLE STATEMENT
- LOGICAL BLOCK

Use SINGLE STATEMENT only when one complete top-level statement
fully satisfies the request.

Use LOGICAL BLOCK when the requested change requires replacing one
complete supported compound block such as:

- if
- for
- while
- try
- with
- match

For either boundary, Section E must contain exactly one complete
valid Python statement.

Do not include surrounding unrelated statements.

Deterministic Python/AST code will independently identify the exact
existing source statement or logical block.

If the source target is ambiguous, return:

PROPOSAL STATUS: MORE INSPECTION REQUIRED

READY OUTPUT FORMAT:

PROPOSAL STATUS: READY
A. CONFIRMED PROBLEM MECHANISM
B. CHANGE SUMMARY
C. CONFIRMED AFFECTED FILES
D. REPLACEMENT BOUNDARY
E. COMPLETE REPLACEMENT CODE
F. WHY THIS CHANGE SHOULD WORK
G. WHY THIS IS SAFE
H. REQUIRED TESTS

End with exactly:

NO FILES WERE MODIFIED
"""

    try:

        response = client.responses.create(
            model=OPENAI_MODEL,
            instructions=(
                DEVELOPMENT_BOT_INSTRUCTIONS
            ),
            input=development_context,
        )

        raw_proposal = response.output_text

        if not raw_proposal.startswith(
            "PROPOSAL STATUS: READY"
        ):

            return raw_proposal

        boundary_section = (
            extract_proposal_section(
                raw_proposal,
                "D. REPLACEMENT BOUNDARY",
                "E. COMPLETE REPLACEMENT CODE",
            )
        ).upper()

        if (
            "LOGICAL BLOCK"
            in boundary_section
        ):

            deterministic_proposal = (
                build_deterministic_logical_block_proposal(
                    target_name,
                    requested_change,
                    raw_proposal,
                )
            )

            if not deterministic_proposal.startswith(
                "PROPOSAL STATUS: READY"
            ):

                return deterministic_proposal

            grounded, grounding_message = (
                validate_logical_block_proposal(
                    deterministic_proposal,
                    target_name,
                )
            )

            if not grounded:

                return (
                    "PROPOSAL STATUS: MORE INSPECTION REQUIRED\n\n"
                    "A. WHY THE CURRENT SOURCE IS INSUFFICIENT\n\n"
                    f"{grounding_message}\n\n"
                    "B. EXACT NEXT INSPECTION REQUIRED\n\n"
                    "Inspect/select the exact logical block before "
                    "generating another proposal.\n\n"
                    "C. WHAT MUST BE CONFIRMED\n\n"
                    "Confirm one unambiguous source logical block.\n\n"
                    "NO FILES WERE MODIFIED"
                )

            return deterministic_proposal

        if (
            "SINGLE STATEMENT"
            in boundary_section
        ):

            deterministic_proposal = (
                build_deterministic_single_statement_proposal(
                    target_name,
                    requested_change,
                    raw_proposal,
                )
            )

            if not deterministic_proposal.startswith(
                "PROPOSAL STATUS: READY"
            ):

                return deterministic_proposal

            grounded, grounding_message = (
                validate_source_grounded_proposal(
                    deterministic_proposal,
                    target_name,
                )
            )

            if not grounded:

                return (
                    "PROPOSAL STATUS: MORE INSPECTION REQUIRED\n\n"
                    "A. WHY THE CURRENT SOURCE IS INSUFFICIENT\n\n"
                    f"{grounding_message}\n\n"
                    "B. EXACT NEXT INSPECTION REQUIRED\n\n"
                    "Inspect/select the exact source statement "
                    "before generating another proposal.\n\n"
                    "C. WHAT MUST BE CONFIRMED\n\n"
                    "Confirm one unambiguous source statement "
                    "for the requested replacement.\n\n"
                    "NO FILES WERE MODIFIED"
                )

            return deterministic_proposal

        return (
            "PROPOSAL STATUS: MORE INSPECTION REQUIRED\n\n"
            "A. WHY THE CURRENT SOURCE IS INSUFFICIENT\n\n"
            "The proposal boundary was not one of the currently "
            "supported deterministic proposal boundaries.\n\n"
            "B. EXACT NEXT INSPECTION REQUIRED\n\n"
            "Use SINGLE STATEMENT or LOGICAL BLOCK.\n\n"
            "C. WHAT MUST BE CONFIRMED\n\n"
            "Confirm the smallest source-backed replacement boundary.\n\n"
            "NO FILES WERE MODIFIED"
        )

    except Exception as error:

        return (
            f"Development Bot Error: {error}"
        )


# ============================================================
# TERMINAL INTERFACE
# ============================================================

def run_development_bot():

    print()
    print("=" * 60)
    print("NOVELIST DEVELOPMENT BOT")
    print("=" * 60)
    print(f"Model: {OPENAI_MODEL}")
    print("Mode: READ / REASON / RECOMMEND")
    print(f"Project: {PROJECT_ROOT.name}")
    print()

    print("Commands:")
    print()

    print("  structure")
    print("      Show project files")
    print()

    print("  project-files")
    print("      Show active Python files")
    print()

    print("  index")
    print("      Display project code index")
    print()

    print("  index-analyze | <question>")
    print("      Analyze architecture using index")
    print()
    print("  context <development request>")
    print("      Find likely relevant code targets")
    print()
    print("  inspect <development request>")
    print("      Inspect likely code for a development request")
    print()
    print("  auto-target <development request>")
    print("      Select likely change target automatically")
    print()
    print("  auto-plan <development request>")
    print("      Automatically select target and build change plan")
    print()
    print("  pending")
    print("      Show the current pending change")
    print()

    print("  approve")
    print("      Approve the current pending change")
    print()

    print("  reject")
    print("      Reject and clear the current pending change")
    print()
    print("  find <function_or_class>")
    print("      Locate a function or class")
    print()

    print("  source <function_or_class>")
    print("      Display only that target's source")
    print()

    print("  deps <function_or_class>")
    print("      Show direct internal dependencies")
    print()
    print("  deep-deps <function_or_class>")
    print("      Show recursive internal dependency tree")
    print()
    print("  callers <function_or_class>")
    print("      Show direct internal callers")
    print()
    print("  deep-callers <function_or_class>")
    print("      Show recursive internal caller tree")
    print()
    print(
        "  plan <function_or_class> | <requested change>"
    )
    print(
        "      Build a safe implementation plan"
    )
    print()
    print(
        "  propose <function_or_class> | <requested change>"
    )
    print(
        "      Generate a safe code proposal"
    )
    print()
    print(
        "  impact <function_or_class> | <question>"
    )
    print(
        "      Analyze change impact on direct callers"
    )
    print()

    print(
        "  trace <function_or_class> | <question>"
    )
    print(
        "      Analyze target with direct dependencies"
    )
    print()

    print(
        "  target <function_or_class> | <question>"
    )
    print(
        "      Analyze only the targeted source code"
    )
    print()

    print("  read <filename.py>")
    print("      Display one Python file")
    print()

    print(
        "  analyze <filename.py> <question>"
    )
    print(
        "      Analyze one Python file"
    )
    print()

    print("  project | <question>")
    print(
        "      Perform deeper project-wide analysis"
    )
    print()

    print("  exit")
    print("      Close the bot")

    print("=" * 60)

    while True:

        print()

        user_request = input(
            "Development Task > "
        ).strip()

        # ----------------------------------------------------
        # EXIT
        # ----------------------------------------------------

        if user_request.lower() in {
            "exit",
            "quit",
            "close",
        }:

            print()
            print(
                "Novelist Development Bot closed."
            )

            break

        # ----------------------------------------------------
        # PROJECT STRUCTURE
        # ----------------------------------------------------

        if user_request.lower() == "structure":

            display_project_structure()

            continue

        # ----------------------------------------------------
        # PROJECT FILE LIST
        # ----------------------------------------------------

        if user_request.lower() == "project-files":

            display_project_files()

            continue

        # ----------------------------------------------------
        # PROJECT INDEX
        # ----------------------------------------------------

        if user_request.lower() == "index":

            display_project_index()

            continue

        # ----------------------------------------------------
        # INDEX ANALYSIS
        # ----------------------------------------------------

        if user_request.lower().startswith(
            "index-analyze"
        ):

            command_content = (
                user_request[13:].strip()
            )

            if command_content.startswith("|"):

                command_content = (
                    command_content[1:].strip()
                )

            if not command_content:

                print(
                    "Usage: "
                    "index-analyze | <question>"
                )

                continue

            print()
            print("Development Bot:")
            print("-" * 60)

            response = analyze_project_index(
                command_content
            )

            print(response)
            print("-" * 60)

            continue

        # ----------------------------------------------------
        # FIND TARGET
        # ----------------------------------------------------

        if user_request.lower().startswith(
            "find "
        ):

            target_name = (
                user_request[5:].strip()
            )

            display_target(
                target_name
            )

            continue

        # ----------------------------------------------------
        # DISPLAY TARGET SOURCE
        # ----------------------------------------------------

        if user_request.lower().startswith(
            "source "
        ):

            target_name = (
                user_request[7:].strip()
            )

            display_target_source(
                target_name
            )

            continue

               # ----------------------------------------------------
        # FORWARD DEPENDENCIES
        # ----------------------------------------------------

        if user_request.lower().startswith(
            "deps "
        ):

            target_name = (
                user_request[5:].strip()
            )

            display_dependencies(
                target_name
            )

            continue

        # ----------------------------------------------------
        # DEEP DEPENDENCY TREE
        # ----------------------------------------------------

        if user_request.lower().startswith(
            "deep-deps "
        ):

            target_name = (
                user_request[10:].strip()
            )

            print()
            print("=" * 60)
            print(
                f"DEEP DEPENDENCIES: {target_name}"
            )
            print("=" * 60)

            print(
                format_dependency_tree(
                    target_name
                )
            )

            print("=" * 60)

            continue

        # ----------------------------------------------------
        # REVERSE DEPENDENCIES / CALLERS
        # ----------------------------------------------------

        if user_request.lower().startswith(
            "callers "
        ):

            target_name = (
                user_request[8:].strip()
            )

            print()
            print("=" * 60)
            print(
                f"CALLERS: {target_name}"
            )
            print("=" * 60)

            print(
                format_reverse_dependencies(
                    target_name
                )
            )

            print("=" * 60)

            continue
                # ----------------------------------------------------
        # DEEP REVERSE DEPENDENCY TREE
        # ----------------------------------------------------

        if user_request.lower().startswith(
            "deep-callers "
        ):

            target_name = (
                user_request[13:].strip()
            )

            print()
            print("=" * 60)
            print(
                f"DEEP CALLERS: {target_name}"
            )
            print("=" * 60)

            print(
                format_caller_tree(
                    target_name
                )
            )

            print("=" * 60)

            continue
                # ----------------------------------------------------
        # SMART CONTEXT SEARCH
        # ----------------------------------------------------

        if user_request.lower().startswith(
            "context "
        ):

            development_request = (
                user_request[8:].strip()
            )

            if not development_request:

                print(
                    "Usage: context "
                    "<development request>"
                )

                continue

            print()
            print("=" * 60)
            print("SMART CODE CONTEXT")
            print("=" * 60)

            print(
                format_relevant_code_targets(
                    development_request
                )
            )

            print("=" * 60)

            continue
                # ----------------------------------------------------
        # SMART DEVELOPMENT REQUEST INSPECTION
        # ----------------------------------------------------

        if user_request.lower().startswith(
            "inspect "
        ):

            development_request = (
                user_request[8:].strip()
            )

            if not development_request:

                print(
                    "Usage: inspect "
                    "<development request>"
                )

                continue

            print()
            print("=" * 60)
            print("SMART DEVELOPMENT INSPECTION")
            print("=" * 60)

            print(
                inspect_development_request(
                    development_request
                )
            )

            print("=" * 60)

            continue
                # ----------------------------------------------------
        # AUTOMATIC CHANGE TARGET
        # ----------------------------------------------------

        if user_request.lower().startswith(
            "auto-target "
        ):

            development_request = (
                user_request[12:].strip()
            )

            if not development_request:

                print(
                    "Usage: auto-target "
                    "<development request>"
                )

                continue

            print()
            print("=" * 60)
            print("AUTOMATIC CHANGE TARGET")
            print("=" * 60)

            print(
                format_selected_change_target(
                    development_request
                )
            )

            print("=" * 60)

            continue
                # ----------------------------------------------------
        # AUTOMATIC SAFE CHANGE PLAN
        # ----------------------------------------------------

        if user_request.lower().startswith(
            "auto-plan "
        ):

            development_request = (
                user_request[10:].strip()
            )

            if not development_request:

                print(
                    "Usage: auto-plan "
                    "<development request>"
                )

                continue

            print()
            print("=" * 60)
            print("AUTOMATIC SAFE CHANGE PLAN")
            print("=" * 60)

            print(
                automatically_plan_change(
                    development_request
                )
            )

            print("=" * 60)

            continue

        # ----------------------------------------------------
        # CHANGE APPROVAL COMMANDS
        # ----------------------------------------------------

        if user_request.lower() == "approve":

            print()
            print("=" * 60)
            print("CHANGE APPROVAL")
            print("=" * 60)

            print(
                approve_pending_change()
            )

            print("=" * 60)

            continue

        if user_request.lower() == "reject":

            print()
            print("=" * 60)
            print("CHANGE REJECTION")
            print("=" * 60)

            print(
                reject_pending_change()
            )

            print("=" * 60)

            continue

        if user_request.lower() == "pending":

            print()
            print("=" * 60)
            print("PENDING CHANGE")
            print("=" * 60)

            pending_change = (
                get_pending_change()
            )

            if pending_change is None:

                print(
                    "There is no pending change."
                )

            else:

                print(
                    f"Target: "
                    f"{pending_change['target_name']}"
                )

                print(
                    f"Request: "
                    f"{pending_change['development_request']}"
                )

                print(
                    f"Boundary: "
                    f"{pending_change.get('boundary_type')}"
                )

                print(
                    "Affected Files: "
                    + ", ".join(
                        pending_change.get(
                            "affected_files",
                            [],
                        )
                    )
                )

                print(
                    f"Approved: "
                    f"{pending_change['approved']}"
                )

                print(
                    f"Backup Path: "
                    f"{pending_change.get('backup_path')}"
                )

                print(
                    f"Implemented: "
                    f"{pending_change.get('implemented', False)}"
                )

                print(
                    f"Implemented File: "
                    f"{pending_change.get('implemented_file')}"
                )

                print()
                print(
                    "VERIFICATION STATUS"
                )

                print(
                    "Post-Implementation Syntax Passed: "
                    f"{pending_change.get('post_implementation_syntax_passed')}"
                )

                print(
                    "Post-Implementation Unit Tests Passed: "
                    f"{pending_change.get('post_implementation_unit_tests_passed')}"
                )

                print(
                    "Post-Implementation Verification Passed: "
                    f"{pending_change.get('post_implementation_verification_passed')}"
                )

                print(
                    "Automatic Rollback Attempted: "
                    f"{pending_change.get('automatic_rollback_attempted')}"
                )

                print(
                    "Automatic Rollback Succeeded: "
                    f"{pending_change.get('automatic_rollback_succeeded')}"
                )

                print(
                    "Post-Rollback Syntax Passed: "
                    f"{pending_change.get('post_rollback_syntax_passed')}"
                )

                print(
                    "Post-Rollback Unit Tests Passed: "
                    f"{pending_change.get('post_rollback_unit_tests_passed')}"
                )

                print(
                    "Post-Rollback Verification Passed: "
                    f"{pending_change.get('post_rollback_verification_passed')}"
                )

                print(
                    f"Statement Selection: "
                    f"{pending_change.get('statement_index')}"
                )

                print(
                    f"Statement Lines: "
                    f"{pending_change.get('statement_start_line')}"
                    f"-"
                    f"{pending_change.get('statement_end_line')}"
                )

                if pending_change.get(
                    "statement_source"
                ):

                    print()
                    print(
                        "Selected Statement:"
                    )

                    print(
                        pending_change.get(
                            "statement_source"
                        )
                    )

                print()
                print("Replacement Code:")

                print(
                    pending_change.get(
                        "replacement_code",
                        "",
                    )
                )

            print("=" * 60)

            continue

        if user_request.lower() == "validate":

            print()
            print("=" * 60)
            print("PRE-IMPLEMENTATION VALIDATION")
            print("=" * 60)

            validation_passed, validation_message = (
                validate_pending_change_state()
            )

            print(
                validation_message
            )

            print(
                f"Validation Passed: "
                f"{validation_passed}"
            )

            print("=" * 60)

            continue

        if user_request.lower() == "backup":

            print()
            print("=" * 60)
            print("SOURCE FILE BACKUP")
            print("=" * 60)

            backup_created, backup_message = (
                create_pending_change_backup()
            )

            print(
                backup_message
            )

            print(
                f"Backup Created: "
                f"{backup_created}"
            )

            print("=" * 60)

            continue

        if user_request.lower() == "readiness":

            print()
            print("=" * 60)
            print("IMPLEMENTATION READINESS")
            print("=" * 60)

            pending_change = get_pending_change()

            if (
                pending_change is not None
                and pending_change.get(
                    "boundary_type"
                )
                == "LOGICAL BLOCK"
            ):

                readiness_passed, readiness_message = (
                    validate_pending_logical_block_readiness()
                )

            else:

                readiness_passed, readiness_message = (
                    validate_implementation_readiness()
                )

            print(
                readiness_message
            )

            print(
                f"Implementation Ready: "
                f"{readiness_passed}"
            )

            print("=" * 60)

            continue

        if user_request.lower() == "implement":

            print()
            print("=" * 60)
            print("CONTROLLED IMPLEMENTATION")
            print("=" * 60)

            implementation_completed, implementation_message = (
                implement_pending_change()
            )

            print(
                implementation_message
            )

            print(
                f"Implementation Completed: "
                f"{implementation_completed}"
            )

            print("=" * 60)

            continue

        if user_request.lower() == "rollback":

            print()
            print("=" * 60)
            print("SOURCE FILE ROLLBACK")
            print("=" * 60)

            rollback_completed, rollback_message = (
                rollback_pending_change_backup()
            )

            print(
                rollback_message
            )

            print(
                f"Rollback Completed: "
                f"{rollback_completed}"
            )

            print("=" * 60)

            continue

        if user_request.lower() == "tests":

            print()
            print("=" * 60)
            print("AUTOMATED TEST RUNNER")
            print("=" * 60)

            syntax_passed, syntax_message = (
                run_project_syntax_validation()
            )

            print(
                syntax_message
            )

            print()
            print(
                format_project_test_files()
            )

            print()
            print(
                f"Syntax Validation Passed: "
                f"{syntax_passed}"
            )

            if syntax_passed:

                print()
                print("-" * 60)
                print("CONTROLLED UNIT TEST EXECUTION")
                print("-" * 60)

                unit_tests_passed, unit_tests_message = (
                    run_project_unit_tests()
                )

                print(
                    unit_tests_message
                )

                print()
                print(
                    f"Unit Tests Passed: "
                    f"{unit_tests_passed}"
                )

            else:

                unit_tests_passed = False

                print()
                print(
                    "Unit tests were not executed because "
                    "project syntax validation failed."
                )

                print()
                print(
                    "Unit Tests Passed: False"
                )

            print()
            print(
                "Overall Test Result: "
                + (
                    "PASSED"
                    if (
                        syntax_passed
                        and unit_tests_passed
                    )
                    else "FAILED"
                )
            )

            print("=" * 60)

            continue

        if user_request.lower() == "statements":

            print()
            print("=" * 60)
            print("SELECTABLE STATEMENTS")
            print("=" * 60)

            pending_change = (
                get_pending_change()
            )

            if pending_change is None:

                print(
                    "There is no pending change."
                )

            elif pending_change.get(
                "boundary_type"
            ) != "SINGLE STATEMENT":

                print(
                    "The pending change is not a "
                    "SINGLE STATEMENT proposal."
                )

            else:

                target_name = (
                    pending_change.get(
                        "target_name"
                    )
                )

                print(
                    format_target_statements(
                        target_name
                    )
                )

            print("=" * 60)

            continue

        if user_request.lower().startswith(
            "select-statement "
        ):

            print()
            print("=" * 60)
            print("STATEMENT SELECTION")
            print("=" * 60)

            selection_text = (
                user_request[
                    len("select-statement "):
                ].strip()
            )

            try:

                selection_number = int(
                    selection_text
                )

            except ValueError:

                print(
                    "Statement selection must be "
                    "a whole number."
                )

                print("=" * 60)

                continue

            selection_passed, selection_message = (
                select_pending_statement(
                    selection_number
                )
            )

            print(
                selection_message
            )

            print(
                f"Statement Selected: "
                f"{selection_passed}"
            )

            print("=" * 60)

            continue

        if user_request.lower().startswith(
            "blocks "
        ):

            print()
            print("=" * 60)
            print("SELECTABLE LOGICAL BLOCKS")
            print("=" * 60)

            target_name = (
                user_request[
                    len("blocks "):
                ].strip()
            )

            if not target_name:

                print(
                    "Usage: blocks <function_or_class>"
                )

            else:

                print(
                    format_target_logical_blocks(
                        target_name
                    )
                )

            print("=" * 60)

            continue

        if user_request.lower().startswith(
            "select-block "
        ):

            print()
            print("=" * 60)
            print("LOGICAL BLOCK SELECTION")
            print("=" * 60)

            selection_request = (
                user_request[
                    len("select-block "):
                ].strip()
            )

            if "|" not in selection_request:

                print(
                    "Usage: select-block "
                    "<function_or_class> | <number>"
                )

                print("=" * 60)

                continue

            target_name, selection_text = (
                selection_request.split(
                    "|",
                    1,
                )
            )

            target_name = (
                target_name.strip()
            )

            selection_text = (
                selection_text.strip()
            )

            try:

                selection_number = int(
                    selection_text
                )

            except ValueError:

                print(
                    "Logical block selection must "
                    "be a whole number."
                )

                print("=" * 60)

                continue

            (
                selection_passed,
                selection_message,
                _selected_block,
            ) = select_target_logical_block(
                target_name,
                selection_number,
            )

            print(
                selection_message
            )

            print(
                f"Logical Block Selected: "
                f"{selection_passed}"
            )

            print("=" * 60)

            continue

        # ----------------------------------------------------
        # STORE PENDING LOGICAL BLOCK
        # ----------------------------------------------------

        if user_request.lower().startswith(
            "store-block "
        ):

            print()
            print("=" * 60)
            print("STORE PENDING LOGICAL BLOCK")
            print("=" * 60)

            selection_text = (
                user_request[
                    len("store-block "):
                ].strip()
            )

            try:

                selection_number = int(
                    selection_text
                )

            except ValueError:

                print(
                    "Usage: store-block <number>"
                )

                print("=" * 60)

                continue

            (
                selection_passed,
                selection_message,
            ) = select_pending_logical_block(
                selection_number
            )

            print(
                selection_message
            )

            print(
                f"Pending Logical Block Stored: "
                f"{selection_passed}"
            )

            print("=" * 60)

            continue


        # ----------------------------------------------------
        # SAFE CHANGE PLAN
        # ----------------------------------------------------

        if user_request.lower().startswith(
            "plan "
        ):

            command_content = (
                user_request[5:].strip()
            )

            if "|" not in command_content:

                print(
                    "Usage: plan "
                    "<function_or_class> | "
                    "<requested change>"
                )

                continue

            target_name, requested_change = (
                command_content.split(
                    "|",
                    maxsplit=1,
                )
            )

            target_name = (
                target_name.strip()
            )

            requested_change = (
                requested_change.strip()
            )

            if not target_name:

                print(
                    "Please provide a target name."
                )

                continue

            if not requested_change:

                print(
                    "Please describe the requested change."
                )

                continue

            print()
            print("Development Bot:")
            print("-" * 60)

            response = analyze_change_plan(
                target_name,
                requested_change,
            )

            print(response)
            print("-" * 60)

            continue
        # ----------------------------------------------------
        # PROPOSE COMMAND ROUTING
        # ----------------------------------------------------

        if user_request.lower().startswith(
            "propose "
        ):

            request_body = (
                user_request[8:].strip()
            )

            if "|" not in request_body:

                print(
                    "Usage: propose "
                    "<function_or_class> | "
                    "<requested change>"
                )

                continue

            target_name, requested_change = (
                request_body.split(
                    "|",
                    1,
                )
            )

            target_name = (
                target_name.strip()
            )

            requested_change = (
                requested_change.strip()
            )

            if (
                not target_name
                or not requested_change
            ):

                print(
                    "Usage: propose "
                    "<function_or_class> | "
                    "<requested change>"
                )

                continue

            print()
            print("=" * 60)
            print(
                f"SAFE CODE PROPOSAL: "
                f"{target_name}"
            )
            print("=" * 60)

            control_flow_request = (
                requested_change
                + "\n\n"
                + "PROPOSAL ACCURACY REQUIREMENTS:\n"
                + "- Analyze the ENTIRE target function or class before "
                + "describing behavior.\n"
                + "- Trace earlier guards, returns, raises, branches, loops, "
                + "and exception paths before claiming which inputs are "
                + "affected.\n"
                + "- Do not claim a later replacement changes an input path "
                + "that exits earlier.\n"
                + "- Distinguish the exact execution paths changed from paths "
                + "that remain unchanged.\n"
                + "- Every statement in CONFIRMED PROBLEM MECHANISM, WHY THIS "
                + "CHANGE SHOULD WORK, WHY THIS IS SAFE, and REQUIRED TESTS "
                + "must be supported by the supplied source.\n"
                + "- If control flow makes the requested behavior broader "
                + "than the selected replacement can achieve, say so and "
                + "return PROPOSAL STATUS: MORE INSPECTION REQUIRED instead "
                + "of inventing coverage.\n"
                + "- Required tests must match the exact paths actually "
                + "affected by the replacement."
            )

            proposal = generate_code_proposal(
                target_name,
                control_flow_request,
            )

            print(proposal)

            if (
                "PROPOSAL STATUS: READY"
                in proposal
            ):

                validation_passed, validation_message = (
                    validate_code_proposal(
                        proposal
                    )
                )

                print()
                print(validation_message)

                if validation_passed:

                    set_pending_change(
                        target_name,
                        requested_change,
                        proposal,
                    )

                    print()
                    print(
                        "Proposal stored as pending "
                        "change."
                    )

                    print(
                        "Use 'pending', 'approve', "
                        "or 'reject'."
                    )

                else:

                    clear_pending_change()

                    print()
                    print(
                        "Proposal was NOT stored "
                        "because validation failed."
                    )

            else:

                clear_pending_change()

                print()
                print(
                    "No pending change was stored "
                    "because the proposal is not "
                    "ready for implementation."
                )

            print("=" * 60)

            continue

        # ----------------------------------------------------
        # CHANGE IMPACT ANALYSIS
        # ----------------------------------------------------

        if user_request.lower().startswith(
            "impact "
        ):

            command_content = (
                user_request[7:].strip()
            )

            if "|" not in command_content:

                print(
                    "Usage: impact "
                    "<function_or_class> | <question>"
                )

                continue

            target_name, question = (
                command_content.split(
                    "|",
                    maxsplit=1,
                )
            )

            target_name = (
                target_name.strip()
            )

            question = (
                question.strip()
            )

            if not target_name:

                print(
                    "Please provide a target name."
                )

                continue

            if not question:

                print(
                    "Please provide a question."
                )

                continue

            print()
            print("Development Bot:")
            print("-" * 60)

            response = (
                analyze_reverse_dependencies(
                    target_name,
                    question,
                )
            )

            print(response)
            print("-" * 60)

            continue
        # ----------------------------------------------------
        # FORWARD DEPENDENCY TRACE
        # ----------------------------------------------------

        if user_request.lower().startswith(
            "trace "
        ):

            command_content = (
                user_request[6:].strip()
            )

            if "|" not in command_content:

                print(
                    "Usage: trace "
                    "<function_or_class> | <question>"
                )

                continue

            target_name, question = (
                command_content.split(
                    "|",
                    maxsplit=1,
                )
            )

            target_name = (
                target_name.strip()
            )

            question = (
                question.strip()
            )

            if not target_name:

                print(
                    "Please provide a target name."
                )

                continue

            if not question:

                print(
                    "Please provide a question."
                )

                continue

            print()
            print("Development Bot:")
            print("-" * 60)

            response = (
                analyze_target_with_dependencies(
                    target_name,
                    question,
                )
            )

            print(response)
            print("-" * 60)

            continue

        # ----------------------------------------------------
        # TARGET-ONLY ANALYSIS
        # ----------------------------------------------------

        if user_request.lower().startswith(
            "target "
        ):

            command_content = (
                user_request[7:].strip()
            )

            if "|" not in command_content:

                print(
                    "Usage: target "
                    "<function_or_class> | <question>"
                )

                continue

            target_name, question = (
                command_content.split(
                    "|",
                    maxsplit=1,
                )
            )

            target_name = (
                target_name.strip()
            )

            question = (
                question.strip()
            )

            if not target_name:

                print(
                    "Please provide a target name."
                )

                continue

            if not question:

                print(
                    "Please provide a question."
                )

                continue

            print()
            print("Development Bot:")
            print("-" * 60)

            response = analyze_code_target(
                target_name,
                question,
            )

            print(response)
            print("-" * 60)

            continue

        # ----------------------------------------------------
        # READ FILE
        # ----------------------------------------------------

        if user_request.lower().startswith(
            "read "
        ):

            filename = (
                user_request[5:].strip()
            )

            display_file(
                filename
            )

            continue

        # ----------------------------------------------------
        # ANALYZE FILE
        # ----------------------------------------------------

        if user_request.lower().startswith(
            "analyze "
        ):

            command_content = (
                user_request[8:].strip()
            )

            parts = command_content.split(
                maxsplit=1
            )

            if len(parts) < 2:

                print(
                    "Usage: analyze "
                    "<filename.py> <question>"
                )

                continue

            filename = parts[0]
            question = parts[1]

            print()
            print("Development Bot:")
            print("-" * 60)

            response = analyze_project_file(
                filename,
                question,
            )

            print(response)
            print("-" * 60)

            continue

        # ----------------------------------------------------
        # PROJECT-WIDE ANALYSIS
        # ----------------------------------------------------

        if user_request.lower().startswith(
            "project"
        ):

            command_content = (
                user_request[7:].strip()
            )

            if command_content.startswith("|"):

                command_content = (
                    command_content[1:].strip()
                )

            if not command_content:

                print(
                    "Usage: project | <question>"
                )

                continue

            print()
            print("Development Bot:")
            print("-" * 60)

            response = analyze_entire_project(
                command_content
            )

            print(response)
            print("-" * 60)

            continue

        # ----------------------------------------------------
        # EMPTY INPUT
        # ----------------------------------------------------

        if not user_request:

            continue

        # ----------------------------------------------------
        # GENERAL DEVELOPMENT QUESTION
        # ----------------------------------------------------

        print()
        print("Development Bot:")
        print("-" * 60)

        response = ask_development_bot(
            user_request
        )

        print(response)
        print("-" * 60)

# ============================================================
# START BOT
# ============================================================

if __name__ == "__main__":
    run_development_bot()