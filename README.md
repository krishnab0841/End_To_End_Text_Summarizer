# End_To_End_Text_Summarizer

## Workflows

1. update config.yaml
2. update params.yaml
3. update entity
4. update the configuration manager in src config
5. update the components
6. update the pipeline
7. update the main.py
8. update the app.py

## Project Overview
This project is a comprehensive End-to-End Text Summarizer built using Python and the Hugging Face Transformers library. It leverages the Pegasus model to generate concise summaries of dialogue-based text (trained on the SAMSum dataset). The project is structured with a modular pipeline design, ensuring scalability and ease of maintenance.

## Key Features
- **Modular Pipeline**: Distinct stages for Data Ingestion, Validation, Transformation, Model Training, and Evaluation.
- **State-of-the-Art Model**: Utilizes Google's Pegasus model for high-quality abstractive summarization.
- **Configuration Management**: Centralized configuration via `config.yaml` and `params.yaml`.
- **Logging**: Robust logging system for tracking pipeline execution.

## Tech Stack
- **Language**: Python
- **Libraries**: Hugging Face Transformers, PyTorch, Datasets, Pandas, NLTK
- **Tools**: Docker, FastAPI (planned)

## How to Run

### 1. Clone the Repository
To get started, clone the repository to your local machine:
```bash
git clone https://github.com/krishnab0841/End_To_End_Text_Summarizer.git
cd End_To_End_Text_Summarizer
```

### 2. Create a Virtual Environment
It is recommended to use a virtual environment to manage dependencies:
```bash
conda create -n summary python=3.8 -y
conda activate summary
```

### 3. Install Dependencies
Install the required Python packages:
```bash
pip install -r requirements.txt
```

### 4. Run the Pipeline
Execute the main script to run the entire training and evaluation pipeline:
```bash
python main.py
```

## Project Structure
- `config/`: Configuration files.
- `src/`: Source code for components and pipelines.
- `research/`: Jupyter notebooks for experimentation.
- `artifacts/`: Generated artifacts (datasets, models, metrics).