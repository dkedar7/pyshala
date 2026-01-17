"""Lesson content display component for Markdown instructions."""

import reflex as rx


def lesson_content(instructions: str) -> rx.Component:
    """Create a lesson content component for displaying instructions.

    Args:
        instructions: Markdown content for the lesson.

    Returns:
        Lesson content component.
    """
    return rx.box(
        rx.markdown(
            instructions,
            component_map={
                "h1": lambda text: rx.heading(
                    text,
                    size="7",
                    margin_bottom="1rem",
                    color="#1f2937",
                ),
                "h2": lambda text: rx.heading(
                    text,
                    size="5",
                    margin_top="1.5rem",
                    margin_bottom="0.75rem",
                    color="#374151",
                ),
                "h3": lambda text: rx.heading(
                    text,
                    size="4",
                    margin_top="1rem",
                    margin_bottom="0.5rem",
                    color="#4b5563",
                ),
                "p": lambda text: rx.text(
                    text,
                    margin_bottom="0.75rem",
                    line_height="1.7",
                    color="#374151",
                ),
                "code": lambda text: rx.code(
                    text,
                    color="#c7254e",
                    background="#f9f2f4",
                    padding="0.125rem 0.25rem",
                    border_radius="0.25rem",
                    font_size="0.875rem",
                ),
                "ul": lambda children: rx.box(
                    children,
                    as_="ul",
                    padding_left="1.5rem",
                    margin_bottom="0.75rem",
                ),
                "ol": lambda children: rx.box(
                    children,
                    as_="ol",
                    padding_left="1.5rem",
                    margin_bottom="0.75rem",
                ),
                "li": lambda text: rx.box(
                    text,
                    as_="li",
                    margin_bottom="0.25rem",
                    line_height="1.6",
                ),
            },
        ),
        width="100%",
        padding="1.5rem",
        background="white",
        border_radius="0.5rem",
        box_shadow="0 1px 3px rgba(0, 0, 0, 0.1)",
    )


def lesson_header(
    title: str, description: str, lesson_number: int, total_lessons: int
) -> rx.Component:
    """Create the lesson header component.

    Args:
        title: Lesson title.
        description: Lesson description.
        lesson_number: Current lesson number (1-indexed).
        total_lessons: Total number of lessons in module.

    Returns:
        Lesson header component.
    """
    return rx.vstack(
        rx.hstack(
            rx.badge(
                f"Lesson {lesson_number} of {total_lessons}",
                color_scheme="purple",
                size="2",
            ),
            width="100%",
        ),
        rx.heading(
            title,
            size="8",
            color="#1f2937",
        ),
        rx.cond(
            description != "",
            rx.text(
                description,
                color="#6b7280",
                font_size="1rem",
            ),
            rx.fragment(),
        ),
        width="100%",
        spacing="2",
        align="start",
        padding_bottom="1rem",
        border_bottom="1px solid #e5e7eb",
        margin_bottom="1rem",
    )
