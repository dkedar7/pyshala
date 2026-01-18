"""Module detail page - displays lessons within a module."""

import reflex as rx

from ..components.navbar import navbar
from ..state.app_state import AppState, LessonInfo


def lesson_row(lesson: LessonInfo) -> rx.Component:
    """Create a lesson row component.

    Args:
        lesson: LessonInfo object.

    Returns:
        Lesson row component.
    """
    return rx.link(
        rx.hstack(
            rx.hstack(
                rx.icon("circle", size=20, color="#d1d5db"),
                rx.text(
                    f"{lesson.order + 1}.",
                    color="#9ca3af",
                    font_size="0.9rem",
                    min_width="2rem",
                ),
                rx.vstack(
                    rx.text(
                        lesson.title,
                        font_weight="500",
                        color="#1f2937",
                    ),
                    spacing="0",
                    align="start",
                ),
                spacing="3",
                align="center",
            ),
            rx.spacer(),
            rx.hstack(
                rx.badge("Start", color_scheme="blue", size="1"),
                rx.icon("chevron-right", size=16, color="#9ca3af"),
                spacing="2",
                align="center",
            ),
            width="100%",
            padding="1rem 1.25rem",
            background="white",
            border_radius="0.5rem",
            border="1px solid #e5e7eb",
            _hover={
                "border_color": "#3b82f6",
                "box_shadow": "0 2px 8px rgba(59, 130, 246, 0.1)",
            },
            transition="all 0.2s ease",
            align="center",
        ),
        href=f"/lesson/{AppState.current_module_id}/{lesson.id}",
        _hover={"text_decoration": "none"},
        width="100%",
    )


def module_page() -> rx.Component:
    """Module detail page component.

    Returns:
        Module page component.
    """
    return rx.box(
        navbar(),
        rx.box(
            rx.vstack(
                # Back link
                rx.link(
                    rx.hstack(
                        rx.icon("arrow-left", size=16, color="#3b82f6"),
                        rx.text("Back to Modules", color="#3b82f6"),
                        spacing="1",
                        align="center",
                    ),
                    href="/",
                    _hover={"opacity": "0.8"},
                ),
                # Module header
                rx.box(
                    rx.vstack(
                        rx.hstack(
                            rx.icon("book-open", size=32, color="#3b82f6"),
                            rx.badge(
                                f"{AppState.current_module_lesson_count} lessons",
                                color_scheme="blue",
                                size="2",
                            ),
                            spacing="3",
                            align="center",
                        ),
                        rx.heading(
                            AppState.current_module_name,
                            size="8",
                            color="#1f2937",
                        ),
                        rx.text(
                            AppState.current_module_description,
                            color="#6b7280",
                            font_size="1.1rem",
                        ),
                        spacing="2",
                        align="start",
                        width="100%",
                    ),
                    width="100%",
                    padding_bottom="1.5rem",
                    border_bottom="1px solid #e5e7eb",
                ),
                # Lesson list
                rx.vstack(
                    rx.foreach(
                        AppState.current_module_lessons,
                        lesson_row,
                    ),
                    width="100%",
                    spacing="2",
                    padding_top="1rem",
                ),
                width="100%",
                max_width="800px",
                margin="0 auto",
                padding="2rem",
                spacing="4",
                align="start",
            ),
            width="100%",
            min_height="calc(100vh - 60px)",
            background="#f9fafb",
        ),
        width="100%",
    )
