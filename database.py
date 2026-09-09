import sqlite3
from datetime import datetime


DB_FILE = "ai_novelist.db"


def get_connection():
    return sqlite3.connect(DB_FILE)


def initialise_database():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS projects (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            plot TEXT,
            plot_type TEXT,
            genre TEXT,
            region TEXT,
            period TEXT,
            characters TEXT,
            word_count INTEGER,
            story_architecture TEXT,
            character_bible TEXT,
            world_bible TEXT,
            timeline TEXT,
            created_at TEXT,
            updated_at TEXT
        )
        """
    )

    connection.commit()

    # Add missing columns if upgrading an older database
    cursor.execute("PRAGMA table_info(projects)")
    existing_columns = {
        row[1]
        for row in cursor.fetchall()
    }

    if "world_bible" not in existing_columns:
        cursor.execute(
            "ALTER TABLE projects ADD COLUMN world_bible TEXT"
        )
    if "primary_plot" not in existing_columns:
        cursor.execute(
            "ALTER TABLE projects ADD COLUMN primary_plot TEXT"
        )

    if "secondary_plot" not in existing_columns:
        cursor.execute(
            "ALTER TABLE projects ADD COLUMN secondary_plot TEXT"
        )

    if "character_arc" not in existing_columns:
        cursor.execute(
            "ALTER TABLE projects ADD COLUMN character_arc TEXT"
        )

    if "relationship_arc" not in existing_columns:
        cursor.execute(
            "ALTER TABLE projects ADD COLUMN relationship_arc TEXT"
        )

    if "mystery_engine" not in existing_columns:
        cursor.execute(
            "ALTER TABLE projects ADD COLUMN mystery_engine TEXT"
        )

    if "structure_complexity" not in existing_columns:
        cursor.execute(
            "ALTER TABLE projects ADD COLUMN structure_complexity TEXT"
        )
    if "timeline" not in existing_columns:
        cursor.execute(
            "ALTER TABLE projects ADD COLUMN timeline TEXT"
        )

    connection.commit()
    connection.close()


def create_project(book, memory):
    connection = get_connection()
    cursor = connection.cursor()

    now = datetime.now().isoformat(timespec="seconds")

    cursor.execute(
        """
        INSERT INTO projects (
            title,
            plot,
            plot_type,
            genre,
            region,
            period,
            characters,
            word_count,
            story_architecture,
            character_bible,
            world_bible,
            timeline,
            created_at,
            updated_at
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            book["title"],
            book["plot"],
            book["plot_type"],
            book["genre"],
            book["region"],
            book["period"],
            book["characters"],
            book["word_count"],
            memory.get("story_architecture", ""),
            memory.get("character_bible", ""),
            memory.get("world_bible", ""),
            memory.get("timeline", ""),
            now,
            now,
        ),
    )

    project_id = cursor.lastrowid

    connection.commit()
    connection.close()

    return project_id


def update_project(
    project_id,
    book,
    memory,
):
    connection = get_connection()
    cursor = connection.cursor()

    now = datetime.now().isoformat(
        timespec="seconds"
    )

    cursor.execute(
        """
        UPDATE projects
        SET
            title = ?,
            plot = ?,
            plot_type = ?,
            genre = ?,
            region = ?,
            period = ?,
            characters = ?,
            word_count = ?,

            primary_plot = ?,
            secondary_plot = ?,
            character_arc = ?,
            relationship_arc = ?,
            mystery_engine = ?,
            structure_complexity = ?,

            story_architecture = ?,
            character_bible = ?,
            world_bible = ?,
            timeline = ?,

            updated_at = ?

        WHERE id = ?
        """,
        (
            book["title"],
            book["plot"],
            book.get("plot_type", ""),
            book["genre"],
            book["region"],
            book["period"],
            book["characters"],
            book["word_count"],

            book.get(
                "primary_plot",
                book.get(
                    "plot_type",
                    "Overcoming the Monster"
                ),
            ),

            book.get(
                "secondary_plot",
                "None",
            ),

            book.get(
                "character_arc",
                "Redemption",
            ),

            book.get(
                "relationship_arc",
                "None",
            ),

            book.get(
                "mystery_engine",
                "None",
            ),

            book.get(
                "structure_complexity",
                "Standard",
            ),

            memory.get(
                "story_architecture",
                "",
            ),

            memory.get(
                "character_bible",
                "",
            ),

            memory.get(
                "world_bible",
                "",
            ),

            memory.get(
                "timeline",
                "",
            ),

            now,
            project_id,
        ),
    )

    connection.commit()
    connection.close()
def get_all_projects():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT id, title, updated_at
        FROM projects
        ORDER BY updated_at DESC
        """
    )

    projects = cursor.fetchall()

    connection.close()

    return projects


def load_project(project_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT
            id,
            title,
            plot,
            plot_type,
            genre,
            region,
            period,
            characters,
            word_count,

            primary_plot,
            secondary_plot,
            character_arc,
            relationship_arc,
            mystery_engine,
            structure_complexity,

            story_architecture,
            character_bible,
            world_bible,
            timeline,

            created_at,
            updated_at

        FROM projects

        WHERE id = ?
        """,
        (project_id,),
    )

    row = cursor.fetchone()

    connection.close()

    if not row:
        return None

    return {
        "id": row[0],
        "title": row[1],
        "plot": row[2] or "",
        "plot_type": row[3] or "",
        "genre": row[4] or "",
        "region": row[5] or "",
        "period": row[6] or "",
        "characters": row[7] or "",
        "word_count": row[8] or 80000,

        "primary_plot": (
            row[9]
            or row[3]
            or "Overcoming the Monster"
        ),

        "secondary_plot": (
            row[10]
            or "None"
        ),

        "character_arc": (
            row[11]
            or "Redemption"
        ),

        "relationship_arc": (
            row[12]
            or "None"
        ),

        "mystery_engine": (
            row[13]
            or "None"
        ),

        "structure_complexity": (
            row[14]
            or "Standard"
        ),

        "story_architecture": (
            row[15] or ""
        ),

        "character_bible": (
            row[16] or ""
        ),

        "world_bible": (
            row[17] or ""
        ),

        "timeline": (
            row[18] or ""
        ),

        "created_at": row[19],
        "updated_at": row[20],
    }
def delete_project(project_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM projects WHERE id = ?",
        (project_id,),
    )

    connection.commit()
    connection.close()

   # =========================================================
# CHAPTER DATABASE
# =========================================================


# =========================================================
# CHAPTER DATABASE
# =========================================================


def initialise_chapter_database():
    """
    Create the chapters table if it does not already exist.
    """

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS chapters (
            id INTEGER PRIMARY KEY AUTOINCREMENT,

            project_id INTEGER NOT NULL,

            chapter_number INTEGER NOT NULL,

            title TEXT,

            chapter_plan TEXT,

            scene_plan TEXT,

            draft TEXT,

            edited_draft TEXT,

            continuity_report TEXT,

            chapter_summary TEXT,

            status TEXT DEFAULT 'planned',

            created_at TEXT,

            updated_at TEXT,

            UNIQUE(project_id, chapter_number),

            FOREIGN KEY(project_id)
                REFERENCES projects(id)
                ON DELETE CASCADE
        )
        """
    )

    connection.commit()
    connection.close()


# =========================================================
# CREATE CHAPTER
# =========================================================


def create_chapter(
    project_id,
    chapter_number,
    title="",
    chapter_plan="",
):

    connection = get_connection()
    cursor = connection.cursor()

    now = datetime.now().isoformat(
        timespec="seconds"
    )

    cursor.execute(
        """
        INSERT INTO chapters (
            project_id,
            chapter_number,
            title,
            chapter_plan,
            scene_plan,
            draft,
            edited_draft,
            continuity_report,
            chapter_summary,
            status,
            created_at,
            updated_at
        )

        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            project_id,
            chapter_number,
            title,
            chapter_plan,
            "",
            "",
            "",
            "",
            "",
            "planned",
            now,
            now,
        ),
    )

    chapter_id = cursor.lastrowid

    connection.commit()
    connection.close()

    return chapter_id


# =========================================================
# SAVE / UPDATE CHAPTER
# =========================================================


def save_chapter(
    project_id,
    chapter_number,
    title="",
    chapter_plan="",
    scene_plan="",
    draft="",
    edited_draft="",
    continuity_report="",
    chapter_summary="",
    status="planned",
):

    connection = get_connection()
    cursor = connection.cursor()

    now = datetime.now().isoformat(
        timespec="seconds"
    )

    cursor.execute(
        """
        INSERT INTO chapters (
            project_id,
            chapter_number,
            title,
            chapter_plan,
            scene_plan,
            draft,
            edited_draft,
            continuity_report,
            chapter_summary,
            status,
            created_at,
            updated_at
        )

        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)

        ON CONFLICT(project_id, chapter_number)

        DO UPDATE SET

            title = excluded.title,
            chapter_plan = excluded.chapter_plan,
            scene_plan = excluded.scene_plan,
            draft = excluded.draft,
            edited_draft = excluded.edited_draft,
            continuity_report = excluded.continuity_report,
            chapter_summary = excluded.chapter_summary,
            status = excluded.status,
            updated_at = excluded.updated_at
        """,
        (
            project_id,
            chapter_number,
            title,
            chapter_plan,
            scene_plan,
            draft,
            edited_draft,
            continuity_report,
            chapter_summary,
            status,
            now,
            now,
        ),
    )

    connection.commit()
    connection.close()


# =========================================================
# LOAD ONE CHAPTER
# =========================================================


def load_chapter(
    project_id,
    chapter_number,
):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT
            id,
            project_id,
            chapter_number,
            title,
            chapter_plan,
            scene_plan,
            draft,
            edited_draft,
            continuity_report,
            chapter_summary,
            status,
            created_at,
            updated_at

        FROM chapters

        WHERE
            project_id = ?
            AND chapter_number = ?
        """,
        (
            project_id,
            chapter_number,
        ),
    )

    row = cursor.fetchone()

    connection.close()

    if not row:
        return None

    return {
        "id": row[0],
        "project_id": row[1],
        "chapter_number": row[2],
        "title": row[3] or "",
        "chapter_plan": row[4] or "",
        "scene_plan": row[5] or "",
        "draft": row[6] or "",
        "edited_draft": row[7] or "",
        "continuity_report": row[8] or "",
        "chapter_summary": row[9] or "",
        "status": row[10] or "",
        "created_at": row[11],
        "updated_at": row[12],
    }


# =========================================================
# LOAD ALL CHAPTERS
# =========================================================


def get_project_chapters(project_id):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT
            chapter_number,
            title,
            status,
            updated_at

        FROM chapters

        WHERE project_id = ?

        ORDER BY chapter_number ASC
        """,
        (project_id,),
    )

    rows = cursor.fetchall()

    connection.close()

    return rows


# =========================================================
# DELETE CHAPTER
# =========================================================


def delete_chapter(
    project_id,
    chapter_number,
):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        DELETE FROM chapters

        WHERE
            project_id = ?
            AND chapter_number = ?
        """,
        (
            project_id,
            chapter_number,
        ),
    )

    connection.commit()
    connection.close()


# =========================================================
# PREVIOUS CHAPTER SUMMARIES
# =========================================================


def get_previous_chapter_summaries(
    project_id,
    before_chapter,
):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT
            chapter_number,
            chapter_summary

        FROM chapters

        WHERE
            project_id = ?
            AND chapter_number < ?
            AND chapter_summary != ''

        ORDER BY chapter_number ASC
        """,
        (
            project_id,
            before_chapter,
        ),
    )

    rows = cursor.fetchall()

    connection.close()

    summaries = []

    for chapter_number, summary in rows:

        summaries.append(
            f"""
CHAPTER {chapter_number}

{summary}
"""
        )

    return "\n".join(summaries)


# =========================================================
# LATEST CHAPTER
# =========================================================


def get_latest_chapter_number(project_id):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT MAX(chapter_number)

        FROM chapters

        WHERE project_id = ?
        """,
        (project_id,),
    )

    result = cursor.fetchone()

    connection.close()

    if not result:
        return 0

    if result[0] is None:
        return 0

    return result[0]

# =========================================================
# CHARACTER NAME MANAGEMENT
# =========================================================

from character_renamer import (
    build_name_replacements,
    rename_text,
    count_exact_name,
)


def initialise_character_rename_database():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS character_rename_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            project_id INTEGER NOT NULL,
            old_name TEXT NOT NULL,
            new_name TEXT NOT NULL,
            changed_at TEXT NOT NULL,

            FOREIGN KEY(project_id)
                REFERENCES projects(id)
                ON DELETE CASCADE
        )
        """
    )

    connection.commit()
    connection.close()


def count_character_name_occurrences(
    project_id,
    name,
):

    connection = get_connection()
    cursor = connection.cursor()

    total = 0

    # -----------------------------------------------------
    # PROJECT TEXT
    # -----------------------------------------------------

    cursor.execute(
        """
        SELECT
            plot,
            characters,
            story_architecture,
            character_bible,
            world_bible,
            timeline

        FROM projects

        WHERE id = ?
        """,
        (project_id,),
    )

    project = cursor.fetchone()

    if project:

        for value in project:

            total += count_exact_name(
                value or "",
                name,
            )

    # -----------------------------------------------------
    # CHAPTER TEXT
    # -----------------------------------------------------

    cursor.execute(
        """
        SELECT
            title,
            chapter_plan,
            scene_plan,
            draft,
            edited_draft,
            continuity_report,
            chapter_summary

        FROM chapters

        WHERE project_id = ?
        """,
        (project_id,),
    )

    rows = cursor.fetchall()

    for row in rows:

        for value in row:

            total += count_exact_name(
                value or "",
                name,
            )

    connection.close()

    return total


def rename_character_across_project(
    project_id,
    old_name,
    new_name,
    replace_first_name=True,
    replace_surname=False,
):

    old_name = old_name.strip()
    new_name = new_name.strip()

    if not old_name:
        raise ValueError(
            "Original character name is required."
        )

    if not new_name:
        raise ValueError(
            "New character name is required."
        )

    if old_name == new_name:
        raise ValueError(
            "The new name is the same as the old name."
        )

    replacements = build_name_replacements(
        old_name,
        new_name,
        replace_first_name,
        replace_surname,
    )

    connection = get_connection()
    cursor = connection.cursor()

    try:

        # -------------------------------------------------
        # LOAD PROJECT
        # -------------------------------------------------

        cursor.execute(
            """
            SELECT
                plot,
                characters,
                story_architecture,
                character_bible,
                world_bible,
                timeline

            FROM projects

            WHERE id = ?
            """,
            (project_id,),
        )

        project = cursor.fetchone()

        if not project:
            raise ValueError(
                "Project could not be found."
            )

        (
            plot,
            characters,
            story_architecture,
            character_bible,
            world_bible,
            timeline,
        ) = project

        # -------------------------------------------------
        # RENAME PROJECT MEMORY
        # -------------------------------------------------

        cursor.execute(
            """
            UPDATE projects

            SET
                plot = ?,
                characters = ?,
                story_architecture = ?,
                character_bible = ?,
                world_bible = ?,
                timeline = ?

            WHERE id = ?
            """,
            (
                rename_text(
                    plot,
                    replacements,
                ),

                rename_text(
                    characters,
                    replacements,
                ),

                rename_text(
                    story_architecture,
                    replacements,
                ),

                rename_text(
                    character_bible,
                    replacements,
                ),

                rename_text(
                    world_bible,
                    replacements,
                ),

                rename_text(
                    timeline,
                    replacements,
                ),

                project_id,
            ),
        )

        # -------------------------------------------------
        # LOAD CHAPTERS
        # -------------------------------------------------

        cursor.execute(
            """
            SELECT
                chapter_number,
                title,
                chapter_plan,
                scene_plan,
                draft,
                edited_draft,
                continuity_report,
                chapter_summary

            FROM chapters

            WHERE project_id = ?
            """,
            (project_id,),
        )

        chapters = cursor.fetchall()

        # -------------------------------------------------
        # UPDATE EACH CHAPTER
        # -------------------------------------------------

        for chapter in chapters:

            (
                chapter_number,
                title,
                chapter_plan,
                scene_plan,
                draft,
                edited_draft,
                continuity_report,
                chapter_summary,
            ) = chapter

            cursor.execute(
                """
                UPDATE chapters

                SET
                    title = ?,
                    chapter_plan = ?,
                    scene_plan = ?,
                    draft = ?,
                    edited_draft = ?,
                    continuity_report = ?,
                    chapter_summary = ?

                WHERE
                    project_id = ?
                    AND chapter_number = ?
                """,
                (
                    rename_text(
                        title,
                        replacements,
                    ),

                    rename_text(
                        chapter_plan,
                        replacements,
                    ),

                    rename_text(
                        scene_plan,
                        replacements,
                    ),

                    rename_text(
                        draft,
                        replacements,
                    ),

                    rename_text(
                        edited_draft,
                        replacements,
                    ),

                    rename_text(
                        continuity_report,
                        replacements,
                    ),

                    rename_text(
                        chapter_summary,
                        replacements,
                    ),

                    project_id,
                    chapter_number,
                ),
            )

        # -------------------------------------------------
        # HISTORY
        # -------------------------------------------------

        now = datetime.now().isoformat(
            timespec="seconds"
        )

        cursor.execute(
            """
            INSERT INTO character_rename_history (
                project_id,
                old_name,
                new_name,
                changed_at
            )

            VALUES (?, ?, ?, ?)
            """,
            (
                project_id,
                old_name,
                new_name,
                now,
            ),
        )

        connection.commit()

    except Exception:

        connection.rollback()

        raise

    finally:

        connection.close()


def get_character_rename_history(
    project_id,
):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT
            old_name,
            new_name,
            changed_at

        FROM character_rename_history

        WHERE project_id = ?

        ORDER BY id DESC
        """,
        (project_id,),
    )
# =========================================================
# CHARACTER RENAME PREVIEW
# =========================================================

def preview_character_rename(
    project_id,
    old_name,
    new_name,
    replace_first_name=True,
    replace_surname=False,
):
    """
    Preview how many references will be affected by a rename.

    Returns counts for:
    - full name
    - first name
    - surname
    - total project/chapter text matches

    No database changes are made.
    """

    old_name = old_name.strip()
    new_name = new_name.strip()

    if not old_name:
        return {
            "full_name": 0,
            "first_name": 0,
            "surname": 0,
            "total": 0,
        }

    old_parts = old_name.split()
    new_parts = new_name.split()

    old_first = (
        old_parts[0]
        if old_parts
        else ""
    )

    old_last = (
        old_parts[-1]
        if len(old_parts) >= 2
        else ""
    )

    connection = get_connection()
    cursor = connection.cursor()

    text_blocks = []

    # -----------------------------------------------------
    # PROJECT TEXT
    # -----------------------------------------------------

    cursor.execute(
        """
        SELECT
            plot,
            characters,
            story_architecture,
            character_bible,
            world_bible,
            timeline

        FROM projects

        WHERE id = ?
        """,
        (project_id,),
    )

    project = cursor.fetchone()

    if project:

        for value in project:

            if value:

                text_blocks.append(
                    value
                )

    # -----------------------------------------------------
    # CHAPTER TEXT
    # -----------------------------------------------------

    cursor.execute(
        """
        SELECT
            title,
            chapter_plan,
            scene_plan,
            draft,
            edited_draft,
            continuity_report,
            chapter_summary

        FROM chapters

        WHERE project_id = ?
        """,
        (project_id,),
    )

    chapter_rows = cursor.fetchall()

    for row in chapter_rows:

        for value in row:

            if value:

                text_blocks.append(
                    value
                )

    connection.close()

    full_name_count = 0
    first_name_count = 0
    surname_count = 0

    for text in text_blocks:

        full_name_count += (
            count_exact_name(
                text,
                old_name,
            )
        )

        if (
            replace_first_name
            and old_first
        ):

            first_name_count += (
                count_exact_name(
                    text,
                    old_first,
                )
            )

        if (
            replace_surname
            and old_last
        ):

            surname_count += (
                count_exact_name(
                    text,
                    old_last,
                )
            )

    return {
        "full_name": (
            full_name_count
        ),

        "first_name": (
            first_name_count
        ),

        "surname": (
            surname_count
        ),

        "total": (
            full_name_count
            + first_name_count
            + surname_count
        ),
    }
    rows = cursor.fetchall()

    connection.close()

    return rows