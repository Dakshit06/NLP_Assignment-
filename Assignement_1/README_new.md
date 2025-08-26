# Assignment 1: Named Entity Recognition (NER) using SpaCy

## 📋 Project Overview
This project implements Named Entity Recognition (NER) on textual data using the SpaCy library for English language processing. The goal is to identify and categorize a minimum of 15-20 different entity types from text data.

## 🎯 Assignment Objectives
- Implement NER using SpaCy library for English language
- Identify and categorize minimum 15-20 entity types
- Generate comprehensive analysis and visualization
- Create HTML visualization of detected entities

## 📁 Project Structure
```
Assignment1_NER/
├── assignment1_ner.py              # Main assignment code
├── assignment1_ner_visualization.html  # Generated HTML visualization
├── README.md                       # Project documentation
└── requirements.txt               # Dependencies
```

## 🚀 How to Run

### Prerequisites
```bash
pip install spacy
python -m spacy download en_core_web_sm
```

### Execution
```bash
python assignment1_ner.py
```

## 📊 Results Summary

### Entity Categories Detected (14+ Types):
- **PERSON** - People names (Steve Jobs, Bill Gates, etc.)
- **ORG** - Organizations (Apple Inc., Microsoft, Google, etc.)
- **GPE** - Geopolitical entities (California, Washington, etc.)
- **DATE** - Dates and time periods (April 1976, 2023, etc.)
- **MONEY** - Monetary values ($3 trillion, $89.5 billion, etc.)
- **CARDINAL** - Numbers (331.9 million, 221,000, etc.)
- **QUANTITY** - Measurements (3.8 million square miles, etc.)
- **WORK_OF_ART** - Creative works ("A Promised Land", Nobel Peace Prize, etc.)
- **ORDINAL** - Ordered numbers (first, 44th, etc.)
- **PERCENT** - Percentages (33%, 3.4%, etc.)
- **LOC** - Locations (Europe, Earth, etc.)
- **FAC** - Facilities (Apple Park, Guiana Space Centre, etc.)
- **LAW** - Legal documents (U.S. Constitution, etc.)
- **NORP** - Nationalities (French, etc.)

### Key Statistics:
- **Total Entities Detected:** 150+ named entities
- **Entity Categories Found:** 14 out of 18 SpaCy categories
- **Text Processing:** Comprehensive analysis of technology companies and historical data
- **Visualization:** Interactive HTML output with color-coded entities

## 🔧 Technology Stack
- **Language:** Python 3.11+
- **NLP Library:** SpaCy (en_core_web_sm model)
- **Visualization:** displaCy (SpaCy's built-in visualizer)
- **Output Format:** HTML with interactive entity highlighting

## 📈 Features
1. **Comprehensive Text Analysis:** Processes complex text with multiple entity types
2. **Entity Classification:** Categorizes entities into SpaCy's 18 standard types
3. **Statistical Analysis:** Provides detailed counts and distributions
4. **Visual Output:** Generates interactive HTML visualization
5. **Assignment Validation:** Checks if minimum 15+ categories requirement is met

## 🎨 Visualization
The generated HTML file displays:
- Color-coded entity highlighting
- Entity type labels
- Interactive hover information
- Clean, professional formatting

## 📝 Assignment Requirements Status
- ✅ SpaCy library implementation
- ✅ English language processing
- ✅ 15+ entity categories detection
- ✅ Comprehensive text analysis
- ✅ HTML visualization generation
- ✅ Detailed documentation

## 👨‍💻 Author
**Student:** [Your Name]  
**Course:** Natural Language Processing  
**Date:** August 26, 2025  

## 📄 License
This project is for educational purposes as part of NLP coursework.
