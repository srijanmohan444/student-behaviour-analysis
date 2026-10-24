# Student Behaviour Analysis Using Social Media
**Subject:** Computer Graphics and Multimedia  
**Branch:** Information Technology (IT), 4th Year

A local, API-key-free Flask demonstration app that searches fictional student records and visualizes rule-based sentiment and topic indicators from sample posts.

## Features
- Search students by full or partial name.
- Show sample profile, posts, post dates and demo engagement counts.
- Transparent keyword-based positive/neutral/negative text labels.
- Topic keyword indicators and Chart.js visualizations.
- Responsive dashboard UI.
- Four fictional student profiles and sample posts.
- No social media scraping, login, API key or external data collection.

## Requirements
- Python 3.9 or newer
- Internet connection for the optional CDN-hosted Chart.js and Google Fonts. The app and analysis run locally; if offline, charts may not render until Chart.js is downloaded locally.

## Run on Windows
1. Extract the ZIP.
2. Open Command Prompt or PowerShell in the project folder.
3. Create a virtual environment:
   ```powershell
   py -m venv .venv
   .venv\Scripts\activate
   ```
4. Install dependencies:
   ```powershell
   pip install -r requirements.txt
   ```
5. Start the application:
   ```powershell
   python app.py
   ```
6. Open `http://127.0.0.1:5000` in your browser.
7. Search for Aanya Sharma, Rohan Verma, Meera Patel, or Kabir Khan.

## Run on macOS / Linux
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```
Then open `http://127.0.0.1:5000`.

## Project structure
```text
student_behaviour_analysis/
├── app.py
├── requirements.txt
├── README.md
├── data/
│   └── sample_data.json
├── templates/
│   └── index.html
└── static/
    └── style.css
```

## How it works
1. The user enters a name.
2. Flask searches the local JSON sample dataset.
3. A transparent keyword lexicon counts a limited list of positive and negative words in each post.
4. A post is labelled Positive, Negative or Neutral based on which count is greater; ties are Neutral.
5. Topic labels are generated from explicit keyword lists.
6. The browser displays the results and charts.

## Limitations and responsible use
- All included people, handles and posts are fictional examples.
- Sentiment and topic detection are simplistic rule-based signals, not validated behavioural measurements.
- The output cannot establish personality, intent, mental health, risk, academic performance or disciplinary issues.
- Do not use the tool to make decisions about real students.
- For any real-world integration, obtain informed consent, use authorized platform APIs and comply with platform terms, privacy law and institutional policy. Never scrape private content or bypass access controls.
- The app currently does not connect to social media platforms and does not retrieve real profiles from a name alone.

## Troubleshooting
- **`python` not found:** install Python 3.9+ and enable “Add Python to PATH” on Windows, or use `py`.
- **`ModuleNotFoundError: flask`:** activate the virtual environment and run `pip install -r requirements.txt`.
- **Port 5000 busy:** change `port=5000` in the last line of `app.py` to another port, such as `5001`, and open that port in the browser.
