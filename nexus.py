import speech_recognition as sr
import webbrowser
import pyautogui
import datetime
import pyttsx3
import time
import os
import tkinter as tk
from tkinter import scrolledtext
import threading

# --- AYARLAR ---
engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('volume', 1.0)

# --- REHBER ---
rehber = {
    "kıvırcık": "905526205852", "curly": "905526205852",
    "öykü": "905526205852",     "story": "905526205852",
    "sevgili": "905526205852",  "darling": "905526205852",
    "babam": "905326302599",    "dad": "905326302599",
    "annem": "905065140754",    "mom": "905065140754"
}

# Global Değişkenler
yazi_alani = None
buton = None 
aktif_dil = "tr-TR" 

def konus(metin, ekranda_goster=True):
    print(f"ASİSTAN: {metin}")
    if yazi_alani and ekranda_goster:
        yazi_alani.config(state='normal') 
        yazi_alani.insert(tk.END, "NEXUS: " + metin + "\n")
        yazi_alani.see(tk.END) 
        yazi_alani.config(state='disabled') 

def son_satiri_sil():
    """Ekrana yazılan son kullanıcı girdisini siler."""
    if yazi_alani:
        yazi_alani.config(state='normal')
        # Son '>>' işaretini bulup oradan sonrasını siliyoruz
        text_content = yazi_alani.get("1.0", tk.END)
        last_index = text_content.rfind(">>")
        
        if last_index != -1:
            # Satır sayısını hesaplayıp siliyoruz (Basitçe son 2 satırı temizler)
            yazi_alani.delete("end-2l", "end-1c") 
            
        yazi_alani.config(state='disabled')

def dinle(r, source, ekrana_yaz=False):
    global aktif_dil
    
    try:
        # Dinleme başlıyor...
        print("Mikrofon dinlemede...") # Terminal kontrolü için
        audio = r.listen(source, timeout=None, phrase_time_limit=5)
        gelen_ses = r.recognize_google(audio, language=aktif_dil).lower()
        
        # DUYULANI EKRANA YAZ
        if ekrana_yaz and yazi_alani and gelen_ses:
            yazi_alani.config(state='normal')
            yazi_alani.insert(tk.END, ">> " + gelen_ses + "\n")
            yazi_alani.see(tk.END)
            yazi_alani.config(state='disabled')
            
        print(f"DUYULAN ({aktif_dil}): {gelen_ses}") 
        return gelen_ses

    except sr.WaitTimeoutError:
        return ""
    except sr.UnknownValueError:
        return ""
    except sr.RequestError:
        konus("İnternet hatası.")
        return ""
    except Exception as e:
        print(f"Hata: {e}")
        return ""

def komutlari_isle(emir):
    global aktif_dil
    emir = emir.replace(".", "").replace(",", "").replace("!", "")

    # --- DİL DEĞİŞTİRME ---
    if "speak english" in emir or "switch to english" in emir or "ingilizce konuş" in emir:
        aktif_dil = "en-US"
        konus("English selected.")
        return True
    elif "türkçe konuş" in emir or "türkçe'ye geç" in emir or "speak turkish" in emir:
        aktif_dil = "tr-TR"
        konus("Türkçe seçildi.")
        return True

    if "iptal" in emir or "cancel" in emir or "tamam" in emir or "stop" in emir:
        return True 

    # --- KİŞİ İŞLEMLERİ ---
    bulunan_isim = None
    bulunan_numara = None
    for isim in rehber:
        if isim in emir:
            bulunan_isim = isim
            bulunan_numara = rehber[isim]
            break
            
    if bulunan_isim and ("ara" in emir or "call" in emir or "mesaj" in emir or "message" in emir or "whatsapp" in emir):
        link = f"whatsapp://send?phone={bulunan_numara}"
        if "video" in emir or "görüntülü" in emir:
            konus(f"Video: {bulunan_isim}")
            webbrowser.open(link); time.sleep(8); pyautogui.click(x=960, y=540); pyautogui.hotkey('ctrl', 'shift', 'u') 
        elif "voice" in emir or "sesli" in emir or "ara" in emir or "call" in emir:
            konus(f"Arama: {bulunan_isim}")
            webbrowser.open(link); time.sleep(8); pyautogui.click(x=960, y=540); pyautogui.hotkey('ctrl', 'shift', 'c')
        else:
            konus(f"Sohbet: {bulunan_isim}")
            webbrowser.open(link)
        return True

    # --- DİĞER KOMUTLAR ---
    elif "whatsapp" in emir or "mesaj" in emir:
        konus("WhatsApp"); os.system("start whatsapp:"); return True
    elif "steam" in emir:
        konus("Steam"); os.system("start steam://"); return True
    elif "nba" in emir:
        konus("NBA 2K26"); os.system("start steam://run/3472040"); return True
    elif "ets" in emir or "truck" in emir:
        konus("ETS 2"); os.system("start steam://run/227300"); return True
    elif "forza" in emir:
        konus("Forza Horizon 5"); os.system("start steam://run/1551360"); return True
    elif "unity" in emir:
        konus("Unity Hub"); os.system(r"""start "" "C:\Program Files\Unity Hub\Unity Hub.exe" """); return True
    elif "saat" in emir or "time" in emir:
        konus(f"{datetime.datetime.now().strftime('%H:%M')}"); return True 
    elif "google" in emir:
        konus("Google"); webbrowser.open("https://www.google.com"); return True
    elif "youtube" in emir:
        konus("YouTube"); webbrowser.open("https://www.youtube.com"); return True
    elif "başlat" in emir or "play" in emir:
        konus("Spotify"); os.system("start spotify:"); time.sleep(3); pyautogui.press('playpause'); return True
    elif "durdur" in emir or "stop" in emir:
        pyautogui.press('playpause'); konus("Pause."); return True
    elif "değiştir" in emir or "next" in emir:
        pyautogui.press('nexttrack'); konus("Next."); return True
    elif "fotoğraf" in emir or "ss al" in emir:
        pyautogui.screenshot("ss_" + datetime.datetime.now().strftime("%Y%m%d_%H%M%S") + ".png"); konus("Screenshot"); return True
    elif "kapat" in emir or "shutdown" in emir:
        if "sonra" in emir or "after" in emir:
            try:
                words = emir.split()
                sure = [int(w) for w in words if w.isdigit()][0]
                os.system(f"shutdown -s -t {sure * 60}"); konus(f"Kapatma: {sure} dk.")
            except: konus("Hata.")
        else: konus("Bye."); os._exit(0)
        return True
    
    return False

def sistem_baslat():
    konus("Kalibrasyon yapılıyor... Lütfen konuşma.")
    
    # --- MİKROFON AYARI (DÜZELTİLDİ) ---
    r = sr.Recognizer()
    r.pause_threshold = 0.8 
    # r.energy_threshold = 4000  <-- BUNU SİLDİK, SORUN BUYDU
    r.dynamic_energy_threshold = True # Ortam sesine göre otomatik ayarlasın

    try:
        with sr.Microphone() as source:
            # Başlangıçta ortam gürültüsünü 1 saniye dinleyip eşik değerini ayarlar
            r.adjust_for_ambient_noise(source, duration=1) 
            print(f"Kalibre edildi. Enerji Eşiği: {r.energy_threshold}") # Terminale yazsın
            konus("Hazır.")
            
            while True:
                # AŞAMA 1: TETİKLEYİCİ BEKLEME
                ses = dinle(r, source, ekrana_yaz=False)
                
                tetikleyiciler = [
                    "nexus", "neksus", "lexus", "mesut", "meksis", "next", "neks", 
                    "maks", "max", "teksas", "sistem", "system", "asistan", "computer", 
                    "hey", "alo", "netbook", "macbook"
                ]
                
                if any(kelime in ses for kelime in tetikleyiciler):
                    
                    # AŞAMA 2: AKTİF MOD
                    konus("Dinliyorum." if aktif_dil == "tr-TR" else "Listening.")
                    
                    while True:
                        emir = dinle(r, source, ekrana_yaz=True)
                        
                        if emir == "": 
                            continue 
                        
                        basari = komutlari_isle(emir)
                        
                        if basari:
                            # Komut başarılı, döngüden çık
                            break 
                        else:
                            # Komut değilse 2 sn bekle ve sil
                            time.sleep(2)
                            son_satiri_sil()
                            break

    except OSError:
        konus("Mikrofon bulunamadı!")
    except Exception as e:
        konus(f"Hata: {e}")

def thread_baslat():
    if buton: buton.config(state="disabled", text="AKTİF", bg="#00E676")
    t = threading.Thread(target=sistem_baslat); t.daemon = True; t.start()

def arayuz_baslat():
    global yazi_alani, buton
    pencere = tk.Tk(); pencere.title("NEXUS"); pencere.geometry("500x700"); pencere.configure(bg="#121212")
    tk.Label(pencere, text="NEXUS", font=("Segoe UI", 24, "bold"), bg="#121212", fg="#00E676").pack(pady=20)
    yazi_alani = scrolledtext.ScrolledText(pencere, width=50, height=20, font=("Consolas", 10), wrap=tk.WORD)
    yazi_alani.pack(padx=20, pady=10, expand=True, fill=tk.BOTH)
    yazi_alani.configure(bg="#1E1E1E", fg="#E0E0E0", borderwidth=0); yazi_alani.config(state='disabled')
    buton = tk.Button(pencere, text="BAŞLAT", command=thread_baslat, bg="#2962FF", fg="white", font=("Segoe UI", 11, "bold"), borderwidth=0, padx=20, pady=10)
    buton.pack(pady=30); pencere.mainloop()

if __name__ == "__main__":
    arayuz_baslat()