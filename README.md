# Build Real-Time AI Voice Assistant with RAG Pipeline and Memory | Mistral LLM | Ollama

This repository contains code for a real-time voice assistant designed for e-commerce and grocery shopping. The assistant continuously listens, transcribes user input, retrieves relevant product details and policies using a RAG pipeline, and generates responses using an AI model.

## Features

- *Real-time voice input processing* using Whisper STT.
- *Dynamic product search and retrieval* using FAISS/ChromaDB with locally stored Amazon product embeddings.
- *Live product details* (price, availability, delivery options) fetched using Playwright/Selenium.
- *Order tracking and policy retrieval* powered by PostgreSQL/SQLite and FAISS.
- *Conversational memory* for context-aware interactions.
- *RAG-based response generation* using LangChain and Ollama (Mistral/DeepSeek).
- *Interactive UI* built with React (Vite), TypeScript, and Tailwind CSS.
- *TTS support* for natural-sounding responses.

## Prerequisites

Before running the project, ensure you have the following dependencies installed:

- Python *3.8+*
- pyaudio
- numpy
- faster_whisper
- qdrant_client
- faiss-cpu
- langchain
- ollama
- Other dependencies specified in requirements.txt

## Usage

### Demo Video
Watch the demo video here:

![Demo Video](video/demo.mp4)

### Setup Instructions

1. *Clone the repository*:
   bash
   git clone https://github.com/your-repo/voice_assistant_ai.git
   cd voice_assistant_ai
## Setup Instructions

### Set up a virtual environment (optional but recommended):
bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


### Install dependencies:
bash
pip install -r requirements.txt


### Start the backend server:
bash
python app.py


### Run the frontend UI:
bash
cd frontend
npm install
npm run dev


## Interact with the Assistant

- Speak into the microphone when prompted.
- The assistant will retrieve and respond with relevant product details.

## Configuration

- Adjust model settings (e.g., chunk size, response delay) in config.py.
- Modify database and storage paths as per your local setup.
- Update web scraping settings in the Playwright/Selenium script if needed.

## Notes

- Ensure your microphone is properly configured.
- API rate limits might apply when fetching live product details.
- Handle exceptions gracefully during real-time data retrieval and processing.

## Team - Byte Me

- *Varshan A V R* - 22BRS1060
- *Sai Sathwik Matury* - 22BRS1018
- *Jasmine Tresa Jose* - 22BRS1046
- *Sam Stewart* - 22BRS1107

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- *Mistral LLM & DeepSeek* for language modeling.
- *faster_whisper* for efficient speech-to-text transcription.
- *LangChain & Ollama* for the RAG pipeline.
- *ChromaDB, FAISS & Qdrant* for knowledge retrieval.
- *Selenium & Playwright* for real-time product details fetching.
- *React, TypeScript, and Tailwind CSS* for UI development.
