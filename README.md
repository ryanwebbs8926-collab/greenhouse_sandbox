# GHU-2 Greenhouse Controller

Team controller for the ENGR 13100 Martian Greenhouse project (GHU-2). The controller reads sensor
values each tick and commands four actuators: heater, grow LEDs, CO2 valve, and irrigation pump.

## Setup (first time)

Requires Python 3.9+, Git, and tkinter (the sandbox GUI toolkit; it ships with the python.org
installers on Windows and macOS, and on Linux install it with `sudo apt install python3-tk`).

**Run the sandbox on your own computer, not in Codespaces or the cloud.** The GUI opens a desktop
window and needs an on-screen display. See `QUICKSTART.md` for details.

**macOS / Linux**
```bash
./scripts/setup.sh
source .venv/bin/activate
```

**Windows (PowerShell)**
```powershell
.\scripts\setup.ps1
.\.venv\Scripts\Activate.ps1
```

Or manually:
```bash
python -m venv .venv
# activate it (see above), then:
pip install -r requirements/dev.txt
```

VS Code will detect `.venv` automatically. If it doesn't, press `Ctrl/Cmd+Shift+P` > **Python: Select Interpreter** > choose `.venv`.

## Updating your environment after pulling

When someone adds a dependency, re-run:
```bash
pip install -r requirements/dev.txt
```

## Adding a dependency

1. `pip install <package>`
2. Add it (with a version pin, e.g. `requests==2.32.3`) to `requirements/base.txt` (needed to run) or `requirements/dev.txt` (tools only).
3. Commit the requirements change.

`pip freeze` can show the exact installed version: `pip freeze | grep <package>`.

## Layout

This repository is the unzipped course sandbox folder with our controller added.

```
run_sandbox.py        launches the sandbox GUI (course file)
practice_test_m3.py   Milestone 3 practice check (course file)
practice_test_m4.py   Milestone 4 practice check (course file)
QUICKSTART.md         course instructions for the sandbox kit
martian_greenhouse_sim/   the simulator (course code - do NOT edit)
student_controller_template/   the original template - leave it alone
student_controller/   our controller package
  heater.py           control_heater(readings, setpoints, dt, state)
  leds.py             LED control
  co2.py              CO2 valve control and sensor-trust rule
  pump.py             irrigation pump control
  hardware.py         declares GLAZING and HEATER_W
  main.py             provided by the course - do NOT edit
  __init__.py         provided by the course - do NOT edit
tests/                our own pytest unit tests for the control functions
analyze_mission.py    mission analysis script (Milestone 4)
requirements/         base.txt (runtime), dev.txt (runtime + dev tools)
scripts/              setup scripts
.venv/                local virtual environment (NOT committed)
```

Mission logs are about 11 MB each and are not committed (see `.gitignore`).

## Run

```bash
python run_sandbox.py                  # interactive sandbox GUI (uses our declared hardware)
python practice_test_m3.py             # Milestone 3 practice acceptance check
python practice_test_m4.py             # Milestone 4 practice check (adds the sensor faults)
python practice_test_m4.py --seed 7    # try other seeds
pytest                                 # our own unit tests (in tests/)
```

`quick_run.py` is optional. It is not part of the download; the assignment page gives its code.

## Team conventions

- **One owner per actuator file.** Work on your own branch and open a pull request into `main`.
- **State keys are shared.** All four files use one `state` dict, so every key starts with its
  actuator's name: `heater_`, `led_`, `co2_`, `pump_`.
- **No hard-coded action sequences.** The controller must respond to sensor readings, and the same
  inputs plus the same state must always give the same outputs (determinism).
- **Log AI use.** Any AI conversation that contributes to project work goes in the AI Use Log with
  its full transcript, following the course AI Usage Policy.
