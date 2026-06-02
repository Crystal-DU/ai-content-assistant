# AI Content Assistant

A modern Flask-based AI content extraction, transcription, and prompt generation tool.

Extract content from files, URLs, manual notes, or live speech input, review and edit the extracted text, then generate structured AI prompts for ChatGPT and other LLMs.

---

## Features

### Content Import

- TXT files
- Markdown files
- PDF documents
- PowerPoint presentations (.pptx)
- Web page URLs
- Manual text input
- Browser speech-to-text input

---

### Content Processing

- Automatic content extraction
- URL content scraping
- PDF text extraction
- PPT slide text extraction
- Editable preview area
- Live speech transcription
- Multi-language speech recognition

---

### Prompt Generation

- Structured AI prompt creation
- Learning summary templates
- Meeting summary mode
- One-click copy

---

### User Interface

- Modern SaaS-style dashboard
- Responsive layout
- Prompt Generator mode
- Meeting Summarizer mode
- Source information display
- File type detection
- Character counter
- Word counter
- Line counter
- Recording status indicator
- Reset All button

---

## Tech Stack

### Backend

- Python
- Flask
- BeautifulSoup4
- PyPDF
- python-pptx

### Frontend

- HTML5
- CSS3
- JavaScript
- Web Speech API

---

## Version History

### V1 – Initial Prompt Generator
Basic prompt generation from manually entered text.

### V2 – Multi-file Support
Added support for importing content from local files.

### V3 – Copy Function
Introduced one-click prompt copy functionality.

### V4 – Flask Web Interface
Migrated from console-based execution to a browser interface.

### V5 – TXT / Markdown Support
Added TXT and Markdown file upload capability.

### V6 – PDF Import Support
Added PDF text extraction using PyPDF.

### V7 – PowerPoint Import Support
Added PowerPoint (.pptx) text extraction.

### V8 – URL Import & Content Extraction
Added webpage scraping and automatic content extraction.

### V8.5 – Dashboard UI Redesign
Redesigned the application into a modern dashboard layout.

### V8.5.1 – UI Polish & Live Statistics
Added source information, file type display, and real-time content statistics.

### V9 – Dual Mode Architecture
Introduced Prompt Generator mode and Meeting Summarizer mode.

### V10 – Multi-Language Speech-to-Text
Added browser-based speech recognition with support for:

- English
- Japanese
- Chinese
- Korean

Included recording controls, language selector, and live transcription.

---

## Future Roadmap

### V11 – OCR Image Recognition
Extract text from screenshots, photos, and scanned documents.

### V12 – Audio / Video File Transcription
Support uploaded audio and video files.

### V13 – OpenAI API Integration
Generate prompts and summaries directly through AI APIs.

### V14 – AI Meeting Analysis
Automatic meeting summaries, action items, and key takeaways.

### V15 – Export Features
Export results to TXT, Markdown, PDF, and Word documents.

---

## License

MIT License
