# Student Study Planner

Project title

Student Study Planner

Overview

Student Study Planner is a compact command-line Python tool that converts a short list of subjects and their estimated study-hour needs into a simple, actionable plan for the day. The program asks how many subjects you want to cover, collects names and estimated hours for each, then allocates your available study time across them in the order entered.

This repository contains the main script `Student Study Planner.py`, a project statement (`Statement.md`), and this README.

## Features

- Interactive CLI input (works in Windows PowerShell and other terminals)
- Simple, deterministic allocation algorithm (first-come, first-served)
- Prints a clear, human-readable daily plan with allocated hours per subject
- Shows leftover free time when available hours exceed estimated needs

## Technologies / Tools used

- Python 3.7+ (standard library only)
- Works in Windows PowerShell, macOS Terminal, and Linux shells

## Files

- `Student Study Planner.py` — main script containing the program logic
- `Statement.md` — project statement / notes (currently empty)
- `README.md` — this file

## Install & run

No installation is required beyond having Python 3.7 or newer installed.

1. Open a terminal (PowerShell on Windows).
2. Change to the project directory, for example:

```powershell
cd C:\path\to\studentstudyplanner
```

3. Run the script:

```powershell
python "Student Study Planner.py"
```

The program will prompt you for input. Follow the prompts to build today's study plan.

## Usage

Open a terminal (PowerShell shown below) in the project directory and run:

```powershell
python "Student Study Planner.py"
```

The script will prompt for the number of subjects, each subject's name and estimated hours required, and the number of hours you can study today. Example interaction:

```
How many subjects? 3
Enter subject 1 name: Math
Estimated hours needed for Math: 2
Enter subject 2 name: History
Estimated hours needed for History: 1.5
Enter subject 3 name: Physics
Estimated hours needed for Physics: 3
How many hours can you study today? 4

Today's Study Plan:
- Math: 2.0 hour(s)
- History: 1.5 hour(s)
- Physics: 0.5 hour(s)

Free time left: 0.0 hour(s)
```

Notes:
- Subjects are allocated in the order entered. If you prefer priority-based allocation, consider sorting subjects by priority or required hours before creating the plan.

## Testing

This project is a small interactive script and doesn't include automated tests yet. To manually test it:

1. Run the script and enter several subjects with varying required hours and available hours. Verify that the allocations sum to the available hours (or the total needed hours if that's smaller).
2. Test edge cases:
	- Zero available hours (should output no allocations and show leftover/no free time as appropriate)
	- More available hours than total needed (should allocate full needs and show leftover)
	- Non-integer hours (script accepts floats)

If you want automated tests, I can add a small test module using `unittest` or `pytest` that simulates input and checks output.

## Screenshots (optional)

You can include screenshots of the terminal run to help users. Recommended workflow on Windows:

1. Run the script in PowerShell and take a screenshot (Win+Shift+S for the snipping tool or PrintScreen).
2. Save the image to the repository (e.g., `screenshots/example-run.png`).
3. Reference it in this README using Markdown:

```markdown
![Example run](screenshots/example-run.png)
```

## Contract (small)

- Input: interactive user input: number of subjects, subject name and hours, available study hours.
- Output: printed study allocation and leftover hours.
- Error modes: invalid numeric input will raise a ValueError from the `float()`/`int()` conversion. The script is small and does not include defensive validation by default.

## Possible Improvements

- Add input validation and friendly error messages
- Support priority or deadline-based allocation
- Allow saving/loading plans to/from a file
- Add a GUI or web front-end

## Contributing

Contributions are welcome. For small projects like this, open an issue first to discuss major changes, or submit a pull request with a clear description of the change.

## License

This project is provided as-is with no explicit license. Add a LICENSE file if you want to grant reuse rights.

## Author

Created by the repository owner.

