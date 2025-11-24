# Student Study Planner — Project Statement

## Problem statement

Many students struggle to manage daily study time across multiple subjects. They often over- or under-allocate time to topics, lack a quick way to translate estimated study needs into a usable daily plan, and waste time deciding what to study next. Beginners and busy students especially benefit from a simple tool that produces an actionable plan from minimal input.

## Scope of the project

- Build a lightweight, easily-run Python CLI tool that takes a short list of subjects and estimated hours and allocates available study time for the day.
- Keep the tool dependency-free (standard library only) and runnable on common platforms (Windows PowerShell, macOS Terminal, Linux shells).
- Focus on a minimal, correct allocation strategy: assign time in the order subjects are entered until available hours are exhausted. Do not attempt advanced scheduling or calendar integrations in this initial scope.
- Provide clear, human-readable output and short guidance for future enhancements.

Out of scope for v1:
- Persistent storage (save/load plans), calendar synchronization, notifications, GUI or web front-ends, and prioritization algorithms beyond simple ordering.

## Target users

- Students (high school and university) who need a simple daily study plan.
- Tutors or parents who want a quick way to break down study hours for a student.
- Beginners learning Python who want to see a compact example of command-line input, simple allocation logic, and printing results.

## High-level features

- Interactive CLI prompts for:
  - Number of subjects
  - Subject names and estimated hours required
  - Available study hours for the day
- Allocation algorithm that:
  - Walks the subject list in input order
  - Allocates min(needed_hours, remaining_available_hours) per subject
  - Stops when available hours are exhausted
- Human-readable plan output listing each subject and allocated hours, plus leftover/free time
- Minimal requirements: Python 3.7+ and no external packages

## Future enhancements (short list)

- Input validation and friendly error messages
- Priority or deadline-based allocation options
- Save/load plans to a simple JSON file
- Small web or GUI front-end for less technical users
