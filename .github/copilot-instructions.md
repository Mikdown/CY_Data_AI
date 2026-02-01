# Copilot Instructions for CL_Data_AI

## Project Context
This is the **Code Louisville 2026 AI class** repository. It's in early stages and will grow to include AI/machine learning and data science projects and coursework.

## Architecture & Structure
- **Purpose**: Educational AI/Data Science project for Code Louisville 2026 class
- **Likely structure** (to be established):
  - `src/` or `notebooks/` - Main project code/analysis
  - `data/` - Datasets and data-related files
  - `docs/` - Documentation and guides
  - `tests/` - Unit and integration tests
  - `requirements.txt` or `pyproject.toml` - Python dependencies (if Python-based)

## Key Conventions to Follow

### Python Projects (if applicable)
- Use meaningful variable and function names that reflect data science terminology
- Document assumptions about data shapes and types in docstrings
- Include type hints for better clarity in data processing functions
- Place data loading logic separately from analysis/modeling logic

### Documentation
- Update README.md with project goals and setup instructions as features are added
- Include clear examples in documentation for any custom utilities
- Document data source schemas and any preprocessing steps

### Development Workflow
- Create feature branches for new assignments or features
- Keep commits focused and descriptive
- Test code locally before pushing
- Update documentation alongside code changes

## When Adding Code
- If creating a new Jupyter notebook, include markdown cells explaining the analysis goal
- If creating classes/modules, include docstrings with usage examples
- If working with data, document the source, format, and any transformations
- Consider reproducibility - include seeds for random operations if applicable

## Current Status
This is an initial repository with only README.md. As code is added, revisit and update this file with project-specific patterns discovered during development.

---
description: 'Python coding conventions and guidelines'
applyTo: '**/*.py'
---

# Python Coding Conventions

## Python Instructions

- Write clear and concise comments for each function.
- Ensure functions have descriptive names and include type hints.
- Provide docstrings following PEP 257 conventions.
- Use the `typing` module for type annotations (e.g., `List[str]`, `Dict[str, int]`).
- Break down complex functions into smaller, more manageable functions.

## General Instructions

- Always prioritize readability and clarity.
- For algorithm-related code, include explanations of the approach used.
- Write code with good maintainability practices, including comments on why certain design decisions were made.
- Handle edge cases and write clear exception handling.
- For libraries or external dependencies, mention their usage and purpose in comments.
- Use consistent naming conventions and follow language-specific best practices.
- Write concise, efficient, and idiomatic code that is also easily understandable.

## Code Style and Formatting

- Follow the **PEP 8** style guide for Python.
- Maintain proper indentation (use 4 spaces for each level of indentation).
- Ensure lines do not exceed 79 characters.
- Place function and class docstrings immediately after the `def` or `class` keyword.
- Use blank lines to separate functions, classes, and code blocks where appropriate.

## Edge Cases and Testing

- Always include test cases for critical paths of the application.
- Account for common edge cases like empty inputs, invalid data types, and large datasets.
- Include comments for edge cases and the expected behavior in those cases.
- Write unit tests for functions and document them with docstrings explaining the test cases.

## Example of Proper Documentation

```python
def calculate_area(radius: float) -> float:
    """
    Calculate the area of a circle given the radius.
    
    Parameters:
    radius (float): The radius of the circle.
    
    Returns:
    float: The area of the circle, calculated as π * radius^2.
    """
    import math
    return math.pi * radius ** 2
```
