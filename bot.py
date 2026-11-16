import os
import time
import threading
import requests
from http.server import BaseHTTPRequestHandler, HTTPServer

TOKEN = "9100885514:AAHZeZlMQdDJycqHJKeNJvbhXud1VEJjg3E"
MY_ID = 8488756952

class DummyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot is alive")

def run_dummy_server():
    port = int(os.environ.get("PORT", 8080))
    server = HTTPServer(('0.0.0.0', port), DummyHandler)
    server.serve_forever()

def main():
    print("Bot en écoute...")
    last_update_id = 0
    while True:
        try:
            url = f"https://api.telegram.org/bot{TOKEN}/getUpdates?offset={last_update_id}&timeout=30"
            response = requests.get(url, timeout=35)
            data = response.json()
            
            if data.get("ok") and data.get("result"):
                for update in data["result"]:
                    last_update_id = update["update_id"] + 1
                    
                    if "message" in update and "text" in update["message"]:
                        message = update["message"]
                        chat_id = message["chat"]["id"]
                        text = message["text"]
                        
                        if chat_id == MY_ID and text == "/start":
                            reply_url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
                            requests.post(reply_url, json={
                                "chat_id": chat_id, 
                                "text": "Caw. Le bot est en ligne et prêt à recevoir."
                            })
        except Exception as e:
            print(f"Erreur réseau, on réessaie dans 2s...")
            time.sleep(2)

if __name__ == '__main__':
    # Lance le faux serveur web pour Render
    threading.Thread(target=run_dummy_server, daemon=True).start()
    # Lance le bot
    main()