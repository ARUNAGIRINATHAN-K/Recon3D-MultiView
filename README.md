<div align="center">

# Recon3D MultiView

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.0+-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![COLMAP](https://img.shields.io/badge/COLMAP-3.8-004B87?style=flat-square&logoColor=white)](https://colmap.github.io/)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)](LICENSE)

**3D reconstruction from multiple 2D images with an interactive web interface**

</div>

## 📋 Overview

Recon3D-MultiView is a Python-based application for reconstructing 3D models from multiple 2D images. It combines industry-standard computer vision algorithms with an intuitive Streamlit interface for seamless 3D reconstruction workflows.

## ✨ Features

- **Feature Detection**: SIFT/ORB algorithms
- **Feature Matching**: Robust correspondence finding
- **3D Reconstruction**: COLMAP-powered pipeline
- **Visualization**: Open3D for interactive model viewing
- **Web UI**: Streamlit-based interface

## Tech Stack

| Component | Technology |
|-----------|-----------|
| **Core** | Python 3.8+ |
| **3D Reconstruction** | COLMAP |
| **Visualization** | Open3D |
| **Web Framework** | Streamlit |
| **Computer Vision** | OpenCV |

## Quick Start

### Prerequisites
- Python 3.8+
- [COLMAP](https://colmap.github.io/) (must be in system PATH)

### Installation

```bash
git clone <repository-url>
cd Recon3D-MultiView
pip install -r requirements.txt
```

### Usage

```bash
python -m streamlit run app.py
```

## Project Structure

```
├── app.py                 # Streamlit application
├── requirements.txt       # Python dependencies
├── src/                   # Source modules
│   ├── feature_extraction.py
│   ├── matching.py
│   ├── pipeline.py
│   └── reconstruction.py
├── colmap/               # COLMAP submodule
└── output_streamlit/     # Results directory
```

## License

MIT License - See LICENSE file for details
