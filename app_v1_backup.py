import os

import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI


# =========================================================
# CONFIGURATION
# =========================================================

load_dotenv()

st.set_page_config(
    page_title="AI Novelist",
    page_icon="📖",
    layout="wide",
)

st.title("📖 AI Novelist")
st.caption("AI-powered story architecture and novel development")


# =========================================================
# OPENAI
# =========================================================

api_key = os.getenv("OPENAI_API_KEY")
model_name = os.getenv("OPENAI_MODEL")

client = OpenAI(api_key=api_key) if api_key else None


def call_ai(system_prompt, user_prompt):
    """Send instructions to the AI and return the generated text."""

    if not client:
        raise RuntimeError(
            "No OpenAI API key was found. "
            "Add OPENAI_API_KEY to your .env file."
        )

    if not model_name:
        raise RuntimeError(
            "No model has been configured. "
            "Add OPENAI_MODEL to your .env file."
        )

    response = client.responses.create(
        model=model_name,
        instructions=system_prompt,
        input=user_prompt,
    )

    return response.output_text


# =========================================================
# SEVEN BASIC PLOTS
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
# STORY ARCHITECT
# =========================================================

def generate_story_architecture(book):

    system_prompt = """
You are the Story Architect for a professional fiction-writing application.

Your job is to transform the user's idea into an original, sophisticated
story architecture.

Do not imitate the distinctive style of any living author.

Instead use broad dramatic principles:

- restrained, believable dialogue
- morally complicated characters
- conflicting motivations
- environmental pressure
- escalating consequences
- subtext
- realistic human behaviour
- meaningful character flaws
- cinematic scene construction
- cause-and-effect storytelling
- victories that have consequences
- avoidance of predictable AI-writing clichés

Build the story around the selected Seven Basic Plots structure.

Produce:

# Story Premise

# Central Dramatic Question

# Themes

# Story World

Explain how geography, culture, economics and environment influence the story.

# Protagonist

Include:
- external goal
- internal need
- flaw
- fear
- contradiction
- moral boundary

# Antagonistic Force

The antagonist does not necessarily need to be evil.
Explain what they want and why they believe they are justified.

# Supporting Characters

# Three-Act Structure

## Act One
Establish the world, characters, wound and inciting incident.

## Act Two
Escalate pressure, consequences and moral compromises.

## Act Three
Force the protagonist to make the defining choice.

# Major Turning Points

# Character Arc

# Ending

The ending must emerge from the protagonist's choices.

# Chapter Outline

Create an appropriate number of chapters for the requested word count.

For every chapter provide:
- chapter purpose
- conflict
- important development
- approximate word target

# Continuity Bible

List facts that future writing agents must never contradict.
"""

    user_prompt = f"""
TITLE:
{book['title']}

USER'S PLOT:
{book['plot']}

BASIC PLOT STRUCTURE:
{book['plot_type']}

GENRE:
{book['genre']}

REGION:
{book['region']}

TIME PERIOD:
{book['period']}

CHARACTERS PROVIDED BY USER:
{book['characters']}

TARGET NOVEL LENGTH:
{book['word_count']:,} words
"""

    return call_ai(system_prompt, user_prompt)


# =========================================================
# CHARACTER ENGINE
# =========================================================

def generate_character_bible(book):

    system_prompt = """
You are the Character Architect for a professional fiction-writing system.

Develop psychologically believable ORIGINAL characters.

Do not imitate the distinctive writing style of any living author.

Characters should contain contradictions.

Avoid simplistic heroes and villains.

For each important character provide:

# Name

## Basic Information
- age
- occupation
- background
- appearance

## Personality

## External Goal

## Internal Need

## Strength

## Primary Flaw

## Fear

## Personal History

## Defining Experience

## Secret

## Moral Boundary

What will this character refuse to do?

## Pressure Point

What could make them cross that boundary?

## Relationships

## Contradictions

## Character Arc

## Dialogue Characteristics

Describe how the character communicates without creating catchphrases
or copying another author's dialogue style.

Finish with:

# Character Relationship Map

Explain the major relationships, alliances, resentments, dependencies,
secrets and conflicts connecting the cast.
"""

    user_prompt = f"""
BOOK:
{book['title']}

PLOT:
{book['plot']}

PLOT STRUCTURE:
{book['plot_type']}

GENRE:
{book['genre']}

REGION:
{book['region']}

TIME PERIOD:
{book['period']}

CHARACTERS SUPPLIED BY USER:
{book['characters']}
"""

    return call_ai(system_prompt, user_prompt)


# =========================================================
# USER INTERFACE
# =========================================================

with st.sidebar:

    st.header("Book Setup")

    title = st.text_input(
        "Book Title",
        value="Untitled Novel",
    )

    plot = st.text_area(
        "Plot",
        height=200,
        placeholder=(
            "Describe your story idea. It can be a few sentences "
            "or several paragraphs."
        ),
    )

    plot_type = st.selectbox(
        "Seven Basic Plots",
        PLOT_TYPES,
    )

    genre = st.text_input(
        "Genre",
        value="Crime Thriller",
    )

    region = st.text_input(
        "Region of the World",
        placeholder="e.g. British Columbia, Canada",
    )

    period = st.text_input(
        "Time Period",
        value="Present Day",
    )

    characters = st.text_area(
        "Characters",
        height=180,
        placeholder=(
            "Enter the characters you already have in mind. "
            "Leave blank if you want the AI to develop them."
        ),
    )

    word_count = st.number_input(
        "Target Word Count",
        min_value=10_000,
        max_value=250_000,
        value=80_000,
        step=5_000,
    )


book = {
    "title": title,
    "plot": plot,
    "plot_type": plot_type,
    "genre": genre,
    "region": region,
    "period": period,
    "characters": characters,
    "word_count": word_count,
}


# =========================================================
# MAIN TABS
# =========================================================

story_tab, character_tab, project_tab = st.tabs(
    [
        "🏗 Story Architect",
        "👤 Character Engine",
        "📋 Project",
    ]
)


# =========================================================
# STORY TAB
# =========================================================

with story_tab:

    st.header("Story Architect")

    st.write(
        "Turn your initial idea into the structural blueprint "
        "for the novel."
    )

    if st.button(
        "Build Story Architecture",
        type="primary",
    ):

        if not plot.strip():

            st.error(
                "Enter your plot in the Book Setup panel first."
            )

        else:

            with st.spinner(
                "The Story Architect is developing your novel..."
            ):

                try:

                    architecture = generate_story_architecture(book)

                    st.session_state["story_architecture"] = architecture

                except Exception as error:

                    st.error(f"Generation failed: {error}")

    if "story_architecture" in st.session_state:

        st.divider()

        st.markdown(
            st.session_state["story_architecture"]
        )

        st.download_button(
            label="Download Story Bible",
            data=st.session_state["story_architecture"],
            file_name="story_bible.md",
            mime="text/markdown",
        )


# =========================================================
# CHARACTER TAB
# =========================================================

with character_tab:

    st.header("Character Engine")

    st.write(
        "Develop the psychological structure and relationships "
        "of the novel's characters."
    )

    if st.button("Build Character Bible"):

        if not plot.strip():

            st.error(
                "Enter your plot in the Book Setup panel first."
            )

        else:

            with st.spinner(
                "The Character Engine is developing the cast..."
            ):

                try:

                    character_bible = generate_character_bible(book)

                    st.session_state["character_bible"] = character_bible

                except Exception as error:

                    st.error(f"Generation failed: {error}")

    if "character_bible" in st.session_state:

        st.divider()

        st.markdown(
            st.session_state["character_bible"]
        )

        st.download_button(
            label="Download Character Bible",
            data=st.session_state["character_bible"],
            file_name="character_bible.md",
            mime="text/markdown",
        )


# =========================================================
# PROJECT TAB
# =========================================================

with project_tab:

    st.header("Current Project")

    st.write(
        "This shows the information currently being supplied "
        "to the writing system."
    )

    st.json(book)