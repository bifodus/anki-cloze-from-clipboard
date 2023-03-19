# Anki Cloze Card Creator

Anki Cloze Card Creator is a Python script that allows you to create Anki cloze cards directly from your macOS clipboard. It utilizes Anki Connect, a plugin that enables external applications to communicate with Anki. This app enables you to select a deck and create cloze cards without having to manually open Anki.

## Prerequisites

1. Anki installed on your system. Download from https://apps.ankiweb.net/.
2. Anki Connect plugin installed on your Anki app. Get it from https://ankiweb.net/shared/info/2055492159 and follow the installation instructions provided.
3. Python 3 installed on your macOS system.

## Usage

1. Copy a text that you want to create a cloze card for to the clipboard.
2. Run the `anki_cloze_from_clipboard.py` script by executing the following command in the terminal:

```bash
python3 anki_cloze_from_clipboard.py
```

3. A dialog box will appear, prompting you to select a deck and highlight the text you want to cloze.
4. After selecting the deck and highlighting the cloze text, click "OK." The script will create a new cloze card in the selected deck with the highlighted text as the clozed part.

To create a global hotkey (Cmd+Shift+C) for running the script, follow the instructions in the hammerspoon_config.lua file and use Hammerspoon.

## License

This project is licensed under the MIT License.

## Acknowledgments

- Anki: https://apps.ankiweb.net/
- Anki Connect: https://ankiweb.net/shared/info/2055492159
