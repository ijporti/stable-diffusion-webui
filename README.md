# Stable Diffusion Web UI

A fork of [AUTOMATIC1111/stable-diffusion-webui](https://github.com/AUTOMATIC1111/stable-diffusion-webui) — a browser interface for Stable Diffusion, based on the Gradio library.

![screenshot](https://github.com/AUTOMATIC1111/stable-diffusion-webui/raw/master/screenshot.png)

## Features

- Text-to-image and image-to-image generation
- Outpainting, inpainting, color sketch
- Prompt matrix and attention control
- Stable Diffusion upscale, GFPGAN, CodeFormer, RealESRGAN, ESRGAN, SwinIR, Sber-RealESRGAN
- Sampling methods: DDIM, PLMS, DPM, DPM++, Euler, Euler a, Heun, LMS
- LoRA, Textual Inversion, Hypernetworks support
- Extras tab with upscaling and face restoration
- PNG info: embed generation parameters into images
- Settings page with many UI options
- Prompt syntax: attention/emphasis, BREAK keyword, alternating words
- Extensions support

## Installation

### Automatic Installation (Windows)

1. Install [Python 3.10.6](https://www.python.org/downloads/release/python-3106/), checking "Add Python to PATH".
2. Install [git](https://git-scm.com/download/win).
3. Download this repository, for example by running `git clone https://github.com/your-org/stable-diffusion-webui`.
4. Run `webui-user.bat` from Windows Explorer as normal, non-administrator user.

### Automatic Installation (Linux)

1. Install the dependencies:
```bash
# Debian-based
sudo apt install wget git python3 python3-venv libgl1 libglib2.0-0
# Red Hat-based
sudo dnf install wget git python3 gperftools-libs libglvnd-glx
# openSUSE-based
sudo zypper install wget git python3 libtcmalloc4 libglvnd
# Arch-based
sudo pacman -S wget git python3
```
2. Navigate to the directory you would like the webui to be installed and execute the following command:
```bash
bash <(wget -qO- https://raw.githubusercontent.com/your-org/stable-diffusion-webui/master/webui.sh)
```

### Installation on Apple Silicon

Find the instructions [in the wiki](https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/Installation-on-Apple-Silicon).

## Usage

```bash
# Run the web UI
python launch.py

# Run with specific options
python launch.py --share --listen --port 7860

# My preferred setup: medvram for my 6GB GPU, auto-open browser, xformers for speed
python launch.py --medvram --autolaunch --xformers
```

### Common Arguments

| Argument | Description |
|---|---|
| `--share` | Create a public Gradio link |
| `--listen` | Make server listen on network |
| `--port PORT` | Set the port (default: 7860) |
| `--no-half` | Do not switch model to 16-bit floats |
| `--medvram` | Enable optimizations for GPUs with ~4GB VRAM |
| `--lowvram` | Enable optimizations for GPUs with very low VRAM |
| `--xformers` | Enable xformers for cross attention layers |
| `--autolaunch` | Open the UI in the browser automatically on startup |
| `--theme` | Set the UI theme: `light` or `dark` (I prefer `dark`) |

## Contributing

Pull requests are welcome. Please read the [contributing guidelines](.github/pull_request_template.md) before submitting a PR.

### Development Setup

