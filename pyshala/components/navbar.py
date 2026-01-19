"""Navigation bar component."""

import os

import reflex as rx


def get_app_name() -> str:
    """Get the application name from environment or default."""
    return os.getenv("APP_NAME", "PyShala")


def navbar() -> rx.Component:
    """Create the navigation bar component.

    Returns:
        Navigation bar component.
    """
    return rx.box(
        rx.hstack(
            rx.link(
                rx.hstack(
                    rx.icon("graduation-cap", size=20, color="white"),
                    rx.text(
                        get_app_name(),
                        font_size="1rem",
                        font_weight="bold",
                        color="white",
                    ),
                    spacing="2",
                    align="center",
                ),
                href="/",
                _hover={"text_decoration": "none"},
            ),
            rx.spacer(),
            rx.link(
                rx.hstack(
                    rx.icon("book-open", size=14, color="white"),
                    rx.text("Lessons", color="white", font_size="0.85rem"),
                    spacing="1",
                    align="center",
                ),
                href="/",
                _hover={"opacity": "0.8"},
            ),
            width="100%",
            padding_x="1rem",
            padding_y="0.5rem",
            align="center",
        ),
        background="#3b82f6",
        width="100%",
        position="sticky",
        top="0",
        z_index="1000",
        box_shadow="0 1px 4px rgba(0, 0, 0, 0.1)",
    )
