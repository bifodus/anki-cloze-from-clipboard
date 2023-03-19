import sys
import requests
import tkinter as tk
from tkinter import simpledialog
from tkinter import Tk
from AppKit import NSPasteboard, NSStringPboardType

ANKI_CONNECT_URL = 'http://127.0.0.1:8765'

def invoke(action, params):
    payload = {'action': action, 'params': params, 'version': 6}
    response = requests.post(ANKI_CONNECT_URL, json=payload)
    return response.json()

def get_decks():
    return invoke('deckNames', {})

def display_deck_selection(decks, full_text):
    def on_deck_selected(*args):
        selected_deck.set(selected.get())

    root = Tk()
    root.withdraw()
    selection_dialog = tk.Toplevel(root)
    selection_dialog.title("Anki Cloze Card Creator")

    tk.Label(selection_dialog, text="Select a deck for the new Anki Cloze Card:").grid(row=0, column=0, padx=10, pady=10, sticky="w")

    selected = tk.StringVar()
    selected.set(decks[0])
    selected_deck = tk.StringVar()
    option_menu = tk.OptionMenu(selection_dialog, selected, *decks, command=on_deck_selected)
    option_menu.grid(row=0, column=1, padx=10)

    tk.Label(selection_dialog, text="Select the text you want to cloze:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
    text_widget = tk.Text(selection_dialog, wrap=tk.WORD)
    text_widget.insert(tk.END, full_text)
    text_widget.grid(row=1, column=1, padx=10)

    def on_ok():
        selected_deck.set(selected.get())
        cloze_start, cloze_end = text_widget.index(tk.SEL_FIRST), text_widget.index(tk.SEL_LAST)
        cloze_text.set(text_widget.get(cloze_start, cloze_end))
        selection_dialog.destroy()

    def on_cancel():
        selected_deck.set(None)
        selection_dialog.destroy()

    cloze_text = tk.StringVar()
    tk.Button(selection_dialog, text="OK", command=on_ok).grid(row=2, column=0, padx=(10, 0), pady=10)
    tk.Button(selection_dialog, text="Cancel", command=on_cancel).grid(row=2, column=1, padx=(0, 10), pady=10)

    root.wait_window(selection_dialog)
    root.destroy()

    return selected_deck.get(), cloze_text.get()

def create_cloze_card(deck_name, cloze_text):
    full_text = get_clipboard_text()
    print(full_text.replace(cloze_text, f"{{c1::{cloze_text}}}"))
    note = {
        "deckName": deck_name,
        "modelName": "Cloze",
        "fields": {
            "Text": full_text.replace(cloze_text, f"{{{{c1::{cloze_text}}}}}"),
            "Extra": "",
        },
        "tags": [],
        "options": {
            "allowDuplicate": False,
        },
    }
    result = invoke("addNote", {"note": note})
    print(result)

def get_clipboard_text():
    pb = NSPasteboard.generalPasteboard()
    return pb.stringForType_(NSStringPboardType)

if __name__ == "__main__":
    full_text = get_clipboard_text()
    if full_text:
        deck_names = get_decks()['result']
        selected_deck, cloze_text = display_deck_selection(deck_names, full_text)
        if selected_deck:
            create_cloze_card(selected_deck, cloze_text)
            print("Cloze card created in deck:", selected_deck)
    else:
        print("No text found in clipboard.")
