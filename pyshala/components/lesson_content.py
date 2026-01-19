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
                    size="4",
                    margin_bottom="0.5rem",
                    color="#1f2937",
                ),
                "h2": lambda text: rx.heading(
                    text,
                    size="3",
                    margin_top="0.75rem",
                    margin_bottom="0.375rem",
                    color="#374151",
                ),
                "h3": lambda text: rx.heading(
                    text,
                    size="2",
                    margin_top="0.5rem",
                    margin_bottom="0.25rem",
                    color="#4b5563",
                ),
                "p": lambda text: rx.text(
                    text,
                    margin_bottom="0.375rem",
                    line_height="1.5",
                    color="#374151",
                    font_size="0.8rem",
                ),
                "code": lambda text: rx.code(
                    text,
                    color="#c7254e",
                    background="#f9f2f4",
                    padding="0.05rem 0.15rem",
                    border_radius="0.15rem",
                    font_size="0.75rem",
                ),
                "ul": lambda children: rx.box(
                    children,
                    as_="ul",
                    padding_left="1rem",
                    margin_bottom="0.375rem",
                    font_size="0.8rem",
                ),
                "ol": lambda children: rx.box(
                    children,
                    as_="ol",
                    padding_left="1rem",
                    margin_bottom="0.375rem",
                    font_size="0.8rem",
                ),
                "li": lambda text: rx.box(
                    text,
                    as_="li",
                    margin_bottom="0.125rem",
                    line_height="1.4",
                    color="#374151",
                ),
                "table": lambda children: rx.box(
                    children,
                    as_="table",
                    width="100%",
                    margin_y="0.5rem",
                    border_collapse="collapse",
                    font_size="0.75rem",
                ),
                "thead": lambda children: rx.box(
                    children,
                    as_="thead",
                    background="#f3f4f6",
                ),
                "tbody": lambda children: rx.box(
                    children,
                    as_="tbody",
                ),
                "tr": lambda children: rx.box(
                    children,
                    as_="tr",
                    border_bottom="1px solid #e5e7eb",
                ),
                "th": lambda text: rx.box(
                    text,
                    as_="th",
                    padding="0.375rem 0.5rem",
                    text_align="left",
                    font_weight="600",
                    color="#1f2937",
                ),
                "td": lambda text: rx.box(
                    text,
                    as_="td",
                    padding="0.375rem 0.5rem",
                    color="#374151",
                ),
            },
        ),
        width="100%",
        padding="0.75rem",
        background="white",
        border_radius="0.375rem",
        box_shadow="0 1px 2px rgba(0, 0, 0, 0.05)",
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
                color_scheme="blue",
                size="1",
            ),
            width="100%",
        ),
        rx.heading(
            title,
            size="3",
            color="#1f2937",
        ),
        rx.cond(
            description != "",
            rx.text(
                description,
                color="#6b7280",
                font_size="0.75rem",
            ),
            rx.fragment(),
        ),
        width="100%",
        spacing="1",
        align="start",
        padding_bottom="0.5rem",
        border_bottom="1px solid #e5e7eb",
        margin_bottom="0.5rem",
    )
