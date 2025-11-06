# AI Reply Bot (Gemini-Powered Automation)

This Python-based automation tool integrates Google Gemini AI with PyAutoGUI to automatically read, process, and respond to on-screen text. It simulates human-like desktop interactions — selecting text, generating a contextual AI reply, and sending it back — creating a fully automated smart reply system.

## Overview

The AI Reply Bot performs the following:

* Extracts text from a target screen region using mouse and keyboard automation.
* Generates a response using the Gemini 1.5 Flash model from Google Generative AI.
* Pastes and sends the AI reply automatically back to the desired text input box.

This setup can automate messaging applications, support chats, or any on-screen text-response workflow.

## Features

* Fully automated mouse and keyboard control with `pyautogui`.
* Contextual, character-based replies generated via Google Gemini AI.
* Clipboard integration through `pyperclip`.
* Cleans Gemini output by removing extra formatting.
* Customizable screen coordinates for different interface layouts.

## Requirements

Install the dependencies:

```bash
pip install pyautogui pyperclip google-generativeai
```

## Usage

1.  Configure your **Google Gemini API key** inside the `ai_gemini()` function.
2.  Adjust the **screen coordinates** in the `automate()` and `send_reply_back()` functions to match your environment.
3.  Run the script:

    ```bash
    python main.py
    ```

The bot will automatically:
1.  Click through your interface
2.  Copy selected text
3.  Generate an AI-based response
4.  Paste and send the reply back

## How It Works

* **`automate()`**: Performs GUI actions to select and copy text.
* **`ai_gemini()`**: Sends text to Gemini and retrieves an adaptive, concise reply.
* **`send_reply_back()`**: Automates pasting and sending the AI-generated message.

## Notes

* Ensure your screen resolution and coordinates match the target interface.
* Avoid using during manual computer control — the bot takes full mouse and keyboard control.
* API key should remain private and never be pushed to public repositories.

## License

This project is released under the [MIT License](LICENSE).
