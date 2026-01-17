"""Sidebar navigation component for lesson navigation."""

import reflex as rx

from ..state.app_state import LessonInfo


def lesson_item(
    lesson: LessonInfo,
    module_id: rx.Var[str],
    current_lesson_id: rx.Var[str],
    completed_lessons: rx.Var[list[str]],
) -> rx.Component:
    """Create a single lesson item in the sidebar.

    Args:
        lesson: LessonInfo object.
        module_id: Parent module ID.
        current_lesson_id: Currently active lesson ID.
        completed_lessons: List of completed lesson IDs.

    Returns:
        Lesson item component.
    """
    full_id = module_id + "/" + lesson.id
    is_current = lesson.id == current_lesson_id
    is_completed = completed_lessons.contains(full_id)

    return rx.link(
        rx.hstack(
            rx.cond(
                is_completed,
                rx.icon("circle-check", size=16, color="#10b981"),
                rx.icon("circle", size=16, color="#9ca3af"),
            ),
            rx.text(
                lesson.title,
                font_size="0.9rem",
                font_weight=rx.cond(is_current, "600", "400"),
                color=rx.cond(is_current, "#667eea", "#374151"),
            ),
            spacing="2",
            width="100%",
            padding="0.5rem 0.75rem",
            border_radius="0.375rem",
            background=rx.cond(
                is_current,
                "rgba(102, 126, 234, 0.1)",
                "transparent",
            ),
            _hover={"background": "rgba(102, 126, 234, 0.05)"},
        ),
        href="/lesson/" + module_id + "/" + lesson.id,
        width="100%",
        _hover={"text_decoration": "none"},
    )


def sidebar(
    module_name: rx.Var[str],
    lessons: rx.Var[list[LessonInfo]],
    module_id: rx.Var[str],
    current_lesson_id: rx.Var[str],
    completed_lessons: rx.Var[list[str]],
) -> rx.Component:
    """Create the sidebar navigation component.

    Args:
        module_name: Name of the current module.
        lessons: List of LessonInfo objects.
        module_id: Current module ID.
        current_lesson_id: Currently active lesson ID.
        completed_lessons: List of completed lesson IDs.

    Returns:
        Sidebar component.
    """
    return rx.box(
        rx.vstack(
            # Module header
            rx.hstack(
                rx.link(
                    rx.icon("arrow-left", size=18, color="#667eea"),
                    href="/module/" + module_id,
                ),
                rx.text(
                    module_name,
                    font_size="1rem",
                    font_weight="600",
                    color="#1f2937",
                ),
                spacing="2",
                align="center",
                padding_bottom="0.75rem",
                border_bottom="1px solid #e5e7eb",
                width="100%",
            ),
            # Lesson list
            rx.vstack(
                rx.foreach(
                    lessons,
                    lambda lesson: lesson_item(
                        lesson, module_id, current_lesson_id, completed_lessons
                    ),
                ),
                width="100%",
                spacing="1",
                padding_top="0.75rem",
            ),
            width="100%",
            spacing="0",
            align="start",
        ),
        width="280px",
        min_width="280px",
        height="calc(100vh - 60px)",
        padding="1rem",
        background="#fafafa",
        border_right="1px solid #e5e7eb",
        overflow_y="auto",
        position="sticky",
        top="60px",
    )
