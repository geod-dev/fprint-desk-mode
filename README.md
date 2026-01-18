# fprint-desk-mode ✨

A tiny utility that disables the fingerprint reader when an external USB keyboard is connected. Designed for Arch Linux and packaged with a `PKGBUILD` for easy installation.

## Features 🚀
- 🔒 Disable fingerprint auth when an external keyboard is present
- 🧭 Automatic PAM integration via install/remove hooks
- 🧰 Small, focused and easy to audit
- 🐧 Built for Arch Linux - simple installation

## Installation 📦
1. Clone or place the project directory containing `PKGBUILD`.
2. Build and install with:
   ```bash
   cd /path/to/project
   makepkg -si
   ```
This installs:
- main binary: `fprint_desk_mode`
- helper scripts: `fdm_post_install` and `fdm_pre_remove`
- utility python files for helper scripts to `/usr/share/fprint-desk-mode/`
- system hooks for automatic helper scripts execution to `/usr/share/libalpm/hooks/`

## Uninstallation 🧹
- If installed via `pacman` / `makepkg`, remove with:
  ```bash
  sudo pacman -Rns fprint-desk-mode
  ```
- Please read the output to be sure PAM modifications were reverted.

## How it works (short) ⚙️
- `fprint_desk_mode` scans `/proc/bus/input/devices` for external USB keyboards.
- Install hooks call Python helpers that insert/remove a `pam_exec` line
  into the `auth` stack of `/etc/pam.d/system-auth` so it can conditionally alter fingerprint behavior.

## Contributing ✍️
Small project — contributions welcome.
- Fork the repo, make a small focused change, and open a PR.
- Keep changes minimal and document behavior in code comments or the README.
- Prefer readable shell and Python.

## License 📜
Licensed under GPLv3 (see [LICENSE](LICENSE) file).

## Contact ✉️
To help with any problem or suggestion, you can either:
- Open an issue on GitHub
- Contact me via email: [geodgit@duck.com](mailto:geodgit@duck.com)

Enjoy!
