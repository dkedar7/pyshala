"""Navigation bar component."""

import reflex as rx


def navbar() -> rx.Component:
    """Create the navigation bar component.

    Returns:
        Navigation bar component.
    """
    return rx.box(
        rx.hstack(
            rx.link(
                rx.hstack(
                    rx.icon("graduation-cap", size=28, color="white"),
                    rx.text(
                        "PyShala",
                        font_size="1.5rem",
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
                    rx.icon("book-open", size=18, color="white"),
                    rx.text("Lessons", color="white"),
                    spacing="1",
                    align="center",
                ),
                href="/",
                _hover={"opacity": "0.8"},
            ),
            width="100%",
            padding_x="2rem",
            padding_y="1rem",
            align="center",
        ),
        background="#3b82f6",
        width="100%",
        position="sticky",
        top="0",
        z_index="1000",
        box_shadow="0 2px 10px rgba(0, 0, 0, 0.1)",
    )
