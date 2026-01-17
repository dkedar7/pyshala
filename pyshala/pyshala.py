"""PyShala - Main Reflex application entry point."""

import reflex as rx

from .pages.index import index
from .pages.lesson import lesson_page
from .pages.module import module_page

# Custom CSS for global styles
GLOBAL_STYLES = {
    "font_family": "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif",
}


app = rx.App(
    style=GLOBAL_STYLES,
    theme=rx.theme(
        accent_color="violet",
        gray_color="slate",
        radius="medium",
    ),
)

# Add routes
app.add_page(index, route="/", title="PyShala - Learn Python")
app.add_page(
    module_page,
    route="/module/[module_id]",
    title="Module - PyShala",
)
app.add_page(
    lesson_page,
    route="/lesson/[module_id]/[lesson_id]",
    title="Lesson - PyShala",
)
