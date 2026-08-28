import re


# =========================================================
# NAME REPLACEMENT UTILITIES
# =========================================================


def replace_exact_name(
    text,
    old_name,
    new_name,
):
    """
    Replace a name using word boundaries so short names do not
    accidentally replace parts of unrelated words.
    """

    if not text:
        return text

    if not old_name.strip():
        return text

    old_name = old_name.strip()
    new_name = new_name.strip()

    pattern = (
        r"(?<!\w)"
        + re.escape(old_name)
        + r"(?!\w)"
    )

    return re.sub(
        pattern,
        new_name,
        text,
    )


def count_exact_name(
    text,
    name,
):
    if not text:
        return 0

    if not name.strip():
        return 0

    pattern = (
        r"(?<!\w)"
        + re.escape(name.strip())
        + r"(?!\w)"
    )

    return len(
        re.findall(
            pattern,
            text,
        )
    )


def build_name_replacements(
    old_name,
    new_name,
    replace_first_name=True,
    replace_surname=False,
):
    """
    Build replacement pairs.

    Full name is always replaced.

    First-name-only and surname-only replacements are optional.
    """

    old_name = old_name.strip()
    new_name = new_name.strip()

    replacements = [
        (
            old_name,
            new_name,
        )
    ]

    old_parts = old_name.split()
    new_parts = new_name.split()

    if (
        replace_first_name
        and len(old_parts) >= 1
        and len(new_parts) >= 1
    ):

        old_first = old_parts[0]
        new_first = new_parts[0]

        if old_first != new_first:

            replacements.append(
                (
                    old_first,
                    new_first,
                )
            )

    if (
        replace_surname
        and len(old_parts) >= 2
        and len(new_parts) >= 2
    ):

        old_last = old_parts[-1]
        new_last = new_parts[-1]

        if old_last != new_last:

            replacements.append(
                (
                    old_last,
                    new_last,
                )
            )

    # Longest names first.
    # This prevents "Daniel" being replaced before
    # "Daniel Mercer".

    replacements.sort(
        key=lambda pair: len(pair[0]),
        reverse=True,
    )

    return replacements


def rename_text(
    text,
    replacements,
):

    result = text or ""

    for old_name, new_name in replacements:

        result = replace_exact_name(
            result,
            old_name,
            new_name,
        )

    return result

# =========================================================
# CHARACTER NAME DETECTION
# =========================================================

def _looks_like_character_name(
    value,
):
    """
    Conservative check for plausible human character names.
    """

    if not value:
        return False

    value = value.strip()

    words = value.split()

    if not 2 <= len(words) <= 5:
        return False

    excluded_words = {
        "Character",
        "Relationship",
        "Information",
        "Goal",
        "Need",
        "History",
        "Experience",
        "Behaviour",
        "Characteristics",
        "Supporting",
        "Minor",
        "Major",
        "Protagonist",
        "Antagonist",
        "Characters",
    }

    if any(
        word in excluded_words
        for word in words
    ):
        return False

    # Accept names containing hyphens/apostrophes,
    # e.g. Jean-Luc Picard or Patrick O'Brien.

    for word in words:

        cleaned = (
            word
            .replace("-", "")
            .replace("'", "")
            .replace("’", "")
        )

        if not cleaned:
            return False

        if not cleaned[0].isupper():
            return False

        if not cleaned.isalpha():
            return False

    return True

def extract_character_names(
    character_bible="",
    user_characters="",
):
    """
    Extract character names.

    Priority:
    1. Explicit CHARACTER INDEX
    2. Character profile headings
    3. User supplied character list

    The Character Index is the authoritative source.
    """

    names = set()

    bible = character_bible or ""

    # =====================================================
    # 1. CHARACTER INDEX
    # =====================================================

    inside_index = False

    for line in bible.splitlines():

        stripped = line.strip()

        if stripped.upper() == "# CHARACTER INDEX":

            inside_index = True
            continue

        if inside_index:

            # The next top-level Markdown heading ends the index.

            if (
                stripped.startswith("# ")
                and stripped.upper()
                != "# CHARACTER INDEX"
            ):

                inside_index = False
                continue

            if stripped.startswith("- "):

                entry = stripped[2:].strip()

                # Expected:
                # Daniel Mercer | Protagonist | Major

                if "|" in entry:

                    possible_name = (
                        entry.split(
                            "|",
                            1,
                        )[0]
                        .strip()
                    )

                else:

                    possible_name = entry

                if _looks_like_character_name(
                    possible_name
                ):

                    names.add(
                        possible_name
                    )

    # =====================================================
    # 2. PROFILE HEADINGS
    # =====================================================

    excluded_headings = {
        "CHARACTER INDEX",
        "CHARACTER RELATIONSHIP MAP",
        "MINOR CHARACTERS",
        "Story Role",
        "Basic Information",
        "Personality",
        "External Goal",
        "Internal Need",
        "Strength",
        "Primary Flaw",
        "Fear",
        "Emotional Wound",
        "Personal History",
        "Defining Experience",
        "Secret",
        "Moral Boundary",
        "Pressure Point",
        "Contradictions",
        "Relationships",
        "Character Arc",
        "Dialogue Behaviour",
        "Dialogue Characteristics",
    }

    for line in bible.splitlines():

        stripped = line.strip()

        # We only want top-level profile headings.
        if not stripped.startswith("# "):
            continue

        heading = (
            stripped[2:].strip()
        )

        if heading in excluded_headings:
            continue

        if heading.upper() in excluded_headings:
            continue

        if _looks_like_character_name(
            heading
        ):

            names.add(
                heading
            )

    # =====================================================
    # 3. USER CHARACTER LIST
    # =====================================================

    for line in (
        user_characters or ""
    ).splitlines():

        stripped = line.strip()

        if not stripped:
            continue

        possible_name = stripped

        # Daniel Mercer - retired police officer

        if " - " in possible_name:

            possible_name = (
                possible_name.split(
                    " - ",
                    1,
                )[0]
                .strip()
            )

        # Daniel Mercer: retired police officer

        elif ":" in possible_name:

            possible_name = (
                possible_name.split(
                    ":",
                    1,
                )[0]
                .strip()
            )

        # Daniel Mercer | protagonist

        elif "|" in possible_name:

            possible_name = (
                possible_name.split(
                    "|",
                    1,
                )[0]
                .strip()
            )

        # Remove common bullet markers.

        possible_name = (
            possible_name
            .lstrip("-*0123456789. ")
            .strip()
        )

        if _looks_like_character_name(
            possible_name
        ):

            names.add(
                possible_name
            )

    return sorted(
        names
    )

    # -----------------------------------------------------
    # MARKDOWN HEADINGS
    # -----------------------------------------------------

    for line in (character_bible or "").splitlines():

        stripped = line.strip()

        if not stripped.startswith("#"):
            continue

        heading = stripped.lstrip("#").strip()

        if not heading:
            continue

        if heading in excluded_headings:
            continue

        words = heading.split()

        # Most fictional names should be 2-4 words.
        if not 2 <= len(words) <= 4:
            continue

        # Require every word to begin with an uppercase letter.
        if all(
            word[0].isupper()
            for word in words
            if word
        ):
            names.add(heading)

    # -----------------------------------------------------
    # USER CHARACTER LIST
    # -----------------------------------------------------

    for line in (user_characters or "").splitlines():

        stripped = line.strip()

        if not stripped:
            continue

        # Supports:
        # Daniel Mercer - 58, former police officer
        # Daniel Mercer: retired police officer
        # Daniel Mercer

        possible_name = stripped

        if " - " in possible_name:
            possible_name = possible_name.split(
                " - ",
                1,
            )[0]

        elif ":" in possible_name:
            possible_name = possible_name.split(
                ":",
                1,
            )[0]

        possible_name = possible_name.strip()

        words = possible_name.split()

        if 2 <= len(words) <= 4:

            if all(
                word[0].isupper()
                for word in words
                if word
            ):
                names.add(
                    possible_name
                )

    return sorted(names)