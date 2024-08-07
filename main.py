import pyautogui
import pyperclip
import time
import google.generativeai as genai  # gemini
import re  # removing *," " in gemini request


# Function to perform the required actions
def automate():
    # 1106,1050 then 1165, 945 icon
    # 697,272 to 1386,895
    # 1850,812 click

    # Click on the icon at (1106, 1050)
    pyautogui.click(1106, 1050)
    time.sleep(0.5)  # Wait for 1 second for the action to complete

    # Click on the icon at (1165, 945)
    pyautogui.click(1165, 945)
    time.sleep(0.5)  # Wait for 1 second for the action to complete

    # Move to the starting point of text selection
    pyautogui.moveTo(697, 272)
    pyautogui.mouseDown()  # Press the mouse button down
    time.sleep(0.5)

    # Drag to the end point of text selection
    pyautogui.moveTo(1386, 895, duration=1)  # Dragging with a duration of 2 seconds
    pyautogui.mouseUp()  # Release the mouse button
    time.sleep(0.5)

    # Press Ctrl+C to copy the selected text
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.5)  # Wait for the clipboard to update

    # Get the text from the clipboard
    extracted_text = pyperclip.paste()

    # Click at (1850, 885)
    pyautogui.click(1850, 812)

    return extracted_text


def ai_gemini(user_command):
    # Configure the API key
    genai.configure(api_key="AIzaSyCy5SpZikvV2SUl97RNm1pSIZjF1lynD3M")

    # Create the model with generation config
    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 64,
        "max_output_tokens": 1000,
        "response_mime_type": "text/plain",
    }

    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config=generation_config,
    )

    # Start a chat session with an initial user message
    chat_history = [
        {
            "role": "user",
            "parts": [
                f"You are 𝘚𝘈𝘓𝘔𝘈𝘕 𝘒𝘏𝘈𝘕, a person who speaks English, Urdu, and Roman Urdu. You are a boy, a BS CS student, and an optimistic person. Respond to the following in character as Naruto in one 1 concise reply: {user_command} Also omit [6/27/2024] Naruto CS: part, it should just have reply"
            ]
        }
    ]

    chat_session = model.start_chat(history=chat_history)

    # Send a message and get a response
    response = chat_session.send_message({"role": "user", "parts": [user_command]})

    # Process the response text to remove asterisks
    clean_text = re.sub(r'\*+', '', response.text)

    return clean_text


def send_reply_back(response_text):
    # Click at the text input box (coordinates 1230, 957)
    pyautogui.click(1230, 957)
    time.sleep(0.5)  # Wait for the action to complete

    # Paste the text from the response
    pyperclip.copy(response_text)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.5)  # Wait for the action to complete

    # Press Enter
    pyautogui.press('enter')


# main starts
if __name__ == "__main__":
    # Run the automation function
    chat_history = automate()
    # Print the chat log
    print(chat_history)
    response = ai_gemini(chat_history)
    # Print the extracted text
    print("Gemini Response:", response)
    # Send the reply back
    send_reply_back(response)

# import pyautogui
#
# while True:
#     print(pyautogui.position())
#     # 1106,1050 then 1165, 945 icon
#     # 697,272 to 1386,895
#     # 1850,812 click
#     # 1230, 957 for enter box
