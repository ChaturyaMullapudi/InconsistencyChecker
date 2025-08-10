# Noogat Inconsistency Checker

A Python tool that uses langchain and Gemini AI to analyze PowerPoint presentations and images for logical inconsistencies, contradictions, and contextual gaps.

## Features

- Extract text from PowerPoint presentations and images
- LangChain integration for robust AI interactions
- Support for batch processing of multiple PowerPoint decks (analyzes each deck independently without cross-deck comparison)
- Parallel OCR processing for faster image analysis
- Smart caching system to avoid reprocessing unchanged files
- Detailed logging of processing steps

## Prerequisites

- Python 3.8 or higher
- Tesseract OCR
- Google Gemini API key

## Installation

### 1. Set Up Dependencies
```powershell
# Install Python packages
pip install -r requirements.txt

# Verify Tesseract installation
tesseract --version
```

### 2. Configure Environment
Create a `.env` file:
```env
GOOGLE_API_KEY=your_gemini_api_key_here
```

## Usage

### Single PowerPoint File
```powershell
python app.py --pptx "path/to/presentation.pptx"
```

### Multiple PowerPoint Files
```powershell
python app.py --pptx-folder "path/to/presentations/folder"
```

### Image Analysis
```powershell
# Analyze a folder of images
python app.py --images "path/to/images/folder"
```

### Example Commands
```powershell
# Single PowerPoint file
python app.py --pptx "data/deck1.pptx"

# Multiple PowerPoint files
python app.py --pptx-folder "data/presentations"

# Image folder analysis
python app.py --images "data/images"
```

## Advanced Features

### LangChain Integration
- Structured prompt management using PromptTemplate
- Simplified AI model interaction through ChatGoogleGenerativeAI
- Built-in error handling and response processing
- Model-agnostic design for easy AI provider switching

### Caching System
- Cache location: `./cache/`
- Stores processed text and OCR results
- Automatically reuses cached results for unchanged files
- Significantly improves processing speed for repeated analyses

### Parallel Processing
- Uses ThreadPoolExecutor for parallel OCR processing
- Improves performance when analyzing multiple images
- Automatically scales based on system capabilities

### Logging
The tool provides detailed logging:
- Processing steps and progress
- Cache usage information
- API request status
- Error messages and warnings

## Project Structure
```
InconsistencyChecker/
│
├── app.py              # Main application file
├── extract.py          # Text extraction utilities
├── llm.py             # Gemini AI integration
├── utils.py           # Utility functions and helpers
├── requirements.txt    # Python dependencies
├── .env               # Environment variables
└── README.md          # Documentation
```

## Troubleshooting

### Common Issues
- **Cache Issues**: Delete the `cache` folder to force reprocessing
- **Token Limits**: Adjust `MAX_SLIDES_PER_CALL` in the script if needed
- **Memory Usage**: For large folders, process in smaller batches

### Verification Commands
```powershell
# Check Tesseract installation
tesseract --version

# Test environment variables
python -c "import os; from dotenv import load_dotenv; load_dotenv(); print(os.getenv('GOOGLE_API_KEY'))"

# Clear cache if needed
rm -r ./cache/*
```