# =========================================================
# AI NOVELIST - PLOT LIBRARY
# =========================================================
#
# This file stores reusable story engines, character arcs,
# relationship arcs, mystery engines, and complexity levels.
#
# The goal is to give the Story Architect structured dramatic
# guidance rather than relying on one generic plot label.
# =========================================================


# =========================================================
# STRUCTURE COMPLEXITY
# =========================================================

STRUCTURE_COMPLEXITY = {
    "Simple": {
        "description": (
            "One dominant plot, one main character arc, "
            "minimal subplot complexity."
        ),
        "recommended_secondary_plots": 0,
        "recommended_relationship_arcs": 0,
        "recommended_mystery_engines": 0,
    },

    "Standard": {
        "description": (
            "One primary plot, one secondary plot, "
            "one main character arc, and one relationship arc."
        ),
        "recommended_secondary_plots": 1,
        "recommended_relationship_arcs": 1,
        "recommended_mystery_engines": 0,
    },

    "Complex": {
        "description": (
            "One primary plot, multiple subplots, "
            "several character pressures, relationship conflict, "
            "and optional mystery structure."
        ),
        "recommended_secondary_plots": 2,
        "recommended_relationship_arcs": 1,
        "recommended_mystery_engines": 1,
    },

    "Epic": {
        "description": (
            "Large ensemble structure with interlocking plots, "
            "multiple POV characters, relationship arcs, "
            "and layered mystery or political engines."
        ),
        "recommended_secondary_plots": 3,
        "recommended_relationship_arcs": 2,
        "recommended_mystery_engines": 1,
    },
}


# =========================================================
# PLOT ENGINES
# =========================================================

PLOT_ENGINES = {

    # -----------------------------------------------------
    # CLASSIC / CORE DRAMATIC ENGINES
    # -----------------------------------------------------

    "Overcoming the Monster": {
        "category": "Classic",
        "core_question": (
            "Can the protagonist defeat a powerful external threat "
            "without becoming what they oppose?"
        ),
        "stages": [
            "Threat emerges",
            "Protagonist resists involvement",
            "Cost of inaction increases",
            "First confrontation",
            "Apparent setback",
            "New understanding",
            "Final confrontation",
            "Consequences",
        ],
    },

    "Rags to Riches": {
        "category": "Classic",
        "core_question": (
            "What does success reveal about the protagonist, "
            "and what does achievement cost?"
        ),
        "stages": [
            "Low starting position",
            "Opportunity",
            "Early success",
            "Transformation",
            "Temptation or corruption",
            "Loss or crisis",
            "Final test",
            "New identity",
        ],
    },

    "The Quest": {
        "category": "Classic",
        "core_question": (
            "Can the protagonist reach the goal while surviving "
            "the sacrifices required by the journey?"
        ),
        "stages": [
            "Call to pursue",
            "Commitment",
            "Allies and obstacles",
            "Escalating trials",
            "Major setback",
            "Approach to goal",
            "Final test",
            "Return or consequence",
        ],
    },

    "Voyage and Return": {
        "category": "Classic",
        "core_question": (
            "How does entering an unfamiliar world transform "
            "the protagonist?"
        ),
        "stages": [
            "Departure",
            "Entry into unfamiliar world",
            "Initial wonder",
            "Growing danger",
            "Loss of control",
            "Escape or breakthrough",
            "Return",
            "Changed perspective",
        ],
    },

    "Comedy": {
        "category": "Classic",
        "core_question": (
            "Can disorder, misunderstanding, or social conflict "
            "be resolved without destroying the relationships involved?"
        ),
        "stages": [
            "Social imbalance",
            "Misunderstanding",
            "Complication",
            "Escalation",
            "Exposure",
            "Recognition",
            "Reconciliation",
            "New social order",
        ],
    },

    "Tragedy": {
        "category": "Classic",
        "core_question": (
            "Will the protagonist's flaw, obsession, or decision "
            "destroy what they value most?"
        ),
        "stages": [
            "Desire",
            "Initial success",
            "Compromise",
            "Escalation",
            "Point of no return",
            "Collapse",
            "Recognition",
            "Consequence",
        ],
    },

    "Rebirth": {
        "category": "Classic",
        "core_question": (
            "Can the protagonist escape the identity or behaviour "
            "that has trapped them?"
        ),
        "stages": [
            "Entrapment",
            "Pressure",
            "Chance for change",
            "Resistance",
            "Crisis",
            "Recognition",
            "Transformation",
            "New life",
        ],
    },

    "Revenge": {
        "category": "Conflict",
        "core_question": (
            "What is the protagonist willing to sacrifice for vengeance?"
        ),
        "stages": [
            "Original injury",
            "Decision to retaliate",
            "First move",
            "Escalation",
            "Collateral damage",
            "Moral cost",
            "Point of no return",
            "Confrontation",
            "Consequences",
        ],
    },

    "Rescue": {
        "category": "Conflict",
        "core_question": (
            "Can the protagonist save another person before time, "
            "opposition, or their own limitations make rescue impossible?"
        ),
        "stages": [
            "Loss or capture",
            "Decision to act",
            "Obstacle",
            "New information",
            "Escalation",
            "Failed attempt",
            "Final approach",
            "Rescue or failure",
            "Aftermath",
        ],
    },

    "Escape": {
        "category": "Conflict",
        "core_question": (
            "Can the protagonist regain freedom while conditions "
            "tighten around them?"
        ),
        "stages": [
            "Entrapment",
            "Assessment",
            "First attempt",
            "Failure",
            "Greater restriction",
            "New plan",
            "Critical risk",
            "Escape",
            "Consequences",
        ],
    },

    "Pursuit": {
        "category": "Conflict",
        "core_question": (
            "Can the pursued survive or the pursuer succeed "
            "before the balance of power changes?"
        ),
        "stages": [
            "Trigger",
            "Flight or chase",
            "Temporary safety",
            "Detection",
            "Escalation",
            "Reversal",
            "Final pursuit",
            "Resolution",
        ],
    },

    "Survival": {
        "category": "Conflict",
        "core_question": (
            "What part of the protagonist survives when comfort, "
            "society, and certainty are stripped away?"
        ),
        "stages": [
            "Crisis",
            "Immediate survival",
            "Resource loss",
            "Adaptation",
            "Physical or moral compromise",
            "Major setback",
            "Final endurance test",
            "Survival or failure",
        ],
    },

    "Sacrifice": {
        "category": "Conflict",
        "core_question": (
            "What is worth giving up everything for?"
        ),
        "stages": [
            "Attachment",
            "Growing threat",
            "Impossible choice",
            "Resistance",
            "Recognition",
            "Decision",
            "Sacrifice",
            "Legacy",
        ],
    },

    "Transformation": {
        "category": "Character",
        "core_question": (
            "What forces the protagonist to become someone fundamentally different?"
        ),
        "stages": [
            "Stable identity",
            "Disruption",
            "Resistance",
            "Pressure",
            "Old self fails",
            "New behaviour",
            "Final test",
            "Changed identity",
        ],
    },

    "Forbidden Goal": {
        "category": "Conflict",
        "core_question": (
            "Why is the protagonist pursuing something they are not supposed to have?"
        ),
        "stages": [
            "Desire established",
            "Boundary identified",
            "First transgression",
            "Reward",
            "Escalating risk",
            "Exposure",
            "Choice",
            "Consequence",
        ],
    },

    "Rise and Fall": {
        "category": "Power",
        "core_question": (
            "Does success create the conditions for the protagonist's collapse?"
        ),
        "stages": [
            "Ambition",
            "Opportunity",
            "Rise",
            "Expansion",
            "Overreach",
            "Betrayal or weakness",
            "Collapse",
            "Aftermath",
        ],
    },

    "Fall and Redemption": {
        "category": "Character",
        "core_question": (
            "Can someone who has failed morally earn a meaningful second chance?"
        ),
        "stages": [
            "Fall",
            "Consequences",
            "Isolation",
            "Chance to repair",
            "Resistance",
            "Act of responsibility",
            "Final test",
            "Redemption or failure",
        ],
    },

    "Underdog": {
        "category": "Conflict",
        "core_question": (
            "Can someone with fewer resources defeat a stronger opponent?"
        ),
        "stages": [
            "Power imbalance",
            "Challenge",
            "Early defeat",
            "Adaptation",
            "Unexpected strength",
            "Major setback",
            "Final contest",
            "Outcome",
        ],
    },

    "Coming of Age": {
        "category": "Character",
        "core_question": (
            "What truth must the protagonist accept in order to mature?"
        ),
        "stages": [
            "Protected worldview",
            "Disruption",
            "Experimentation",
            "Loss",
            "Moral challenge",
            "Recognition",
            "Adult choice",
            "New identity",
        ],
    },

    "Return Home": {
        "category": "Character",
        "core_question": (
            "Can someone return to the place that formed them "
            "without being consumed by the past?"
        ),
        "stages": [
            "Return",
            "Old relationships",
            "Buried tension",
            "Past resurfaces",
            "Conflict",
            "Truth revealed",
            "Decision",
            "Stay, leave, or redefine home",
        ],
    },


    # -----------------------------------------------------
    # CRIME / POWER / THRILLER
    # -----------------------------------------------------

    "Investigation": {
        "category": "Crime / Mystery",
        "core_question": (
            "Can the protagonist uncover the truth before the truth "
            "destroys them or someone else?"
        ),
        "stages": [
            "Disturbing event",
            "Initial theory",
            "First evidence",
            "Contradiction",
            "Expanded suspects",
            "False conclusion",
            "Critical discovery",
            "Truth",
            "Consequences",
        ],
    },

    "Manhunt": {
        "category": "Crime / Thriller",
        "core_question": (
            "Can the target be found before they escape, strike again, "
            "or reveal something dangerous?"
        ),
        "stages": [
            "Target identified",
            "Search begins",
            "Near contact",
            "Misdirection",
            "Escalation",
            "Reversal",
            "Closing net",
            "Capture or escape",
        ],
    },

    "Conspiracy": {
        "category": "Crime / Thriller",
        "core_question": (
            "How deep does the hidden system go, and who can still be trusted?"
        ),
        "stages": [
            "Anomaly",
            "Suspicion",
            "First connection",
            "Dismissal or resistance",
            "Evidence grows",
            "Trusted figure implicated",
            "System exposed",
            "Confrontation",
            "Aftermath",
        ],
    },

    "Corruption": {
        "category": "Power",
        "core_question": (
            "Can the protagonist resist or expose a system in which wrongdoing "
            "has become normal?"
        ),
        "stages": [
            "Corrupt norm established",
            "Protagonist encounters it",
            "Initial compromise",
            "Reward or pressure",
            "Deepening involvement",
            "Moral crisis",
            "Exposure or participation",
            "Consequences",
        ],
    },

    "Heist": {
        "category": "Crime",
        "core_question": (
            "Can the team execute a high-risk plan when trust and precision "
            "are equally fragile?"
        ),
        "stages": [
            "Target chosen",
            "Team assembled",
            "Plan",
            "Preparation",
            "Hidden weakness",
            "Execution",
            "Complication",
            "Escape",
            "Division of consequences",
        ],
    },

    "Crime Gone Wrong": {
        "category": "Crime",
        "core_question": (
            "How far will the characters go to survive the consequences "
            "of one failed crime?"
        ),
        "stages": [
            "Crime planned",
            "Crime committed",
            "Unexpected failure",
            "Cover-up",
            "Escalating consequences",
            "Betrayal",
            "Exposure",
            "Final consequence",
        ],
    },

    "Infiltration": {
        "category": "Thriller",
        "core_question": (
            "Can the protagonist survive inside the enemy's world "
            "without losing their identity or cover?"
        ),
        "stages": [
            "Mission",
            "Entry",
            "First test",
            "Trust gained",
            "Compromise",
            "Suspicion",
            "Identity threatened",
            "Extraction or exposure",
        ],
    },

    "Witness in Danger": {
        "category": "Thriller",
        "core_question": (
            "Can the witness survive long enough for what they know to matter?"
        ),
        "stages": [
            "Witness sees or knows something",
            "Threat emerges",
            "Protection",
            "Breach",
            "Isolation",
            "Truth questioned",
            "Final attack",
            "Testimony or silence",
        ],
    },

    "Wrongly Accused": {
        "category": "Thriller",
        "core_question": (
            "Can the protagonist prove innocence while every system "
            "treats them as guilty?"
        ),
        "stages": [
            "Accusation",
            "Loss of status",
            "Search for truth",
            "Evidence against them grows",
            "False ally",
            "Critical discovery",
            "Confrontation",
            "Vindication or defeat",
        ],
    },

    "Cat and Mouse": {
        "category": "Thriller",
        "core_question": (
            "Which opponent understands the other better?"
        ),
        "stages": [
            "Opponents identified",
            "First move",
            "Countermove",
            "Psychological probing",
            "Reversal",
            "Personal stakes",
            "Trap",
            "Final contest",
        ],
    },

    "Organized Crime": {
        "category": "Crime / Power",
        "core_question": (
            "Can an individual survive a system where loyalty, money, "
            "family, and violence are inseparable?"
        ),
        "stages": [
            "Entry or inherited position",
            "Rules established",
            "Opportunity",
            "Conflict between factions",
            "Loyalty tested",
            "Betrayal",
            "Power struggle",
            "New order",
        ],
    },

    "Succession Struggle": {
        "category": "Power",
        "core_question": (
            "Who deserves power, and what are they willing to do to inherit it?"
        ),
        "stages": [
            "Power vacuum approaches",
            "Potential successors emerge",
            "Alliances",
            "Tests of loyalty",
            "Sabotage",
            "Betrayal",
            "Final struggle",
            "Succession",
        ],
    },

    "Power Vacuum": {
        "category": "Power",
        "core_question": (
            "What happens when an established authority suddenly disappears?"
        ),
        "stages": [
            "Authority removed",
            "Uncertainty",
            "Factions emerge",
            "Competing claims",
            "Violence or instability",
            "Realignment",
            "Final struggle",
            "New order",
        ],
    },

    "Betrayal": {
        "category": "Conflict",
        "core_question": (
            "What happens when trust becomes the weapon?"
        ),
        "stages": [
            "Trust established",
            "Hidden motive",
            "Warning signs",
            "Betrayal",
            "Damage",
            "Search for motive",
            "Response",
            "Final relationship state",
        ],
    },

    "Cover-Up": {
        "category": "Crime / Mystery",
        "core_question": (
            "How many additional wrongs are required to keep the original truth hidden?"
        ),
        "stages": [
            "Original event",
            "Decision to conceal",
            "First lie",
            "Evidence remains",
            "New threat",
            "Further concealment",
            "Exposure",
            "Consequences",
        ],
    },


    # -----------------------------------------------------
    # FAMILY / SOCIAL / RELATIONSHIP
    # -----------------------------------------------------

    "Family Conflict": {
        "category": "Family",
        "core_question": (
            "Can love survive incompatible needs, loyalties, and histories?"
        ),
        "stages": [
            "Old tension",
            "Trigger",
            "Sides form",
            "Past grievance returns",
            "Escalation",
            "Truth or betrayal",
            "Choice",
            "New family order",
        ],
    },

    "Inheritance": {
        "category": "Family",
        "core_question": (
            "What does an inheritance reveal about the living and the dead?"
        ),
        "stages": [
            "Death or transfer",
            "Terms revealed",
            "Competing expectations",
            "Old secrets",
            "Conflict",
            "Reinterpretation",
            "Decision",
            "Legacy",
        ],
    },

    "Generational Conflict": {
        "category": "Family",
        "core_question": (
            "Can different generations preserve what matters "
            "without repeating old failures?"
        ),
        "stages": [
            "Difference established",
            "Trigger",
            "Value conflict",
            "Escalation",
            "Past revealed",
            "Break",
            "Recognition",
            "New relationship",
        ],
    },

    "Estranged Family": {
        "category": "Family",
        "core_question": (
            "Can people reconnect after years of distance and unresolved harm?"
        ),
        "stages": [
            "Estrangement established",
            "Forced contact",
            "Defensiveness",
            "Shared pressure",
            "Old wound exposed",
            "Choice",
            "Repair or permanent separation",
        ],
    },

    "Forbidden Love": {
        "category": "Relationship",
        "core_question": (
            "What is the cost of choosing love against social, familial, "
            "political, or moral boundaries?"
        ),
        "stages": [
            "Connection",
            "Boundary identified",
            "Secret relationship",
            "Deepening attachment",
            "Exposure risk",
            "Choice",
            "Sacrifice",
            "Outcome",
        ],
    },

    "Love Triangle": {
        "category": "Relationship",
        "core_question": (
            "What does each relationship reveal about what the protagonist truly wants?"
        ),
        "stages": [
            "Existing attachment",
            "Second connection",
            "Comparison",
            "Growing conflict",
            "Deception or indecision",
            "Exposure",
            "Choice",
            "Consequences",
        ],
    },

    "Enemies to Allies": {
        "category": "Relationship",
        "core_question": (
            "Can people with incompatible loyalties cooperate when they need each other?"
        ),
        "stages": [
            "Hostility",
            "Forced cooperation",
            "Distrust",
            "First success",
            "Personal revelation",
            "Trust test",
            "Shared risk",
            "Alliance",
        ],
    },

    "Friends to Enemies": {
        "category": "Relationship",
        "core_question": (
            "What can destroy a bond that once seemed permanent?"
        ),
        "stages": [
            "Friendship",
            "Difference",
            "First fracture",
            "Competing loyalties",
            "Betrayal",
            "Open conflict",
            "Final confrontation",
            "Aftermath",
        ],
    },

    "Rivalry": {
        "category": "Relationship",
        "core_question": (
            "Does competition improve the characters or consume them?"
        ),
        "stages": [
            "Comparison",
            "Challenge",
            "Escalation",
            "Personalization",
            "Crossed boundary",
            "Cost",
            "Final contest",
            "New relationship",
        ],
    },

    "Mentor and Protégé": {
        "category": "Relationship",
        "core_question": (
            "What happens when the student no longer needs, trusts, "
            "or agrees with the teacher?"
        ),
        "stages": [
            "Mentorship",
            "Learning",
            "Dependence",
            "Difference emerges",
            "Challenge",
            "Break",
            "Independent test",
            "New relationship",
        ],
    },

    "Broken Partnership": {
        "category": "Relationship",
        "core_question": (
            "Can people who once depended on each other work together again?"
        ),
        "stages": [
            "Past partnership",
            "Break established",
            "Forced reunion",
            "Distrust",
            "Old strength returns",
            "Old wound returns",
            "Decision",
            "Repair or final separation",
        ],
    },

    "Reconciliation": {
        "category": "Relationship",
        "core_question": (
            "What must be acknowledged before forgiveness becomes possible?"
        ),
        "stages": [
            "Distance",
            "Contact",
            "Resistance",
            "Shared experience",
            "Truth",
            "Responsibility",
            "Choice",
            "New relationship",
        ],
    },

    "Loyalty Tested": {
        "category": "Relationship",
        "core_question": (
            "What happens when loyalty to one person requires betrayal of another?"
        ),
        "stages": [
            "Loyalty established",
            "Competing obligation",
            "First compromise",
            "Pressure",
            "Impossible choice",
            "Decision",
            "Consequences",
        ],
    },

    "Community vs Individual": {
        "category": "Social",
        "core_question": (
            "When does belonging become conformity, and when does independence become betrayal?"
        ),
        "stages": [
            "Community norms",
            "Individual difference",
            "Pressure",
            "Public conflict",
            "Isolation",
            "Choice",
            "Community response",
            "New balance",
        ],
    },


    # -----------------------------------------------------
    # ADVENTURE / DISCOVERY
    # -----------------------------------------------------

    "Expedition": {
        "category": "Adventure",
        "core_question": (
            "Can the group reach the objective before environment, conflict, "
            "or human weakness destroys the mission?"
        ),
        "stages": [
            "Objective",
            "Team formation",
            "Departure",
            "Early obstacle",
            "Internal conflict",
            "Major environmental threat",
            "Final approach",
            "Discovery or failure",
            "Return",
        ],
    },

    "Discovery": {
        "category": "Adventure / Mystery",
        "core_question": (
            "What happens when the protagonist uncovers something "
            "that changes their understanding of the world?"
        ),
        "stages": [
            "Anomaly",
            "Curiosity",
            "First discovery",
            "Implications",
            "Opposition",
            "Deeper truth",
            "Decision",
            "Consequences",
        ],
    },

    "Lost World": {
        "category": "Adventure",
        "core_question": (
            "What hidden society, place, or system exists beyond the known world?"
        ),
        "stages": [
            "Rumour",
            "Journey",
            "Entry",
            "Wonder",
            "Rules discovered",
            "Danger",
            "Truth",
            "Escape or integration",
        ],
    },

    "Journey Home": {
        "category": "Adventure",
        "core_question": (
            "Can the protagonist return home after the journey has changed them?"
        ),
        "stages": [
            "Separation",
            "Journey begins",
            "Obstacle",
            "Loss",
            "Adaptation",
            "Final barrier",
            "Return",
            "Changed relationship to home",
        ],
    },

    "Treasure Hunt": {
        "category": "Adventure",
        "core_question": (
            "What is the true value of what everyone is trying to find?"
        ),
        "stages": [
            "Clue",
            "Decision to pursue",
            "Competition",
            "Puzzle or obstacle",
            "False lead",
            "Major discovery",
            "Final race",
            "Treasure",
            "Meaning of reward",
        ],
    },

    "Race Against Time": {
        "category": "Thriller",
        "core_question": (
            "Can the protagonist solve the problem before an irreversible deadline?"
        ),
        "stages": [
            "Deadline established",
            "Initial plan",
            "First obstacle",
            "Time loss",
            "Escalation",
            "Critical setback",
            "Final attempt",
            "Deadline outcome",
        ],
    },

    "Disaster": {
        "category": "Adventure / Survival",
        "core_question": (
            "Who do people become when normal systems suddenly fail?"
        ),
        "stages": [
            "Normal world",
            "Warning",
            "Disaster",
            "Immediate survival",
            "Systems collapse",
            "Human conflict",
            "Final danger",
            "Aftermath",
        ],
    },

    "Siege": {
        "category": "Conflict",
        "core_question": (
            "How long can the defenders resist pressure from outside "
            "and division from within?"
        ),
        "stages": [
            "Encirclement",
            "Defence",
            "Resource pressure",
            "Internal division",
            "Breach",
            "Desperation",
            "Final stand",
            "Outcome",
        ],
    },

    "War Mission": {
        "category": "Adventure / Conflict",
        "core_question": (
            "Can the mission succeed when military objectives conflict "
            "with human consequences?"
        ),
        "stages": [
            "Mission assigned",
            "Team assembled",
            "Insertion",
            "Complication",
            "Moral conflict",
            "Mission threatened",
            "Final objective",
            "Extraction and consequence",
        ],
    },

    "Frontier": {
        "category": "Adventure / Social",
        "core_question": (
            "What happens when people try to impose order on a place "
            "where institutions are weak or changing?"
        ),
        "stages": [
            "Arrival",
            "Opportunity",
            "Local rules",
            "Conflict",
            "Claim or settlement",
            "Resistance",
            "Final struggle",
            "New order",
        ],
    },
}


# =========================================================
# CHARACTER ARCS
# =========================================================

CHARACTER_ARCS = {
    "Redemption": {
        "core_change": "From guilt or failure toward earned responsibility.",
    },

    "Corruption": {
        "core_change": "From compromise toward moral collapse.",
    },

    "Disillusionment": {
        "core_change": "From idealism toward a more painful understanding of reality.",
    },

    "Coming of Age": {
        "core_change": "From dependence or innocence toward adult responsibility.",
    },

    "Self-Acceptance": {
        "core_change": "From rejection of self toward honest acceptance.",
    },

    "Loss of Innocence": {
        "core_change": "From protected worldview toward awareness of moral complexity.",
    },

    "Recovery": {
        "core_change": "From damage or dysfunction toward functioning and connection.",
    },

    "Obsession": {
        "core_change": "From focused desire toward destructive fixation.",
    },

    "Reconciliation": {
        "core_change": "From emotional separation toward renewed connection.",
    },

    "Liberation": {
        "core_change": "From control or dependency toward autonomy.",
    },

    "Moral Awakening": {
        "core_change": "From passive complicity toward conscious moral action.",
    },

    "Fall From Grace": {
        "core_change": "From respected position toward exposure, failure, or disgrace.",
    },

    "Rise to Responsibility": {
        "core_change": "From avoidance toward leadership and duty.",
    },

    "Identity Discovery": {
        "core_change": "From uncertainty about self toward a chosen identity.",
    },

    "Acceptance of Mortality": {
        "core_change": "From denial of death toward meaningful acceptance.",
    },

    "Learning to Trust": {
        "core_change": "From guarded independence toward chosen vulnerability.",
    },

    "Learning to Lead": {
        "core_change": "From individual action toward responsibility for others.",
    },

    "Breaking the Cycle": {
        "core_change": "From repeating inherited behaviour toward conscious change.",
    },

    "Reclaiming Identity": {
        "core_change": "From imposed identity toward a self-defined life.",
    },

    "Steadfast Arc": {
        "core_change": (
            "The protagonist changes the world around them more than "
            "they change internally."
        ),
    },
}


# =========================================================
# RELATIONSHIP ARCS
# =========================================================

RELATIONSHIP_ARCS = {
    "None": {
        "description": "No major relationship arc selected.",
    },

    "Strangers to Allies": {
        "description": "Two strangers develop functional trust under pressure.",
    },

    "Allies to Friends": {
        "description": "Practical cooperation develops into genuine personal loyalty.",
    },

    "Friends to Enemies": {
        "description": "A close relationship fractures into active opposition.",
    },

    "Enemies to Allies": {
        "description": "Opponents are forced into cooperation and gradually gain trust.",
    },

    "Enemies to Lovers": {
        "description": "Conflict evolves into attraction and intimacy.",
    },

    "Mentor to Rival": {
        "description": "Teacher and student become competitors or ideological opponents.",
    },

    "Estranged Parent and Child": {
        "description": "A damaged parent-child relationship moves toward repair or final separation.",
    },

    "Estranged Family to Reconciliation": {
        "description": "Family members confront the reasons they became separated.",
    },

    "Trust to Betrayal": {
        "description": "A trusted bond is destroyed by hidden motives or competing loyalties.",
    },

    "Betrayal to Forgiveness": {
        "description": "A damaged relationship tests whether trust can ever be rebuilt.",
    },

    "Partners to Rivals": {
        "description": "Shared ambition turns former partners into competitors.",
    },

    "Rivals to Mutual Respect": {
        "description": "Competition remains, but contempt develops into respect.",
    },

    "Dependency to Independence": {
        "description": "One person learns to function without emotional or practical dependence.",
    },

    "Protector to Equal": {
        "description": "An unequal protective relationship becomes a partnership between equals.",
    },

    "Marriage Breakdown": {
        "description": "A marriage deteriorates under unresolved emotional or external pressure.",
    },

    "Forbidden Relationship": {
        "description": "A relationship conflicts with social, familial, legal, or moral expectations.",
    },

    "Unrequited Love": {
        "description": "One-sided love forces acceptance, change, or self-deception.",
    },

    "Love to Sacrifice": {
        "description": "Love culminates in a meaningful personal sacrifice.",
    },

    "Loyalty Tested": {
        "description": "A relationship is tested by incompatible obligations.",
    },

    "Found Family": {
        "description": "Unrelated characters gradually form a chosen family structure.",
    },
}


# =========================================================
# MYSTERY ENGINES
# =========================================================

MYSTERY_ENGINES = {
    "None": {
        "core_question": "No mystery structure selected.",
        "stages": [],
    },

    "Hidden Identity": {
        "core_question": "Who is this person really?",
        "stages": [
            "Inconsistency",
            "Suspicion",
            "Partial clue",
            "Misdirection",
            "Identity pressure",
            "Reveal",
        ],
    },

    "Missing Person": {
        "core_question": "What happened to the missing person?",
        "stages": [
            "Disappearance",
            "Initial search",
            "Contradictory evidence",
            "Hidden life discovered",
            "False explanation",
            "Truth",
        ],
    },

    "Unknown Killer": {
        "core_question": "Who committed the killing, and why?",
        "stages": [
            "Crime",
            "Suspects",
            "Evidence",
            "False lead",
            "New victim or escalation",
            "Critical clue",
            "Identification",
            "Confrontation",
        ],
    },

    "Buried Crime": {
        "core_question": "What crime from the past was hidden, and who benefited?",
        "stages": [
            "Past disturbance resurfaces",
            "First clue",
            "Resistance",
            "Old relationships examined",
            "Cover story fails",
            "Truth exposed",
        ],
    },

    "Family Secret": {
        "core_question": "What truth has the family protected from outsiders or itself?",
        "stages": [
            "Odd behaviour",
            "Contradictory memory",
            "Hidden evidence",
            "Family resistance",
            "Partial revelation",
            "Full truth",
        ],
    },

    "Political Conspiracy": {
        "core_question": "Who benefits from the hidden political operation?",
        "stages": [
            "Anomaly",
            "Institutional resistance",
            "Connection",
            "Misdirection",
            "Powerful figure implicated",
            "System exposed",
        ],
    },

    "Corporate Conspiracy": {
        "core_question": "What is the organization hiding and why?",
        "stages": [
            "Suspicious event",
            "Internal contradiction",
            "Documents or witness",
            "Suppression",
            "Broader scheme",
            "Exposure",
        ],
    },

    "False Accusation": {
        "core_question": "Who created the false narrative and why?",
        "stages": [
            "Accusation",
            "Evidence appears convincing",
            "Contradiction",
            "Alternative suspect",
            "Hidden motive",
            "Truth",
        ],
    },

    "Unreliable Witness": {
        "core_question": "Which parts of the witness account can be trusted?",
        "stages": [
            "Testimony",
            "Inconsistency",
            "Alternative explanation",
            "New evidence",
            "Reason for distortion",
            "Truth reconstructed",
        ],
    },

    "Hidden Motive": {
        "core_question": "Why did the apparent event really happen?",
        "stages": [
            "Surface motive",
            "Contradiction",
            "Secondary motive",
            "Misdirection",
            "Personal connection",
            "True motive",
        ],
    },

    "Past Crime Returns": {
        "core_question": "Why has an old crime become dangerous again now?",
        "stages": [
            "Present disturbance",
            "Past connection",
            "Old participants",
            "Suppressed evidence",
            "New danger",
            "Truth and consequence",
        ],
    },

    "Locked-Room Mystery": {
        "core_question": "How could the crime have happened under apparently impossible conditions?",
        "stages": [
            "Impossible event",
            "Physical constraints",
            "Suspects",
            "False mechanism",
            "Critical overlooked detail",
            "Solution",
        ],
    },

    "Multiple Suspects": {
        "core_question": "Which plausible suspect is actually responsible?",
        "stages": [
            "Crime",
            "Suspect field",
            "Evidence against several",
            "Misdirection",
            "Suspect eliminated",
            "Hidden connection",
            "Responsible party revealed",
        ],
    },

    "False Solution": {
        "core_question": "Why does the apparent solution fail to explain everything?",
        "stages": [
            "Mystery",
            "Evidence",
            "Apparent solution",
            "Celebration or closure",
            "Contradiction",
            "Deeper investigation",
            "True solution",
        ],
    },

    "Double Betrayal": {
        "core_question": "Who is betraying whom, and which betrayal is the real one?",
        "stages": [
            "Trust",
            "First betrayal",
            "Reaction",
            "Second layer revealed",
            "Loyalties reassessed",
            "True betrayal exposed",
        ],
    },

    "Secret Organization": {
        "core_question": "Who belongs to the hidden organization and what does it want?",
        "stages": [
            "Symbol or anomaly",
            "Rumour",
            "Evidence",
            "Hidden members",
            "Purpose revealed",
            "Confrontation",
        ],
    },

    "Hidden Inheritance": {
        "core_question": "Who truly has a claim to the inheritance or legacy?",
        "stages": [
            "Inheritance issue",
            "Unexpected evidence",
            "Competing claims",
            "Suppressed history",
            "Identity or document reveal",
            "Final claim",
        ],
    },

    "Disappearance": {
        "core_question": "Did the person leave willingly, vanish accidentally, or become a victim?",
        "stages": [
            "Disappearance",
            "Search",
            "Conflicting signs",
            "Hidden activity",
            "False assumption",
            "Truth",
        ],
    },

    "Unknown Parentage": {
        "core_question": "Who are the protagonist's biological or true parents?",
        "stages": [
            "Identity doubt",
            "Family resistance",
            "Evidence",
            "False assumption",
            "Hidden relationship",
            "Truth",
        ],
    },

    "Cover-Up": {
        "core_question": "What event is being concealed, by whom, and why?",
        "stages": [
            "Visible inconsistency",
            "First lie",
            "Evidence removed",
            "Witness pressure",
            "Cover-up expands",
            "Truth exposed",
        ],
    },
}


# =========================================================
# HELPER LISTS FOR STREAMLIT DROPDOWNS
# =========================================================

PLOT_ENGINE_NAMES = list(PLOT_ENGINES.keys())

CHARACTER_ARC_NAMES = list(CHARACTER_ARCS.keys())

RELATIONSHIP_ARC_NAMES = list(RELATIONSHIP_ARCS.keys())

MYSTERY_ENGINE_NAMES = list(MYSTERY_ENGINES.keys())

STRUCTURE_COMPLEXITY_NAMES = list(STRUCTURE_COMPLEXITY.keys())


# =========================================================
# HELPER FUNCTIONS
# =========================================================

def get_plot_engine(name):
    return PLOT_ENGINES.get(name, {})


def get_character_arc(name):
    return CHARACTER_ARCS.get(name, {})


def get_relationship_arc(name):
    return RELATIONSHIP_ARCS.get(name, {})


def get_mystery_engine(name):
    return MYSTERY_ENGINES.get(name, {})


def get_structure_complexity(name):
    return STRUCTURE_COMPLEXITY.get(name, {})