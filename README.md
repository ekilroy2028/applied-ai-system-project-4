# CartoonPal

A cartoon copyright and visual history explorer built as an extension of the PawPal OOP project.

## Original project
PawPal was a pet care management system using Python OOP — Owner, Pet, Task, and Scheduler classes. CartoonPal replaces those with Cartoon, Creator, ProductionCompany, Series, OwnershipRecord, Era, Library, and CartoonAnalyzer, applying the same architectural principles to a new domain.

## What it does
- Identifies any cartoon by name, description, type, and debut year
- Tracks who created it (individual human creators)
- Tracks what company produced it (original studio)
- Records every series the character appeared in with years and medium
- Stores the complete ownership chain — who owned it originally, how it changed hands, and who owns it now
- Determines US copyright status using the 95-year corporate rule
- Shows how the character looked across visual eras with image links
- Flags cartoons approaching public domain and those that changed hands

## Quick start

```bash
pip install -r requirements.txt

# Verify backend logic
python main.py

# Run tests
python -m pytest tests/ -v

# Launch UI
streamlit run app.py
```

## File structure
```
cartoonpal/
├── cartoon_system.py      # All OOP classes (core logic)
├── seed_data.py           # Pre-built cartoon records
├── main.py                # CLI demo / verification script
├── app.py                 # Streamlit UI
├── tests/
│   └── test_cartoonpal.py # Automated test suite
├── assets/                # Architecture diagrams, screenshots
├── requirements.txt
└── README.md
```

## AI feature
CartoonPal uses the Anthropic Claude API (RAG pattern) to analyze copyright status for any cartoon the user searches. The AI receives structured data — name, debut year, ownership history — and returns a plain-English explanation with a confidence rating (HIGH / MEDIUM / LOW).

## Testing
```bash
python -m pytest tests/ -v
```
Tests cover: creator addition, series sorting, ownership chain logic, copyright boundary rules, library search/filter, analyzer sorting, series overlap detection, and seed data integrity.