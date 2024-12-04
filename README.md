# HeNN eLibrary Projects

## 👋 Welcome

This repository contains the database of eLibrary deployments carried out by [Help Nepal Network](https://helpnepal.net/) in various parts of Nepal.

Help Nepal Network aims to support rural Nepal in the fields of health and education. Under this mission, the eLibrary project was launched with the vision of **“One eLibrary per district”**.

The eLibrary initiative is a low-cost, low-maintenance project designed to provide computer facilities to students and communities in all 75 districts of Nepal. This innovative effort helps bridge the digital divide by introducing modern information and communication technology (ICT), enhancing learning opportunities, and building essential computer skills in rural areas.

## 💻 Getting Started

### Setting Up the Environment

1. Create and activate a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Updating the Website

- To update the website content, modify files in the `src/html/` directory.
- To update deployment data, edit the `src/data/HeNN eLibraries - Clean.csv` file, then regenerate the site by running:
  ```bash
  python generate_site.py
  ```

## 🗒️ TODO

- [x] Create a script to automatically populate GeoJSON files.

Feel free to contribute and enhance this project! 😊
