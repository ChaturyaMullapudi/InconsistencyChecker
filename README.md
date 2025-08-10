# Noogat Inconsistency Checker

A Python tool that uses Gemini AI to analyze PowerPoint presentations and images for logical inconsistencies, contradictions, and contextual gaps.

## Features

- Extract text from PowerPoint presentations
- Extract text from images using OCR (Optical Character Recognition)
- Analyze content using Google's Gemini AI
- Detect inconsistencies across slides
- Support for multiple image formats (PNG, JPG, JPEG)

## Prerequisites

- Python 3.8 or higher
- Tesseract OCR
- Google Gemini API key

## System Dependencies

### 1. Tesseract OCR Installation
1. Download the installer from [Tesseract at UB Mannheim](https://github.com/UB-Mannheim/tesseract/wiki)
2. Run the installer (select "Add to PATH" during installation)
3. Default installation path: `C:\Program Files\Tesseract-OCR`
4. Verify installation:
```powershell
tesseract --version
```

## Installation

### 1. Clone the Repository
```powershell
git clone https://github.com/ChaturyaMullapudi/InconsistencyChecker.git
cd InconsistencyChecker
```

### 2. Set Up Python Environment
```powershell
python -m venv venv
.\venv\Scripts\activate
```

### 3. Install Dependencies

```powershell
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Create a `.env` file in the project root:
```env
GOOGLE_API_KEY=your_gemini_api_key_here
```

## Usage

### Analyzing PowerPoint Files
```powershell
python noogat_inconsistency_checker.py --pptx "path/to/presentation.pptx"
```

### Analyzing Images
```powershell
python noogat_inconsistency_checker.py --images "path/to/images/folder"
```

### Example Commands
```powershell
# Analyze a PowerPoint file
python noogat_inconsistency_checker.py --pptx "presentations/deck.pptx"

# Analyze a folder of images
python noogat_inconsistency_checker.py --images "images/folder"
```

## Project Structure
```
InconsistencyChecker/
│
├── noogat_inconsistency_checker.py  # Main script
├── requirements.txt                 # Python dependencies
├── .env                            # Environment variables (create this)
└── README.md                       # Documentation
```

## Troubleshooting

### Tesseract Not Found
- Verify Tesseract installation:
```powershell
tesseract --version
```
- Check if Tesseract is in PATH:
```powershell
$env:Path -split ';' | Select-String "Tesseract"
```
- Update Tesseract path in script if needed:
```python
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
```
