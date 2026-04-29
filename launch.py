#!/usr/bin/env python3
"""Main entry point for stable-diffusion-webui.

This script handles environment preparation, dependency installation,
and launching the web UI application.
"""

import subprocess
import os
import sys
import importlib.util
import shlex
import platform


def check_python_version():
    """Ensure Python version meets minimum requirements."""
    python_version = sys.version_info
    if python_version < (3, 8):
        print(
            f"ERROR: Python 3.8 or higher is required. "
            f"Current version: {python_version.major}.{python_version.minor}"
        )
        sys.exit(1)


def is_installed(package_name):
    """Check if a Python package is installed."""
    return importlib.util.find_spec(package_name) is not None


def run_pip(command, desc=None):
    """Run a pip command and handle errors."""
    if desc:
        print(f"Installing {desc}...")

    result = subprocess.run(
        [sys.executable, "-m", "pip"] + shlex.split(command),
        capture_output=True,
        text=True,
    )

    if result.returncode != 0:
        print(f"ERROR: Failed to run pip command: pip {command}")
        print(result.stderr)
        return False

    return True


def prepare_environment():
    """Install required packages if not already present."""
    # Ensure pip and setuptools are up to date
    run_pip("install --upgrade pip", "pip")

    # Core dependencies needed before requirements.txt can be processed
    if not is_installed("torch"):
        torch_command = os.environ.get(
            "TORCH_COMMAND",
            "install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118",
        )
        run_pip(torch_command, "torch")

    requirements_file = os.environ.get("REQS_FILE", "requirements.txt")
    if os.path.exists(requirements_file):
        print(f"Installing requirements from {requirements_file}...")
        run_pip(f"install -r {requirements_file}", "requirements")


def get_launch_args():
    """Build the argument list for launching the webui."""
    args = []

    # Allow passing additional args via environment variable
    commandline_args = os.environ.get("COMMANDLINE_ARGS", "")
    if commandline_args:
        args += shlex.split(commandline_args)

    # Append any args passed directly to this script
    args += sys.argv[1:]

    return args


def start():
    """Start the webui application."""
    webui_script = os.path.join(os.path.dirname(__file__), "webui.py")

    if not os.path.exists(webui_script):
        print(f"ERROR: Could not find webui.py at {webui_script}")
        sys.exit(1)

    launch_args = get_launch_args()
    cmd = [sys.executable, webui_script] + launch_args

    print(f"Launching: {' '.join(cmd)}")
    print(f"Platform: {platform.system()} {platform.release()}")
    print(f"Python: {sys.version}")
    print("-" * 60)

    result = subprocess.run(cmd)
    sys.exit(result.returncode)


if __name__ == "__main__":
    check_python_version()

    # Skip environment preparation if requested
    if "--skip-prepare-environment" not in sys.argv:
        prepare_environment()

    start()
