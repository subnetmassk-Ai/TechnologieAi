import json
import re
import subprocess
import speech_recognition as sr

def get_phone_contacts():
    print("[+] Fetching contacts from your phone...")
    res = subprocess.run("termux-contact-list", shell=True, capture_output=True, text=True)
    try:
        contacts_list = json.loads(res.stdout)
        return contacts_list
    except Exception:
        return []

def open_whatsapp(digits):
    print(f"[+] Opening WhatsApp for: {digits}")
    cmd = f"am start -a android.intent.action.VIEW -d 'whatsapp://send?phone={digits}'"
    subprocess.run(cmd, shell=True)

# Option 1: Search / Scroll from contacts
def hidden_scroll_contacts():
    contacts = get_phone_contacts()
    if not contacts:
        print("[-] No contacts found or permission denied.")
        return

    print("\n==============================")
    print("    CONTACTS LIST (SCROLL)    ")
    print("==============================")
    print(" - Contacts loaded. Scroll up/down or type a name to search.")
    print(" - Type '0' to go back.")
    print("==============================")
    
    for idx, contact in enumerate(contacts, start=1):
        name = contact.get('name', 'Unknown')
        print(f"[{idx}] {name}")

    print("==============================")
    user_input = input("Enter index number or type name to search: ").strip()

    if user_input == '0':
        return
    elif user_input.isdigit():
        idx = int(user_input) - 1
        if 0 <= idx < len(contacts):
            selected_num = contacts[idx].get('number', '')
            digits = re.sub(r'\D', '', selected_num)
            if len(digits) == 8:
                digits = '961' + digits
            open_whatsapp(digits)
        else:
            print("[-] Invalid contact index.")
    else:
        search_query = user_input.lower()
        matches = [c for c in contacts if search_query in c.get('name', '').lower()]
        if not matches:
            print("[-] No matching contacts found.")
        else:
            print(f"\n[+] Matching results ({len(matches)}):")
            for m_idx, match in enumerate(matches, start=1):
                print(f"[{m_idx}] {match.get('name')}")
            
            sub_choice = input("Select number from search results: ").strip()
            if sub_choice.isdigit() and 1 <= int(sub_choice) <= len(matches):
                selected_num = matches[int(sub_choice) - 1].get('number', '')
                digits = re.sub(r'\D', '', selected_num)
                if len(digits) == 8:
                    digits = '961' + digits
                open_whatsapp(digits)

# Option 2: Manual number entry
def manual_input_direct():
    num_input = input("\nEnter phone number directly: ").strip()
    digits = re.sub(r'\D', '', num_input)
    if len(digits) == 8:
        digits = '961' + digits

    if digits and digits != '961':
        open_whatsapp(digits)
    else:
        print("[-] Invalid phone number.")

# Option 3: Voice search
def fast_voice_search():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("\n[+] Speak now (Fast Listening)...")
        try:
            audio_data = recognizer.listen(source, timeout=6, phrase_time_limit=6)
        except sr.WaitTimeoutError:
            print("[-] No speech detected.")
            return

    print("[+] Processing audio instantly...")
    try:
        text = recognizer.recognize_google(audio_data, language="ar-SA")
        print(f"[+] Recognized: {text}")

        digits = re.sub(r'\D', '', text)
        if len(digits) == 8:
            digits = '961' + digits

        if digits:
            open_whatsapp(digits)
        else:
            print("[-] No valid number found.")
    except Exception as e:
        print(f"[-] Error: {e}")

def main():
    while True:
        print("\n==============================")
        print("      WHATSAPP ASSISTANT      ")
        print("==============================")
        print("[1] Search / Scroll Contacts")
        print("[2] Manual Phone Number Entry")
        print("[3] Voice Search")
        print("[0] Exit")
        print("==============================")
        
        choice = input("Select an option: ").strip()
        
        if choice == '1':
            hidden_scroll_contacts()
        elif choice == '2':
            manual_input_direct()
        elif choice == '3':
            fast_voice_search()
        elif choice == '0':
            print("Exiting...")
            break
        else:
            print("[-] Invalid choice, try again.")

if __name__ == "__main__":
    main()

