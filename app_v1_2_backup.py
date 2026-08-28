import streamlit as st

from database import (
    initialise_database,
    create_project,
    update_project,
    get_all_projects,
    load_project,
    delete_project,
)

from ai_engine import (
    generate_story_architecture,
    generate_character_bible,
    generate_world_bible,
    generate_timeline,
)


# =========================================================
# CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="AI Novelist",
    page_icon="📖",
    layout="wide",
)

st.title("📖 AI Novelist")
st.caption("AI-powered story development and novel planning system")


# =========================================================
# INITIALISE DATABASE
# =========================================================

initialise_database()


# =========================================================
# CONSTANTS
# =========================================================

PLOT_TYPES = [
    "Overcoming the Monster",
    "Rags to Riches",
    "The Quest",
    "Voyage and Return",
    "Comedy",
    "Tragedy",
    "Rebirth",
]


# =========================================================
# SESSION STATE
# =========================================================

defaults = {
    "current_project_id": None,
    "title": "Untitled Novel",
    "plot": "",
    "plot_type": "Overcoming the Monster",
    "genre": "Crime Thriller",
    "region": "",
    "period": "Present Day",
    "characters_input": "",
    "word_count": 80000,
    "story_architecture": "",
    "character_bible": "",
    "world_bible": "",
    "timeline": "",
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
        "plot_type": st.session_state.plot_type,
        "genre": st.session_state.genre,
        "region": st.session_state.region,
        "period": st.session_state.period,
        "characters": st.session_state.characters_input,
        "word_count": st.session_state.word_count,
    }


def current_memory():
    return {
        "story_architecture": st.session_state.story_architecture,
        "character_bible": st.session_state.character_bible,
        "world_bible": st.session_state.world_bible,
        "timeline": st.session_state.timeline,
    }


def reset_project():
    st.session_state.current_project_id = None
    st.session_state.title = "Untitled Novel"
    st.session_state.plot = ""
    st.session_state.plot_type = "Overcoming the Monster"
    st.session_state.genre = "Crime Thriller"
    st.session_state.region = ""
    st.session_state.period = "Present Day"
    st.session_state.characters_input = ""
    st.session_state.word_count = 80000
    st.session_state.story_architecture = ""
    st.session_state.character_bible = ""
    st.session_state.world_bible = ""
    st.session_state.timeline = ""


def save_current_project():
    book = current_book()
    memory = current_memory()

    if not book["title"].strip():
        st.error("Give the project a title before saving.")
        return

    if st.session_state.current_project_id is None:
        project_id = create_project(book, memory)
        st.session_state.current_project_id = project_id
        st.success(f"Project saved. Project ID: {project_id}")
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


# =========================================================
# SIDEBAR - PROJECT MANAGEMENT
# =========================================================

with st.sidebar:

    st.header("Project Management")

    projects = get_all_projects()

    project_options = {
        f"{title} | ID {project_id}": project_id
        for project_id, title, updated_at in projects
    }

    selected_project_label = st.selectbox(
        "Saved Projects",
        ["-- Select Project --"] + list(project_options.keys()),
    )

    load_col, new_col = st.columns(2)

    with load_col:

        if st.button("Load"):

            if selected_project_label == "-- Select Project --":
                st.warning("Choose a saved project first.")

            else:

                project_id = project_options[selected_project_label]
                project = load_project(project_id)

                if project:

                    st.session_state.current_project_id = project["id"]
                    st.session_state.title = project["title"]
                    st.session_state.plot = project["plot"] or ""
                    st.session_state.plot_type = (
                        project["plot_type"]
                        or "Overcoming the Monster"
                    )
                    st.session_state.genre = project["genre"] or ""
                    st.session_state.region = project["region"] or ""
                    st.session_state.period = project["period"] or ""
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

                    st.rerun()

    with new_col:

        if st.button("New"):

            reset_project()
            st.rerun()

    st.divider()

    st.header("Book Setup")

    st.text_input(
        "Book Title",
        key="title",
    )

    st.text_area(
        "Plot",
        height=190,
        key="plot",
        placeholder="Describe the story you want to tell...",
    )

    st.selectbox(
        "Seven Basic Plots",
        PLOT_TYPES,
        key="plot_type",
    )

    st.text_input(
        "Genre",
        key="genre",
    )

    st.text_input(
        "Region of the World",
        key="region",
        placeholder="e.g. British Columbia, Canada",
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


# =========================================================
# SAVE AREA
# =========================================================

save_col, status_col = st.columns([1, 3])

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
    world_tab,
    timeline_tab,
    project_tab,
    database_tab,
) = st.tabs(
    [
        "🏗 Story Architect",
        "👤 Character Engine",
        "🌍 World Builder",
        "🕒 Timeline",
        "📋 Project",
        "💾 Saved Data",
    ]
)


# =========================================================
# STORY ARCHITECT
# =========================================================

with story_tab:

    st.header("Story Architect")

    st.write(
        "Develop the structural blueprint for the novel."
    )

    if st.button(
        "Build Story Architecture",
        type="primary",
    ):

        book = current_book()

        if not book["plot"].strip():

            st.error(
                "Enter your plot in Book Setup first."
            )

        else:

            with st.spinner(
                "The Story Architect is developing the novel..."
            ):

                try:

                    result = generate_story_architecture(book)

                    st.session_state.story_architecture = result

                    autosave_if_possible()

                except Exception as error:

                    st.error(
                        f"Generation failed: {error}"
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
        "Develop psychologically believable characters "
        "and relationships."
    )

    if st.button("Build Character Bible"):

        book = current_book()

        if not book["plot"].strip():

            st.error(
                "Enter your plot in Book Setup first."
            )

        else:

            with st.spinner(
                "The Character Architect is developing the cast..."
            ):

                try:

                    result = generate_character_bible(
                        book,
                        st.session_state.story_architecture,
                    )

                    st.session_state.character_bible = result

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
# WORLD BUILDER
# =========================================================

with world_tab:

    st.header("World Builder")

    st.write(
        "Build the physical, cultural, economic and social "
        "world in which the story takes place."
    )

    if st.button(
        "Build World Bible"
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
                "The World Builder is developing the story world..."
            ):

                try:

                    result = generate_world_bible(
                        book,
                        st.session_state.story_architecture,
                        st.session_state.character_bible,
                    )

                    st.session_state.world_bible = result

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
# TIMELINE ENGINE
# =========================================================

with timeline_tab:

    st.header("Timeline Architect")

    st.write(
        "Create a chronological record of the novel's events, "
        "character states, revelations and unresolved threads."
    )

    if st.button(
        "Build Timeline"
    ):

        book = current_book()

        if not book["plot"].strip():

            st.error(
                "Enter your plot in Book Setup first."
            )

        else:

            with st.spinner(
                "The Timeline Architect is building continuity..."
            ):

                try:

                    result = generate_timeline(
                        book,
                        st.session_state.story_architecture,
                        st.session_state.character_bible,
                        st.session_state.world_bible,
                    )

                    st.session_state.timeline = result

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
# PROJECT STATUS
# =========================================================

with project_tab:

    st.header("Current Project")

    book = current_book()

    st.json(book)

    st.subheader("Memory Status")

    if st.session_state.story_architecture:
        st.success("Story Bible exists")
    else:
        st.warning("Story Bible missing")

    if st.session_state.character_bible:
        st.success("Character Bible exists")
    else:
        st.warning("Character Bible missing")

    if st.session_state.world_bible:
        st.success("World Bible exists")
    else:
        st.warning("World Bible missing")

    if st.session_state.timeline:
        st.success("Timeline exists")
    else:
        st.warning("Timeline missing")


# =========================================================
# SAVED PROJECTS
# =========================================================

with database_tab:

    st.header("Saved Projects")

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
                f"{project_title} — Project {project_id}"
            ):

                project = load_project(project_id)

                st.write(
                    f"Last updated: {updated_at}"
                )

                if project:

                    st.write(
                        f"Genre: {project['genre']}"
                    )

                    st.write(
                        f"Region: {project['region']}"
                    )

                    if project["word_count"]:

                        st.write(
                            f"Target words: "
                            f"{project['word_count']:,}"
                        )

                    st.write(
                        "Story Bible:",
                        "Yes"
                        if project["story_architecture"]
                        else "No",
                    )

                    st.write(
                        "Character Bible:",
                        "Yes"
                        if project["character_bible"]
                        else "No",
                    )

                    st.write(
                        "World Bible:",
                        "Yes"
                        if project["world_bible"]
                        else "No",
                    )

                    st.write(
                        "Timeline:",
                        "Yes"
                        if project["timeline"]
                        else "No",
                    )

                    if st.button(
                        "Delete Project",
                        key=f"delete_{project_id}",
                    ):

                        delete_project(project_id)

                        if (
                            st.session_state.current_project_id
                            == project_id
                        ):

                            reset_project()

                        st.rerun()