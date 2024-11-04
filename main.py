from dotenv import load_dotenv
import pyautogui
import time
import pyperclip
import google.generativeai as genai
import os

# Global variables for API keys
api_key = None

def configure():
    global api_key
    load_dotenv()
    api_key = os.getenv('api_key')

def process(custom_prompt):
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(custom_prompt)

  # Step 7: Get the response and print it
    response_text = response.text.strip()
    print("Gemini's suggested response:", response_text)
    pyperclip.copy(response_text)
    time.sleep(0.8)

  # Click on the chat window (adjust coordinates if needed)
    pyautogui.click(788, 1024)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')

# Initialize Gemini API
genai.configure(api_key=api_key)

#Take the name of the user of this bot
username=input(f"Enter Your Name: \n")
#Take the Display Name of the user to be replied
displayname=input("Enter the Display name of the user you want to reply to as it is:\n")

# Step 1: Move the cursor to the bottom of the screen (simulating taskbar appearing)
pyautogui.moveTo(314, 1078)

# Step 2: Wait for 1 second before clicking (giving the taskbar time to appear)
time.sleep(1)

# Step 3: Click on the icon at position (315, 1050)
pyautogui.click(315, 1050)

# Step 4: Pause for a moment to ensure the click is registered
time.sleep(0.5)  # Adjust the delay if necessary

configure()
while True:


  # Step 5: Drag from (601, 186) to (1869, 942)
  pyautogui.moveTo(601, 186)  # Move to the starting position
  pyautogui.mouseDown()       # Start the drag
  pyautogui.moveTo(1860, 978, duration=0.8)  # Drag to the ending position with a duration
  pyautogui.mouseUp()         # Release the mouse button

  # Step 6: Press Ctrl+C to copy the selected text
  pyautogui.hotkey('ctrl', 'c')
  pyautogui.click(1869,942)

  # Step 7: Get the copied text from the clipboard
  time.sleep(0.5)  # Give some time for the clipboard to update
  copied_text = pyperclip.paste()
  if copied_text:
      # Split the chat by lines
      chat_lines = copied_text.strip().splitlines()

      # Reverse the list to check from the last message
      chat_lines.reverse()

      # Now, we go through the reversed chat to find the most recent message
      last_sender = None
      for line in chat_lines:   
          line = line.strip()
          if line == displayname:
              last_sender = "displayname"
              break
          elif line == "You sent":
              last_sender = "You"
              break
      # Check if the last message was from displayname  
      if last_sender == "displayname":

          print("Last message is from displayname. Processing...")

          # Step 9: Send the chat history to Gemini for processing
          custom_prompt = f" You are someone named {username}, let's say. Here is a chat history:\n\n{copied_text}\n\nWhat would be a suitable response to this chat? Please don't say anything else, just exactly what would be suitable to say, very exact. And remember to speak like {username}. Please don't use too many emojis and don't be repetitive pls. Keep in mind, don't be repetitive. And write an essay if asked."

          try:
              process(custom_prompt)  # Run the Gemini processing function
          except Exception as e:
              print(f"Error processing with Gemini: {e}")
      else:
          print("The last message is not from displayname. No action taken.")
  else:
      print("No text copied to clipboard.")

  # Print or store the copied text in a variable
  print("Copied text:", copied_text)
  time.sleep(1)

