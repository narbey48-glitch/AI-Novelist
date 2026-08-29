import difflib
import html
import importlib.util
import inspect
import json
import re
import sys
from datetime import datetime
from pathlib import Path

import streamlit as st

from database import (
    initialise_database,
    initialise_chapter_database,
    initialise_character_rename_database,
    create_project,
    update_project,
    get_all_projects,
    load_project,
    delete_project,
    save_chapter,
    load_chapter,
    get_project_chapters,
    delete_chapter,
    get_previous_chapter_summaries,
    get_latest_chapter_number,
    count_character_name_occurrences,
    rename_character_across_project,
    get_character_rename_history,
    preview_character_rename,
)

# =========================================================
# LOCAL AI ENGINE LOADER
# =========================================================
# Always load ai_engine.py from the same folder as this app.py.
# This prevents Streamlit/Python from accidentally importing an older
# copy of ai_engine.py from another folder or cached environment.

APP_DIR = Path(__file__).resolve().parent
AI_ENGINE_PATH = APP_DIR / "ai_engine.py"

if not AI_ENGINE_PATH.exists():
    raise FileNotFoundError(
        f"Required AI engine not found: {AI_ENGINE_PATH}"
    )

if str(APP_DIR) not in sys.path:
    sys.path.insert(0, str(APP_DIR))

_ai_engine_spec = importlib.util.spec_from_file_location(
    "ai_novelist_local_ai_engine",
    AI_ENGINE_PATH,
)

if _ai_engine_spec is None or _ai_engine_spec.loader is None:
    raise ImportError(
        f"Could not load AI engine from: {AI_ENGINE_PATH}"
    )

_ai_engine = importlib.util.module_from_spec(_ai_engine_spec)
_ai_engine_spec.loader.exec_module(_ai_engine)

generate_story_architecture = _ai_engine.generate_story_architecture
generate_character_bible = _ai_engine.generate_character_bible
generate_world_bible = _ai_engine.generate_world_bible
generate_timeline = _ai_engine.generate_timeline
generate_chapter_plan = _ai_engine.generate_chapter_plan
generate_chapter_draft = _ai_engine.generate_chapter_draft
generate_character_name = _ai_engine.generate_character_name
analyze_chapter = _ai_engine.analyze_chapter
rewrite_chapter = _ai_engine.rewrite_chapter
from plot_library import (
    PLOT_ENGINE_NAMES,
    CHARACTER_ARC_NAMES,
    RELATIONSHIP_ARC_NAMES,
    MYSTERY_ENGINE_NAMES,
    STRUCTURE_COMPLEXITY_NAMES,
)

from character_renamer import (
    extract_character_names,
)


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="AI Novelist",
    page_icon="📖",
    layout="wide",
)

st.title("📖 AI Novelist")
st.caption("BUILD: EDITOR FIX 2026-08-28")
st.caption(
    "AI-powered story architecture, character development, "
    "world building, chapter planning, and novel writing."
)


# =========================================================
# DATABASE INITIALISATION
# =========================================================

initialise_database()
initialise_chapter_database()
initialise_character_rename_database()


# =========================================================
# SESSION STATE
# =========================================================

defaults = {
    "current_project_id": None,
    "reload_project_after_rename": False,
    "rename_success_message": "",

    "title": "Untitled Novel",
    "plot": "",

    "primary_plot": "Overcoming the Monster",
    "secondary_plot": "None",

    "character_arc": "Redemption",
    "relationship_arc": "None",
    "mystery_engine": "None",

    "structure_complexity": "Standard",

    "genre": "Crime Thriller",
    "region": "",
    "period": "Present Day",

    "characters_input": "",

    "word_count": 80000,

    "story_architecture": "",
    "character_bible": "",
    "world_bible": "",
    "timeline": "",

    "generated_character_name": "",
}

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value


# =========================================================
# HELPER FUNCTIONS
# =========================================================

def current_book():
    return {
        "title": st.session_state.title,
        "plot": st.session_state.plot,

        # Backwards compatibility for older functions.
        "plot_type": st.session_state.primary_plot,

        "primary_plot": st.session_state.primary_plot,
        "secondary_plot": st.session_state.secondary_plot,

        "character_arc": st.session_state.character_arc,
        "relationship_arc": st.session_state.relationship_arc,
        "mystery_engine": st.session_state.mystery_engine,

        "structure_complexity": (
            st.session_state.structure_complexity
        ),

        "writing_style_profile": (
            st.session_state.writing_style_profile
        ),

        "style_dialogue": (
            st.session_state.style_dialogue
        ),

        "style_technical_detail": (
            st.session_state.style_technical_detail
        ),

        "style_pacing": (
            st.session_state.style_pacing
        ),

        "style_moral_complexity": (
            st.session_state.style_moral_complexity
        ),

        "style_description": (
            st.session_state.style_description
        ),

        "style_violence": (
            st.session_state.style_violence
        ),

        "style_institutional_detail": (
            st.session_state.style_institutional_detail
        ),

        "style_subtext": (
            st.session_state.style_subtext
        ),

        "genre": st.session_state.genre,
        "region": st.session_state.region,
        "period": st.session_state.period,

        "characters": st.session_state.characters_input,

        "word_count": st.session_state.word_count,
    }
def current_memory():
    return {
        "story_architecture": (
            st.session_state.story_architecture
        ),
        "character_bible": (
            st.session_state.character_bible
        ),
        "world_bible": (
            st.session_state.world_bible
        ),
        "timeline": (
            st.session_state.timeline
        ),
    }


def reset_project():
    st.session_state.current_project_id = None

    st.session_state.title = "Untitled Novel"
    st.session_state.plot = ""

    st.session_state.primary_plot = (
        "Overcoming the Monster"
    )
    st.session_state.secondary_plot = "None"

    st.session_state.character_arc = "Redemption"
    st.session_state.relationship_arc = "None"
    st.session_state.mystery_engine = "None"

    st.session_state.structure_complexity = "Standard"

    st.session_state.genre = "Crime Thriller"
    st.session_state.region = ""
    st.session_state.period = "Present Day"

    st.session_state.characters_input = ""
    st.session_state.word_count = 80000

    st.session_state.story_architecture = ""
    st.session_state.character_bible = ""
    st.session_state.world_bible = ""
    st.session_state.timeline = ""

    st.session_state.generated_character_name = ""


def save_current_project():
    book = current_book()
    memory = current_memory()

    if not book["title"].strip():
        st.error(
            "Give the project a title before saving."
        )
        return

    if st.session_state.current_project_id is None:
        project_id = create_project(
            book,
            memory,
        )

        st.session_state.current_project_id = (
            project_id
        )

        st.success(
            f"Project saved. Project ID: {project_id}"
        )

    else:
        update_project(
            st.session_state.current_project_id,
            book,
            memory,
        )

        st.success("Project updated.")


def autosave_if_possible():
    if st.session_state.current_project_id is not None:
        update_project(
            st.session_state.current_project_id,
            current_book(),
            current_memory(),
        )


def load_project_into_session(project):
    if not project:
        return

    st.session_state.current_project_id = (
        project["id"]
    )

    st.session_state.title = (
        project["title"]
    )

    st.session_state.plot = (
        project["plot"] or ""
    )

    st.session_state.primary_plot = (
        project["primary_plot"]
        or "Overcoming the Monster"
    )

    st.session_state.secondary_plot = (
        project["secondary_plot"]
        or "None"
    )

    st.session_state.character_arc = (
        project["character_arc"]
        or "Redemption"
    )

    st.session_state.relationship_arc = (
        project["relationship_arc"]
        or "None"
    )

    st.session_state.mystery_engine = (
        project["mystery_engine"]
        or "None"
    )

    st.session_state.structure_complexity = (
        project["structure_complexity"]
        or "Standard"
    )

    st.session_state.genre = (
        project["genre"] or ""
    )

    st.session_state.region = (
        project["region"] or ""
    )

    st.session_state.period = (
        project["period"] or ""
    )

    st.session_state.characters_input = (
        project["characters"] or ""
    )

    st.session_state.word_count = (
        project["word_count"] or 80000
    )

    st.session_state.story_architecture = (
        project["story_architecture"] or ""
    )

    st.session_state.character_bible = (
        project["character_bible"] or ""
    )

    st.session_state.world_bible = (
        project["world_bible"] or ""
    )

    st.session_state.timeline = (
        project["timeline"] or ""
    )


def reload_current_project_into_session():
    project_id = (
        st.session_state.current_project_id
    )

    if project_id is None:
        return

    project = load_project(
        project_id
    )

    load_project_into_session(
        project
    )


# =========================================================
# EDITOR WORKFLOW HELPERS
# =========================================================

EDITOR_STATE_FILE = Path(__file__).with_name(
    "editor_state.json"
)


def load_editor_state():
    if not EDITOR_STATE_FILE.exists():
        return {
            "versions": {},
            "protected_passages": {},
        }

    try:
        data = json.loads(
            EDITOR_STATE_FILE.read_text(
                encoding="utf-8"
            )
        )

        if not isinstance(data, dict):
            raise ValueError(
                "Editor state must be a JSON object."
            )

        data.setdefault("versions", {})
        data.setdefault("protected_passages", {})

        return data

    except Exception:
        return {
            "versions": {},
            "protected_passages": {},
        }


def save_editor_state(state):
    temp_path = EDITOR_STATE_FILE.with_suffix(
        ".json.tmp"
    )

    temp_path.write_text(
        json.dumps(
            state,
            indent=2,
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )

    temp_path.replace(
        EDITOR_STATE_FILE
    )


def editor_chapter_key(
    project_id,
    chapter_number,
):
    return (
        f"{project_id}:"
        f"{chapter_number}"
    )


def add_editor_version(
    project_id,
    chapter_number,
    content,
    label,
):
    content = (content or "").strip()

    if not content:
        return

    state = load_editor_state()
    key = editor_chapter_key(
        project_id,
        chapter_number,
    )

    versions = state[
        "versions"
    ].setdefault(
        key,
        [],
    )

    if versions:
        latest = versions[-1]

        if (
            latest.get("content", "")
            == content
            and latest.get("label", "")
            == label
        ):
            return

    versions.append(
        {
            "timestamp": datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            ),
            "label": label,
            "word_count": len(
                content.split()
            ),
            "content": content,
        }
    )

    # Keep a useful history without allowing the local
    # editor-state file to grow forever.
    state["versions"][key] = (
        versions[-30:]
    )

    save_editor_state(
        state
    )


def get_editor_versions(
    project_id,
    chapter_number,
):
    state = load_editor_state()
    key = editor_chapter_key(
        project_id,
        chapter_number,
    )

    return list(
        state[
            "versions"
        ].get(
            key,
            [],
        )
    )


def get_protected_passages_text(
    project_id,
    chapter_number,
):
    state = load_editor_state()
    key = editor_chapter_key(
        project_id,
        chapter_number,
    )

    return state[
        "protected_passages"
    ].get(
        key,
        "",
    )


def save_protected_passages_text(
    project_id,
    chapter_number,
    text,
):
    state = load_editor_state()
    key = editor_chapter_key(
        project_id,
        chapter_number,
    )

    state[
        "protected_passages"
    ][key] = text or ""

    save_editor_state(
        state
    )


def parse_protected_passages(text):
    if not (text or "").strip():
        return []

    passages = re.split(
        r"\n\s*---{3,}\s*\n",
        text.strip(),
    )

    return [
        passage.strip()
        for passage in passages
        if passage.strip()
    ]


def build_inline_diff_html(
    original_text,
    edited_text,
):
    token_pattern = r"\s+|[^\s]+"

    original_tokens = re.findall(
        token_pattern,
        original_text or "",
    )

    edited_tokens = re.findall(
        token_pattern,
        edited_text or "",
    )

    matcher = difflib.SequenceMatcher(
        None,
        original_tokens,
        edited_tokens,
    )

    output = []

    for tag, i1, i2, j1, j2 in matcher.get_opcodes():
        original_chunk = html.escape(
            "".join(
                original_tokens[i1:i2]
            )
        )

        edited_chunk = html.escape(
            "".join(
                edited_tokens[j1:j2]
            )
        )

        if tag == "equal":
            output.append(
                original_chunk
            )

        elif tag == "delete":
            output.append(
                "<span style='background:#ffd7d7;"
                "text-decoration:line-through;'>"
                f"{original_chunk}</span>"
            )

        elif tag == "insert":
            output.append(
                "<span style='background:#d9f7d9;'>"
                f"{edited_chunk}</span>"
            )

        else:
            output.append(
                "<span style='background:#ffd7d7;"
                "text-decoration:line-through;'>"
                f"{original_chunk}</span>"
            )

            output.append(
                "<span style='background:#d9f7d9;'>"
                f"{edited_chunk}</span>"
            )

    diff_body = "".join(
        output
    ).replace(
        "\n",
        "<br>",
    )

    return (
        "<div style='white-space:pre-wrap;"
        "line-height:1.55;font-family:serif;'>"
        f"{diff_body}"
        "</div>"
    )


# =========================================================
# PENDING RENAME RELOAD
# =========================================================

if st.session_state.reload_project_after_rename:

    st.session_state.reload_project_after_rename = (
        False
    )

    reload_current_project_into_session()


if st.session_state.rename_success_message:

    st.success(
        st.session_state.rename_success_message
    )

    st.session_state.rename_success_message = ""


# =========================================================
# SIDEBAR - PROJECT MANAGEMENT
# =========================================================

with st.sidebar:

    st.header("Project Management")

    with st.expander("Runtime Diagnostics", expanded=False):
        st.code(
            f"App: {Path(__file__).resolve()}\n"
            f"AI engine: {AI_ENGINE_PATH.resolve()}\n"
            f"rewrite_chapter: {inspect.signature(rewrite_chapter)}",
            language="text",
        )

    projects = get_all_projects()

    project_options = {
        f"{title} | ID {project_id}": project_id
        for project_id, title, updated_at in projects
    }

    selected_project_label = st.selectbox(
        "Saved Projects",
        ["-- Select Project --"]
        + list(project_options.keys()),
    )

    load_col, new_col = st.columns(2)

    with load_col:

        if st.button("Load"):

            if (
                selected_project_label
                == "-- Select Project --"
            ):
                st.warning(
                    "Choose a saved project first."
                )

            else:
                project_id = project_options[
                    selected_project_label
                ]

                project = load_project(
                    project_id
                )

                if project:
                    load_project_into_session(
                        project
                    )
                    st.rerun()

    with new_col:

        if st.button("New"):
            reset_project()
            st.rerun()

    st.divider()

    # -----------------------------------------------------
    # BOOK SETUP
    # -----------------------------------------------------

    st.header("Book Setup")

    st.text_input(
        "Book Title",
        key="title",
    )

    st.text_area(
        "Plot",
        height=190,
        key="plot",
        placeholder=(
            "Describe the story you want to tell..."
        ),
    )

    st.text_input(
        "Genre",
        key="genre",
    )

    st.text_input(
        "Region of the World",
        key="region",
        placeholder=(
            "e.g. British Columbia, Canada"
        ),
    )

    st.text_input(
        "Time Period",
        key="period",
    )

    st.text_area(
        "Characters",
        height=170,
        key="characters_input",
        placeholder=(
            "Enter characters you already have in mind. "
            "Leave blank if you want the AI to create them."
        ),
    )

    st.number_input(
        "Target Word Count",
        min_value=10000,
        max_value=250000,
        step=5000,
        key="word_count",
    )

       # -----------------------------------------------------
    # STORY STRUCTURE
    # -----------------------------------------------------

    st.divider()

    st.header("Story Structure")

    st.selectbox(
        "Structure Complexity",
        STRUCTURE_COMPLEXITY_NAMES,
        key="structure_complexity",
    )

    st.selectbox(
        "Primary Plot",
        PLOT_ENGINE_NAMES,
        key="primary_plot",
    )

    secondary_choices = (
        ["None"]
        + PLOT_ENGINE_NAMES
    )

    st.selectbox(
        "Secondary Plot",
        secondary_choices,
        key="secondary_plot",
    )

    st.selectbox(
        "Character Arc",
        CHARACTER_ARC_NAMES,
        key="character_arc",
    )

    st.selectbox(
        "Relationship Arc",
        RELATIONSHIP_ARC_NAMES,
        key="relationship_arc",
    )

    st.selectbox(
        "Mystery Engine",
        MYSTERY_ENGINE_NAMES,
        key="mystery_engine",
    )


     # -----------------------------------------------------
    # WRITING STYLE
    # -----------------------------------------------------

    st.divider()

    st.header("Writing Style")

    st.caption(
        "Choose the overall storytelling profile, then fine-tune "
        "how the novel should feel on the page."
    )

    writing_style_profiles = [
        "Cinematic Technical Thriller",
        "Grounded Cinematic Drama",
        "Technical / Geopolitical Thriller",
        "Literary Crime",
        "Psychological Suspense",
        "Custom",
    ]

    st.selectbox(
        "Storytelling Profile",
        writing_style_profiles,
        key="writing_style_profile",
    )

    st.subheader(
        "Detailed Style Controls"
    )

    st.caption(
        "These controls will later be passed into the Story Architect, "
        "Chapter Planner, Chapter Writer, and Editor."
    )

    st.slider(
        "Dialogue Style",
        min_value=0,
        max_value=100,
        value=35,
        step=5,
        key="style_dialogue",
        help=(
            "0 = highly restrained and minimal dialogue. "
            "100 = highly expressive and conversational."
        ),
    )

    st.slider(
        "Technical Detail",
        min_value=0,
        max_value=100,
        value=75,
        step=5,
        key="style_technical_detail",
        help=(
            "0 = very light technical detail. "
            "100 = extensive technical, procedural, "
            "and operational detail."
        ),
    )

    st.slider(
        "Pacing",
        min_value=0,
        max_value=100,
        value=65,
        step=5,
        key="style_pacing",
        help=(
            "0 = slow-burn pacing. "
            "100 = very fast-moving pacing."
        ),
    )

    st.slider(
        "Moral Complexity",
        min_value=0,
        max_value=100,
        value=85,
        step=5,
        key="style_moral_complexity",
        help=(
            "0 = clearer heroes and villains. "
            "100 = highly conflicted motives and moral ambiguity."
        ),
    )

    st.slider(
        "Description Density",
        min_value=0,
        max_value=100,
        value=45,
        step=5,
        key="style_description",
        help=(
            "0 = sparse description. "
            "100 = highly detailed descriptive prose."
        ),
    )

    st.slider(
        "Violence Treatment",
        min_value=0,
        max_value=100,
        value=60,
        step=5,
        key="style_violence",
        help=(
            "0 = violence mostly implied or briefly described. "
            "100 = explicit physical detail and aftermath."
        ),
    )

    st.slider(
        "Institutional / Political Detail",
        min_value=0,
        max_value=100,
        value=75,
        step=5,
        key="style_institutional_detail",
        help=(
            "0 = little institutional detail. "
            "100 = detailed government, corporate, military, "
            "intelligence, legal, or organizational systems."
        ),
    )

    st.slider(
        "Subtext",
        min_value=0,
        max_value=100,
        value=80,
        step=5,
        key="style_subtext",
        help=(
            "0 = characters usually say what they mean. "
            "100 = heavy use of implication, silence, "
            "avoidance, and hidden intention."
        ),
    )



# =========================================================
# SAVE AREA
# =========================================================
save_col, status_col = st.columns(
    [1, 3]
)

with save_col:

    if st.button(
        "💾 Save Project",
        type="primary",
    ):
        save_current_project()


with status_col:

    if st.session_state.current_project_id:
        st.info(
            f"Current Project ID: "
            f"{st.session_state.current_project_id}"
        )

    else:
        st.info(
            "Current project has not been saved yet."
        )


# =========================================================
# MAIN TABS
# =========================================================

(
    story_tab,
    character_tab,
    character_names_tab,
    world_tab,
    timeline_tab,
    chapter_tab,
    chapter_writer_tab,
    editor_tab,
    project_tab,
    database_tab,
) = st.tabs(
    [
        "🏗 Story Architect",
        "👤 Character Engine",
        "👥 Character Names",
        "🌍 World Builder",
        "🕒 Timeline",
        "📋 Chapter Planner",
        "✍️ Chapter Writer",
        "📝 Editor",
        "📚 Project",
        "💾 Saved Data",
    ]
)

# =========================================================
# STORY ARCHITECT
# =========================================================

with story_tab:

    st.header("Story Architect")

    st.write(
        "Develop the structural blueprint for the novel "
        "using the current plot, story engines, and "
        "authoritative Character Bible."
    )

    if st.button(
        "Build Story Architecture",
        type="primary",
        key="build_story_architecture",
    ):

        book = current_book()

        if not book["plot"].strip():

            st.error(
                "Enter your plot in Book Setup first."
            )

        else:

            with st.spinner(
                "The Story Architect is developing "
                "the novel..."
            ):

                try:

                    result = (
                        generate_story_architecture(
                            book,
                            st.session_state.character_bible,
                        )
                    )

                    st.session_state.story_architecture = (
                        result
                    )

                    autosave_if_possible()

                except Exception as error:

                    st.error(
                        f"Generation failed: {error}"
                    )

    if st.session_state.character_bible:

        st.info(
            "The Story Architect will use the current "
            "Character Bible as the authoritative source "
            "for character names and identities."
        )

    else:

        st.warning(
            "No Character Bible currently exists. "
            "The Story Architect may create or use "
            "temporary character identities."
        )

    if st.session_state.story_architecture:

        st.divider()

        st.markdown(
            st.session_state.story_architecture
        )

        st.download_button(
            "Download Story Bible",
            st.session_state.story_architecture,
            file_name="story_bible.md",
            mime="text/markdown",
        )



# =========================================================
# CHARACTER ENGINE
# =========================================================

with character_tab:

    st.header("Character Engine")

    st.write(
        "Build the complete cast and detailed "
        "character profiles."
    )

    if st.button(
        "Build Character Bible",
        key="build_character_bible",
    ):

        book = current_book()

        if not book["plot"].strip():

            st.error(
                "Enter your plot in Book Setup first."
            )

        else:

            with st.spinner(
                "The Character Architect is developing "
                "the complete cast..."
            ):

                try:

                    result = generate_character_bible(
                        book,
                        st.session_state.story_architecture,
                    )

                    st.session_state.character_bible = (
                        result
                    )

                    autosave_if_possible()

                except Exception as error:

                    st.error(
                        f"Generation failed: {error}"
                    )

    if st.session_state.character_bible:

        st.divider()

        st.markdown(
            st.session_state.character_bible
        )

        st.download_button(
            "Download Character Bible",
            st.session_state.character_bible,
            file_name="character_bible.md",
            mime="text/markdown",
        )


# =========================================================
# CHARACTER NAME MANAGER
# =========================================================

with character_names_tab:

    st.header("Character Names")

    st.write(
        "Change a character's name without changing "
        "their background, personality, relationships, "
        "story role, or existing chapters."
    )

    if st.session_state.current_project_id is None:

        st.warning(
            "Save or load a project before "
            "renaming characters."
        )

    else:

        project_id = (
            st.session_state.current_project_id
        )

        detected_names = extract_character_names(
            character_bible=(
                st.session_state.character_bible
            ),
            user_characters=(
                st.session_state.characters_input
            ),
        )

        st.subheader(
            "Select Character"
        )

        if detected_names:

            old_name = st.selectbox(
                "Character to Rename",
                detected_names,
                key="detected_character_name",
            )

            st.caption(
                f"Detected characters: "
                f"{len(detected_names)}"
            )

        else:

            st.warning(
                "No character names were detected "
                "automatically."
            )

            old_name = st.text_input(
                "Current Character Name",
                key="manual_old_character_name",
                placeholder="e.g. Daniel Mercer",
            )

        st.divider()

        rename_method = st.radio(
            "New Name Method",
            [
                "Manual",
                "Auto-generate",
            ],
            horizontal=True,
            key="rename_method",
        )

        # -------------------------------------------------
        # AUTO GENERATED NAME
        # -------------------------------------------------

        if rename_method == "Auto-generate":

            if st.button(
                "🎲 Generate New Name",
                key="generate_character_name_button",
            ):

                if not old_name.strip():

                    st.error(
                        "Select a character first."
                    )

                else:

                    with st.spinner(
                        "Generating a replacement name..."
                    ):

                        try:

                            generated_name = (
                                generate_character_name(
                                    current_book(),
                                    old_name,
                                    st.session_state.character_bible,
                                )
                            )

                            st.session_state[
                                "generated_character_name"
                            ] = generated_name

                            st.rerun()

                        except Exception as error:

                            st.error(
                                f"Name generation failed: "
                                f"{error}"
                            )

            new_name = st.text_input(
                "New Character Name",
                value=st.session_state.get(
                    "generated_character_name",
                    "",
                ),
                key="auto_new_character_name",
            )

        # -------------------------------------------------
        # MANUAL NAME
        # -------------------------------------------------

        else:

            new_name = st.text_input(
                "New Character Name",
                key="manual_new_character_name",
                placeholder="e.g. Jack Callahan",
            )

        st.divider()

        st.subheader(
            "Replacement Options"
        )

        replace_first_name = st.checkbox(
            "Replace first-name-only references",
            value=True,
            help=(
                "Daniel Mercer → Jack Callahan "
                "also changes Daniel → Jack."
            ),
            key="replace_first_name_checkbox",
        )

        replace_surname = st.checkbox(
            "Replace surname-only references",
            value=False,
            help=(
                "Use carefully if several characters "
                "share the same surname."
            ),
            key="replace_surname_checkbox",
        )

        # -------------------------------------------------
        # RENAME PREVIEW
        # -------------------------------------------------

        st.divider()

        st.subheader(
            "Rename Preview"
        )

        if (
            old_name.strip()
            and new_name.strip()
        ):

            preview = preview_character_rename(
                project_id=project_id,
                old_name=old_name,
                new_name=new_name,
                replace_first_name=(
                    replace_first_name
                ),
                replace_surname=(
                    replace_surname
                ),
            )

            full_col, first_col, surname_col = (
                st.columns(3)
            )

            with full_col:

                st.metric(
                    "Full Name",
                    preview["full_name"],
                )

            with first_col:

                st.metric(
                    "First Name",
                    (
                        preview["first_name"]
                        if replace_first_name
                        else 0
                    ),
                )

            with surname_col:

                st.metric(
                    "Surname",
                    (
                        preview["surname"]
                        if replace_surname
                        else 0
                    ),
                )

            st.info(
                f"Potential replacements across the "
                f"saved project: {preview['total']}"
            )

            st.write(
                f"**Full name:** "
                f"{old_name} → {new_name}"
            )

            old_parts = old_name.split()
            new_parts = new_name.split()

            if (
                replace_first_name
                and old_parts
                and new_parts
            ):

                st.write(
                    f"**First name:** "
                    f"{old_parts[0]} → "
                    f"{new_parts[0]}"
                )

            if (
                replace_surname
                and len(old_parts) >= 2
                and len(new_parts) >= 2
            ):

                st.write(
                    f"**Surname:** "
                    f"{old_parts[-1]} → "
                    f"{new_parts[-1]}"
                )

                if preview["surname"] > 0:

                    st.warning(
                        "Surname replacement can also "
                        "change references to relatives "
                        "with the same surname."
                    )

        else:

            st.caption(
                "Select a character and enter or "
                "generate a new name to preview changes."
            )

        # -------------------------------------------------
        # APPLY RENAME
        # -------------------------------------------------

        st.divider()

        confirm_rename = st.checkbox(
            "I have reviewed the rename preview "
            "and want to apply these changes.",
            key="confirm_character_rename",
        )

        if st.button(
            "Apply Character Rename",
            type="primary",
            key="apply_character_rename",
        ):

            if not old_name.strip():

                st.error(
                    "Select a character."
                )

            elif not new_name.strip():

                st.error(
                    "Enter or generate a new "
                    "character name."
                )

            elif not confirm_rename:

                st.error(
                    "Confirm the rename first."
                )

            else:

                try:

                    rename_character_across_project(
                        project_id=project_id,
                        old_name=old_name,
                        new_name=new_name,
                        replace_first_name=(
                            replace_first_name
                        ),
                        replace_surname=(
                            replace_surname
                        ),
                    )

                    st.session_state[
                        "generated_character_name"
                    ] = ""

                    st.session_state[
                        "reload_project_after_rename"
                    ] = True

                    st.session_state[
                        "rename_success_message"
                    ] = (
                        f"{old_name} has been renamed "
                        f"to {new_name}."
                    )

                    st.rerun()

                except Exception as error:

                    st.error(
                        f"Rename failed: {error}"
                    )

        # -------------------------------------------------
        # RENAME HISTORY
        # -------------------------------------------------

        st.divider()

        st.subheader(
            "Rename History"
        )

        rename_history = (
            get_character_rename_history(
                project_id
            )
        )

        if not rename_history:

            st.caption(
                "No character names have been changed."
            )

        else:

            for (
                previous_name,
                changed_name,
                changed_at,
            ) in rename_history:

                st.write(
                    f"**{previous_name}** → "
                    f"**{changed_name}** "
                    f"— {changed_at}"
                )


# =========================================================
# WORLD BUILDER
# =========================================================

with world_tab:

    st.header("World Builder")

    st.write(
        "Build the physical, cultural, economic, "
        "and social world of the novel."
    )

    if st.button(
        "Build World Bible",
        key="build_world_bible",
    ):

        book = current_book()

        if not book["plot"].strip():

            st.error(
                "Enter your plot in Book Setup first."
            )

        elif not book["region"].strip():

            st.error(
                "Enter a region of the world first."
            )

        else:

            with st.spinner(
                "The World Builder is developing "
                "the story world..."
            ):

                try:

                    result = generate_world_bible(
                        book,
                        st.session_state.story_architecture,
                        st.session_state.character_bible,
                    )

                    st.session_state.world_bible = (
                        result
                    )

                    autosave_if_possible()

                except Exception as error:

                    st.error(
                        f"Generation failed: {error}"
                    )

    if st.session_state.world_bible:

        st.divider()

        st.markdown(
            st.session_state.world_bible
        )

        st.download_button(
            "Download World Bible",
            st.session_state.world_bible,
            file_name="world_bible.md",
            mime="text/markdown",
        )


# =========================================================
# TIMELINE
# =========================================================

with timeline_tab:

    st.header("Timeline Architect")

    st.write(
        "Track chronology, character states, "
        "revelations, and unresolved threads."
    )

    if st.button(
        "Build Timeline",
        key="build_timeline",
    ):

        book = current_book()

        if not book["plot"].strip():

            st.error(
                "Enter your plot in Book Setup first."
            )

        else:

            with st.spinner(
                "The Timeline Architect is building "
                "continuity..."
            ):

                try:

                    result = generate_timeline(
                        book,
                        st.session_state.story_architecture,
                        st.session_state.character_bible,
                        st.session_state.world_bible,
                    )

                    st.session_state.timeline = (
                        result
                    )

                    autosave_if_possible()

                except Exception as error:

                    st.error(
                        f"Generation failed: {error}"
                    )

    if st.session_state.timeline:

        st.divider()

        st.markdown(
            st.session_state.timeline
        )

        st.download_button(
            "Download Timeline",
            st.session_state.timeline,
            file_name="timeline.md",
            mime="text/markdown",
        )


# =========================================================
# CHAPTER PLANNER
# =========================================================

with chapter_tab:

    st.header("Chapter Planner")

    st.write(
        "Plan individual chapters using the Story Bible, "
        "Character Bible, World Bible, Timeline, "
        "and previous chapter summaries."
    )

    if st.session_state.current_project_id is None:

        st.warning(
            "Save the project before creating chapters."
        )

    else:

        project_id = (
            st.session_state.current_project_id
        )

        existing_chapters = (
            get_project_chapters(
                project_id
            )
        )

        latest_chapter = (
            get_latest_chapter_number(
                project_id
            )
        )

        suggested_chapter = (
            1
            if latest_chapter == 0
            else latest_chapter + 1
        )

        # -------------------------------------------------
        # CHAPTER NUMBER
        # -------------------------------------------------

        chapter_number = st.number_input(
            "Chapter Number",
            min_value=1,
            max_value=200,
            value=suggested_chapter,
            step=1,
            key="planner_chapter_number",
        )

        chapter_number = int(
            chapter_number
        )

        existing_chapter = load_chapter(
            project_id,
            chapter_number,
        )

        # -------------------------------------------------
        # CHAPTER TITLE
        # -------------------------------------------------

        if existing_chapter:

            st.info(
                f"Chapter {chapter_number} already exists."
            )

            chapter_title = st.text_input(
                "Chapter Title",
                value=(
                    existing_chapter["title"]
                    or ""
                ),
                key=(
                    f"planner_title_"
                    f"{chapter_number}"
                ),
            )

        else:

            chapter_title = st.text_input(
                "Chapter Title",
                value="",
                key=(
                    f"planner_title_"
                    f"{chapter_number}"
                ),
                placeholder=(
                    "Optional — leave blank to "
                    "generate a title later"
                ),
            )

        # -------------------------------------------------
        # PLANNING MODE
        # -------------------------------------------------

        st.divider()

        st.subheader(
            "Planning Mode"
        )

        planning_mode = st.radio(
            "Choose how you want to plan this chapter",
            [
                "AI Generated",
                "Manual / Guided",
            ],
            horizontal=True,
            key=(
                f"planning_mode_"
                f"{chapter_number}"
            ),
        )

        # =================================================
        # AI GENERATED MODE
        # =================================================

        if planning_mode == "AI Generated":

            st.caption(
                "The AI will create the chapter plan "
                "using your existing story material."
            )

            if st.button(
                "Generate Chapter Plan",
                type="primary",
                key=(
                    f"generate_plan_"
                    f"{chapter_number}"
                ),
            ):

                book = current_book()

                if not (
                    st.session_state
                    .story_architecture
                ):

                    st.error(
                        "Generate the Story Bible first."
                    )

                else:

                    previous_summaries = (
                        get_previous_chapter_summaries(
                            project_id,
                            chapter_number,
                        )
                    )

                    with st.spinner(
                        f"Planning Chapter "
                        f"{chapter_number}..."
                    ):

                        try:

                            chapter_plan = (
                                generate_chapter_plan(
                                    book=book,
                                    chapter_number=(
                                        chapter_number
                                    ),
                                    story_architecture=(
                                        st.session_state
                                        .story_architecture
                                    ),
                                    character_bible=(
                                        st.session_state
                                        .character_bible
                                    ),
                                    world_bible=(
                                        st.session_state
                                        .world_bible
                                    ),
                                    timeline=(
                                        st.session_state
                                        .timeline
                                    ),
                                    previous_chapter_summaries=(
                                        previous_summaries
                                    ),
                                )
                            )

                            previous = load_chapter(
                                project_id,
                                chapter_number,
                            )

                            save_chapter(
                                project_id=(
                                    project_id
                                ),
                                chapter_number=(
                                    chapter_number
                                ),
                                title=(
                                    chapter_title
                                ),
                                chapter_plan=(
                                    chapter_plan
                                ),
                                scene_plan=(
                                    previous[
                                        "scene_plan"
                                    ]
                                    if previous
                                    else ""
                                ),
                                draft=(
                                    previous[
                                        "draft"
                                    ]
                                    if previous
                                    else ""
                                ),
                                edited_draft=(
                                    previous[
                                        "edited_draft"
                                    ]
                                    if previous
                                    else ""
                                ),
                                continuity_report=(
                                    previous[
                                        "continuity_report"
                                    ]
                                    if previous
                                    else ""
                                ),
                                chapter_summary=(
                                    previous[
                                        "chapter_summary"
                                    ]
                                    if previous
                                    else ""
                                ),
                                status="planned",
                            )

                            st.success(
                                f"Chapter "
                                f"{chapter_number} "
                                "plan saved."
                            )

                            st.rerun()

                        except Exception as error:

                            st.error(
                                "Chapter planning failed: "
                                f"{error}"
                            )

        # =================================================
        # MANUAL / GUIDED MODE
        # =================================================

        else:

            st.caption(
                "You control the important events of "
                "the chapter. The Chapter Writer will "
                "use these instructions as locked "
                "story decisions."
            )

            st.divider()

            st.subheader(
                "Manual Chapter Instructions"
            )

            # ---------------------------------------------
            # WORD COUNT
            # ---------------------------------------------

            manual_word_target = (
                st.number_input(
                    "Approximate Chapter Word Count",
                    min_value=500,
                    max_value=10000,
                    value=3500,
                    step=250,
                    key=(
                        f"manual_words_"
                        f"{chapter_number}"
                    ),
                )
            )

            # ---------------------------------------------
            # POV CHARACTER
            # ---------------------------------------------

            manual_pov = st.text_input(
                "Point-of-View Character",
                key=(
                    f"manual_pov_"
                    f"{chapter_number}"
                ),
                placeholder=(
                    "Example: Marcus Reid"
                ),
            )

            # ---------------------------------------------
            # OPENING SCENE
            # ---------------------------------------------

            manual_opening = st.text_area(
                "Opening Scene",
                height=140,
                key=(
                    f"manual_opening_"
                    f"{chapter_number}"
                ),
                placeholder=(
                    "Describe exactly how you want "
                    "the chapter to begin."
                ),
            )

            # ---------------------------------------------
            # CHAPTER OBJECTIVE
            # ---------------------------------------------

            manual_objective = st.text_area(
                "Chapter Objective",
                height=130,
                key=(
                    f"manual_objective_"
                    f"{chapter_number}"
                ),
                placeholder=(
                    "What must this chapter accomplish "
                    "in the overall story?"
                ),
            )

            # ---------------------------------------------
            # MAIN LOCATION
            # ---------------------------------------------

            manual_location = st.text_input(
                "Main Location",
                key=(
                    f"manual_location_"
                    f"{chapter_number}"
                ),
                placeholder=(
                    "Example: Reid family ranch"
                ),
            )

            # ---------------------------------------------
            # CHARACTERS PRESENT
            # ---------------------------------------------

            manual_characters = st.text_area(
                "Characters Present",
                height=110,
                key=(
                    f"manual_characters_"
                    f"{chapter_number}"
                ),
                placeholder=(
                    "List the characters who should "
                    "appear in this chapter."
                ),
            )

            # ---------------------------------------------
            # MAIN CONFLICT
            # ---------------------------------------------

            manual_conflict = st.text_area(
                "Main Conflict",
                height=130,
                key=(
                    f"manual_conflict_"
                    f"{chapter_number}"
                ),
                placeholder=(
                    "What opposition, argument, danger, "
                    "problem, or pressure drives "
                    "the chapter?"
                ),
            )

            # ---------------------------------------------
            # KEY EVENTS
            # ---------------------------------------------

            manual_events = st.text_area(
                "Key Events",
                height=180,
                key=(
                    f"manual_events_"
                    f"{chapter_number}"
                ),
                placeholder=(
                    "List the important events in the "
                    "order you want them to happen."
                ),
            )

            # ---------------------------------------------
            # REVELATION
            # ---------------------------------------------

            manual_revelation = st.text_area(
                "Important Information or Revelation",
                height=120,
                key=(
                    f"manual_revelation_"
                    f"{chapter_number}"
                ),
                placeholder=(
                    "What should the reader or "
                    "characters discover?"
                ),
            )

            # ---------------------------------------------
            # CHARACTER / RELATIONSHIP CHANGE
            # ---------------------------------------------

            manual_emotional_change = (
                st.text_area(
                    "Character or Relationship Change",
                    height=120,
                    key=(
                        f"manual_emotion_"
                        f"{chapter_number}"
                    ),
                    placeholder=(
                        "What should change emotionally "
                        "or between characters?"
                    ),
                )
            )

            # ---------------------------------------------
            # CLOSING SCENE
            # ---------------------------------------------

            manual_closing_scene = (
                st.text_area(
                    "Closing Scene",
                    height=140,
                    key=(
                        f"manual_closing_scene_"
                        f"{chapter_number}"
                    ),
                    placeholder=(
                        "Describe the final scene you "
                        "want in this chapter."
                    ),
                )
            )

            # ---------------------------------------------
            # ENDING / HOOK
            # ---------------------------------------------

            manual_ending = st.text_area(
                "Chapter Ending / Hook",
                height=120,
                key=(
                    f"manual_ending_"
                    f"{chapter_number}"
                ),
                placeholder=(
                    "What final moment, discovery, "
                    "decision, threat, question, or "
                    "emotional beat should end "
                    "the chapter?"
                ),
            )

            # ---------------------------------------------
            # ADDITIONAL INSTRUCTIONS
            # ---------------------------------------------

            manual_notes = st.text_area(
                "Additional Instructions",
                height=130,
                key=(
                    f"manual_notes_"
                    f"{chapter_number}"
                ),
                placeholder=(
                    "Anything else the Chapter Writer "
                    "must follow."
                ),
            )

            # ---------------------------------------------
            # SAVE MANUAL PLAN
            # ---------------------------------------------

            if st.button(
                "Save Manual Chapter Plan",
                type="primary",
                key=(
                    f"save_manual_plan_"
                    f"{chapter_number}"
                ),
            ):

                if not manual_opening.strip():

                    st.error(
                        "Enter an Opening Scene first."
                    )

                elif not manual_objective.strip():

                    st.error(
                        "Enter a Chapter Objective first."
                    )

                else:

                    title_for_plan = (
                        chapter_title.strip()
                        if chapter_title.strip()
                        else "To be generated"
                    )

                    pov_for_plan = (
                        manual_pov.strip()
                        if manual_pov.strip()
                        else "Not specified"
                    )

                    location_for_plan = (
                        manual_location.strip()
                        if manual_location.strip()
                        else (
                            "Use established "
                            "story locations"
                        )
                    )

                    characters_for_plan = (
                        manual_characters.strip()
                        if manual_characters.strip()
                        else (
                            "Use characters required "
                            "by the story"
                        )
                    )

                    conflict_for_plan = (
                        manual_conflict.strip()
                        if manual_conflict.strip()
                        else (
                            "Develop naturally from "
                            "established story pressure"
                        )
                    )

                    events_for_plan = (
                        manual_events.strip()
                        if manual_events.strip()
                        else (
                            "Follow the established "
                            "story architecture"
                        )
                    )

                    revelation_for_plan = (
                        manual_revelation.strip()
                        if manual_revelation.strip()
                        else (
                            "No specific revelation "
                            "required"
                        )
                    )

                    emotion_for_plan = (
                        manual_emotional_change.strip()
                        if (
                            manual_emotional_change
                            .strip()
                        )
                        else (
                            "No specific relationship "
                            "change locked"
                        )
                    )

                    closing_for_plan = (
                        manual_closing_scene.strip()
                        if (
                            manual_closing_scene
                            .strip()
                        )
                        else (
                            "Develop a natural closing "
                            "scene from the plan"
                        )
                    )

                    ending_for_plan = (
                        manual_ending.strip()
                        if manual_ending.strip()
                        else (
                            "End at the natural "
                            "dramatic point"
                        )
                    )

                    notes_for_plan = (
                        manual_notes.strip()
                        if manual_notes.strip()
                        else "None"
                    )

                    manual_plan = f"""
# Chapter Number

{chapter_number}

# Working Title

{title_for_plan}

# Approximate Word Target

{manual_word_target:,} words

# Point of View

{pov_for_plan}

# Opening Situation

{manual_opening.strip()}

# Chapter Purpose

{manual_objective.strip()}

# Main Location

{location_for_plan}

# Characters Present

{characters_for_plan}

# Main Conflict

{conflict_for_plan}

# Key Events

{events_for_plan}

# Important Information or Revelation

{revelation_for_plan}

# Character or Relationship Change

{emotion_for_plan}

# Closing Scene

{closing_for_plan}

# Chapter Ending / Hook

{ending_for_plan}

# Additional Writer Instructions

{notes_for_plan}

# Manual Plan Authority

This chapter contains decisions manually specified
by the writer.

These decisions are authoritative.

The Chapter Writer MUST preserve the writer's:

- opening scene
- chapter objective
- point of view
- required characters
- main location where specified
- main conflict
- key events
- revelations
- character or relationship changes
- closing scene
- chapter ending
- additional instructions

The Chapter Writer may creatively develop dialogue,
description, action, transitions, and scene-level
detail around these decisions.

The Chapter Writer must not replace, reverse, ignore,
or substantially alter the manually specified story
events merely to create a different chapter.
"""

                    previous = load_chapter(
                        project_id,
                        chapter_number,
                    )

                    save_chapter(
                        project_id=(
                            project_id
                        ),
                        chapter_number=(
                            chapter_number
                        ),
                        title=(
                            chapter_title
                        ),
                        chapter_plan=(
                            manual_plan
                        ),
                        scene_plan=(
                            previous[
                                "scene_plan"
                            ]
                            if previous
                            else ""
                        ),
                        draft=(
                            previous[
                                "draft"
                            ]
                            if previous
                            else ""
                        ),
                        edited_draft=(
                            previous[
                                "edited_draft"
                            ]
                            if previous
                            else ""
                        ),
                        continuity_report=(
                            previous[
                                "continuity_report"
                            ]
                            if previous
                            else ""
                        ),
                        chapter_summary=(
                            previous[
                                "chapter_summary"
                            ]
                            if previous
                            else ""
                        ),
                        status="planned",
                    )

                    st.success(
                        f"Manual plan for Chapter "
                        f"{chapter_number} saved."
                    )

                    st.rerun()

        # =================================================
        # SAVED CHAPTER PLAN
        # =================================================

        chapter_data = load_chapter(
            project_id,
            chapter_number,
        )

        if chapter_data:

            st.divider()

            st.subheader(
                f"Chapter {chapter_number} Plan"
            )

            if chapter_data["title"]:

                st.write(
                    f"**Working title:** "
                    f"{chapter_data['title']}"
                )

            st.write(
                f"**Status:** "
                f"{chapter_data['status']}"
            )

            if chapter_data["chapter_plan"]:

                st.markdown(
                    chapter_data[
                        "chapter_plan"
                    ]
                )

                st.download_button(
                    label=(
                        "Download Chapter Plan"
                    ),
                    data=(
                        chapter_data[
                            "chapter_plan"
                        ]
                    ),
                    file_name=(
                        f"chapter_"
                        f"{chapter_number}"
                        f"_plan.md"
                    ),
                    mime="text/markdown",
                    key=(
                        f"planner_download_"
                        f"{chapter_number}"
                    ),
                )

        # =================================================
        # EXISTING CHAPTERS
        # =================================================

        if existing_chapters:

            st.divider()

            st.subheader(
                "Existing Chapters"
            )

            for (
                number,
                title,
                status,
                updated_at,
            ) in existing_chapters:

                title_display = (
                    title
                    if title
                    else "Untitled"
                )

                st.write(
                    f"**Chapter {number}:** "
                    f"{title_display} — "
                    f"{status}"
                )



# =========================================================
# CHAPTER WRITER
# =========================================================

with chapter_writer_tab:

    st.header("Chapter Writer")

    st.write(
        "Turn an approved chapter plan into "
        "finished novel prose."
    )

    if st.session_state.current_project_id is None:

        st.warning(
            "Save or load a project before "
            "writing chapters."
        )

    else:

        project_id = (
            st.session_state.current_project_id
        )

        chapters = get_project_chapters(
            project_id
        )

        if not chapters:

            st.warning(
                "No chapter plans exist yet. "
                "Create one in Chapter Planner first."
            )

        else:

            # -------------------------------------------------
            # CHAPTER SELECTION
            # -------------------------------------------------

            chapter_options = {}

            for (
                number,
                title,
                status,
                updated_at,
            ) in chapters:

                title_display = (
                    title
                    if title
                    else "Untitled"
                )

                label = (
                    f"Chapter {number}: "
                    f"{title_display} [{status}]"
                )

                chapter_options[label] = number

            selected_chapter_label = (
                st.selectbox(
                    "Select Chapter",
                    list(
                        chapter_options.keys()
                    ),
                    key="writer_chapter_select",
                )
            )

            chapter_number = (
                chapter_options[
                    selected_chapter_label
                ]
            )

            chapter_data = load_chapter(
                project_id,
                chapter_number,
            )

            # -------------------------------------------------
            # CHAPTER INFORMATION
            # -------------------------------------------------

            if chapter_data:

                st.subheader(
                    f"Chapter {chapter_number}"
                )

                if chapter_data["title"]:

                    st.write(
                        f"**Working title:** "
                        f"{chapter_data['title']}"
                    )

                st.write(
                    f"**Status:** "
                    f"{chapter_data['status']}"
                )

                # ---------------------------------------------
                # CHAPTER PLAN
                # ---------------------------------------------

                with st.expander(
                    "View Chapter Plan"
                ):

                    if chapter_data[
                        "chapter_plan"
                    ]:

                        st.markdown(
                            chapter_data[
                                "chapter_plan"
                            ]
                        )

                    else:

                        st.warning(
                            "This chapter has no plan."
                        )

                # ---------------------------------------------
                # WRITE / REGENERATE CHAPTER
                # ---------------------------------------------

                if chapter_data[
                    "chapter_plan"
                ]:

                    if chapter_data["draft"]:

                        write_button_label = (
                            "🔄 Regenerate Chapter"
                        )

                    else:

                        write_button_label = (
                            "✍️ Write Chapter"
                        )

                    if st.button(
                        write_button_label,
                        type="primary",
                        key=(
                            f"writer_write_"
                            f"{chapter_number}"
                        ),
                    ):

                        previous_summaries = (
                            get_previous_chapter_summaries(
                                project_id,
                                chapter_number,
                            )
                        )

                        with st.spinner(
                            f"Writing Chapter "
                            f"{chapter_number}..."
                        ):

                            try:

                                chapter_draft = (
                                    generate_chapter_draft(
                                        book=(
                                            current_book()
                                        ),
                                        chapter_number=(
                                            chapter_number
                                        ),
                                        chapter_plan=(
                                            chapter_data[
                                                "chapter_plan"
                                            ]
                                        ),
                                        story_architecture=(
                                            st.session_state
                                            .story_architecture
                                        ),
                                        character_bible=(
                                            st.session_state
                                            .character_bible
                                        ),
                                        world_bible=(
                                            st.session_state
                                            .world_bible
                                        ),
                                        timeline=(
                                            st.session_state
                                            .timeline
                                        ),
                                        previous_chapter_summaries=(
                                            previous_summaries
                                        ),
                                    )
                                )

                                save_chapter(
                                    project_id=(
                                        project_id
                                    ),
                                    chapter_number=(
                                        chapter_number
                                    ),
                                    title=(
                                        chapter_data[
                                            "title"
                                        ]
                                    ),
                                    chapter_plan=(
                                        chapter_data[
                                            "chapter_plan"
                                        ]
                                    ),
                                    scene_plan=(
                                        chapter_data[
                                            "scene_plan"
                                        ]
                                    ),
                                    draft=(
                                        chapter_draft
                                    ),
                                    edited_draft=(
                                        chapter_data[
                                            "edited_draft"
                                        ]
                                    ),
                                    continuity_report=(
                                        chapter_data[
                                            "continuity_report"
                                        ]
                                    ),
                                    chapter_summary=(
                                        chapter_data[
                                            "chapter_summary"
                                        ]
                                    ),
                                    status="drafted",
                                )

                                st.success(
                                    f"Chapter "
                                    f"{chapter_number} "
                                    "written and saved."
                                )

                                st.rerun()

                            except Exception as error:

                                st.error(
                                    f"Chapter writing "
                                    f"failed: {error}"
                                )

                # ---------------------------------------------
                # DRAFT DISPLAY
                # ---------------------------------------------

                if chapter_data["draft"]:

                    st.divider()

                    st.subheader(
                        "Chapter Draft"
                    )

                    word_total = len(
                        chapter_data[
                            "draft"
                        ].split()
                    )

                    st.caption(
                        f"Draft word count: "
                        f"{word_total:,}"
                    )

                    st.markdown(
                        chapter_data[
                            "draft"
                        ]
                    )

                    # -----------------------------------------
                    # DOWNLOAD DRAFT
                    # -----------------------------------------

                    st.download_button(
                        label=(
                            "⬇️ Download Chapter Draft"
                        ),
                        data=(
                            chapter_data[
                                "draft"
                            ]
                        ),
                        file_name=(
                            f"chapter_"
                            f"{chapter_number}"
                            f"_draft.md"
                        ),
                        mime="text/markdown",
                        key=(
                            f"writer_download_"
                            f"{chapter_number}"
                        ),
                    )

                    # -----------------------------------------
                    # DELETE DRAFT
                    # -----------------------------------------

                    st.divider()

                    st.subheader(
                        "Draft Management"
                    )

                    st.warning(
                        "Deleting the draft keeps the "
                        "chapter plan intact. You can then "
                        "generate a completely new draft."
                    )

                    confirm_delete_draft = (
                        st.checkbox(
                            "I want to delete this "
                            "chapter draft.",
                            key=(
                                f"confirm_delete_draft_"
                                f"{chapter_number}"
                            ),
                        )
                    )

                    if st.button(
                        "🗑 Delete Chapter Draft",
                        key=(
                            f"delete_draft_"
                            f"{chapter_number}"
                        ),
                    ):

                        if not confirm_delete_draft:

                            st.error(
                                "Confirm that you want "
                                "to delete the draft first."
                            )

                        else:

                            try:

                                save_chapter(
                                    project_id=(
                                        project_id
                                    ),
                                    chapter_number=(
                                        chapter_number
                                    ),
                                    title=(
                                        chapter_data[
                                            "title"
                                        ]
                                    ),
                                    chapter_plan=(
                                        chapter_data[
                                            "chapter_plan"
                                        ]
                                    ),
                                    scene_plan=(
                                        chapter_data[
                                            "scene_plan"
                                        ]
                                    ),

                                    # Delete written versions.
                                    draft="",
                                    edited_draft="",

                                    # Keep continuity information.
                                    continuity_report=(
                                        chapter_data[
                                            "continuity_report"
                                        ]
                                    ),

                                    # Clear the summary because
                                    # it described the old draft.
                                    chapter_summary="",

                                    # Return chapter to planned.
                                    status="planned",
                                )

                                st.success(
                                    f"Chapter "
                                    f"{chapter_number} "
                                    "draft deleted."
                                )

                                st.rerun()

                            except Exception as error:

                                st.error(
                                    f"Draft deletion "
                                    f"failed: {error}"
                                )

# =========================================================
# EDITOR
# =========================================================

with editor_tab:

    st.header("Editor")

    st.write(
        "Analyze, revise, compare, manually refine, protect, "
        "version, and accept completed chapters without "
        "silently overwriting the current master draft."
    )

    if st.session_state.current_project_id is None:

        st.warning(
            "Save or load a project before using the Editor."
        )

    else:

        project_id = (
            st.session_state.current_project_id
        )

        chapters = get_project_chapters(
            project_id
        )

        if not chapters:

            st.warning(
                "No chapters exist yet. Create and write "
                "a chapter before using the Editor."
            )

        else:

            # -------------------------------------------------
            # CHAPTER SELECTION
            # -------------------------------------------------

            editor_chapter_options = {}

            for (
                number,
                title,
                status,
                updated_at,
            ) in chapters:

                title_display = (
                    title
                    if title
                    else "Untitled"
                )

                label = (
                    f"Chapter {number}: "
                    f"{title_display} [{status}]"
                )

                editor_chapter_options[
                    label
                ] = number

            selected_editor_chapter = st.selectbox(
                "Select Chapter",
                list(
                    editor_chapter_options.keys()
                ),
                key="editor_chapter_select",
            )

            editor_chapter_number = (
                editor_chapter_options[
                    selected_editor_chapter
                ]
            )

            editor_chapter_data = load_chapter(
                project_id,
                editor_chapter_number,
            )

            if editor_chapter_data:

                st.subheader(
                    f"Chapter "
                    f"{editor_chapter_number}"
                )

                if editor_chapter_data["title"]:

                    st.write(
                        f"**Title:** "
                        f"{editor_chapter_data['title']}"
                    )

                st.write(
                    f"**Status:** "
                    f"{editor_chapter_data['status']}"
                )

                if not editor_chapter_data["draft"]:

                    st.warning(
                        "This chapter does not have a master draft "
                        "yet. Write the chapter before using "
                        "the Editor."
                    )

                else:

                    master_draft = (
                        editor_chapter_data[
                            "draft"
                        ]
                    )

                    edited_draft = (
                        editor_chapter_data[
                            "edited_draft"
                        ]
                        or ""
                    )

                    original_word_count = len(
                        master_draft.split()
                    )

                    top_col_1, top_col_2, top_col_3 = (
                        st.columns(3)
                    )

                    with top_col_1:
                        st.metric(
                            "Master Draft",
                            f"{original_word_count:,} words",
                        )

                    with top_col_2:
                        st.metric(
                            "Edited Candidate",
                            (
                                f"{len(edited_draft.split()):,} words"
                                if edited_draft
                                else "None"
                            ),
                        )

                    with top_col_3:
                        st.metric(
                            "Saved Versions",
                            len(
                                get_editor_versions(
                                    project_id,
                                    editor_chapter_number,
                                )
                            ),
                        )

                    # =============================================
                    # EDITING MODE
                    # =============================================

                    st.divider()
                    st.subheader("Editing Mode")

                    editing_mode = st.radio(
                        "Choose the level of editing",
                        [
                            "Light Polish",
                            "Standard Edit",
                            "Deep Edit",
                        ],
                        index=1,
                        key=(
                            f"editor_mode_"
                            f"{editor_chapter_number}"
                        ),
                    )

                    if editing_mode == "Light Polish":
                        st.info(
                            "Minimal correction: grammar, readability, "
                            "repetition, sentence flow, and minor "
                            "dialogue cleanup."
                        )

                    elif editing_mode == "Standard Edit":
                        st.info(
                            "Moderate revision of prose, dialogue, "
                            "pacing, subtext, character voice, POV, "
                            "and scene flow while preserving the plot."
                        )

                    else:
                        st.info(
                            "Stronger editorial rewrite of scene "
                            "execution, pacing, dialogue, POV, emotional "
                            "credibility, and continuity while keeping "
                            "major story decisions locked."
                        )

                    # =============================================
                    # EDITING CHECKS
                    # =============================================

                    st.divider()
                    st.subheader("Editing Checks")

                    checks_col_1, checks_col_2 = (
                        st.columns(2)
                    )

                    with checks_col_1:
                        check_grammar = st.checkbox(
                            "Grammar & readability",
                            value=True,
                            key=f"edit_grammar_{editor_chapter_number}",
                        )
                        check_dialogue = st.checkbox(
                            "Dialogue & character voice",
                            value=True,
                            key=f"edit_dialogue_{editor_chapter_number}",
                        )
                        check_pacing = st.checkbox(
                            "Pacing",
                            value=True,
                            key=f"edit_pacing_{editor_chapter_number}",
                        )
                        check_characters = st.checkbox(
                            "Character consistency",
                            value=True,
                            key=f"edit_characters_{editor_chapter_number}",
                        )
                        check_continuity = st.checkbox(
                            "Story continuity",
                            value=True,
                            key=f"edit_continuity_{editor_chapter_number}",
                        )

                    with checks_col_2:
                        check_pov = st.checkbox(
                            "POV consistency",
                            value=True,
                            key=f"edit_pov_{editor_chapter_number}",
                        )
                        check_repetition = st.checkbox(
                            "Remove unnecessary repetition",
                            value=True,
                            key=f"edit_repetition_{editor_chapter_number}",
                        )
                        check_names = st.checkbox(
                            "First-name usage after introduction",
                            value=True,
                            key=f"edit_names_{editor_chapter_number}",
                        )
                        check_subtext = st.checkbox(
                            "Strengthen dialogue subtext",
                            value=True,
                            key=f"edit_subtext_{editor_chapter_number}",
                        )
                        check_scenes = st.checkbox(
                            "Scene effectiveness",
                            value=True,
                            key=f"edit_scenes_{editor_chapter_number}",
                        )

                    editing_checks = {
                        "Grammar & readability": check_grammar,
                        "Dialogue & character voice": check_dialogue,
                        "Pacing": check_pacing,
                        "Character consistency": check_characters,
                        "Story continuity": check_continuity,
                        "POV consistency": check_pov,
                        "Remove unnecessary repetition": check_repetition,
                        "First-name usage after introduction": check_names,
                        "Strengthen dialogue subtext": check_subtext,
                        "Scene effectiveness": check_scenes,
                    }

                    # =============================================
                    # PASSAGE PROTECTION
                    # =============================================

                    st.divider()
                    st.subheader("Passage Protection")

                    st.caption(
                        "Paste any wording that the AI must reproduce "
                        "verbatim during the next rewrite. Separate "
                        "multiple protected passages with a line "
                        "containing ---."
                    )

                    protection_key = (
                        f"protected_passages_"
                        f"{project_id}_"
                        f"{editor_chapter_number}"
                    )

                    persisted_protection = (
                        get_protected_passages_text(
                            project_id,
                            editor_chapter_number,
                        )
                    )

                    protection_source_key = (
                        f"{protection_key}_source"
                    )

                    if (
                        st.session_state.get(
                            protection_source_key
                        )
                        != persisted_protection
                    ):
                        st.session_state[
                            protection_key
                        ] = persisted_protection
                        st.session_state[
                            protection_source_key
                        ] = persisted_protection

                    protected_text = st.text_area(
                        "Protected Passages",
                        height=180,
                        key=protection_key,
                        placeholder=(
                            "Paste exact prose here.\n\n---\n\n"
                            "Paste another protected passage here."
                        ),
                    )

                    protection_col_1, protection_col_2 = (
                        st.columns([1, 3])
                    )

                    with protection_col_1:
                        if st.button(
                            "🔒 Save Protection",
                            key=(
                                f"save_protection_"
                                f"{editor_chapter_number}"
                            ),
                        ):
                            save_protected_passages_text(
                                project_id,
                                editor_chapter_number,
                                protected_text,
                            )
                            st.session_state[
                                protection_source_key
                            ] = protected_text
                            st.success(
                                "Protected passages saved."
                            )

                    with protection_col_2:
                        protected_passages = (
                            parse_protected_passages(
                                protected_text
                            )
                        )
                        st.caption(
                            f"{len(protected_passages)} protected "
                            "passage(s) will be locked during AI editing."
                        )

                    # =============================================
                    # MASTER DRAFT
                    # =============================================

                    st.divider()

                    with st.expander(
                        "View Current Master Draft"
                    ):
                        st.markdown(
                            master_draft
                        )

                    # =============================================
                    # STEP 1 — ANALYZE
                    # =============================================

                    st.divider()
                    st.subheader("Step 1 — Analyze")

                    st.write(
                        "Analyze the current master chapter first. "
                        "The Editor Report guides the selected edit."
                    )

                    if st.button(
                        "🔎 Analyze Chapter",
                        type="primary",
                        key=(
                            f"analyze_chapter_"
                            f"{editor_chapter_number}"
                        ),
                    ):

                        previous_summaries = (
                            get_previous_chapter_summaries(
                                project_id,
                                editor_chapter_number,
                            )
                        )

                        with st.spinner(
                            f"Analyzing Chapter "
                            f"{editor_chapter_number}..."
                        ):

                            try:
                                editor_report = analyze_chapter(
                                    book=current_book(),
                                    chapter_number=(
                                        editor_chapter_number
                                    ),
                                    chapter_plan=(
                                        editor_chapter_data[
                                            "chapter_plan"
                                        ]
                                    ),
                                    chapter_draft=master_draft,
                                    story_architecture=(
                                        st.session_state
                                        .story_architecture
                                    ),
                                    character_bible=(
                                        st.session_state
                                        .character_bible
                                    ),
                                    world_bible=(
                                        st.session_state
                                        .world_bible
                                    ),
                                    timeline=(
                                        st.session_state
                                        .timeline
                                    ),
                                    previous_chapter_summaries=(
                                        previous_summaries
                                    ),
                                    editing_mode=editing_mode,
                                    editing_checks=editing_checks,
                                )

                                save_chapter(
                                    project_id=project_id,
                                    chapter_number=(
                                        editor_chapter_number
                                    ),
                                    title=editor_chapter_data["title"],
                                    chapter_plan=(
                                        editor_chapter_data[
                                            "chapter_plan"
                                        ]
                                    ),
                                    scene_plan=(
                                        editor_chapter_data[
                                            "scene_plan"
                                        ]
                                    ),
                                    draft=master_draft,
                                    edited_draft=edited_draft,
                                    continuity_report=editor_report,
                                    chapter_summary=(
                                        editor_chapter_data[
                                            "chapter_summary"
                                        ]
                                    ),
                                    status="analyzed",
                                )

                                st.success(
                                    f"Chapter {editor_chapter_number} "
                                    "analysis completed."
                                )
                                st.rerun()

                            except Exception as error:
                                st.error(
                                    f"Chapter analysis failed: "
                                    f"{error}"
                                )

                    # =============================================
                    # EDITOR REPORT
                    # =============================================

                    editor_report = (
                        editor_chapter_data[
                            "continuity_report"
                        ]
                        or ""
                    )

                    if editor_report:
                        st.divider()
                        st.subheader("Editor Report")

                        with st.expander(
                            "View Editor Report",
                            expanded=False,
                        ):
                            st.markdown(
                                editor_report
                            )

                                        # =============================================
                    # STEP 2 — CREATE EDITED DRAFT
                    # =============================================

                    if editor_report:
                        st.divider()
                        st.subheader(
                            "Step 2 — Create Edited Draft"
                        )

                        st.caption(
                            "Choose exactly what the Editor should fix. "
                            "The master remains untouched until you accept "
                            "the edited candidate."
                        )

                        # -----------------------------------------
                        # EXTRACT PRIORITY REVISIONS
                        # -----------------------------------------

                        priority_match = re.search(
                            r"##\s*Priority Revisions"
                            r"(.*?)"
                            r"(?=##\s*Optional Improvements|"
                            r"##\s*Editor Verdict|\Z)",
                            editor_report,
                            flags=(
                                re.IGNORECASE
                                | re.DOTALL
                            ),
                        )

                        priority_section = (
                            priority_match.group(1)
                            if priority_match
                            else ""
                        )

                        issue_pattern = re.compile(
                            r"(?P<number>\d+)\.\s*"
                            r"\**PROBLEM:\**\s*"
                            r"(?P<problem>.*?)"
                            r"(?=\n\s*-\s*\**WHY IT MATTERS:\**)"
                            r".*?"
                            r"\**SEVERITY:\**\s*"
                            r"(?P<severity>"
                            r"Critical|Major|Moderate|Minor"
                            r")",
                            flags=(
                                re.IGNORECASE
                                | re.DOTALL
                            ),
                        )

                        extracted_issues = []

                        for match in issue_pattern.finditer(
                            priority_section
                        ):
                            problem = (
                                match.group("problem")
                                .strip()
                                .replace("\n", " ")
                            )

                            severity = (
                                match.group("severity")
                                .strip()
                                .title()
                            )

                            full_issue = (
                                match.group(0).strip()
                            )

                            label = (
                                f"{severity} — {problem}"
                            )

                            extracted_issues.append(
                                {
                                    "label": label,
                                    "text": full_issue,
                                    "severity": severity,
                                }
                            )

                        # -----------------------------------------
                        # TARGETED EDITING
                        # -----------------------------------------

                        st.markdown(
                            "### 🎯 Targeted Editing"
                        )

                        targeted_editing = st.checkbox(
                            "Only edit selected Analyzer issues",
                            value=bool(
                                extracted_issues
                            ),
                            key=(
                                f"targeted_editing_"
                                f"{editor_chapter_number}"
                            ),
                            help=(
                                "When enabled, the AI is instructed "
                                "to leave unrelated prose alone."
                            ),
                        )

                        selected_issue_labels = []

                        if targeted_editing:

                            if extracted_issues:
                                default_issue_labels = [
                                    item["label"]
                                    for item in extracted_issues
                                    if item["severity"]
                                    in {
                                        "Critical",
                                        "Major",
                                        "Moderate",
                                    }
                                ]

                                if not default_issue_labels:
                                    default_issue_labels = [
                                        item["label"]
                                        for item in extracted_issues
                                    ]

                                selected_issue_labels = (
                                    st.multiselect(
                                        "Select Analyzer issues to fix",
                                        options=[
                                            item["label"]
                                            for item
                                            in extracted_issues
                                        ],
                                        default=(
                                            default_issue_labels
                                        ),
                                        key=(
                                            f"selected_editor_issues_"
                                            f"{editor_chapter_number}"
                                        ),
                                    )
                                )

                                st.caption(
                                    f"{len(selected_issue_labels)} "
                                    "target issue(s) selected."
                                )

                            else:
                                st.info(
                                    "No structured Priority Revisions "
                                    "were found in this Editor Report. "
                                    "You can use Additional Editing "
                                    "Instructions below."
                                )

                        else:
                            st.caption(
                                "Full-report editing is active. "
                                "The Editor may address all relevant "
                                "issues in the report."
                            )

                        # -----------------------------------------
                        # ADDITIONAL INSTRUCTIONS
                        # -----------------------------------------

                        additional_editing_instructions = (
                            st.text_area(
                                "Additional Editing Instructions",
                                height=130,
                                key=(
                                    f"additional_editing_"
                                    f"{editor_chapter_number}"
                                ),
                                placeholder=(
                                    "Optional: e.g. Tighten only the "
                                    "Sofia/Lucas exchange. Preserve "
                                    "the interrogation scene exactly."
                                ),
                            )
                        )

                        # -----------------------------------------
                        # CREATE EDIT
                        # -----------------------------------------

                        if st.button(
                            f"✍️ Create {editing_mode}",
                            type="primary",
                            key=(
                                f"rewrite_chapter_"
                                f"{editor_chapter_number}"
                            ),
                        ):

                            if (
                                targeted_editing
                                and extracted_issues
                                and not selected_issue_labels
                                and not additional_editing_instructions.strip()
                            ):
                                st.error(
                                    "Select at least one Analyzer issue "
                                    "or enter an Additional Editing "
                                    "Instruction."
                                )

                            else:
                                previous_summaries = (
                                    get_previous_chapter_summaries(
                                        project_id,
                                        editor_chapter_number,
                                    )
                                )

                                current_protection_text = (
                                    st.session_state.get(
                                        protection_key,
                                        "",
                                    )
                                )

                                protected_passages = (
                                    parse_protected_passages(
                                        current_protection_text
                                    )
                                )

                                save_protected_passages_text(
                                    project_id,
                                    editor_chapter_number,
                                    current_protection_text,
                                )

                                selected_issue_texts = []

                                if targeted_editing:
                                    selected_issue_texts = [
                                        item["text"]
                                        for item in extracted_issues
                                        if item["label"]
                                        in selected_issue_labels
                                    ]

                                with st.spinner(
                                    f"Creating {editing_mode} for "
                                    f"Chapter "
                                    f"{editor_chapter_number}..."
                                ):

                                    try:
                                        new_edited_draft = (
                                            rewrite_chapter(
                                                book=current_book(),
                                                chapter_number=(
                                                    editor_chapter_number
                                                ),
                                                chapter_plan=(
                                                    editor_chapter_data[
                                                        "chapter_plan"
                                                    ]
                                                ),
                                                chapter_draft=(
                                                    master_draft
                                                ),
                                                editor_report=(
                                                    editor_report
                                                ),
                                                editing_mode=(
                                                    editing_mode
                                                ),
                                                story_architecture=(
                                                    st.session_state
                                                    .story_architecture
                                                ),
                                                character_bible=(
                                                    st.session_state
                                                    .character_bible
                                                ),
                                                world_bible=(
                                                    st.session_state
                                                    .world_bible
                                                ),
                                                timeline=(
                                                    st.session_state
                                                    .timeline
                                                ),
                                                previous_chapter_summaries=(
                                                    previous_summaries
                                                ),
                                                protected_passages=(
                                                    protected_passages
                                                ),
                                                targeted_issues=(
                                                    selected_issue_texts
                                                ),
                                                additional_editing_instructions=(
                                                    additional_editing_instructions
                                                ),
                                            )
                                        )

                                        missing_locked = [
                                            passage
                                            for passage
                                            in protected_passages
                                            if passage
                                            not in new_edited_draft
                                        ]

                                        if missing_locked:
                                            raise ValueError(
                                                "The AI changed or removed "
                                                "a protected passage. "
                                                "The edited draft was "
                                                "rejected and nothing "
                                                "was saved."
                                            )

                                        if edited_draft:
                                            add_editor_version(
                                                project_id,
                                                editor_chapter_number,
                                                edited_draft,
                                                (
                                                    "Previous edited "
                                                    "candidate"
                                                ),
                                            )

                                        save_chapter(
                                            project_id=project_id,
                                            chapter_number=(
                                                editor_chapter_number
                                            ),
                                            title=(
                                                editor_chapter_data[
                                                    "title"
                                                ]
                                            ),
                                            chapter_plan=(
                                                editor_chapter_data[
                                                    "chapter_plan"
                                                ]
                                            ),
                                            scene_plan=(
                                                editor_chapter_data[
                                                    "scene_plan"
                                                ]
                                            ),
                                            draft=master_draft,
                                            edited_draft=(
                                                new_edited_draft
                                            ),
                                            continuity_report=(
                                                editor_report
                                            ),
                                            chapter_summary=(
                                                editor_chapter_data[
                                                    "chapter_summary"
                                                ]
                                            ),
                                            status="edited",
                                        )

                                        manual_key = (
                                            f"manual_editor_text_"
                                            f"{project_id}_"
                                            f"{editor_chapter_number}"
                                        )

                                        st.session_state.pop(
                                            manual_key,
                                            None,
                                        )

                                        st.session_state.pop(
                                            f"{manual_key}_source",
                                            None,
                                        )

                                        if targeted_editing:
                                            st.success(
                                                "Targeted edit completed. "
                                                "Only the selected issues "
                                                "were supplied as editing "
                                                "targets."
                                            )
                                        else:
                                            st.success(
                                                f"{editing_mode} completed "
                                                f"for Chapter "
                                                f"{editor_chapter_number}."
                                            )

                                        st.rerun()

                                    except Exception as error:
                                        st.error(
                                            f"Chapter edit failed: "
                                            f"{error}"
                                        )

                    # =============================================
                    # EDITED DRAFT WORKSPACE
                    # =============================================

                    if edited_draft:
                        st.divider()
                        st.subheader("Edited Draft Workspace")

                        edited_word_count = len(
                            edited_draft.split()
                        )

                        word_difference = (
                            edited_word_count
                            - original_word_count
                        )

                        metric_col_1, metric_col_2 = (
                            st.columns(2)
                        )

                        with metric_col_1:
                            st.metric(
                                "Edited Draft",
                                f"{edited_word_count:,} words",
                            )

                        with metric_col_2:
                            st.metric(
                                "Difference",
                                f"{word_difference:+,} words",
                            )

                        # -------------------------------------
                        # CHANGE HIGHLIGHTING
                        # -------------------------------------

                        view_mode = st.radio(
                            "Comparison View",
                            [
                                "Highlighted Changes",
                                "Side by Side",
                                "Edited Only",
                            ],
                            horizontal=True,
                            key=(
                                f"editor_compare_view_"
                                f"{editor_chapter_number}"
                            ),
                        )

                        if view_mode == "Highlighted Changes":
                            st.caption(
                                "Red strike-through text was removed. "
                                "Green text was added."
                            )
                            st.markdown(
                                build_inline_diff_html(
                                    master_draft,
                                    edited_draft,
                                ),
                                unsafe_allow_html=True,
                            )

                        elif view_mode == "Side by Side":
                            original_col, edited_col = (
                                st.columns(2)
                            )

                            with original_col:
                                st.markdown("### Master")
                                st.markdown(
                                    master_draft
                                )

                            with edited_col:
                                st.markdown("### Edited")
                                st.markdown(
                                    edited_draft
                                )

                        else:
                            st.markdown(
                                edited_draft
                            )

                        # -------------------------------------
                        # MANUAL EDITING
                        # -------------------------------------

                        st.divider()
                        st.subheader("Manual Editing")

                        st.caption(
                            "Make your own changes to the edited candidate. "
                            "Saving here does not replace the master draft."
                        )

                        manual_key = (
                            f"manual_editor_text_"
                            f"{project_id}_"
                            f"{editor_chapter_number}"
                        )

                        manual_source_key = (
                            f"{manual_key}_source"
                        )

                        if (
                            st.session_state.get(
                                manual_source_key
                            )
                            != edited_draft
                        ):
                            st.session_state[
                                manual_key
                            ] = edited_draft
                            st.session_state[
                                manual_source_key
                            ] = edited_draft

                        manual_edited_text = st.text_area(
                            "Edit Draft",
                            height=650,
                            key=manual_key,
                        )

                        manual_col_1, manual_col_2 = (
                            st.columns([1, 3])
                        )

                        with manual_col_1:
                            if st.button(
                                "💾 Save Manual Changes",
                                key=(
                                    f"save_manual_edit_"
                                    f"{editor_chapter_number}"
                                ),
                            ):

                                if not manual_edited_text.strip():
                                    st.error(
                                        "The edited draft cannot be empty."
                                    )

                                else:
                                    add_editor_version(
                                        project_id,
                                        editor_chapter_number,
                                        edited_draft,
                                        "Before manual edit",
                                    )

                                    save_chapter(
                                        project_id=project_id,
                                        chapter_number=(
                                            editor_chapter_number
                                        ),
                                        title=editor_chapter_data["title"],
                                        chapter_plan=(
                                            editor_chapter_data[
                                                "chapter_plan"
                                            ]
                                        ),
                                        scene_plan=(
                                            editor_chapter_data[
                                                "scene_plan"
                                            ]
                                        ),
                                        draft=master_draft,
                                        edited_draft=(
                                            manual_edited_text.strip()
                                        ),
                                        continuity_report=(
                                            editor_report
                                        ),
                                        chapter_summary=(
                                            editor_chapter_data[
                                                "chapter_summary"
                                            ]
                                        ),
                                        status="edited",
                                    )

                                    st.session_state[
                                        manual_source_key
                                    ] = manual_edited_text.strip()

                                    st.success(
                                        "Manual changes saved to the "
                                        "edited candidate."
                                    )
                                    st.rerun()

                        with manual_col_2:
                            st.caption(
                                f"Manual workspace: "
                                f"{len(manual_edited_text.split()):,} words"
                            )

                        # -------------------------------------
                        # DOWNLOAD
                        # -------------------------------------

                        st.download_button(
                            label="⬇️ Download Edited Draft",
                            data=edited_draft,
                            file_name=(
                                f"chapter_"
                                f"{editor_chapter_number}"
                                f"_edited.md"
                            ),
                            mime="text/markdown",
                            key=(
                                f"download_edited_"
                                f"{editor_chapter_number}"
                            ),
                        )

                        # -------------------------------------
                        # ACCEPT EDITED DRAFT
                        # -------------------------------------

                        st.divider()
                        st.subheader("Accept Edited Draft")

                        st.caption(
                            "Accepting promotes the edited candidate to "
                            "the current master. The existing master is "
                            "saved to Version History first."
                        )

                        confirm_accept = st.checkbox(
                            "I want to make this edited draft the new master.",
                            key=(
                                f"confirm_accept_edit_"
                                f"{editor_chapter_number}"
                            ),
                        )

                        if st.button(
                            "✅ Accept Edited Draft",
                            type="primary",
                            key=(
                                f"accept_edited_draft_"
                                f"{editor_chapter_number}"
                            ),
                        ):

                            if not confirm_accept:
                                st.error(
                                    "Confirm that you want to promote "
                                    "the edited draft first."
                                )

                            else:
                                try:
                                    add_editor_version(
                                        project_id,
                                        editor_chapter_number,
                                        master_draft,
                                        "Master before accepted edit",
                                    )

                                    accepted_draft = (
                                        edited_draft.strip()
                                    )

                                    save_chapter(
                                        project_id=project_id,
                                        chapter_number=(
                                            editor_chapter_number
                                        ),
                                        title=editor_chapter_data["title"],
                                        chapter_plan=(
                                            editor_chapter_data[
                                                "chapter_plan"
                                            ]
                                        ),
                                        scene_plan=(
                                            editor_chapter_data[
                                                "scene_plan"
                                            ]
                                        ),
                                        draft=accepted_draft,
                                        edited_draft="",
                                        continuity_report="",
                                        chapter_summary=(
                                            editor_chapter_data[
                                                "chapter_summary"
                                            ]
                                        ),
                                        status="accepted",
                                    )

                                    st.session_state.pop(
                                        manual_key,
                                        None,
                                    )
                                    st.session_state.pop(
                                        manual_source_key,
                                        None,
                                    )

                                    st.success(
                                        "Edited draft accepted. It is now "
                                        "the current master draft."
                                    )
                                    st.rerun()

                                except Exception as error:
                                    st.error(
                                        f"Accepting edited draft failed: "
                                        f"{error}"
                                    )

                        # -------------------------------------
                        # DELETE EDITED CANDIDATE
                        # -------------------------------------

                        st.divider()

                        confirm_delete_edit = st.checkbox(
                            "I want to delete the edited candidate.",
                            key=(
                                f"confirm_delete_edit_"
                                f"{editor_chapter_number}"
                            ),
                        )

                        if st.button(
                            "🗑 Delete Edited Draft",
                            key=(
                                f"delete_edited_draft_"
                                f"{editor_chapter_number}"
                            ),
                        ):

                            if not confirm_delete_edit:
                                st.error(
                                    "Confirm that you want to delete "
                                    "the edited draft first."
                                )

                            else:
                                try:
                                    add_editor_version(
                                        project_id,
                                        editor_chapter_number,
                                        edited_draft,
                                        "Deleted edited candidate",
                                    )

                                    save_chapter(
                                        project_id=project_id,
                                        chapter_number=(
                                            editor_chapter_number
                                        ),
                                        title=editor_chapter_data["title"],
                                        chapter_plan=(
                                            editor_chapter_data[
                                                "chapter_plan"
                                            ]
                                        ),
                                        scene_plan=(
                                            editor_chapter_data[
                                                "scene_plan"
                                            ]
                                        ),
                                        draft=master_draft,
                                        edited_draft="",
                                        continuity_report=(
                                            editor_report
                                        ),
                                        chapter_summary=(
                                            editor_chapter_data[
                                                "chapter_summary"
                                            ]
                                        ),
                                        status=(
                                            "analyzed"
                                            if editor_report
                                            else "drafted"
                                        ),
                                    )

                                    st.success(
                                        "Edited candidate deleted. A copy "
                                        "was saved to Version History."
                                    )
                                    st.rerun()

                                except Exception as error:
                                    st.error(
                                        f"Edited draft deletion failed: "
                                        f"{error}"
                                    )

                    # =============================================
                    # VERSION HISTORY
                    # =============================================

                    st.divider()
                    st.subheader("Version History")

                    versions = get_editor_versions(
                        project_id,
                        editor_chapter_number,
                    )

                    if not versions:
                        st.caption(
                            "No previous editor versions have been saved yet."
                        )

                    else:
                        version_options = {}

                        for index, version in enumerate(
                            reversed(versions)
                        ):
                            label = (
                                f"{version.get('timestamp', '')} — "
                                f"{version.get('label', 'Version')} — "
                                f"{version.get('word_count', 0):,} words"
                            )
                            version_options[label] = (
                                len(versions) - 1 - index
                            )

                        selected_version_label = st.selectbox(
                            "Saved Version",
                            list(version_options.keys()),
                            key=(
                                f"version_select_"
                                f"{editor_chapter_number}"
                            ),
                        )

                        selected_version = versions[
                            version_options[
                                selected_version_label
                            ]
                        ]

                        with st.expander(
                            "Preview Selected Version"
                        ):
                            st.markdown(
                                selected_version[
                                    "content"
                                ]
                            )

                        restore_col_1, restore_col_2 = (
                            st.columns(2)
                        )

                        with restore_col_1:
                            if st.button(
                                "↩ Restore as Edited Draft",
                                key=(
                                    f"restore_version_edit_"
                                    f"{editor_chapter_number}"
                                ),
                            ):
                                if edited_draft:
                                    add_editor_version(
                                        project_id,
                                        editor_chapter_number,
                                        edited_draft,
                                        "Edited draft before version restore",
                                    )

                                save_chapter(
                                    project_id=project_id,
                                    chapter_number=(
                                        editor_chapter_number
                                    ),
                                    title=editor_chapter_data["title"],
                                    chapter_plan=(
                                        editor_chapter_data[
                                            "chapter_plan"
                                        ]
                                    ),
                                    scene_plan=(
                                        editor_chapter_data[
                                            "scene_plan"
                                        ]
                                    ),
                                    draft=master_draft,
                                    edited_draft=(
                                        selected_version[
                                            "content"
                                        ]
                                    ),
                                    continuity_report=(
                                        editor_report
                                    ),
                                    chapter_summary=(
                                        editor_chapter_data[
                                            "chapter_summary"
                                        ]
                                    ),
                                    status="edited",
                                )
                                st.success(
                                    "Version restored as the edited candidate."
                                )
                                st.rerun()

                        with restore_col_2:
                            confirm_master_restore = st.checkbox(
                                "Allow master restore",
                                key=(
                                    f"confirm_master_restore_"
                                    f"{editor_chapter_number}"
                                ),
                            )

                            if st.button(
                                "⏪ Restore as Master Draft",
                                key=(
                                    f"restore_version_master_"
                                    f"{editor_chapter_number}"
                                ),
                            ):
                                if not confirm_master_restore:
                                    st.error(
                                        "Enable 'Allow master restore' first."
                                    )
                                else:
                                    add_editor_version(
                                        project_id,
                                        editor_chapter_number,
                                        master_draft,
                                        "Master before version restore",
                                    )

                                    save_chapter(
                                        project_id=project_id,
                                        chapter_number=(
                                            editor_chapter_number
                                        ),
                                        title=editor_chapter_data["title"],
                                        chapter_plan=(
                                            editor_chapter_data[
                                                "chapter_plan"
                                        ]
                                        ),
                                        scene_plan=(
                                            editor_chapter_data[
                                                "scene_plan"
                                            ]
                                        ),
                                        draft=(
                                            selected_version[
                                                "content"
                                            ]
                                        ),
                                        edited_draft="",
                                        continuity_report="",
                                        chapter_summary=(
                                            editor_chapter_data[
                                                "chapter_summary"
                                            ]
                                        ),
                                        status="restored",
                                    )
                                    st.success(
                                        "Selected version restored as "
                                        "the current master draft."
                                    )
                                    st.rerun()


# =========================================================
# PROJECT STATUS
# =========================================================

with project_tab:

    st.header(
        "Current Project"
    )

    st.json(
        current_book()
    )

    st.subheader(
        "Memory Status"
    )

    if st.session_state.story_architecture:
        st.success(
            "Story Bible exists"
        )
    else:
        st.warning(
            "Story Bible missing"
        )

    if st.session_state.character_bible:
        st.success(
            "Character Bible exists"
        )
    else:
        st.warning(
            "Character Bible missing"
        )

    if st.session_state.world_bible:
        st.success(
            "World Bible exists"
        )
    else:
        st.warning(
            "World Bible missing"
        )

    if st.session_state.timeline:
        st.success(
            "Timeline exists"
        )
    else:
        st.warning(
            "Timeline missing"
        )

    if st.session_state.current_project_id:

        chapters = get_project_chapters(
            st.session_state.current_project_id
        )

        st.write(
            f"Saved chapters: {len(chapters)}"
        )


# =========================================================
# SAVED PROJECTS
# =========================================================

with database_tab:

    st.header(
        "Saved Projects"
    )

    saved_projects = get_all_projects()

    if not saved_projects:

        st.info(
            "No projects have been saved yet."
        )

    else:

        for (
            project_id,
            project_title,
            updated_at,
        ) in saved_projects:

            with st.expander(
                f"{project_title} "
                f"— Project {project_id}"
            ):

                project = load_project(
                    project_id
                )

                st.write(
                    f"Last updated: "
                    f"{updated_at}"
                )

                if project:

                    st.write(
                        f"Genre: "
                        f"{project['genre']}"
                    )

                    st.write(
                        f"Region: "
                        f"{project['region']}"
                    )

                    st.write(
                        f"Primary Plot: "
                        f"{project['primary_plot']}"
                    )

                    st.write(
                        f"Secondary Plot: "
                        f"{project['secondary_plot']}"
                    )

                    st.write(
                        f"Character Arc: "
                        f"{project['character_arc']}"
                    )

                    st.write(
                        f"Relationship Arc: "
                        f"{project['relationship_arc']}"
                    )

                    st.write(
                        f"Mystery Engine: "
                        f"{project['mystery_engine']}"
                    )

                    if project["word_count"]:

                        st.write(
                            f"Target words: "
                            f"{project['word_count']:,}"
                        )

                    st.write(
                        "Story Bible:",
                        (
                            "Yes"
                            if project[
                                "story_architecture"
                            ]
                            else "No"
                        ),
                    )

                    st.write(
                        "Character Bible:",
                        (
                            "Yes"
                            if project[
                                "character_bible"
                            ]
                            else "No"
                        ),
                    )

                    st.write(
                        "World Bible:",
                        (
                            "Yes"
                            if project[
                                "world_bible"
                            ]
                            else "No"
                        ),
                    )

                    st.write(
                        "Timeline:",
                        (
                            "Yes"
                            if project[
                                "timeline"
                            ]
                            else "No"
                        ),
                    )

                    project_chapters = (
                        get_project_chapters(
                            project_id
                        )
                    )

                    st.write(
                        f"Chapters: "
                        f"{len(project_chapters)}"
                    )

                    if st.button(
                        "Delete Project",
                        key=(
                            f"delete_project_"
                            f"{project_id}"
                        ),
                    ):

                        delete_project(
                            project_id
                        )

                        if (
                            st.session_state
                            .current_project_id
                            == project_id
                        ):

                            reset_project()

                        st.rerun()