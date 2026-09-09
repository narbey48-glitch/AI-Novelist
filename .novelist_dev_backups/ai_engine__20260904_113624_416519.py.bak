import os

from dotenv import load_dotenv
from openai import OpenAI

from prompts import (
    STORY_ARCHITECT_PROMPT,
    CHARACTER_ARCHITECT_PROMPT,
    WORLD_BUILDER_PROMPT,
    TIMELINE_ARCHITECT_PROMPT,
    CHAPTER_PLANNER_PROMPT,
    CHAPTER_WRITER_PROMPT,
    EDITOR_ANALYST_PROMPT,
    EDITOR_REWRITE_PROMPT,
)


# =========================================================
# ENVIRONMENT / OPENAI
# =========================================================

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
model_name = os.getenv("OPENAI_MODEL")

client = OpenAI(api_key=api_key) if api_key else None


# =========================================================
# CORE AI CALL
# =========================================================

def call_ai(system_prompt, user_prompt):

    if not client:
        raise RuntimeError(
            "No OpenAI API key was found. "
            "Check the OPENAI_API_KEY value in your .env file."
        )

    if not model_name:
        raise RuntimeError(
            "No OpenAI model has been configured. "
            "Check OPENAI_MODEL in your .env file."
        )

    response = client.responses.create(
        model=model_name,
        instructions=system_prompt,
        input=user_prompt,
    )

    return response.output_text



# =========================================================
# CHARACTER ARCHITECT
# =========================================================

def generate_character_bible(
    book,
    previous_character_bible="",
    *args,
    **kwargs,
):
    if not client:
        raise RuntimeError(
            "No OpenAI API key was found. "
            "Check the OPENAI_API_KEY value in your .env file."
        )

    if not model_name:
        raise RuntimeError(
            "No OpenAI model has been configured. "
            "Check OPENAI_MODEL in your .env file."
        )

    existing_character_bible = (
        previous_character_bible
        or kwargs.get("existing_character_bible", "")
        or kwargs.get("character_bible", "")
    )

    user_prompt = f"""
=========================================================
BOOK INFORMATION
=========================================================

TITLE:
{book.get('title', '')}

PLOT:
{book.get('plot', '')}

GENRE:
{book.get('genre', '')}

REGION:
{book.get('region', '')}

TIME PERIOD:
{book.get('period', '')}

PRIMARY PLOT:
{book.get('primary_plot', book.get('plot_type', ''))}

SECONDARY PLOT:
{book.get('secondary_plot', 'None')}

CHARACTER ARC:
{book.get('character_arc', '')}

RELATIONSHIP ARC:
{book.get('relationship_arc', 'None')}

MYSTERY ENGINE:
{book.get('mystery_engine', 'None')}

WRITING STYLE PROFILE:
{book.get('writing_style_profile', 'Cinematic Technical Thriller')}

USER-SUPPLIED CHARACTER INFORMATION:
{book.get('characters', '')}

PREVIOUS CHARACTER BIBLE, IF ANY:
{existing_character_bible}

=========================================================
CHARACTER ARCHITECT INSTRUCTIONS
=========================================================

Create a detailed, continuity-safe Character Bible for this novel.

NAME RULES:

- Every named character must have a believable FIRST and LAST name.
- Names must fit the story's region, culture, period, and character background.
- Avoid duplicate first names and duplicate surnames unless the characters are intentionally related.
- Do not use celebrity names or famous fictional-character names.
- If regenerating characters, prefer fresh names unless a name was explicitly supplied by the user or must be retained for continuity.
- Once a name is established in this Character Bible, treat it as authoritative for future story generation.

CHARACTER DEPTH:

For major characters establish:

- full name
- age or approximate age where useful
- role in the story
- occupation / professional competence
- background
- external goal
- internal need
- fears
- flaws
- contradictions
- moral boundaries
- loyalties
- vulnerabilities
- secrets
- important relationships
- relevant history before the novel begins
- knowledge they currently possess
- important information they do not possess
- likely pressure points
- speech / dialogue tendencies
- physical or behavioral habits only when meaningful

Keep characters psychologically believable and distinct.

Do not make every character equally articulate, equally competent, or morally simple.

Professional, institutional, technical, criminal, military, legal, medical, political, or corporate details must remain plausible for the setting.

Do not invent unsupported relationships that contradict user-supplied material.

=========================================================
OUTPUT FORMAT
=========================================================

Return detailed Markdown using exactly these major headings:

# CHARACTER INDEX

List every established named character with their full name and story role.
This section is the authoritative source for character names.

# PRIMARY CHARACTERS

Provide detailed profiles for the protagonist, antagonist where applicable, and other central characters.

# SUPPORTING CHARACTERS

Provide concise but useful profiles for supporting characters.

# RELATIONSHIP MAP

Explain important relationships, loyalties, tensions, dependencies, conflicts, family links, professional connections, and hidden agendas.

# CHARACTER KNOWLEDGE MAP

Track what major characters know, suspect, misunderstand, conceal, and do not yet know.

# CHARACTER CONTINUITY RULES

List facts future Story Architect, Chapter Planner, Chapter Writer, and Editor agents must not contradict.
"""

    return call_ai(
        CHARACTER_ARCHITECT_PROMPT,
        user_prompt,
    )

# =========================================================
# STORY ARCHITECT
# =========================================================

def generate_story_architecture(
    book,
    character_bible="",
):

    writing_style_profile = book.get(
        "writing_style_profile",
        "Cinematic Technical Thriller",
    )

    style_dialogue = book.get(
        "style_dialogue",
        35,
    )

    style_technical_detail = book.get(
        "style_technical_detail",
        75,
    )

    style_pacing = book.get(
        "style_pacing",
        65,
    )

    style_moral_complexity = book.get(
        "style_moral_complexity",
        85,
    )

    style_description = book.get(
        "style_description",
        45,
    )

    style_violence = book.get(
        "style_violence",
        60,
    )

    style_institutional_detail = book.get(
        "style_institutional_detail",
        75,
    )

    style_subtext = book.get(
        "style_subtext",
        80,
    )


    # -----------------------------------------------------
    # STYLE INTERPRETATION HELPERS
    # -----------------------------------------------------

    def dialogue_guidance(value):

        if value <= 25:
            return (
                "Dialogue should be highly restrained. "
                "Characters speak economically and often avoid "
                "stating emotion directly."
            )

        elif value <= 50:
            return (
                "Dialogue should remain controlled and natural, "
                "with moderate emotional expression."
            )

        elif value <= 75:
            return (
                "Dialogue may be more expressive and conversational "
                "while remaining character-specific."
            )

        else:
            return (
                "Dialogue may be highly expressive, energetic, "
                "emotionally open, and conversational."
            )


    def technical_guidance(value):

        if value <= 25:
            return (
                "Use very little technical detail. "
                "Include only what the reader needs to understand "
                "the immediate dramatic situation."
            )

        elif value <= 50:
            return (
                "Use moderate technical detail when it helps establish "
                "credibility, stakes, or practical constraints."
            )

        elif value <= 75:
            return (
                "Use substantial technical, procedural, operational, "
                "or professional detail where it directly affects events."
            )

        else:
            return (
                "Use extensive technically credible detail, including "
                "procedure, logistics, systems, technology, and professional "
                "decision-making, while keeping it understandable."
            )


    def pacing_guidance(value):

        if value <= 25:
            return (
                "Use slow-burn pacing with substantial room for atmosphere, "
                "observation, character tension, and gradual escalation."
            )

        elif value <= 50:
            return (
                "Use measured pacing with a balance between character "
                "development and forward plot movement."
            )

        elif value <= 75:
            return (
                "Use relatively fast pacing with frequent meaningful "
                "developments while preserving scene depth."
            )

        else:
            return (
                "Use aggressive forward momentum, short delays between "
                "consequences, and frequent changes in the story situation."
            )


    def moral_guidance(value):

        if value <= 25:
            return (
                "Moral positions may be relatively clear, with stronger "
                "distinctions between justified and unjustified behavior."
            )

        elif value <= 50:
            return (
                "Use moderate moral complexity. Important characters may "
                "have understandable flaws and mixed motives."
            )

        elif value <= 75:
            return (
                "Use strong moral ambiguity, conflicting legitimate goals, "
                "and difficult trade-offs."
            )

        else:
            return (
                "Use very high moral complexity. Major characters should "
                "often have understandable but conflicting reasons, with "
                "choices producing ethical costs."
            )


    def description_guidance(value):

        if value <= 25:
            return (
                "Keep description sparse and functional. "
                "Favor action, dialogue, and selective concrete details."
            )

        elif value <= 50:
            return (
                "Use controlled description with selective sensory and "
                "environmental detail."
            )

        elif value <= 75:
            return (
                "Use substantial descriptive detail where it strengthens "
                "setting, atmosphere, characterization, or tension."
            )

        else:
            return (
                "Use rich, detailed description with strong sensory, "
                "environmental, and atmospheric presence."
            )


    def violence_guidance(value):

        if value <= 25:
            return (
                "Violence should usually be restrained, brief, or partially "
                "implied, with emphasis on consequence rather than detail."
            )

        elif value <= 50:
            return (
                "Violence may be shown directly but without unnecessary "
                "graphic detail."
            )

        elif value <= 75:
            return (
                "Violence may be portrayed realistically and directly, "
                "including physical and emotional aftermath."
            )

        else:
            return (
                "Violence may be depicted in explicit physical detail when "
                "dramatically justified, while retaining realistic aftermath "
                "and consequences."
            )


    def institutional_guidance(value):

        if value <= 25:
            return (
                "Keep institutional and political systems mostly in the "
                "background unless essential to the plot."
            )

        elif value <= 50:
            return (
                "Use moderate institutional detail where organizations "
                "directly influence character choices."
            )

        elif value <= 75:
            return (
                "Develop institutions, hierarchies, competing priorities, "
                "bureaucracy, and organizational conflict in meaningful detail."
            )

        else:
            return (
                "Use extensive institutional and political complexity, "
                "including chains of command, bureaucracy, competing agencies, "
                "resource constraints, internal agendas, and power structures."
            )


    def subtext_guidance(value):

        if value <= 25:
            return (
                "Characters may communicate relatively directly. "
                "Important intentions should generally remain clear."
            )

        elif value <= 50:
            return (
                "Use moderate subtext. Characters sometimes avoid saying "
                "exactly what they think or feel."
            )

        elif value <= 75:
            return (
                "Use strong subtext, implication, silence, avoidance, "
                "and conflicting surface versus hidden intentions."
            )

        else:
            return (
                "Use very strong subtext. Important emotional and strategic "
                "meaning should often exist beneath what characters explicitly say."
            )


    detailed_style_guidance = f"""
DIALOGUE STYLE: {style_dialogue}/100
{dialogue_guidance(style_dialogue)}

TECHNICAL DETAIL: {style_technical_detail}/100
{technical_guidance(style_technical_detail)}

PACING: {style_pacing}/100
{pacing_guidance(style_pacing)}

MORAL COMPLEXITY: {style_moral_complexity}/100
{moral_guidance(style_moral_complexity)}

DESCRIPTION DENSITY: {style_description}/100
{description_guidance(style_description)}

VIOLENCE TREATMENT: {style_violence}/100
{violence_guidance(style_violence)}

INSTITUTIONAL / POLITICAL DETAIL:
{style_institutional_detail}/100
{institutional_guidance(style_institutional_detail)}

SUBTEXT: {style_subtext}/100
{subtext_guidance(style_subtext)}
"""


    # -----------------------------------------------------
    # PROFILE PRESETS
    # -----------------------------------------------------

    style_guidance = {
        "Cinematic Technical Thriller": """
Blend grounded cinematic human drama with technically credible
thriller mechanics.

Prioritize:

- morally complicated characters
- restrained emotional expression
- subtext-heavy dialogue
- credible institutions and chains of command
- strategic decision-making
- realistic professional procedures
- technical details that directly affect the plot
- geopolitical, economic, legal, military, corporate, or criminal
  systems where relevant
- characters possessing incomplete information
- escalating consequences from believable decisions
- multiple pressures operating at the same time
- quiet interpersonal scenes between major confrontations
- environmental and geographical pressure
- violence that creates lasting practical and emotional consequences
- strong cause-and-effect storytelling
- tension created through knowledge gaps
- credible logistics
- strategic reversals
- victories that carry costs

Technical material must remain understandable to a general reader.

Do not turn the novel into a technical manual.

Human conflict and character choices remain more important than
displaying research.
""",

        "Grounded Cinematic Drama": """
Prioritize grounded character drama.

Emphasize:

- psychologically believable characters
- moral ambiguity
- family history
- loyalty
- betrayal
- restrained dialogue
- subtext
- physical behavior revealing emotion
- strong sense of place
- economic and social pressure
- quiet scenes carrying dramatic weight
- imperfect relationships
- consequential choices
- violence only when dramatically justified
- unresolved emotional tension where appropriate

Avoid melodrama and excessive explanation.
""",

        "Technical / Geopolitical Thriller": """
Prioritize technically credible thriller construction.

Emphasize:

- geopolitical pressure
- intelligence gathering
- military or security procedures where relevant
- government institutions
- corporations
- organized crime
- logistics
- communications
- surveillance
- technology
- strategic planning
- chains of command
- competing agencies or organizations
- multiple interconnected viewpoints
- incomplete intelligence
- misinformation
- operational consequences
- escalating threat systems
- plausible cause and effect

Technical detail should increase suspense rather than interrupt it.

Keep explanations understandable and dramatically relevant.
""",

        "Literary Crime": """
Prioritize character, atmosphere, moral complexity, and consequence.

Emphasize:

- flawed people
- competing motivations
- social and economic pressure
- crime as a consequence of human decisions
- psychologically credible behavior
- restrained exposition
- strong atmosphere
- meaningful setting
- subtext
- ambiguity
- guilt
- loyalty
- betrayal
- consequences that persist beyond individual scenes

Avoid simplistic criminals, heroes, or moral lessons.
""",

        "Psychological Suspense": """
Prioritize uncertainty, perception, fear, and psychological pressure.

Emphasize:

- unreliable assumptions
- incomplete information
- escalating suspicion
- internal conflict
- subtle behavioral clues
- relationship tension
- hidden motives
- controlled revelation
- shifting interpretations
- psychological manipulation where appropriate
- claustrophobic or isolating situations
- consequences of mistaken beliefs

Do not rely on arbitrary twists.

Revelations should be supported by earlier evidence.
""",

        "Custom": """
Use the user's existing genre, plot, characters, structure choices,
and story information without imposing a predefined narrative style.

Maintain grounded characterization, clear cause and effect,
continuity, believable motivation, and professional-quality
story construction.
""",
    }

    selected_style_guidance = style_guidance.get(
        writing_style_profile,
        style_guidance["Cinematic Technical Thriller"],
    )



    user_prompt = f"""
=========================================================
BOOK INFORMATION
=========================================================

BOOK TITLE:
{book['title']}

USER'S PLOT:
{book['plot']}

PRIMARY PLOT ENGINE:
{book.get('primary_plot', book.get('plot_type', ''))}

SECONDARY PLOT ENGINE:
{book.get('secondary_plot', 'None')}

CHARACTER ARC:
{book.get('character_arc', '')}

RELATIONSHIP ARC:
{book.get('relationship_arc', 'None')}

MYSTERY ENGINE:
{book.get('mystery_engine', 'None')}

STRUCTURE COMPLEXITY:
{book.get('structure_complexity', 'Standard')}

WRITING STYLE PROFILE:
{writing_style_profile}

GENRE:
{book['genre']}

REGION:
{book['region']}

TIME PERIOD:
{book['period']}

TARGET WORD COUNT:
{book['word_count']:,}


=========================================================
SELECTED WRITING STYLE PROFILE
=========================================================

{selected_style_guidance}


=========================================================
DETAILED WRITING STYLE CONTROLS
=========================================================

{detailed_style_guidance}


=========================================================
STYLE CONTROL PRIORITY
=========================================================

The Writing Style Profile establishes the broad storytelling approach.

The Detailed Writing Style Controls fine-tune that profile.

When a detailed slider conflicts with the default characteristics
of the selected profile, the slider value takes priority.

Example:

A Cinematic Technical Thriller normally uses substantial technical
detail.

However, if Technical Detail is set very low, reduce technical
explanation while preserving the broader thriller character and
structure.

Likewise:

- Dialogue Style controls how restrained or expressive dialogue feels.
- Technical Detail controls the depth of technical and procedural material.
- Pacing controls the speed of escalation and scene progression.
- Moral Complexity controls ethical ambiguity and competing motives.
- Description Density controls environmental and sensory detail.
- Violence Treatment controls how directly physical violence is portrayed.
- Institutional / Political Detail controls organizational complexity.
- Subtext controls how much meaning remains beneath explicit dialogue.

Treat these values as intentional creative decisions.


=========================================================
WRITING STYLE AUTHORITY
=========================================================

The selected Writing Style Profile and Detailed Style Controls
should influence:

- story architecture
- pacing
- scene construction
- dialogue philosophy
- information flow
- amount and purpose of technical detail
- institutional complexity
- character conflict
- level of moral ambiguity
- suspense construction
- environmental pressure
- chapter structure
- revelation timing
- consequences

They affect HOW the story is developed.

They must NOT override:

- the user's plot
- established character identities
- established relationships
- selected plot engines
- established world rules
- established chronology

Do not imitate the distinctive prose or voice of any living author.

Instead, use these high-level narrative characteristics to create
an original novel voice.


=========================================================
USER'S ORIGINAL CHARACTER INFORMATION
=========================================================

{book['characters']}


=========================================================
CURRENT AUTHORITATIVE CHARACTER BIBLE
=========================================================

{character_bible}


=========================================================
CRITICAL CHARACTER-NAME RULE
=========================================================

If a Current Character Bible is supplied above, it is the
AUTHORITATIVE source for all current character identities.

Use the exact current names from its:

# CHARACTER INDEX

throughout the Story Architecture.

Do NOT:

- restore old character names from an earlier plot version
- invent replacement names for established characters
- rename established characters
- use temporary names from the user's older plot when the
  Character Bible contains newer names

If the user's Plot uses an OLD character name but the Character
Bible clearly identifies that same character under a NEW name,
use the NEW Character Bible name.

The Story Premise itself should name the important established
characters where doing so improves clarity.

The Protagonist section MUST use the current protagonist's name.

The Antagonistic Force section should use established names where
the antagonistic force is a character.

Supporting Characters must use names from the Character Bible.

The chapter outline must use those same current names consistently.


=========================================================
STORY DEVELOPMENT INSTRUCTIONS
=========================================================

Build the novel around the user's current plot while respecting:

- Primary Plot Engine
- Secondary Plot Engine
- Character Arc
- Relationship Arc
- Mystery Engine
- Structure Complexity
- Writing Style Profile
- Detailed Writing Style Controls

Do not casually replace established story decisions.

Develop an original dramatic structure using these core craft
principles:

- psychologically grounded characters
- detailed implied lives before the novel begins
- conflicting legitimate motivations
- moral ambiguity where appropriate
- restrained exposition
- delayed revelation where dramatically useful
- subtext
- consequential choices
- environmental and economic pressure
- institutions that affect individual lives
- family history affecting present behavior
- loyalty and betrayal
- quiet human moments between major confrontations
- physical action carrying emotional meaning
- victories that create costs
- violence with lasting consequences
- endings driven by choices rather than convenience

Avoid simplistic heroes and villains.

Where possible, allow opposing characters to possess understandable
reasons for their actions.

Do not force artificial emotional closure simply because the plot
reaches its conclusion.


=========================================================
TECHNICAL AND INSTITUTIONAL REALISM
=========================================================

The amount of technical and institutional detail must reflect
the user's slider settings.

Technical information should serve one or more dramatic functions:

- creates a problem
- provides a possible solution
- limits a character's choices
- reveals competence or incompetence
- creates suspense
- creates misunderstanding
- changes the balance of power
- exposes institutional conflict
- creates a logistical obstacle
- produces an unintended consequence
- reveals information
- conceals information
- forces a strategic decision

Do not include technical detail merely to demonstrate expertise.

Where specialized concepts are necessary, make their dramatic
importance understandable through context.

Depending on the Institutional / Political Detail setting,
institutions may contain varying levels of:

- competing priorities
- imperfect information
- bureaucracy
- hierarchy
- political considerations
- resource limitations
- individual agendas


=========================================================
INFORMATION AND SUSPENSE
=========================================================

Track who knows what.

Characters should not possess information they have not reasonably
obtained.

Suspense may come from differences between:

- what the reader knows
- what the protagonist knows
- what opposing characters know
- what institutions believe
- what is actually true

Use withheld information carefully.

Mystery and surprise must remain consistent with previously
established facts.


=========================================================
OUTPUT REQUIREMENTS
=========================================================

Produce detailed Markdown containing:


# Story Premise

Use the CURRENT character names.

Explain the central situation through specific characters rather than
generic labels such as "a man" or "the protagonist" when those
characters have already been established.

The premise should reflect both the selected Writing Style Profile
and Detailed Writing Style Controls.


# Central Dramatic Question


# Themes


# Narrative Style Profile

Explain how the selected Writing Style Profile and detailed slider
settings will shape this specific novel.

Address:

- overall narrative feel
- dialogue style
- pacing philosophy
- technical-detail level
- institutional complexity
- moral complexity
- suspense approach
- description density
- violence treatment
- subtext
- information control


# Story World

Explain how:

- geography
- culture
- history
- economics
- institutions
- family history
- environment

place pressure on the characters.

Where appropriate, explain how physical geography affects:

- travel
- communication
- logistics
- surveillance
- security
- escape
- vulnerability
- strategic decisions


# Protagonist

Use the protagonist's CURRENT FULL NAME.

Include:

- external goal
- internal need
- primary flaw
- fear
- contradiction
- moral boundary
- emotional wound
- relevant history before the novel begins
- professional competence where relevant
- important blind spots
- information they currently possess
- important information they do not possess


# Antagonistic Force

Use established character names when applicable.

Explain:

- what they want
- why they want it
- what they believe they are protecting
- why they believe they are justified
- resources available to them
- constraints upon them
- what information they possess
- what they misunderstand
- how their objective conflicts with the protagonist


# Supporting Characters

Use the CURRENT Character Bible names.

Explain each person's dramatic function rather than merely listing them.

Where relevant, include:

- allegiance
- professional role
- personal objective
- conflicting loyalty
- useful knowledge
- knowledge gaps
- leverage
- vulnerability


# Primary Plot Engine

Explain how the selected Primary Plot operates across this specific novel.


# Secondary Plot Engine

If one is selected, explain how it intersects with the Primary Plot
rather than existing as an unrelated subplot.


# Character Arc

Explain how the selected Character Arc manifests through choices
and consequences.


# Relationship Arc

Explain how the selected Relationship Arc develops through specific
characters.


# Mystery Structure

If a Mystery Engine is selected, explain:

- underlying truth
- information withheld
- clues
- misdirection
- partial revelations
- major revelation

Do not reveal information to characters before they are supposed
to know it.


# Institutional and Strategic Pressure

Where relevant to the genre and Detailed Style Controls,
identify the major systems affecting the story.

These may include:

- government
- intelligence
- military
- police
- corporations
- organized crime
- courts
- media
- financial institutions
- communities
- political organizations
- families
- informal power networks

Explain:

- what each institution wants
- what resources it possesses
- what constraints it faces
- how its interests conflict with other groups
- how those conflicts affect individual characters


# Information Map

Identify major pieces of important information.

For each major piece of information explain:

- what is true
- who knows it
- who suspects it
- who misunderstands it
- who is deliberately hiding it
- when it should become known


# Three-Act Structure

## Act One

Establish:

- world
- important relationships
- existing pressures
- protagonist's life before disruption
- relevant institutions
- existing knowledge gaps
- inciting incident

Do not explain the entire story immediately.


## Act Two

Develop:

- escalating consequences
- moral compromise
- conflicting loyalties
- economic or institutional pressure
- relationship changes
- revelations
- setbacks
- opposing character logic
- technical or logistical obstacles where appropriate
- strategic decisions
- misinformation
- changing alliances
- accumulating consequences


## Act Three

Force decisive choices whose consequences arise from everything
established earlier.

Major solutions should emerge from previously established:

- character abilities
- relationships
- information
- resources
- geography
- technology
- institutional pressures
- earlier decisions

Avoid convenient solutions introduced only at the climax.


# Major Turning Points


# Character Arc Progression


# Relationship Progression


# Escalation Ladder

Explain how pressure increases across the novel.

Track escalation through combinations of:

- personal stakes
- relationship stakes
- physical danger
- institutional pressure
- political pressure
- financial pressure
- time pressure
- information loss or discovery
- logistical complications
- strategic reversals


# Ending

The ending should emerge from accumulated character decisions.

Avoid convenient coincidence.

Do not require complete emotional closure.

Where appropriate, victory should create a meaningful cost or
unresolved consequence.


# Chapter-by-Chapter Outline

For EVERY chapter include:

- chapter number
- working title
- POV character
- chapter objective
- important characters present
- central conflict
- major development
- relationship development
- information revealed
- information deliberately withheld
- technical or institutional element if relevant
- consequence created by the chapter
- approximate word target
- reason the reader continues

Use the CURRENT character names consistently.

The chapter sequence should reflect both the selected Writing Style
Profile and Detailed Writing Style Controls.


# Continuity Bible

List factual information future writing agents must not contradict,
including:

- current character names
- identities
- relationships
- chronology
- locations
- important objects
- injuries
- resources
- established technology
- institutional relationships
- secrets
- information each major character currently knows
- unresolved story obligations
"""

    return call_ai(
        STORY_ARCHITECT_PROMPT,
        user_prompt,
    )
# =========================================================
# WORLD BUILDER
# =========================================================

def generate_world_bible(
    book,
    story_architecture="",
    character_bible="",
):

    user_prompt = f"""
BOOK TITLE:
{book['title']}

PLOT:
{book['plot']}

SEVEN BASIC PLOT:
{book['plot_type']}

GENRE:
{book['genre']}

REGION:
{book['region']}

TIME PERIOD:
{book['period']}

TARGET WORD COUNT:
{book['word_count']:,}

USER-SUPPLIED CHARACTERS:
{book['characters']}

STORY ARCHITECTURE:
{story_architecture}

CHARACTER BIBLE:
{character_bible}
"""

    return call_ai(
        WORLD_BUILDER_PROMPT,
        user_prompt,
    )


# =========================================================
# TIMELINE ARCHITECT
# =========================================================

def generate_timeline(
    book,
    story_architecture="",
    character_bible="",
    world_bible="",
):

    user_prompt = f"""
BOOK TITLE:
{book['title']}

PLOT:
{book['plot']}

GENRE:
{book['genre']}

REGION:
{book['region']}

TIME PERIOD:
{book['period']}

STORY ARCHITECTURE:
{story_architecture}

CHARACTER BIBLE:
{character_bible}

WORLD BIBLE:
{world_bible}

Construct the timeline using all established information above.

Do not casually change established facts.

If the supplied material contains contradictions,
identify them under Continuity Risks rather than silently
choosing one version.
"""

    return call_ai(
        TIMELINE_ARCHITECT_PROMPT,
        user_prompt,
    )
# =========================================================
# CHAPTER PLANNER
# =========================================================

def generate_chapter_plan(
    book,
    chapter_number,
    story_architecture="",
    character_bible="",
    world_bible="",
    timeline="",
    previous_chapter_summaries="",
):

    writing_style_profile = book.get(
        "writing_style_profile",
        "Cinematic Technical Thriller",
    )

    style_dialogue = book.get(
        "style_dialogue",
        35,
    )

    style_technical_detail = book.get(
        "style_technical_detail",
        75,
    )

    style_pacing = book.get(
        "style_pacing",
        65,
    )

    style_moral_complexity = book.get(
        "style_moral_complexity",
        85,
    )

    style_description = book.get(
        "style_description",
        45,
    )

    style_violence = book.get(
        "style_violence",
        60,
    )

    style_institutional_detail = book.get(
        "style_institutional_detail",
        75,
    )

    style_subtext = book.get(
        "style_subtext",
        80,
    )


    # -----------------------------------------------------
    # STYLE INTERPRETATION HELPERS
    # -----------------------------------------------------

    def dialogue_guidance(value):

        if value <= 25:
            return (
                "Plan restrained dialogue scenes. Characters should often "
                "speak economically and avoid directly stating emotion."
            )

        elif value <= 50:
            return (
                "Plan controlled, natural dialogue with moderate emotional "
                "expression and selective directness."
            )

        elif value <= 75:
            return (
                "Allow more expressive and conversational exchanges while "
                "keeping dialogue character-specific."
            )

        else:
            return (
                "Plan highly expressive, energetic, emotionally open, "
                "and conversational dialogue where appropriate."
            )


    def technical_guidance(value):

        if value <= 25:
            return (
                "Keep technical and procedural material minimal. "
                "Only plan details required to understand the immediate conflict."
            )

        elif value <= 50:
            return (
                "Use moderate technical detail when it helps credibility, "
                "stakes, or practical constraints."
            )

        elif value <= 75:
            return (
                "Plan substantial technical, procedural, operational, "
                "and professional detail where it changes events."
            )

        else:
            return (
                "Plan extensive technically credible procedure, logistics, "
                "technology, systems, and professional decision-making "
                "while keeping dramatic purpose clear."
            )


    def pacing_guidance(value):

        if value <= 25:
            return (
                "Plan slow-burn pacing with room for atmosphere, observation, "
                "character pressure, and gradual escalation."
            )

        elif value <= 50:
            return (
                "Plan measured pacing with a balance between character "
                "development and forward movement."
            )

        elif value <= 75:
            return (
                "Plan relatively fast pacing with frequent meaningful "
                "developments while preserving scene depth."
            )

        else:
            return (
                "Plan aggressive forward momentum with rapid consequences, "
                "short transitions, and frequent changes in the story situation."
            )


    def moral_guidance(value):

        if value <= 25:
            return (
                "Keep moral positions relatively clear. Conflicts may have "
                "stronger distinctions between justified and unjustified actions."
            )

        elif value <= 50:
            return (
                "Use moderate moral complexity with understandable flaws "
                "and mixed motives."
            )

        elif value <= 75:
            return (
                "Plan strong moral ambiguity, conflicting legitimate goals, "
                "and difficult trade-offs."
            )

        else:
            return (
                "Plan very high moral complexity. Important choices should "
                "often create ethical costs even when characters have "
                "understandable motives."
            )


    def description_guidance(value):

        if value <= 25:
            return (
                "Plan sparse description. Focus primarily on action, dialogue, "
                "and selective concrete details."
            )

        elif value <= 50:
            return (
                "Plan controlled descriptive beats with selective sensory "
                "and environmental detail."
            )

        elif value <= 75:
            return (
                "Plan substantial descriptive opportunities where setting "
                "or atmosphere strengthens tension and characterization."
            )

        else:
            return (
                "Plan rich descriptive passages with strong sensory, "
                "environmental, and atmospheric presence."
            )


    def violence_guidance(value):

        if value <= 25:
            return (
                "Plan violence as restrained, brief, partially implied, "
                "or focused primarily on aftermath and consequence."
            )

        elif value <= 50:
            return (
                "Violence may occur directly but should avoid unnecessary "
                "physical detail."
            )

        elif value <= 75:
            return (
                "Plan realistic and direct violence when justified, including "
                "physical, practical, and emotional aftermath."
            )

        else:
            return (
                "Violence may be depicted in explicit physical detail when "
                "dramatically justified, with realistic consequences and aftermath."
            )


    def institutional_guidance(value):

        if value <= 25:
            return (
                "Keep institutions and political systems mostly in the background "
                "unless they are essential to the chapter conflict."
            )

        elif value <= 50:
            return (
                "Plan moderate institutional detail where organizations "
                "directly influence character choices."
            )

        elif value <= 75:
            return (
                "Plan meaningful institutional complexity, including hierarchy, "
                "bureaucracy, competing priorities, and organizational conflict."
            )

        else:
            return (
                "Plan extensive institutional and political detail, including "
                "chains of command, bureaucracy, competing agencies, internal "
                "agendas, resource limits, and power structures."
            )


    def subtext_guidance(value):

        if value <= 25:
            return (
                "Characters may communicate relatively directly. "
                "Important intentions should usually remain understandable."
            )

        elif value <= 50:
            return (
                "Plan moderate subtext. Characters may occasionally avoid "
                "saying exactly what they think or feel."
            )

        elif value <= 75:
            return (
                "Plan strong subtext using implication, silence, avoidance, "
                "and differences between surface statements and real intention."
            )

        else:
            return (
                "Plan very strong subtext. Important emotional or strategic "
                "meaning should frequently remain beneath explicit dialogue."
            )


    detailed_style_guidance = f"""
DIALOGUE STYLE: {style_dialogue}/100
{dialogue_guidance(style_dialogue)}

TECHNICAL DETAIL: {style_technical_detail}/100
{technical_guidance(style_technical_detail)}

PACING: {style_pacing}/100
{pacing_guidance(style_pacing)}

MORAL COMPLEXITY: {style_moral_complexity}/100
{moral_guidance(style_moral_complexity)}

DESCRIPTION DENSITY: {style_description}/100
{description_guidance(style_description)}

VIOLENCE TREATMENT: {style_violence}/100
{violence_guidance(style_violence)}

INSTITUTIONAL / POLITICAL DETAIL:
{style_institutional_detail}/100
{institutional_guidance(style_institutional_detail)}

SUBTEXT: {style_subtext}/100
{subtext_guidance(style_subtext)}
"""


    # -----------------------------------------------------
    # STYLE PROFILE GUIDANCE
    # -----------------------------------------------------

    style_guidance = {
        "Cinematic Technical Thriller": """
Plan the chapter as grounded cinematic thriller fiction.

Prioritize:

- clear scene objectives
- restrained emotional beats
- subtext-heavy dialogue opportunities
- credible professional behavior
- technical or institutional detail only where it affects events
- information gaps
- strategic choices
- logistical constraints
- moral ambiguity
- cause-and-effect escalation
- quiet human moments between pressure sequences
- consequences that carry into later chapters

Do not overload the chapter with exposition.
""",

        "Grounded Cinematic Drama": """
Plan the chapter around psychologically believable human conflict.

Prioritize:

- relationship pressure
- moral ambiguity
- restrained emotion
- subtext
- physical behavior
- meaningful setting
- family or personal history
- quiet dramatic beats
- imperfect choices
- lasting consequences

Avoid melodrama and over-explanation.
""",

        "Technical / Geopolitical Thriller": """
Plan the chapter around credible strategic and institutional pressure.

Prioritize:

- operational objectives
- chains of command
- intelligence gaps
- logistics
- technology
- surveillance or communications where relevant
- competing organizations
- strategic decisions
- misinformation
- credible procedures
- escalating threat
- consequences of incomplete information

Technical beats must advance conflict or suspense.
""",

        "Literary Crime": """
Plan the chapter around character, atmosphere, crime, and consequence.

Prioritize:

- flawed motivations
- moral ambiguity
- social or economic pressure
- guilt
- loyalty
- betrayal
- atmosphere
- subtext
- psychologically credible decisions
- consequences that persist

Avoid simplistic heroes and villains.
""",

        "Psychological Suspense": """
Plan the chapter around uncertainty and psychological pressure.

Prioritize:

- suspicion
- incomplete information
- hidden motives
- behavioral clues
- escalating anxiety
- relationship tension
- controlled revelation
- mistaken assumptions
- shifting interpretation

Twists must be supported by previously established evidence.
""",

        "Custom": """
Follow the established story material without imposing a predefined
style.

Prioritize strong continuity, believable motivation, clear scene
purpose, natural escalation, and meaningful consequences.
""",
    }

    selected_style_guidance = style_guidance.get(
        writing_style_profile,
        style_guidance["Cinematic Technical Thriller"],
    )


    user_prompt = f"""
=========================================================
BOOK INFORMATION
=========================================================

BOOK TITLE:
{book['title']}

PLOT:
{book['plot']}

GENRE:
{book['genre']}

REGION:
{book['region']}

TIME PERIOD:
{book['period']}

TARGET NOVEL LENGTH:
{book['word_count']:,} words

WRITING STYLE PROFILE:
{writing_style_profile}

CHAPTER TO PLAN:
Chapter {chapter_number}


=========================================================
SELECTED WRITING STYLE PROFILE
=========================================================

{selected_style_guidance}


=========================================================
DETAILED WRITING STYLE CONTROLS
=========================================================

{detailed_style_guidance}


=========================================================
STYLE CONTROL PRIORITY
=========================================================

The Writing Style Profile establishes the broad storytelling approach.

The Detailed Writing Style Controls fine-tune that profile.

If a detailed control conflicts with the default characteristics
of the selected profile, the detailed control takes priority.

For example:

If the profile normally favors substantial technical detail but
Technical Detail is set low, reduce technical content.

If the profile normally favors restrained dialogue but Dialogue Style
is set high, allow more expressive conversation.

Treat all eight slider values as deliberate creative decisions.


=========================================================
STYLE AUTHORITY
=========================================================

The selected Writing Style Profile and Detailed Style Controls
should influence HOW this chapter is planned.

They may influence:

- scene order
- pacing
- dialogue opportunities
- technical-detail level
- institutional pressure
- information control
- suspense
- emotional restraint
- description density
- violence and consequence
- strategic decision-making
- transitions
- chapter ending

They must NOT override established:

- plot events
- character identities
- relationships
- chronology
- world rules
- previous chapter facts
- Story Architecture

Do not imitate the distinctive voice of any living author.

Use only the high-level narrative characteristics supplied above.


=========================================================
STORY ARCHITECTURE
=========================================================

{story_architecture}


=========================================================
CHARACTER BIBLE
=========================================================

{character_bible}


=========================================================
WORLD BIBLE
=========================================================

{world_bible}


=========================================================
TIMELINE
=========================================================

{timeline}


=========================================================
PREVIOUS CHAPTER SUMMARIES
=========================================================

{previous_chapter_summaries}


=========================================================
PLANNING INSTRUCTIONS
=========================================================

Create the detailed plan for Chapter {chapter_number}.

If the Story Architecture already contains a chapter outline,
use that as the primary structural guide.

Do not silently rewrite the novel's established direction.

Maintain strict continuity with all supplied story material.

Characters must not know information they have not yet learned.

Each scene should have a clear dramatic function.

Where appropriate, build scenes around:

- character objective
- obstacle
- conflict
- decision
- consequence

Avoid scenes that exist only to explain information.


=========================================================
DIALOGUE AND SUBTEXT PLANNING
=========================================================

Use the Dialogue Style and Subtext sliders deliberately.

For each scene containing meaningful dialogue, consider:

- what each character wants from the exchange
- what each character is willing to say directly
- what each character avoids saying
- whether silence carries meaning
- whether one character misunderstands another
- whether information is deliberately withheld
- whether status, fear, loyalty, or power changes how they speak

Do not plan exposition in which characters explain information
both of them already know.

Dialogue scenes should create:

- conflict
- discovery
- relationship change
- strategic pressure
- deception
- emotional tension
- decision
- consequence

where appropriate.


=========================================================
INFORMATION CONTROL
=========================================================

Track important information carefully.

For this chapter identify:

- what the POV character knows
- what other important characters know
- what remains hidden
- what is suspected
- what is misunderstood
- what the reader may learn
- what must remain concealed

Do not reveal information early simply because it exists in the
Story Architecture or Character Bible.


=========================================================
TECHNICAL AND INSTITUTIONAL DETAIL
=========================================================

The amount of technical and institutional material must reflect
the detailed slider settings.

Possible technical or institutional elements include:

- police procedure
- military procedure
- intelligence activity
- government decisions
- corporate systems
- criminal organizations
- communications
- surveillance
- transportation
- weapons
- technology
- finance
- law
- medical realities
- logistics

Only include these elements where they affect:

- choices
- timing
- danger
- access
- knowledge
- resources
- strategy
- consequences

Do not add technical material purely for decoration.

At low settings, keep these elements simple and functional.

At high settings, plan credible procedural steps, hierarchy,
constraints, logistics, and consequences.


=========================================================
DESCRIPTION AND ENVIRONMENT
=========================================================

Use the Description Density setting to determine how much room
the plan should create for:

- physical environment
- sensory detail
- geography
- weather
- architecture
- objects
- clothing
- vehicles
- equipment
- atmosphere

Description should have dramatic purpose.

Where possible it should:

- affect movement
- influence mood
- create vulnerability
- create obstacles
- reveal character
- reinforce social or economic conditions
- establish practical realities

Do not plan description merely as decoration.


=========================================================
MORAL COMPLEXITY
=========================================================

Use the Moral Complexity setting when designing:

- character decisions
- competing objectives
- alliances
- betrayals
- compromises
- sacrifices
- consequences

At higher settings, avoid solutions where one side is entirely
correct and the other side is entirely irrational.

Characters may pursue legitimate goals that cannot all be satisfied.


=========================================================
VIOLENCE AND CONSEQUENCE
=========================================================

Use the Violence Treatment setting to determine how directly
violent scenes should be planned.

Regardless of intensity:

Violence should have consequences.

Consider:

- injuries
- fear
- trauma
- legal consequences
- professional consequences
- tactical consequences
- relationship consequences
- retaliation
- resource loss
- changes in future behavior

Do not use violence solely as visual spectacle.


=========================================================
SCENE CONSTRUCTION
=========================================================

Plan enough scene depth to support finished novel prose.

For each major scene, consider:

- POV character
- location
- immediate objective
- characters present
- conflict
- emotional pressure
- information entering the scene
- information leaving the scene
- technical or institutional pressure if relevant
- relationship change
- decision
- consequence
- transition into the next scene

Scenes should not simply repeat the same emotional or informational beat.


=========================================================
CHAPTER PACING
=========================================================

Use the Pacing slider deliberately.

Low pacing values should allow:

- longer scenes
- greater observation
- atmosphere
- gradual pressure
- quiet character moments
- slower information release

High pacing values should favor:

- shorter delays between developments
- stronger scene objectives
- rapid consequences
- tighter transitions
- increased time pressure
- frequent changes in the tactical or emotional situation

Fast pacing must not eliminate important character logic.

Slow pacing must not become inactivity.


=========================================================
CHAPTER ESCALATION
=========================================================

The chapter should create measurable movement.

Possible escalation may include:

- increased personal risk
- increased relationship pressure
- new information
- loss of information
- institutional pressure
- strategic setbacks
- logistical complications
- moral compromise
- narrowing options
- changing alliances
- physical danger
- time pressure

The chapter should leave the story in a meaningfully different
state than it began.


=========================================================
CHAPTER ENDING
=========================================================

Plan an ending that naturally creates forward momentum.

The ending may involve:

- a decision
- consequence
- revelation
- threat
- changed relationship
- new objective
- strategic setback
- unanswered question
- irreversible action

Avoid arbitrary cliffhangers.


=========================================================
OUTPUT REQUIREMENTS
=========================================================

Produce detailed Markdown containing:

# Chapter Number

Chapter {chapter_number}


# Working Title


# Approximate Word Target


# Writing Style Profile

State the selected profile.

Then briefly explain how the eight detailed style controls should
affect this specific chapter.


# Point of View


# Opening Situation


# Chapter Purpose


# Characters Present


# Character Objectives

Explain what each important character wants during this chapter.


# Main Conflict


# Scene Plan

For each scene include:

## Scene 1

- Location
- POV
- Characters Present
- Immediate Objective
- Conflict
- Important Action
- Dialogue / Subtext Opportunity
- Information Revealed
- Information Withheld
- Technical or Institutional Element
- Description / Environmental Opportunity
- Moral or Strategic Pressure
- Relationship Development
- Violence / Consequence if relevant
- Decision
- Consequence
- Transition

Continue this format for every planned scene.


# Information Map

List:

- information known at chapter start
- new information learned
- information misunderstood
- information deliberately concealed
- information that must remain unknown


# Technical / Institutional Requirements

List any details future writing agents should portray accurately.

The amount of detail should reflect the Technical Detail and
Institutional / Political Detail settings.

If none are relevant, state that clearly.


# Dialogue and Subtext Requirements

Explain:

- how restrained or expressive dialogue should be
- where important subtext should occur
- what characters should avoid saying directly
- any important conversational power dynamics


# Description Requirements

Explain how much environmental and sensory description the
Chapter Writer should use based on the Description Density setting.


# Moral Complexity Requirements

Identify any difficult trade-offs, conflicting legitimate motives,
or ethical costs that should shape the chapter.


# Violence Treatment

If violence occurs, explain how directly it should be portrayed
and what consequences must remain afterward.

If no violence occurs, state that clearly.


# Character Development

Explain the character movement produced by this chapter.


# Relationship Development


# Pacing and Tension

Explain how pressure should rise and fall through the chapter.

The plan must reflect the selected Pacing slider value.


# Chapter Ending

Describe the intended final dramatic beat.


# Reason the Reader Continues


# Continuity Requirements

List facts the Chapter Writer must not contradict.

If there is a contradiction between supplied sources, identify it here
rather than silently choosing a new version.


# Chapter Writer Authority

The Chapter Writer must treat this plan as authoritative.

It may develop prose, dialogue, physical action, description, and
scene texture, but it must not casually replace the chapter's:

- objective
- key events
- revelations
- continuity
- character identities
- established relationships
- intended ending
- writing-style requirements
"""

    return call_ai(
        CHAPTER_PLANNER_PROMPT,
        user_prompt,
    )
# =========================================================
# CHAPTER WRITER
# =========================================================

def extract_chapter_word_target(
    chapter_plan,
    default_target=3000,
):
    """
    Extract the requested chapter word target from the
    Chapter Planner output.
    """

    import re

    if not chapter_plan:
        return default_target

    patterns = [
        r"Approximate Word Target[^0-9]*([\d,]+)",
        r"Word Target[^0-9]*([\d,]+)",
        r"Target Word Count[^0-9]*([\d,]+)",
        r"approximately\s+([\d,]+)\s+words",
        r"([\d,]+)\s+words",
    ]

    for pattern in patterns:

        match = re.search(
            pattern,
            chapter_plan,
            re.IGNORECASE,
        )

        if match:

            try:

                target = int(
                    match.group(1).replace(
                        ",",
                        "",
                    )
                )

                if 500 <= target <= 10000:
                    return target

            except ValueError:
                pass

    return default_target


# =========================================================
# CHAPTER PART WRITER
# =========================================================

def generate_chapter_part(
    book,
    chapter_number,
    chapter_plan,
    story_architecture,
    character_bible,
    world_bible,
    timeline,
    previous_chapter_summaries,
    previous_generated_text,
    part_number,
    total_parts,
    part_word_target,
):

    if not client:
        raise RuntimeError(
            "No OpenAI API key was found."
        )

    if not model_name:
        raise RuntimeError(
            "No OpenAI model has been configured."
        )

    minimum_part_words = int(
        part_word_target * 0.85
    )

    maximum_part_words = int(
        part_word_target * 1.15
    )

    writing_style_profile = book.get(
        "writing_style_profile",
        "Cinematic Technical Thriller",
    )

    style_dialogue = book.get(
        "style_dialogue",
        35,
    )

    style_technical_detail = book.get(
        "style_technical_detail",
        75,
    )

    style_pacing = book.get(
        "style_pacing",
        65,
    )

    style_moral_complexity = book.get(
        "style_moral_complexity",
        85,
    )

    style_description = book.get(
        "style_description",
        45,
    )

    style_violence = book.get(
        "style_violence",
        60,
    )

    style_institutional_detail = book.get(
        "style_institutional_detail",
        75,
    )

    style_subtext = book.get(
        "style_subtext",
        80,
    )


    # -----------------------------------------------------
    # STYLE INTERPRETATION HELPERS
    # -----------------------------------------------------

    def dialogue_guidance(value):

        if value <= 25:
            return (
                "Use highly restrained dialogue. Characters should speak "
                "economically and often avoid directly stating emotion."
            )

        elif value <= 50:
            return (
                "Use controlled, natural dialogue with moderate emotional "
                "expression."
            )

        elif value <= 75:
            return (
                "Use more expressive and conversational dialogue while "
                "keeping speech character-specific."
            )

        else:
            return (
                "Use highly expressive, energetic, emotionally open, "
                "and conversational dialogue where appropriate."
            )


    def technical_guidance(value):

        if value <= 25:
            return (
                "Use very little technical or procedural detail. Include only "
                "what the reader needs to understand the immediate situation."
            )

        elif value <= 50:
            return (
                "Use moderate technical detail when it supports credibility, "
                "stakes, or practical constraints."
            )

        elif value <= 75:
            return (
                "Use substantial technical, procedural, operational, and "
                "professional detail where it directly affects the scene."
            )

        else:
            return (
                "Use extensive technically credible detail involving procedure, "
                "logistics, systems, technology, and professional decision-making, "
                "while keeping it understandable."
            )


    def pacing_guidance(value):

        if value <= 25:
            return (
                "Use slow-burn pacing. Allow scenes room for observation, "
                "atmosphere, hesitation, character tension, and gradual escalation."
            )

        elif value <= 50:
            return (
                "Use measured pacing with a balance between character development "
                "and forward plot movement."
            )

        elif value <= 75:
            return (
                "Use relatively fast pacing with frequent meaningful developments "
                "while preserving scene depth."
            )

        else:
            return (
                "Use aggressive forward momentum, short delays between "
                "consequences, tight transitions, and frequent changes "
                "in the situation."
            )


    def moral_guidance(value):

        if value <= 25:
            return (
                "Allow relatively clear moral positions, with stronger distinctions "
                "between justified and unjustified behavior."
            )

        elif value <= 50:
            return (
                "Use moderate moral complexity with understandable flaws "
                "and mixed motives."
            )

        elif value <= 75:
            return (
                "Use strong moral ambiguity, competing legitimate motives, "
                "and difficult trade-offs."
            )

        else:
            return (
                "Use very high moral complexity. Important choices should often "
                "carry ethical costs, even when characters have understandable motives."
            )


    def description_guidance(value):

        if value <= 25:
            return (
                "Keep description sparse and functional. Favor action, dialogue, "
                "and selective concrete details."
            )

        elif value <= 50:
            return (
                "Use controlled description with selective sensory and "
                "environmental detail."
            )

        elif value <= 75:
            return (
                "Use substantial descriptive detail where setting, atmosphere, "
                "or physical environment strengthens the scene."
            )

        else:
            return (
                "Use rich descriptive prose with strong sensory, environmental, "
                "and atmospheric presence."
            )


    def violence_guidance(value):

        if value <= 25:
            return (
                "Keep violence restrained, brief, partially implied, or focused "
                "primarily on aftermath and consequence."
            )

        elif value <= 50:
            return (
                "Violence may be shown directly but without unnecessary "
                "graphic physical detail."
            )

        elif value <= 75:
            return (
                "Violence may be portrayed realistically and directly, including "
                "physical, practical, and emotional aftermath."
            )

        else:
            return (
                "Violence may be depicted in explicit physical detail when "
                "dramatically justified, while preserving realistic aftermath "
                "and consequences."
            )


    def institutional_guidance(value):

        if value <= 25:
            return (
                "Keep institutional and political systems mostly in the background "
                "unless essential to the immediate conflict."
            )

        elif value <= 50:
            return (
                "Use moderate institutional detail where organizations directly "
                "influence character decisions."
            )

        elif value <= 75:
            return (
                "Use meaningful institutional complexity including hierarchy, "
                "bureaucracy, competing priorities, and organizational conflict."
            )

        else:
            return (
                "Use extensive institutional and political detail including "
                "chains of command, competing organizations, bureaucracy, "
                "internal agendas, resource limits, and power structures."
            )


    def subtext_guidance(value):

        if value <= 25:
            return (
                "Characters may communicate relatively directly. Important "
                "intentions should generally remain clear."
            )

        elif value <= 50:
            return (
                "Use moderate subtext. Characters may sometimes avoid saying "
                "exactly what they think or feel."
            )

        elif value <= 75:
            return (
                "Use strong subtext through implication, silence, avoidance, "
                "misdirection, interruption, and hidden intention."
            )

        else:
            return (
                "Use very strong subtext. Important emotional and strategic "
                "meaning should frequently remain beneath explicit dialogue."
            )


    detailed_style_guidance = f"""
DIALOGUE STYLE: {style_dialogue}/100
{dialogue_guidance(style_dialogue)}

TECHNICAL DETAIL: {style_technical_detail}/100
{technical_guidance(style_technical_detail)}

PACING: {style_pacing}/100
{pacing_guidance(style_pacing)}

MORAL COMPLEXITY: {style_moral_complexity}/100
{moral_guidance(style_moral_complexity)}

DESCRIPTION DENSITY: {style_description}/100
{description_guidance(style_description)}

VIOLENCE TREATMENT: {style_violence}/100
{violence_guidance(style_violence)}

INSTITUTIONAL / POLITICAL DETAIL:
{style_institutional_detail}/100
{institutional_guidance(style_institutional_detail)}

SUBTEXT: {style_subtext}/100
{subtext_guidance(style_subtext)}
"""


    # -----------------------------------------------------
    # PROFILE GUIDANCE
    # -----------------------------------------------------

    style_guidance = {
        "Cinematic Technical Thriller": """
Write with a grounded cinematic thriller approach.

Prioritize:

- strong visual scene construction
- restrained emotional expression
- dialogue driven by subtext
- morally complicated characters
- credible professional behavior
- technical details only when they affect choices or danger
- realistic institutional pressure
- believable chains of command
- incomplete information
- strategic decision-making
- geography and logistics affecting events
- escalating cause and effect
- quiet human moments between high-pressure scenes
- physical behavior revealing emotion
- consequential violence
- tension created through what characters know and do not know

Technical material must remain understandable to a general reader.

Do not overload scenes with exposition.

Human conflict must remain more important than technical detail.
""",

        "Grounded Cinematic Drama": """
Write with a grounded cinematic dramatic approach.

Prioritize:

- psychologically believable behavior
- restrained dialogue
- subtext
- moral ambiguity
- family and relationship tension
- physical action carrying emotion
- strong sense of place
- economic and social pressure
- silence and hesitation
- imperfect choices
- quiet scenes with dramatic weight
- meaningful consequences
- emotionally credible conflict

Avoid melodrama and excessive explanation.
""",

        "Technical / Geopolitical Thriller": """
Write as a technically credible geopolitical thriller.

Prioritize:

- realistic institutions
- government, intelligence, military, police, corporate,
  or criminal systems where relevant
- strategy
- logistics
- technology
- surveillance
- communications
- competing organizations
- chains of command
- operational planning
- incomplete intelligence
- misinformation
- professional competence
- procedural realism
- escalating threats
- believable consequences

Technical detail should create suspense or constrain choices.

Do not turn scenes into lectures or manuals.
""",

        "Literary Crime": """
Write with a literary crime approach.

Prioritize:

- flawed characters
- moral ambiguity
- atmosphere
- social and economic pressure
- psychologically credible crime
- guilt
- loyalty
- betrayal
- restrained exposition
- subtext
- consequence
- strong setting
- ambiguity where dramatically appropriate

Avoid simplistic heroes, villains, or moral lessons.
""",

        "Psychological Suspense": """
Write with a psychological suspense approach.

Prioritize:

- uncertainty
- incomplete information
- suspicion
- shifting interpretation
- internal pressure
- hidden motives
- behavioral clues
- relationship tension
- controlled revelation
- psychological manipulation where appropriate
- escalating fear
- unreliable assumptions

Do not manufacture twists without prior support.
""",

        "Custom": """
Follow the existing Chapter Plan, Story Architecture,
Character Bible, World Bible, Timeline, and genre.

Use grounded professional-quality prose with:

- believable motivation
- strong continuity
- clear cause and effect
- natural dialogue
- controlled exposition
- meaningful scene progression
""",
    }

    selected_style_guidance = style_guidance.get(
        writing_style_profile,
        style_guidance["Cinematic Technical Thriller"],
    )


    user_prompt = f"""
=========================================================
NOVEL INFORMATION
=========================================================

TITLE:
{book['title']}

GENRE:
{book['genre']}

REGION:
{book['region']}

TIME PERIOD:
{book['period']}

WRITING STYLE PROFILE:
{writing_style_profile}


=========================================================
SELECTED WRITING STYLE PROFILE
=========================================================

{selected_style_guidance}


=========================================================
DETAILED WRITING STYLE CONTROLS
=========================================================

{detailed_style_guidance}


=========================================================
STYLE CONTROL PRIORITY
=========================================================

The Writing Style Profile establishes the broad storytelling approach.

The Detailed Writing Style Controls fine-tune how the actual prose
must be written.

If a detailed control conflicts with a default characteristic of the
selected profile, the detailed control takes priority.

For example:

- A low Dialogue Style setting requires more restrained dialogue.
- A high Dialogue Style setting allows more expressive conversation.
- A low Technical Detail setting requires lighter procedural explanation.
- A high Technical Detail setting allows deeper technical realism.
- A low Pacing setting permits slower scene development.
- A high Pacing setting requires stronger forward momentum.
- Moral Complexity controls ethical ambiguity and competing motives.
- Description Density controls how much sensory and environmental prose appears.
- Violence Treatment controls how directly violence is portrayed.
- Institutional / Political Detail controls organizational complexity.
- Subtext controls how much meaning remains beneath explicit dialogue.

Treat all eight values as intentional creative decisions.


=========================================================
STYLE AUTHORITY
=========================================================

The selected Writing Style Profile and Detailed Style Controls
control HOW the prose is written.

They should influence:

- dialogue
- pacing
- sentence rhythm
- paragraph rhythm
- description
- scene depth
- technical detail
- suspense
- information control
- institutional realism
- emotional restraint
- moral complexity
- action
- violence
- consequences
- transitions

They must NOT override:

- Chapter Plan
- Story Architecture
- Character Bible
- World Bible
- Timeline
- established relationships
- established chronology
- existing character knowledge

Do not imitate the distinctive prose or voice of any living author.

Create an original narrative voice using only the high-level
storytelling characteristics described above.


=========================================================
CHAPTER INFORMATION
=========================================================

CHAPTER:
{chapter_number}

YOU ARE WRITING:
Part {part_number} of {total_parts}

TARGET LENGTH FOR THIS PART:
Approximately {part_word_target:,} words

ACCEPTABLE RANGE:
{minimum_part_words:,} to {maximum_part_words:,} words


=========================================================
FULL CHAPTER PLAN
=========================================================

{chapter_plan}


=========================================================
STORY ARCHITECTURE
=========================================================

{story_architecture}


=========================================================
CHARACTER BIBLE
=========================================================

{character_bible}


=========================================================
WORLD BIBLE
=========================================================

{world_bible}


=========================================================
TIMELINE
=========================================================

{timeline}


=========================================================
PREVIOUS CHAPTER SUMMARIES
=========================================================

{previous_chapter_summaries}


=========================================================
TEXT ALREADY WRITTEN FOR THIS CHAPTER
=========================================================

{previous_generated_text}


=========================================================
YOUR TASK
=========================================================

Write Part {part_number} of {total_parts} of Chapter {chapter_number}.

This is NOT a summary.

This is finished novel prose.

The entire chapter will be assembled from multiple parts.

Each part must move naturally into the next.

Write approximately {part_word_target:,} words for THIS PART.

Do not attempt to finish the whole chapter early.

Follow the Chapter Plan in order.

Distribute the planned scenes sensibly across the
{total_parts} parts.


=========================================================
CHARACTER NAME USAGE
=========================================================

When an established character first appears in the chapter,
their full name may be used where natural.

After introduction, narration should normally use the
character's first name.

Use surnames, ranks, titles, or formal names only where naturally
appropriate, such as:

- professional settings
- military or police environments
- formal address
- dialogue
- deliberate emotional distance
- situations where multiple characters share a first name

Do not repeatedly reintroduce established characters by full name.


=========================================================
DIALOGUE STYLE
=========================================================

Apply the Dialogue Style setting directly to the finished prose.

At restrained settings:

- use shorter exchanges
- allow silence
- allow unfinished thoughts
- rely more heavily on behavior
- avoid emotional explanation

At expressive settings:

- allow longer conversations
- allow stronger emotional expression
- allow greater conversational energy
- allow characters to verbalize more of their thinking

Regardless of setting:

Dialogue must sound specific to each character.

Characters should have:

- individual histories
- professional backgrounds
- different goals
- different vocabulary
- different levels of knowledge
- different emotional pressures

Avoid dialogue whose only purpose is explaining information both
speakers already know.


=========================================================
SUBTEXT
=========================================================

Apply the Subtext setting independently from Dialogue Style.

High subtext does NOT simply mean less dialogue.

It means the literal words and the actual intention may differ.

Subtext may appear through:

- implication
- interruption
- avoidance
- silence
- hesitation
- strategic politeness
- sarcasm
- misdirection
- changed subjects
- questions that are not answered
- physical behavior
- what a character refuses to acknowledge

At low settings, allow characters to communicate more directly.

Do not make dialogue confusing merely to create subtext.


=========================================================
TECHNICAL DETAIL
=========================================================

Apply the Technical Detail setting directly.

Technical or professional information may appear through:

- action
- decisions
- dialogue
- observation
- consequences
- constraints
- mistakes
- problem-solving

Technical information should matter to the scene.

Good technical detail may:

- create or solve a problem
- reveal competence
- reveal incompetence
- limit options
- increase danger
- explain why a decision matters
- affect timing
- affect logistics
- alter the balance of power

At low settings, compress or simplify technical explanation.

At high settings, include more procedural steps, realistic terminology,
professional logic, equipment limitations, logistics, and operational detail.

Never turn the novel into a textbook or manual.


=========================================================
INSTITUTIONAL AND POLITICAL DETAIL
=========================================================

Apply the Institutional / Political Detail setting directly.

Depending on the setting, portray appropriate levels of:

- hierarchy
- chains of command
- organizational procedure
- jurisdiction
- bureaucracy
- competing agencies
- legal constraints
- political pressure
- corporate interests
- internal agendas
- resource limitations
- institutional rivalry

At low settings, keep these systems mostly in the background.

At high settings, allow them to become active sources of conflict,
delay, leverage, misunderstanding, and strategic pressure.

Do not explain institutions merely for worldbuilding.

They should affect what characters can actually do.


=========================================================
INFORMATION CONTROL
=========================================================

Maintain strict knowledge boundaries.

A character may only act on information they have reasonably learned.

Track differences between:

- what the reader knows
- what the POV character knows
- what allies know
- what opponents know
- what institutions believe
- what is actually true

Do not accidentally reveal secrets early.

Do not allow narration to casually disclose information the selected
POV would not reasonably perceive unless the established POV approach
permits it.


=========================================================
MORAL COMPLEXITY
=========================================================

Apply the Moral Complexity setting to character decisions.

At lower settings:

- motivations may be clearer
- ethical positions may be easier to distinguish
- opposition may be more clearly unjustified

At higher settings:

- competing characters may both have legitimate concerns
- choices may solve one problem while creating another
- loyalty may conflict with duty
- law may conflict with justice
- professional responsibility may conflict with personal obligation
- survival may require compromise
- victories may create ethical costs

Do not manufacture ambiguity by making characters behave irrationally.

Moral complexity should arise from believable conflicting interests.


=========================================================
DESCRIPTION DENSITY
=========================================================

Apply the Description Density setting directly to prose.

At low settings:

- use selective concrete details
- keep environmental description concise
- prioritize action and dialogue

At moderate settings:

- use enough sensory and environmental detail to establish place,
  mood, and physical reality

At high settings:

- allow richer sensory passages
- stronger atmosphere
- more environmental observation
- more detailed geography
- greater attention to physical objects, weather, architecture,
  clothing, machinery, vehicles, and surroundings

Description should still have dramatic purpose.

Where possible, setting should affect:

- movement
- visibility
- vulnerability
- mood
- distance
- sound
- access
- communication
- tactics
- character behavior


=========================================================
PACING
=========================================================

Apply the Pacing setting to:

- scene length
- paragraph rhythm
- transition speed
- frequency of new developments
- amount of reflection
- information release
- delay between decision and consequence

At low pacing settings:

- permit longer scenes
- allow observation
- allow atmosphere
- allow emotional processing
- allow gradual pressure
- allow slower revelation

At high pacing settings:

- tighten scene objectives
- reduce unnecessary pauses
- shorten delays between consequences
- use stronger transitions
- increase time pressure
- increase meaningful developments

Fast pacing must not become shallow.

Slow pacing must not become inactivity.


=========================================================
SCENE DEPTH
=========================================================

Develop scenes fully through:

- physical action
- dialogue
- subtext
- character reactions
- observation
- setting
- movement
- conflict
- hesitation
- choices
- consequences
- relationship tension
- environmental pressure

Use setting as an active part of the scene where appropriate.

Geography, weather, buildings, transportation, distance,
visibility, communications, and access may affect what characters
can realistically do.

Do not rush from plot point to plot point.

Do not use filler simply to reach the word target.


=========================================================
ACTION AND VIOLENCE
=========================================================

Apply the Violence Treatment setting directly.

When action or violence occurs:

- preserve physical cause and effect
- respect geography and timing
- respect established character abilities
- avoid effortless competence unless justified
- allow mistakes
- allow confusion
- allow incomplete information
- show practical consequences afterward

Violence may affect:

- bodies
- relationships
- decisions
- institutions
- investigations
- resources
- future behavior

At low Violence Treatment settings:

- emphasize implication
- shorten physical description
- focus on shock, danger, and aftermath

At high settings:

- allow more direct physical detail
- portray realistic mechanics of injury where dramatically relevant
- retain emotional and practical consequences

Do not treat violence as consequence-free spectacle.


=========================================================
SENTENCE AND PARAGRAPH RHYTHM
=========================================================

Sentence rhythm should respond to the scene rather than remain uniform.

During:

- danger
- pursuit
- confrontation
- rapid decisions

use tighter syntax where appropriate.

During:

- observation
- reflection
- atmosphere
- complicated emotional moments

allow longer sentence structures where appropriate.

Avoid monotonous sentence length.

Avoid repetitive paragraph openings.

Avoid excessive fragments.

Avoid artificial dramatic fragments used only to make prose appear intense.


=========================================================
COMMON AI WRITING PROBLEMS TO AVOID
=========================================================

Avoid:

- explaining emotions immediately after showing them
- repeated rhetorical questions
- repeated sentence structures
- unnecessary character-name repetition
- constant references to breathing, heartbeats, jaws, fists, or eyes
- excessive adjectives
- excessive adverbs
- generic sensory description
- melodramatic internal monologue
- artificial cliffhanger sentences
- overly polished dialogue where every line sounds quotable
- exposition disguised as conversation
- characters summarizing what just happened
- stating the obvious
- repetitive reminders of stakes already established
- repetitive atmospheric descriptions
- generic phrases that could belong in any novel

Prefer specific observation, concrete behavior, character-specific
thinking, and credible cause and effect.


=========================================================
CONTINUITY
=========================================================

Maintain strict continuity with:

- Character Bible
- Story Architecture
- World Bible
- Timeline
- Chapter Plan
- previous chapter summaries
- chapter prose already written

Characters must not know information they have not learned.

Preserve:

- names
- family relationships
- ages
- occupations
- injuries
- chronology
- geography
- possessions
- secrets
- unresolved plot threads
- institutional relationships
- established technology
- established resources


=========================================================
CONTINUATION RULE
=========================================================

The section called TEXT ALREADY WRITTEN contains the prose
that precedes this part.

Continue naturally from it.

Do NOT:

- repeat earlier scenes
- restart the chapter
- repeat introductions
- retell previous dialogue
- summarize material already written
- contradict previous prose

If previous text ends during a scene, continue that scene naturally.

Maintain the same narrative voice and style-control settings
across every part of the chapter.


=========================================================
PART ENDING RULE
=========================================================

If Part {part_number} is NOT the final part:

End at a natural transition point.

Do NOT create an artificial chapter ending.

Do NOT write:

"To be continued."

Do NOT add a heading for the next part.


If Part {part_number} IS the final part:

Complete the remaining Chapter Plan.

End at the intended dramatic ending for Chapter
{chapter_number}.


=========================================================
OUTPUT
=========================================================

Return ONLY finished novel prose.

Do not include:

- Part numbers
- analysis
- notes
- word counts
- explanations
- commentary
"""

    max_output_tokens = int(
        part_word_target * 2.5
    )

    max_output_tokens = max(
        max_output_tokens,
        2500,
    )

    response = client.responses.create(
        model=model_name,
        instructions=CHAPTER_WRITER_PROMPT,
        input=user_prompt,
        max_output_tokens=max_output_tokens,
    )

    return response.output_text.strip()
# =========================================================
# COMPLETE MULTI-PASS CHAPTER WRITER
# =========================================================

def generate_chapter_draft(
    book,
    chapter_number,
    chapter_plan,
    story_architecture="",
    character_bible="",
    world_bible="",
    timeline="",
    previous_chapter_summaries="",
):

    if not chapter_plan.strip():

        raise ValueError(
            "A chapter plan is required before "
            "writing the chapter."
        )

    # -----------------------------------------------------
    # TARGET WORD COUNT
    # -----------------------------------------------------

    target_words = (
        extract_chapter_word_target(
            chapter_plan
        )
    )

    # -----------------------------------------------------
    # DECIDE NUMBER OF WRITING PASSES
    # -----------------------------------------------------

    if target_words <= 1500:

        total_parts = 2

    elif target_words <= 3000:

        total_parts = 3

    elif target_words <= 4500:

        total_parts = 4

    elif target_words <= 6000:

        total_parts = 5

    else:

        total_parts = 6

    part_word_target = int(
        target_words / total_parts
    )

    # -----------------------------------------------------
    # WRITE CHAPTER IN PARTS
    # -----------------------------------------------------

    generated_parts = []

    for part_number in range(
        1,
        total_parts + 1,
    ):

        # Only pass a reasonable amount of the already
        # generated chapter back to the model.
        #
        # This preserves continuity without making every
        # later request unnecessarily enormous.

        combined_so_far = "\n\n".join(
            generated_parts
        )

        if len(combined_so_far) > 12000:

            previous_generated_text = (
                combined_so_far[-12000:]
            )

        else:

            previous_generated_text = (
                combined_so_far
            )

        part = generate_chapter_part(
            book=book,
            chapter_number=chapter_number,
            chapter_plan=chapter_plan,
            story_architecture=(
                story_architecture
            ),
            character_bible=(
                character_bible
            ),
            world_bible=(
                world_bible
            ),
            timeline=(
                timeline
            ),
            previous_chapter_summaries=(
                previous_chapter_summaries
            ),
            previous_generated_text=(
                previous_generated_text
            ),
            part_number=(
                part_number
            ),
            total_parts=(
                total_parts
            ),
            part_word_target=(
                part_word_target
            ),
        )

        generated_parts.append(
            part
        )

    # -----------------------------------------------------
    # COMBINE PARTS
    # -----------------------------------------------------

    complete_chapter = "\n\n".join(
        generated_parts
    )

    return complete_chapter

# =========================================================
# EDITOR ANALYST
# =========================================================

import re


def _force_editor_verdict(editor_report):
    """
    Deterministically corrects the AI's final editor verdict.

    The AI still performs the editorial analysis, but Python makes
    the final decision based on the severities the AI itself reported.

    This prevents endless Standard Edit / Light Polish loops.
    """

    if not editor_report:
        return editor_report

    report_upper = editor_report.upper()

    # -----------------------------------------------------
    # Extract Priority Revisions section only
    # -----------------------------------------------------

    priority_match = re.search(
        r"##\s*PRIORITY REVISIONS(.*?)(?=##\s*OPTIONAL IMPROVEMENTS|##\s*EDITOR VERDICT|\Z)",
        editor_report,
        flags=re.IGNORECASE | re.DOTALL,
    )

    priority_section = (
        priority_match.group(1)
        if priority_match
        else ""
    )

    priority_upper = priority_section.upper()

    # -----------------------------------------------------
    # Count issue severities
    # -----------------------------------------------------

    critical_count = len(
        re.findall(
            r"SEVERITY:\s*\**CRITICAL",
            priority_upper,
        )
    )

    major_count = len(
        re.findall(
            r"SEVERITY:\s*\**MAJOR",
            priority_upper,
        )
    )

    moderate_count = len(
        re.findall(
            r"SEVERITY:\s*\**MODERATE",
            priority_upper,
        )
    )

    minor_count = len(
        re.findall(
            r"SEVERITY:\s*\**MINOR",
            priority_upper,
        )
    )

    # -----------------------------------------------------
    # Detect genuine continuity problems
    # -----------------------------------------------------

    continuity_match = re.search(
        r"##\s*CONTINUITY FINDINGS(.*?)(?=##\s*CHARACTER FINDINGS|\Z)",
        editor_report,
        flags=re.IGNORECASE | re.DOTALL,
    )

    continuity_section = (
        continuity_match.group(1).strip()
        if continuity_match
        else ""
    )

    continuity_upper = continuity_section.upper()

    continuity_is_sound = any(
        phrase in continuity_upper
        for phrase in [
            "NO SIGNIFICANT CONTINUITY CONFLICTS DETECTED",
            "NO CONTINUITY CONFLICTS DETECTED",
            "NO SIGNIFICANT CONTINUITY ISSUES",
            "NO CONTINUITY ISSUES",
        ]
    )

    # -----------------------------------------------------
    # Determine verdict in Python
    # -----------------------------------------------------

    if not continuity_is_sound:
        continuity_problem_words = [
            "CONTRADICTION",
            "CONFLICT",
            "INCONSISTENCY",
            "TIMELINE ERROR",
            "IMPOSSIBLE",
            "VIOLATES",
        ]

        genuine_continuity_problem = any(
            word in continuity_upper
            for word in continuity_problem_words
        )

        if genuine_continuity_problem:
            forced_verdict = "CONTINUITY REPAIR REQUIRED"
            forced_reason = (
                "The analysis identified a genuine continuity conflict "
                "that should be repaired before normal editing continues."
            )

        elif critical_count > 0:
            forced_verdict = "NEEDS DEEP EDIT"
            forced_reason = (
                "The analysis identified at least one Critical issue "
                "requiring substantial reconstruction."
            )

        elif major_count >= 2:
            forced_verdict = "NEEDS DEEP EDIT"
            forced_reason = (
                "The analysis identified multiple Major issues requiring "
                "substantial chapter reconstruction."
            )

        elif major_count == 1:
            forced_verdict = "NEEDS STANDARD EDIT"
            forced_reason = (
                "The analysis identified a Major issue requiring meaningful "
                "rewriting beyond a light polish."
            )

        elif moderate_count > 0:
            forced_verdict = "READY FOR LIGHT POLISH"
            forced_reason = (
                "The chapter is structurally sound, but the analysis identified "
                "localized Moderate issues that can be improved with a Light Polish."
            )

        else:
            forced_verdict = "EDITING COMPLETE"
            forced_reason = (
                "The chapter has no Critical, Major, or Moderate revision issues. "
                "Any remaining concerns are Minor or optional, so further editing "
                "would likely produce only marginal changes."
            )

    else:

        if critical_count > 0:
            forced_verdict = "NEEDS DEEP EDIT"
            forced_reason = (
                "The analysis identified at least one Critical issue requiring "
                "substantial reconstruction."
            )

        elif major_count >= 2:
            forced_verdict = "NEEDS DEEP EDIT"
            forced_reason = (
                "The analysis identified multiple Major issues requiring "
                "substantial reconstruction."
            )

        elif major_count == 1:
            forced_verdict = "NEEDS STANDARD EDIT"
            forced_reason = (
                "The analysis identified a Major issue requiring meaningful "
                "rewriting beyond a Light Polish."
            )

        elif moderate_count > 0:
            forced_verdict = "READY FOR LIGHT POLISH"
            forced_reason = (
                "The chapter is structurally sound, but localized Moderate "
                "issues remain that are appropriate for Light Polish."
            )

        else:
            forced_verdict = "EDITING COMPLETE"
            forced_reason = (
                "The chapter has no Critical, Major, or Moderate revision issues. "
                "Continuity is sound and any remaining concerns are Minor or "
                "optional. Further editing is not required."
            )

    # -----------------------------------------------------
    # Replace AI verdict with deterministic verdict
    # -----------------------------------------------------

    replacement = (
        "## Editor Verdict\n\n"
        f"{forced_verdict}\n\n"
        f"{forced_reason}"
    )

    verdict_pattern = re.compile(
        r"##\s*EDITOR VERDICT.*\Z",
        flags=re.IGNORECASE | re.DOTALL,
    )

    if verdict_pattern.search(editor_report):
        editor_report = verdict_pattern.sub(
            replacement,
            editor_report,
        )
    else:
        editor_report = (
            editor_report.rstrip()
            + "\n\n"
            + replacement
        )

    return editor_report


def analyze_chapter(
    book,
    chapter_number,
    chapter_plan,
    chapter_draft,
    story_architecture="",
    character_bible="",
    world_bible="",
    timeline="",
    previous_chapter_summaries="",
    editing_mode="Standard Edit",
    editing_checks=None,
):
    if not chapter_draft or not chapter_draft.strip():
        return "No chapter draft was provided for analysis."

    if editing_checks is None:
        editing_checks = []

    writing_style_profile = book.get(
        "writing_style_profile",
        "Cinematic Technical Thriller",
    )

    style_dialogue = book.get(
        "style_dialogue",
        35,
    )

    style_technical_detail = book.get(
        "style_technical_detail",
        75,
    )

    style_pacing = book.get(
        "style_pacing",
        65,
    )

    style_moral_complexity = book.get(
        "style_moral_complexity",
        85,
    )

    style_description = book.get(
        "style_description",
        45,
    )

    style_violence = book.get(
        "style_violence",
        60,
    )

    style_institutional_detail = book.get(
        "style_institutional_detail",
        75,
    )

    style_subtext = book.get(
        "style_subtext",
        80,
    )

    enabled_checks = (
        "\n".join(
            f"- {check}"
            for check in editing_checks
        )
        if editing_checks
        else "- Full editorial analysis"
    )

    user_prompt = f"""
You are performing a professional editorial analysis of Chapter {chapter_number}.

Analyze the chapter.

Do NOT rewrite the chapter.

Do NOT invent problems merely to justify another edit.

=========================================================
BOOK
=========================================================

{book}

=========================================================
CHAPTER NUMBER
=========================================================

Chapter {chapter_number}

=========================================================
EDITING MODE
=========================================================

{editing_mode}

=========================================================
ENABLED CHECKS
=========================================================

{enabled_checks}

=========================================================
WRITING STYLE TARGETS
=========================================================

Writing Style Profile:
{writing_style_profile}

Dialogue:
{style_dialogue}/100

Technical Detail:
{style_technical_detail}/100

Pacing:
{style_pacing}/100

Moral Complexity:
{style_moral_complexity}/100

Description Density:
{style_description}/100

Violence Treatment:
{style_violence}/100

Institutional / Political Detail:
{style_institutional_detail}/100

Subtext:
{style_subtext}/100

These are creative targets.

Judge whether the chapter uses these traits effectively.

Do not assume higher always means better.

=========================================================
STORY ARCHITECTURE
=========================================================

{story_architecture}

=========================================================
CHARACTER BIBLE
=========================================================

{character_bible}

=========================================================
WORLD BIBLE
=========================================================

{world_bible}

=========================================================
TIMELINE
=========================================================

{timeline}

=========================================================
PREVIOUS CHAPTER SUMMARIES
=========================================================

{previous_chapter_summaries}

=========================================================
CHAPTER PLAN
=========================================================

{chapter_plan}

=========================================================
CHAPTER DRAFT
=========================================================

{chapter_draft}

=========================================================
EDITORIAL PRINCIPLES
=========================================================

Judge actual writing quality.

Do not search for faults simply because an Editor Report
must be produced.

Do not punish deliberate stylistic choices.

Do not recommend unnecessary:

- characters
- POVs
- scenes
- exposition
- conflict
- structural complexity

A professional chapter does not need perfect scores.

Scores:

9.0-10.0 = Excellent
8.0-8.9 = Strong
7.5-7.9 = Good
7.0-7.4 = Acceptable
Below 7.0 = Meaningful weakness

=========================================================
EDITORIAL SCORECARD
=========================================================

Score each category from 0.0 to 10.0.

Use one decimal place.

Required categories:

1. Plot Progression
2. Chapter Objective
3. Character Development
4. Dialogue
5. Pacing
6. Tension
7. Subtext
8. Description
9. Technical Credibility
10. Institutional / Political Realism
11. Moral Complexity
12. Continuity
13. POV Consistency
14. Exposition / Repetition
15. Opening Strength
16. Ending / Hook

Use:

## Editorial Scorecard

| Category | Score | Assessment |
| --- | --- | --- |

=========================================================
PRIORITY REVISION RULES
=========================================================

Only include genuine revision issues.

Maximum 7.

Each issue MUST contain:

**PROBLEM:**

**WHY IT MATTERS:**

**RECOMMENDED APPROACH:**

**SEVERITY:** Minor

Severity MUST be exactly one of:

Critical
Major
Moderate
Minor

Use Critical only for fundamental failures.

Use Major for substantial problems requiring meaningful
scene or structural rewriting.

Use Moderate for localized issues worth correcting.

Use Minor for small improvements that do not materially
damage the chapter.

Do NOT classify an issue as Moderate merely because it could
be improved.

If only Minor issues remain, that is acceptable.

=========================================================
OUTPUT FORMAT
=========================================================

Return exactly these sections:

# Chapter {chapter_number} — Editor Analysis

## Editorial Scorecard

Provide scorecard.

## Overall Assessment

Concise professional assessment.

## Chapter Plan Compliance

Use:

- Achieved:
- Partially Achieved:
- Missed:
- Contradicted:

Use "None." where appropriate.

## Continuity Findings

Only identify genuine continuity conflicts.

If continuity is sound, write EXACTLY:

No significant continuity conflicts detected.

## Character Findings

Assess:

- motivation
- behavior
- voice
- emotional logic
- relationships
- Character Bible consistency

## Style Target Findings

Assess:

- Writing Style Profile
- Dialogue
- Technical Detail
- Pacing
- Moral Complexity
- Description Density
- Violence Treatment
- Institutional / Political Detail
- Subtext

## Priority Revisions

List genuine problems only.

If there are no meaningful revisions, write:

None required.

## Optional Improvements

Only genuinely optional suggestions.

If none:

None recommended.

## Editor Verdict

You may provide your recommended verdict.

Use exactly one of:

EDITING COMPLETE
READY FOR LIGHT POLISH
NEEDS STANDARD EDIT
NEEDS DEEP EDIT
CONTINUITY REPAIR REQUIRED

IMPORTANT:

Python will independently validate and may override your verdict
based on the severities you report.

Therefore make your severity classifications accurate.
"""

    editor_report = call_ai(
        EDITOR_ANALYST_PROMPT,
        user_prompt,
    )

    editor_report = _force_editor_verdict(
        editor_report,
    )

    return editor_report
# =========================================================
# EDITOR REWRITE ENGINE
# =========================================================


def rewrite_chapter(
    book,
    chapter_number,
    chapter_plan,
    chapter_draft,
    editor_report,
    editing_mode="Standard Edit",
    story_architecture="",
    character_bible="",
    world_bible="",
    timeline="",
    previous_chapter_summaries="",
    protected_passages=None,
    targeted_issues=None,
    additional_editing_instructions="",
):

    if not chapter_draft.strip():
        raise ValueError(
            "A chapter draft is required before editing."
        )

    if not editor_report.strip():
        raise ValueError(
            "Analyze the chapter before creating "
            "an edited draft."
        )

    original_word_count = len(
        chapter_draft.split()
    )

    if editing_mode == "Light Polish":

        minimum_words = int(
            original_word_count * 0.95
        )

        maximum_words = int(
            original_word_count * 1.05
        )

    elif editing_mode == "Deep Edit":

        minimum_words = int(
            original_word_count * 0.85
        )

        maximum_words = int(
            original_word_count * 1.15
        )

    else:

        minimum_words = int(
            original_word_count * 0.90
        )

        maximum_words = int(
            original_word_count * 1.10
        )


    writing_style_profile = book.get(
        "writing_style_profile",
        "Cinematic Technical Thriller",
    )

    style_dialogue = book.get(
        "style_dialogue",
        35,
    )

    style_technical_detail = book.get(
        "style_technical_detail",
        75,
    )

    style_pacing = book.get(
        "style_pacing",
        65,
    )

    style_moral_complexity = book.get(
        "style_moral_complexity",
        85,
    )

    style_description = book.get(
        "style_description",
        45,
    )

    style_violence = book.get(
        "style_violence",
        60,
    )

    style_institutional_detail = book.get(
        "style_institutional_detail",
        75,
    )

    style_subtext = book.get(
        "style_subtext",
        80,
    )


    # -----------------------------------------------------
    # STYLE INTERPRETATION HELPERS
    # -----------------------------------------------------

    def dialogue_guidance(value):

        if value <= 25:
            return (
                "Preserve highly restrained dialogue. "
                "Characters should speak economically and avoid "
                "unnecessary emotional explanation."
            )

        elif value <= 50:
            return (
                "Preserve controlled, natural dialogue with moderate "
                "emotional expression."
            )

        elif value <= 75:
            return (
                "Allow more expressive and conversational dialogue "
                "while preserving distinct character voices."
            )

        else:
            return (
                "Allow highly expressive, energetic, emotionally open, "
                "and conversational dialogue where appropriate."
            )


    def technical_guidance(value):

        if value <= 25:
            return (
                "Keep technical and procedural explanation light. "
                "Do not expand technical material unless necessary."
            )

        elif value <= 50:
            return (
                "Preserve moderate technical detail where it supports "
                "credibility or practical constraints."
            )

        elif value <= 75:
            return (
                "Preserve substantial technical, procedural, operational, "
                "and professional detail where it affects events."
            )

        else:
            return (
                "Preserve extensive technically credible detail involving "
                "procedure, logistics, systems, technology, and professional "
                "decision-making while keeping it readable."
            )


    def pacing_guidance(value):

        if value <= 25:
            return (
                "Preserve slow-burn pacing. Do not aggressively compress "
                "atmosphere, observation, hesitation, or character pressure."
            )

        elif value <= 50:
            return (
                "Maintain measured pacing with a balance between character "
                "development and forward movement."
            )

        elif value <= 75:
            return (
                "Maintain relatively fast pacing with frequent meaningful "
                "developments while preserving scene depth."
            )

        else:
            return (
                "Maintain strong forward momentum, tight transitions, "
                "and short delays between meaningful consequences."
            )


    def moral_guidance(value):

        if value <= 25:
            return (
                "Preserve relatively clear moral positions where they exist."
            )

        elif value <= 50:
            return (
                "Preserve moderate moral complexity, mixed motives, "
                "and believable flaws."
            )

        elif value <= 75:
            return (
                "Preserve strong moral ambiguity, competing legitimate goals, "
                "and difficult trade-offs."
            )

        else:
            return (
                "Preserve very high moral complexity. Do not simplify "
                "conflicted motivations or remove meaningful ethical costs."
            )


    def description_guidance(value):

        if value <= 25:
            return (
                "Keep description sparse and functional. Remove unnecessary "
                "descriptive clutter but preserve important concrete details."
            )

        elif value <= 50:
            return (
                "Preserve controlled sensory and environmental description."
            )

        elif value <= 75:
            return (
                "Preserve substantial descriptive detail where setting and "
                "atmosphere strengthen the scene."
            )

        else:
            return (
                "Preserve rich sensory, environmental, and atmospheric "
                "description unless it clearly harms the chapter."
            )


    def violence_guidance(value):

        if value <= 25:
            return (
                "Keep violence restrained, brief, implied where appropriate, "
                "and focused on consequence."
            )

        elif value <= 50:
            return (
                "Preserve direct violence without unnecessary graphic detail."
            )

        elif value <= 75:
            return (
                "Preserve realistic and direct violence, including physical, "
                "practical, and emotional aftermath."
            )

        else:
            return (
                "Preserve explicit physical detail when dramatically justified, "
                "along with realistic aftermath and consequences."
            )


    def institutional_guidance(value):

        if value <= 25:
            return (
                "Keep institutional and political systems mostly in the "
                "background unless essential."
            )

        elif value <= 50:
            return (
                "Preserve moderate institutional detail where organizations "
                "directly affect character choices."
            )

        elif value <= 75:
            return (
                "Preserve meaningful institutional complexity including "
                "hierarchy, bureaucracy, competing priorities, and conflict."
            )

        else:
            return (
                "Preserve extensive institutional and political complexity "
                "including chains of command, competing organizations, "
                "internal agendas, resource limits, and power structures."
            )


    def subtext_guidance(value):

        if value <= 25:
            return (
                "Allow relatively direct communication. Do not artificially "
                "obscure character intentions."
            )

        elif value <= 50:
            return (
                "Preserve moderate subtext and selective emotional avoidance."
            )

        elif value <= 75:
            return (
                "Preserve strong subtext through implication, silence, "
                "avoidance, hesitation, and hidden intention."
            )

        else:
            return (
                "Preserve very strong subtext. Do not edit important implied "
                "emotional or strategic meaning into explicit explanation."
            )


    detailed_style_guidance = f"""
DIALOGUE STYLE: {style_dialogue}/100
{dialogue_guidance(style_dialogue)}

TECHNICAL DETAIL: {style_technical_detail}/100
{technical_guidance(style_technical_detail)}

PACING: {style_pacing}/100
{pacing_guidance(style_pacing)}

MORAL COMPLEXITY: {style_moral_complexity}/100
{moral_guidance(style_moral_complexity)}

DESCRIPTION DENSITY: {style_description}/100
{description_guidance(style_description)}

VIOLENCE TREATMENT: {style_violence}/100
{violence_guidance(style_violence)}

INSTITUTIONAL / POLITICAL DETAIL:
{style_institutional_detail}/100
{institutional_guidance(style_institutional_detail)}

SUBTEXT: {style_subtext}/100
{subtext_guidance(style_subtext)}
"""


    # -----------------------------------------------------
    # PROFILE GUIDANCE
    # -----------------------------------------------------

    style_guidance = {
        "Cinematic Technical Thriller": """
Preserve and strengthen a grounded cinematic thriller approach.

Protect:

- restrained emotional expression
- subtext-heavy dialogue
- moral ambiguity
- visual scene construction
- credible professional behavior
- realistic institutional pressure
- believable technical detail
- strategic decision-making
- information gaps
- geographical and logistical realism
- strong cause and effect
- quiet human moments between pressure scenes
- violence with practical and emotional consequences

Do not make the prose more generic, melodramatic, or over-explanatory.

Technical detail should remain understandable and should serve the story.
""",

        "Grounded Cinematic Drama": """
Preserve and strengthen grounded cinematic drama.

Protect:

- psychologically believable behavior
- restrained emotion
- subtext
- relationship tension
- moral ambiguity
- meaningful physical behavior
- strong sense of place
- quiet dramatic moments
- imperfect choices
- lasting consequences

Avoid melodrama and excessive explanation.
""",

        "Technical / Geopolitical Thriller": """
Preserve and strengthen technically credible thriller storytelling.

Protect:

- procedural realism
- credible institutions
- chains of command
- strategic thinking
- logistics
- technology
- surveillance
- communications
- intelligence gaps
- misinformation
- professional competence
- escalating operational consequences

Do not simplify technical or institutional material so aggressively
that the story loses credibility.

Do not turn technical material into lectures.
""",

        "Literary Crime": """
Preserve and strengthen literary crime qualities.

Protect:

- atmosphere
- flawed motivations
- moral ambiguity
- social and economic pressure
- guilt
- loyalty
- betrayal
- psychological credibility
- restrained exposition
- consequence

Avoid simplistic moral framing.
""",

        "Psychological Suspense": """
Preserve and strengthen psychological suspense.

Protect:

- uncertainty
- suspicion
- hidden motives
- incomplete information
- behavioral clues
- controlled revelation
- relationship pressure
- shifting interpretations
- psychological tension

Do not manufacture unsupported twists during editing.
""",

        "Custom": """
Preserve the original chapter's established narrative approach.

Improve clarity, continuity, dialogue, pacing, and prose without
forcing the chapter into a predefined style.
""",
    }

    selected_style_guidance = style_guidance.get(
        writing_style_profile,
        style_guidance["Cinematic Technical Thriller"],
    )

    protected_passages = protected_passages or []
    targeted_issues = targeted_issues or []

    if targeted_issues:
        targeted_issue_text = "\n\n".join(
            f"TARGET ISSUE {index + 1}:\n{issue}"
            for index, issue in enumerate(targeted_issues)
        )

        targeted_editing_rules = f"""
=========================================================
TARGETED EDITING MODE
=========================================================

TARGETED EDITING IS ACTIVE.

Only address the selected editorial issues below:

{targeted_issue_text}

Make the SMALLEST EFFECTIVE CHANGES needed to materially improve
those selected issues.

Every change must directly address a selected issue.

Do not make cosmetic synonym swaps or general polish outside the
selected issues. If existing prose is already effective, leave it
unchanged. Preserve unrelated dialogue, plot, pacing, characterization,
exposition, description, transitions, terminology, and scene structure.

Before keeping any change, verify both:
1. The selected issue required this change.
2. The new wording is materially better than the original.

If either test fails, restore the original wording.

Ignore unselected Priority Revisions and unselected Optional Improvements.
"""
    else:
        targeted_editing_rules = """
=========================================================
TARGETED EDITING MODE
=========================================================

Targeted Editing is not active.
Use the full Editor Report as the editing guide, subject to the selected
Editing Mode.
"""

    if additional_editing_instructions.strip():
        additional_instructions_block = f"""
=========================================================
WRITER'S ADDITIONAL EDITING INSTRUCTIONS
=========================================================

{additional_editing_instructions.strip()}
"""
    else:
        additional_instructions_block = ""

    if protected_passages:
        protected_passages_block = (
            "\n=========================================================\n"
            "PROTECTED PASSAGES — DO NOT ALTER\n"
            "=========================================================\n\n"
            + "\n\n--- PROTECTED PASSAGE ---\n\n".join(protected_passages)
        )
    else:
        protected_passages_block = ""



    user_prompt = f"""
=========================================================
BOOK INFORMATION
=========================================================

TITLE:
{book['title']}

GENRE:
{book['genre']}

REGION:
{book['region']}

TIME PERIOD:
{book['period']}

PRIMARY PLOT:
{book.get('primary_plot', '')}

SECONDARY PLOT:
{book.get('secondary_plot', 'None')}

CHARACTER ARC:
{book.get('character_arc', '')}

RELATIONSHIP ARC:
{book.get('relationship_arc', 'None')}

MYSTERY ENGINE:
{book.get('mystery_engine', 'None')}

WRITING STYLE PROFILE:
{writing_style_profile}


=========================================================
SELECTED WRITING STYLE PROFILE
=========================================================

{selected_style_guidance}


=========================================================
DETAILED WRITING STYLE CONTROLS
=========================================================

{detailed_style_guidance}


=========================================================
STYLE CONTROL PRIORITY
=========================================================

The Writing Style Profile establishes the broad narrative approach.

The Detailed Writing Style Controls fine-tune that approach and are
AUTHORITATIVE editing constraints.

When a detailed slider conflicts with a default characteristic
of the profile, the detailed slider takes priority.

Do not edit the chapter toward a generic middle setting.

For example:

- Do not make restrained dialogue more expressive unless the Dialogue
  Style setting supports it.
- Do not remove technical material merely because it is complex when
  Technical Detail is intentionally high.
- Do not aggressively accelerate a chapter when Pacing is intentionally low.
- Do not explain morally ambiguous behavior when Moral Complexity is high.
- Do not strip atmosphere when Description Density is high.
- Do not make violence more graphic than the Violence Treatment setting allows.
- Do not simplify organizational conflict when Institutional Detail is high.
- Do not turn implied meaning into explicit dialogue when Subtext is high.


=========================================================
STYLE PRESERVATION RULE
=========================================================

The selected Writing Style Profile and Detailed Style Controls are
AUTHORITATIVE editing constraints.

The edited chapter should still clearly feel like it belongs to
the same novel.

Preserve the intended approach to:

- dialogue
- pacing
- sentence rhythm
- paragraph rhythm
- technical detail
- emotional restraint
- description
- suspense
- information control
- institutional realism
- moral complexity
- action
- violence
- scene rhythm
- consequences
- subtext

Do not normalize the prose into generic commercial fiction.

Do not imitate the distinctive prose or voice of any living author.

Use only the high-level narrative characteristics supplied above.


=========================================================
EDITING MODE
=========================================================

{editing_mode}


=========================================================
CHAPTER
=========================================================

CHAPTER NUMBER:
{chapter_number}


=========================================================
ORIGINAL WORD COUNT
=========================================================

{original_word_count:,} words

TARGET EDITED RANGE:
{minimum_words:,} to {maximum_words:,} words


=========================================================
AUTHORITATIVE CHAPTER PLAN
=========================================================

{chapter_plan}


=========================================================
ORIGINAL CHAPTER DRAFT
=========================================================

{chapter_draft}


=========================================================
EDITOR REPORT
=========================================================

{editor_report}


=========================================================
STORY ARCHITECTURE
=========================================================

{story_architecture}


=========================================================
CHARACTER BIBLE
=========================================================

{character_bible}


=========================================================
WORLD BIBLE
=========================================================

{world_bible}


=========================================================
TIMELINE
=========================================================

{timeline}


=========================================================
PREVIOUS CHAPTER SUMMARIES
=========================================================

{previous_chapter_summaries}


{targeted_editing_rules}

{additional_instructions_block}

{protected_passages_block}


=========================================================
REWRITE INSTRUCTIONS
=========================================================

Produce a polished edited version of the complete chapter.

Follow the selected editing mode exactly.

Use the Editor Report as a repair guide.

Correct genuine issues while preserving:

- the chapter plan
- manually specified chapter decisions
- major plot events
- character identities
- established relationships
- revelations
- chronology
- world rules
- character knowledge boundaries
- the chapter ending
- the selected Writing Style Profile
- all eight Detailed Writing Style Controls

Do not create a different story.

Do not invent new major events.

Do not remove required story events.

Do not change established character motivations without clear
authority from the supplied story material.

If the Editor Report contains optional suggestions that would:

- weaken the prose
- damage continuity
- undermine the Writing Style Profile
- override a detailed style slider
- make the prose more generic

do not implement those suggestions mechanically.


=========================================================
EDITING MODE RULES
=========================================================

If the mode is LIGHT POLISH:

Make minimal corrections.

Focus on:

- grammar
- punctuation
- awkward wording
- clarity
- repeated words
- unnecessary repetition
- paragraph flow
- minor dialogue cleanup
- name usage

Preserve the original author's wording and structure wherever
reasonable.

Do not significantly change:

- scene pacing
- dialogue content
- technical-detail density
- description density
- degree of subtext
- story events
- narrative structure


If the mode is STANDARD EDIT:

Make moderate improvements.

You may improve:

- sentence construction
- paragraph rhythm
- dialogue
- subtext
- pacing
- transitions
- POV consistency
- emotional restraint
- character voice
- repetitive prose
- physical behavior
- cause and effect

You may rewrite sentences or paragraphs where necessary.

Do not significantly alter:

- plot
- chapter objective
- major revelations
- chapter ending
- character identity
- established continuity
- intended detailed style settings


If the mode is DEEP EDIT:

Perform a strong editorial rewrite while preserving the story
and selected style controls.

Improve:

- scene effectiveness
- pacing
- dialogue
- subtext
- POV
- emotional credibility
- character consistency
- grounded detail
- continuity
- prose rhythm
- cause and effect
- scene entry
- scene exit
- generic or artificial AI-like phrasing
- excessive exposition
- weak transitions
- unsupported emotional statements

You may restructure paragraphs.

You may slightly expand or compress scenes.

You may strengthen existing dramatic beats.

You may not:

- invent a new plot
- remove required events
- add major characters
- change the intended ending
- contradict the Story Architecture
- contradict the Character Bible
- contradict the World Bible
- contradict the Timeline
- override manual Chapter Plan instructions
- override the Detailed Writing Style Controls


=========================================================
DIALOGUE STYLE
=========================================================

Preserve the intended Dialogue Style setting.

At low settings:

- keep dialogue restrained
- preserve silence
- preserve unfinished thoughts
- reduce unnecessary explanation
- allow behavior to carry emotion

At high settings:

- allow greater conversational energy
- preserve emotional openness where established
- allow longer exchanges where dramatically useful

Do not make every character speak in the same way.

Dialogue must remain specific to:

- personality
- background
- profession
- education
- social role
- emotional state
- objective
- knowledge


=========================================================
SUBTEXT
=========================================================

Preserve the intended Subtext setting.

High subtext means important meaning may exist beneath literal words.

Preserve effective use of:

- implication
- silence
- avoidance
- hesitation
- interruption
- misdirection
- strategic politeness
- changed subjects
- unanswered questions
- physical behavior

Do not edit implied emotion into explicit explanation unless clarity
truly requires it.

At low subtext settings, allow characters to communicate more directly.


=========================================================
CHARACTER NAME USAGE
=========================================================

After a character is clearly identified, narration should normally
use their first name.

Use surnames, full names, ranks, or titles only where naturally
appropriate.

Examples include:

- formal situations
- professional environments
- military or police settings
- deliberate emotional distance
- dialogue
- situations where multiple characters share a first name

Do not repeatedly reintroduce established characters with full names.


=========================================================
TECHNICAL DETAIL
=========================================================

Preserve the intended Technical Detail setting.

At low settings:

- simplify unnecessary terminology
- compress technical explanation
- keep only details needed for credibility and comprehension

At high settings:

- preserve procedure
- preserve realistic terminology
- preserve equipment limitations
- preserve logistics
- preserve professional decision-making
- preserve technical cause and effect

Technical material may be improved for clarity.

Do not remove important constraints involving:

- timing
- geography
- communications
- logistics
- resources
- surveillance
- weapons
- technology
- law
- procedure
- hierarchy
- chains of command
- professional limitations

Do not add unnecessary jargon.

Do not simplify important technical material into implausibility.


=========================================================
INSTITUTIONAL / POLITICAL DETAIL
=========================================================

Preserve the intended Institutional / Political Detail setting.

At lower settings, avoid expanding organizational explanation unnecessarily.

At higher settings, preserve relevant:

- hierarchy
- jurisdiction
- bureaucracy
- competing agencies
- chains of command
- legal constraints
- political pressure
- corporate interests
- organizational agendas
- resource limitations
- institutional rivalry

Do not remove institutional friction if it materially affects what
characters can do.


=========================================================
INFORMATION CONTROL
=========================================================

Maintain strict knowledge boundaries.

Characters must not suddenly know information they have not learned.

Preserve differences between:

- what the reader knows
- what the POV character knows
- what allies know
- what opponents know
- what institutions believe
- what is actually true

Do not accidentally reveal secrets early during editing.


=========================================================
MORAL COMPLEXITY
=========================================================

Preserve the intended Moral Complexity setting.

At lower settings:

- retain clearer moral distinctions where established
- do not manufacture unnecessary ambiguity

At higher settings:

- preserve conflicting legitimate motives
- preserve difficult trade-offs
- preserve ethical costs
- preserve conflicting loyalties
- preserve tension between law, duty, justice, survival, and personal obligation

Do not simplify morally complicated characters merely to make
their motivations easier to explain.


=========================================================
DESCRIPTION DENSITY
=========================================================

Preserve the intended Description Density setting.

At low settings:

- remove redundant description
- favor selective concrete details
- protect pace and clarity

At moderate settings:

- preserve sensory and environmental grounding

At high settings:

- preserve meaningful atmosphere
- preserve geography
- preserve sensory texture
- preserve environmental detail
- preserve objects, machinery, clothing, weather, architecture,
  vehicles, and surroundings when dramatically relevant

Description should still serve the scene.

Do not remove environmental detail that affects:

- movement
- visibility
- access
- vulnerability
- mood
- communication
- tactics
- character behavior


=========================================================
PACING
=========================================================

Preserve the intended Pacing setting.

Do not automatically make every edited chapter faster.

At low pacing settings:

- preserve longer scenes
- preserve atmosphere
- preserve observation
- preserve emotional processing
- preserve gradual tension

At high pacing settings:

- tighten unnecessary delays
- improve transitions
- remove redundant beats
- preserve strong forward movement
- keep meaningful consequences close to decisions

Fast pacing must not become shallow.

Slow pacing must not become inactivity.


=========================================================
ACTION AND VIOLENCE
=========================================================

Preserve the intended Violence Treatment setting.

When violence, action, injury, or major confrontation occurs,
maintain realistic cause and effect.

At lower settings:

- preserve implication where effective
- avoid adding graphic detail
- emphasize danger and aftermath

At higher settings:

- preserve direct physical detail where dramatically justified
- preserve realistic injury mechanics
- preserve practical consequences

Violence may affect:

- injuries
- relationships
- investigations
- resources
- legal exposure
- institutional response
- future decisions
- emotional behavior

Do not remove aftermath simply to make the chapter move faster.

Do not intensify violence merely to make a scene more dramatic.


=========================================================
COMMON AI WRITING PROBLEMS TO REMOVE
=========================================================

When appropriate for the selected editing mode, reduce:

- unnecessary emotion explanation
- repeated rhetorical questions
- repetitive sentence structures
- excessive character-name repetition
- constant references to breathing, heartbeats, jaws, fists, or eyes
- unnecessary adjectives
- unnecessary adverbs
- generic sensory descriptions
- melodramatic internal monologue
- artificial dramatic fragments
- exposition disguised as dialogue
- characters repeating information they already know
- characters summarizing events that just occurred
- repeated reminders of established stakes
- generic phrases that could appear in any novel
- dialogue in which every character sounds equally polished

Do not remove intentional repetition that serves rhythm, characterization,
tension, or theme.


=========================================================
WORD COUNT
=========================================================

Maintain the complete edited chapter within approximately:

{minimum_words:,} to {maximum_words:,} words.

Do not drastically shorten scenes simply to produce a cleaner draft.

Do not add filler simply to reach the target range.


=========================================================
CHAPTER HEADING
=========================================================

Preserve the chapter heading at the top of the edited chapter.

Do not create a second heading.


=========================================================
OUTPUT
=========================================================

Return ONLY the complete edited chapter.

Do not include:

- analysis
- notes
- explanations
- change summaries
- editing comments
- word counts
"""

    max_output_tokens = int(
        max(
            original_word_count * 2.5,
            3000,
        )
    )

    max_output_tokens = min(
        max_output_tokens,
        12000,
    )

    response = client.responses.create(
        model=model_name,
        instructions=EDITOR_REWRITE_PROMPT,
        input=user_prompt,
        max_output_tokens=max_output_tokens,
    )

    edited_chapter = response.output_text.strip()

    for passage in protected_passages:
        if passage not in edited_chapter:
            raise ValueError(
                "Protected passage was altered or removed during editing."
            )

    return edited_chapter

# =========================================================
# CHARACTER NAME GENERATOR
# =========================================================

def generate_character_name(
    book,
    old_name,
    character_bible="",
):

    user_prompt = f"""
Generate ONE replacement name for a fictional character.

CURRENT CHARACTER NAME:
{old_name}

REGION:
{book['region']}

TIME PERIOD:
{book['period']}

GENRE:
{book['genre']}

CHARACTER INFORMATION:
{character_bible}

Requirements:

- Keep the character's existing background unchanged.
- Choose a believable name for the region and time period.
- Avoid celebrity names.
- Avoid famous fictional character names.
- Do not explain your choice.
- Return ONLY the replacement full name.
"""

    system_prompt = """
You generate believable original fictional character names.

Return only the requested name.

Do not include explanation, quotation marks, headings,
bullet points, or commentary.
"""

    return call_ai(
        system_prompt,
        user_prompt,
    ).strip()