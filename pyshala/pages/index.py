"""Home page - displays all available modules."""

import reflex as rx

from ..components.navbar import navbar
from ..state.app_state import AppState, ModuleInfo


def module_card(module: ModuleInfo) -> rx.Component:
    """Create a module card component.

    Args:
        module: ModuleInfo object.

    Returns:
        Module card component.
    """
    return rx.link(
        rx.box(
            rx.vstack(
                rx.hstack(
                    rx.icon("book-open", size=24, color="#3b82f6"),
                    rx.spacer(),
                    rx.badge(
                        f"{module.lesson_count} lessons",
                        color_scheme="blue",
                        size="1",
                    ),
                    width="100%",
                ),
                rx.heading(
                    module.name,
                    size="5",
                    color="#1f2937",
                    margin_top="0.5rem",
                ),
                rx.text(
                    module.description,
                    color="#6b7280",
                    font_size="0.9rem",
                    line_height="1.5",
                    min_height="3rem",
                ),
                rx.spacer(),
                width="100%",
                height="100%",
                spacing="2",
                align="start",
            ),
            padding="1.5rem",
            background="white",
            border_radius="0.75rem",
            box_shadow="0 1px 3px rgba(0, 0, 0, 0.1)",
            _hover={
                "box_shadow": "0 4px 12px rgba(0, 0, 0, 0.15)",
                "transform": "translateY(-2px)",
            },
            transition="all 0.2s ease",
            height="100%",
            min_height="180px",
        ),
        href=f"/module/{module.id}",
        _hover={"text_decoration": "none"},
        width="100%",
    )


def empty_state() -> rx.Component:
    """Display when no modules are available."""
    return rx.center(
        rx.vstack(
            rx.icon("folder-open", size=64, color="#9ca3af"),
            rx.heading(
                "No Lessons Yet",
                size="6",
                color="#374151",
            ),
            rx.text(
                "Lessons will appear here once they're configured.",
                color="#6b7280",
                text_align="center",
            ),
            rx.text(
                "Add lesson YAML files to the lessons directory to get started.",
                color="#9ca3af",
                font_size="0.875rem",
                text_align="center",
            ),
            spacing="3",
            align="center",
            padding="3rem",
        ),
        width="100%",
        min_height="400px",
    )


def index() -> rx.Component:
    """Home page component displaying all modules.

    Returns:
        Home page component.
    """
    return rx.box(
        navbar(),
        rx.box(
            rx.vstack(
                # Hero section
                rx.box(
                    rx.vstack(
                        rx.heading(
                            "Learn Python, One Lesson at a Time",
                            size="8",
                            color="#1f2937",
                            text_align="center",
                        ),
                        rx.text(
                            "Interactive lessons with hands-on coding exercises and instant feedback",
                            color="#6b7280",
                            font_size="1.1rem",
                            text_align="center",
                            max_width="600px",
                        ),
                        spacing="3",
                        align="center",
                        padding_y="2rem",
                    ),
                    width="100%",
                ),
                # Modules grid
                rx.cond(
                    AppState.modules.length() > 0,
                    rx.box(
                        rx.grid(
                            rx.foreach(
                                AppState.modules,
                                module_card,
                            ),
                            columns="3",
                            spacing="4",
                            width="100%",
                        ),
                        width="100%",
                    ),
                    empty_state(),
                ),
                width="100%",
                max_width="1200px",
                margin="0 auto",
                padding="2rem",
                spacing="4",
            ),
            width="100%",
            min_height="calc(100vh - 60px)",
            background="#f9fafb",
        ),
        on_mount=[AppState.load_modules, AppState.load_progress],
        width="100%",
    )
