================
Text-to-Text NLP
================

This project uses t5-base to translate English text to German, French or Romanian.

Machine Specs:

- RAM 16GB
- CPU 4CORE
- GPU 24GB Memory

Run locally:

    .. code-block:: bash

        $ chmod +x download_model_data.sh
        $ ./download_model_data.sh
        $ poetry install
        $ chmod +x run_app.sh
        $ ./run_app.sh

Run with docker:

    .. code-block:: bash

        $ chmod +x build_run_image.sh
        $ ./build_run_image.sh

Run linters:

    .. code-block:: bash

        $ chmod +x run_linters.sh
        $ ./run_linters.sh


