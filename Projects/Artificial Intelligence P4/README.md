# Smart OCR Engine (Apple Native Vision)

A high-performance, lightweight OCR tool built specifically for macOS. Unlike standard Python OCR tools that require setting up bulky external tools like Tesseract-OCR or heavy machine learning dependencies like PyTorch, this engine interfaces directly with Apple's built-in **Vision Framework** via native APIs. It handles single images and batch-processes entire folders instantly.

## Features
* **Zero System Dependencies:** No Homebrew, MacPorts, or Tesseract installations required.
* **Blazing Fast Execution:** Uses native Apple hardware-accelerated image intelligence.
* **Drag-and-Drop Validation:** Automatically sanitizes file path quotation marks added when files are dragged directly into the Terminal.
* **Batch Processing:** Scans an entire folder of images sequentially and creates neat execution reports.
* **Isolated Project Scopes:** Saves output reports relative to your scanned images, avoiding macOS root read-only directory conflicts.

---

## Installation

The script runs on your system's default Python environment (`python3`). It only requires a few Python structural bridges to communicate with the macOS system core:

```bash
python3 -m pip install pyobjc-framework-Vision --break-system-packages
