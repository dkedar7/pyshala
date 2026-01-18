"""Lesson viewer page - displays lesson content and code editor."""

import reflex as rx

from ..components.code_editor import code_editor, editor_toolbar
from ..components.lesson_content import lesson_content, lesson_header
from ..components.navbar import navbar
from ..components.sidebar import sidebar
from ..components.test_results import test_results
from ..state.app_state import AppState


def lesson_navigation() -> rx.Component:
    """Create the lesson navigation buttons.

    Returns:
        Navigation component.
    """
    return rx.hstack(
        rx.cond(
            AppState.has_previous_lesson,
            rx.link(
                rx.button(
                    rx.hstack(
                        rx.icon("arrow-left", size=16),
                        rx.text("Previous"),
                        spacing="1",
                    ),
                    variant="outline",
                    color_scheme="gray",
                    size="2",
                ),
                href=AppState.previous_lesson_url,
            ),
            rx.box(),
        ),
        rx.spacer(),
        rx.cond(
            AppState.tests_all_passed & AppState.has_next_lesson,
            rx.link(
                rx.button(
                    rx.hstack(
                        rx.text("Next Lesson"),
                        rx.icon("arrow-right", size=16),
                        spacing="1",
                    ),
                    color_scheme="green",
                    size="2",
                ),
                href=AppState.next_lesson_url,
            ),
            rx.cond(
                AppState.has_next_lesson,
                rx.button(
                    rx.hstack(
                        rx.text("Next Lesson"),
                        rx.icon("arrow-right", size=16),
                        spacing="1",
                    ),
                    variant="outline",
                    color_scheme="gray",
                    size="2",
                    disabled=True,
                ),
                rx.box(),
            ),
        ),
        width="100%",
        padding_y="1rem",
    )


def lesson_page() -> rx.Component:
    """Lesson viewer page component.

    Returns:
        Lesson page component.
    """
    return rx.box(
        navbar(),
        rx.hstack(
            # Sidebar
            sidebar(
                module_name=AppState.current_module_name,
                lessons=AppState.current_module_lessons,
                module_id=AppState.current_module_id,
                current_lesson_id=AppState.current_lesson_id,
                completed_lessons=AppState.completed_lessons,
            ),
            # Main content area
            rx.box(
                rx.hstack(
                    # Left column - Instructions
                    rx.box(
                        rx.vstack(
                            lesson_header(
                                title=AppState.current_lesson_title,
                                description=AppState.current_lesson_description,
                                lesson_number=AppState.lesson_number,
                                total_lessons=AppState.current_lesson_total,
                            ),
                            lesson_content(AppState.current_lesson_instructions),
                            width="100%",
                            spacing="3",
                            align="start",
                        ),
                        width="50%",
                        padding="1.5rem",
                        overflow_y="auto",
                        height="calc(100vh - 60px)",
                        background="white",
                    ),
                    # Right column - Code editor and results
                    rx.box(
                        rx.vstack(
                            # Editor toolbar
                            editor_toolbar(
                                on_run=AppState.run_code,
                                on_reset=AppState.reset_code,
                                is_running=AppState.is_running,
                            ),
                            # Code editor
                            code_editor(
                                code=AppState.current_code,
                                on_change=AppState.set_code,
                                height="350px",
                                editor_key=AppState.editor_key,
                            ),
                            # Test results
                            test_results(
                                results=AppState.test_results,
                                is_running=AppState.is_running,
                                all_passed=AppState.tests_all_passed,
                                passed_count=AppState.tests_passed_count,
                                total_count=AppState.tests_total_count,
                            ),
                            # Navigation
                            lesson_navigation(),
                            width="100%",
                            spacing="3",
                            align="start",
                        ),
                        width="50%",
                        padding="1.5rem",
                        overflow_y="auto",
                        height="calc(100vh - 60px)",
                        background="#f9fafb",
                    ),
                    width="100%",
                    spacing="0",
                    align="start",
                ),
                flex="1",
                width="100%",
            ),
            width="100%",
            spacing="0",
            align="start",
        ),
        width="100%",
        height="100vh",
        overflow="hidden",
    )
