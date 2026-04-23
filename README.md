# Jarvis AI

A desktop voice assistant built with Python, Eel, JavaScript, and a browser-based UI.

## Features

- Voice input using `SpeechRecognition`
- Text-to-speech replies using `pyttsx3`
- Siri-style frontend wave UI
- Open apps using voice commands
- Play songs on YouTube
- Local SQLite database support through `jarvis.db`

## Project Structure

```text
Jarvis_ai/
|-- engine/
|   |-- command.py
|   |-- config.py
|   |-- db.py
|   |-- features.py
|-- www/
|   |-- index.html
|   |-- main.js
|   |-- controller.js
|   |-- style.css
|-- main.py
|-- requirements.txt
|-- jarvis.db
```

## Requirements

- Python 3.x
- Microsoft Edge installed
- Working microphone

Install dependencies:

```bash
pip install -r requirements.txt
```

## Running The Project

If you already have the local virtual environment:

```bash
.\envjarvis\Scripts\python.exe .\main.py
```

Or activate the environment first:

```bash
.\envjarvis\Scripts\Activate.ps1
python .\main.py
```

## Database

The project uses SQLite with `jarvis.db`.

`engine/db.py` is currently used to create tables and insert command data like app names and paths.

Example:

```python
INSERT INTO sys_command VALUES (null, 'One Note', 'C:\\Program Files\\Microsoft Office\\root\\Office16\\ONENOTE.exe')
```

## Main Files

- `main.py`: starts the app and opens the frontend
- `engine/command.py`: voice recognition and command routing
- `engine/features.py`: actions like opening apps and playing YouTube
- `engine/db.py`: database setup and inserts
- `www/index.html`: main UI
- `www/main.js`: frontend interactions
- `www/controller.js`: Eel UI updates

## Notes

- Make sure the Python packages are installed in the same environment you use to run the app.
- If voice modules like `eel`, `pyttsx3`, or `SpeechRecognition` fail to import, you are likely using the wrong Python interpreter.
- Some frontend animations are still under active development and may need further cleanup.

## Future Improvements

- Better database integration for app opening
- Cleaner frontend animation flow
- More voice commands
- Better error handling
- Smarter assistant responses
