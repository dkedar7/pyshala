# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.1] - 2026-01-18

### Added
- **Quiz Lessons**: New lesson type supporting multiple choice questions (MCQ) and text-based questions
  - Single-select MCQ with radio buttons
  - Multi-select MCQ with checkboxes
  - Text input questions with case-insensitive matching
  - Automatic grading with instant feedback
- **App Configuration**: New `config.yaml` file for customizing:
  - App title and subtitle
  - Home page description
  - About link URL and text
  - Navbar icon (Lucide icons)
- **Enhanced Documentation**: Comprehensive guide for building effective modules, quiz best practices, and LLM prompt templates

### Changed
- Simplified navigation by removing intermediate module page - users now go directly from home to lessons
- Renamed "Run Code" button to "Submit" for consistency across code and quiz lessons

### Fixed
- Fixed rxconfig.py location for proper package structure
- Added .gitignore to exclude build artifacts

## [0.1.0] - 2025-01-18

### Added
- Initial public release
- Interactive Python lessons with live code execution
- Monaco code editor integration
- Automated test case validation with instant feedback
- YAML-based lesson configuration
- Module and lesson organization system
- Data file support for lessons (CSV, JSON, etc.)
- Local Python code execution (no Docker required)
- CLI tool (`pyshala`) with configurable options
- Python API for programmatic usage
- Dark mode theme toggle
- Collapsible sidebar navigation
- Session-based progress tracking
- Customizable app name and description
- Docker deployment support

### Features
- **Lesson System**: Create custom lessons using simple YAML files
- **Code Execution**: Secure local Python subprocess execution with timeout
- **Test Cases**: Define test cases with expected outputs, hidden tests support
- **UI/UX**: Responsive design with light/dark themes, compact layout
- **CLI**: Full-featured command line interface with all configuration options
- **API**: Python API for embedding in custom applications

### Documentation
- README with quick start guide
- LESSONS.md guide for content creators
- Docker deployment instructions
- Environment variable configuration
