# Secure Password Generator

A small terminal program that generates random passwords using Python's `secrets` module.

## English

### Features

- Choose a password length from 8 to 128 characters.
- Choose how many passwords to generate.
- Choose whether to include numbers and symbols.
- Always include at least one lowercase and one uppercase letter.
- Include at least one character from each optional group that you select.
- Use only Python's standard library. No extra packages are required.

### Requirements

- Python 3.9 or newer

### Run locally

1. Download or clone this repository.
2. Open a terminal in the project folder.
3. Run the program:

   **Windows:**
   ```powershell
   py password_generator.py
   ```

   **macOS / Linux:**
   ```bash
   python3 password_generator.py
   ```

4. Answer the questions in the terminal. Press Enter to accept each default value.

### Project file

- `password_generator.py` — contains the input helpers, password-generation function, and main program.

### How it works

- `ask_for_number()` checks that the length and number of passwords are valid.
- `ask_yes_no()` reads the optional number and symbol choices.
- `generate_password()` builds the character groups, selects characters with `secrets.choice()`, and shuffles the result with `secrets.SystemRandom()`.
- `main()` asks the questions and prints the generated passwords.

Python's `secrets` module is designed for generating values used in security-sensitive contexts. Do not share generated passwords or save them in a public repository. Use a trusted password manager to store passwords safely.

<img width="1203" height="540" alt="image" src="https://github.com/user-attachments/assets/dc56fdbc-22cb-45c8-a0e4-8d0d3dfd3dd0" />

## Deutsch

Ein kleines Terminalprogramm, das zufällige Passwörter mit dem Python-Modul `secrets` erstellt.

### Funktionen

- Auswahl einer Passwortlänge von 8 bis 128 Zeichen.
- Auswahl der Anzahl der zu erstellenden Passwörter.
- Optionale Einbindung von Zahlen und Sonderzeichen.
- Mindestens ein Kleinbuchstabe und ein Großbuchstabe sind immer enthalten.
- Aus jeder zusätzlich ausgewählten Zeichengruppe wird mindestens ein Zeichen verwendet.
- Verwendet nur die Python-Standardbibliothek. Zusätzliche Pakete sind nicht erforderlich.

### Voraussetzungen

- Python 3.9 oder neuer

### Lokal starten

1. Lade dieses Repository herunter oder klone es.
2. Öffne ein Terminal im Projektordner.
3. Starte das Programm:

   **Windows:**
   ```powershell
   py password_generator.py
   ```

   **macOS / Linux:**
   ```bash
   python3 password_generator.py
   ```

4. Beantworte die Fragen im Terminal. Mit Enter übernimmst du jeweils den Standardwert.

### Projektdatei

- `password_generator.py` — enthält die Eingabe-Funktionen, die Passwortgenerierung und das Hauptprogramm.

### Funktionsweise

- `ask_for_number()` prüft, ob die Passwortlänge und die Anzahl der Passwörter gültig sind.
- `ask_yes_no()` liest die Auswahl für Zahlen und Sonderzeichen.
- `generate_password()` erstellt die Zeichengruppen, wählt Zeichen mit `secrets.choice()` aus und mischt das Ergebnis mit `secrets.SystemRandom()`.
- `main()` stellt die Fragen und gibt die generierten Passwörter aus.

Das Python-Modul `secrets` wurde für die Erzeugung von Werten entwickelt, die in sicherheitsrelevanten Bereichen verwendet werden. Teile generierte Passwörter nicht und speichere sie nicht in einem öffentlichen Repository. Verwende einen vertrauenswürdigen Passwortmanager zur sicheren Aufbewahrung.

## Suggested GitHub repository details / GitHub-Repository-Angaben

- **Repository name:** `secure_password_generator`
- **Description:** `Generate random passwords in the terminal using Python's secrets module.`
- **Topics:** `python`, `cli`, `command-line`, `password-generator`, `secrets-module`, `cybersecurity`, `beginner-project`, `portfolio`
