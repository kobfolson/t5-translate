================
Text-to-Text NLP
================

This project uses t5-base to translate English text to German, French or Romanian.

Machine Specs:

- RAM 16GB
- CPU 4CORE
- GPU 24GB Memory

Run locally:

1. Download model-data, add permissions to download_model_data.sh > chmod +x download_model_data.sh
2. Run download_model_data.sh > ./download_model_data.sh
3. Install dependencies > poetry install
4. Add permissions to run_app.sh > chmod +x run_app.sh
5. Run file >  ./run_app.sh

Run with docker:

1. Add permissions to build_run_image.sh > chmod +x build_run_image.sh
2. Run file > ./build_run_image.sh

Run linters:

1. Add permissions to run_linters.sh > chmod +x run_linters.sh
2. Run file > ./run_linters.sh


