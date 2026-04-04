import math
import customtkinter as ctk
import google.generativeai as genai
from sqlalchemy.dialects.mysql import insert
import time

# Interface graphique
Ui = ctk.CTk()
Ui.geometry("1000x500")
Ui.title("Calculatrice Artificielle")
Ui.resizable(False, False)


# AI
fram_d = ctk.CTkFrame(Ui, width=500, height=500)
fram_d.pack(side="right", padx=10, pady=10)

# Ecran
ecranai = (ctk.CTkTextbox
           (
               fram_d, border_width=0.5, corner_radius=2, height=350, width=450, border_color="black",
               fg_color="black"
           )
           )
ecranai.grid(columnspan=9, pady=15, padx=5)


# définition de la première fonction, pour taper des choses

calcul = ""


def ajout_calcul(symbole):
    global calcul
    calcul += str(symbole)

    ecran.delete(1.0, "end")
    ecran.insert(1.0, calcul)


def delete():
    global calcul

    calcul = ""
    ecran.delete(1.0, "end")


def evaluation_de_calcul():
    global calcul
    try:
        calcul = str(eval(calcul))
        ecran.delete(1.0, "end")
        ecran.insert(1.0, calcul)

    except:

        ecran.insert(1.0, "AI n'a pas trouvé")


framefield = (ctk.CTkFrame
              (
                  fram_d, border_width=0.5, corner_radius=2, height=40, width=450, border_color="black",
                  fg_color="black"
              )
              )
framefield.grid(columnspan=9, pady=1, padx=5)


# cal
fram_cal = ctk.CTkFrame(Ui, width=500, height=500)
fram_cal.pack(side="left", padx=10, pady=10)

# Ecran
ecran = (ctk.CTkTextbox
         (
             fram_cal, border_width=0.5, corner_radius=2, height=80, width=450, border_color="black",
             fg_color="black"
         )
         )
ecran.grid(columnspan=9, pady=15, padx=5)

# btn : Niveau 1

btn = ctk.CTkButton(
    fram_cal, text="AC", command=lambda: delete(), border_width=0, width=25, height=25, corner_radius=20, fg_color="black",
)
btn.grid(row=1, column=0, padx=2, pady=2)

btn = ctk.CTkButton(fram_cal, text="log", border_width=0, width=25, height=25, corner_radius=20, fg_color="black",
                    )
btn.grid(row=1, column=1, padx=2, pady=2)


def sinus():
    pass


btn = ctk.CTkButton(
    fram_cal, text="sin", command=lambda: sinus(), border_width=0, width=25, height=25, corner_radius=20, fg_color="black",
)
btn.grid(row=1, column=2, padx=2, pady=2)

btn = ctk.CTkButton(
    fram_cal, text="cos", border_width=0, width=25, height=25, corner_radius=20, fg_color="black",
)
btn.grid(row=1, column=3, padx=2, pady=2)

btn = ctk.CTkButton(
    fram_cal, text="tan", border_width=0, width=25, height=25, corner_radius=20, fg_color="black",
)
btn.grid(row=1, column=4, padx=2, pady=2)

btn = ctk.CTkButton(
    fram_cal, text="cot", border_width=0, width=25, height=25, corner_radius=20, fg_color="black",
)
btn.grid(row=1, column=5, padx=2, pady=2)

btn = ctk.CTkButton(
    fram_cal, text="log", border_width=0, width=25, height=25, corner_radius=20, fg_color="black",
)
btn.grid(row=1, column=6, padx=2, pady=2)

# btn : Niveau 2

btn = ctk.CTkButton(
    fram_cal, text="off", border_width=0, width=25, height=25, corner_radius=20, fg_color="black",
)
btn.grid(row=2, column=0, padx=2, pady=2)

btn = ctk.CTkButton(
    fram_cal, text="ln", border_width=0, width=25, height=25, corner_radius=20, fg_color="black",
)
btn.grid(row=2, column=1, padx=2, pady=2)

btn = ctk.CTkButton(
    fram_cal, text="abs", border_width=0, width=25, height=25, corner_radius=20, fg_color="black",
)
btn.grid(row=2, column=2, padx=2, pady=2)

btn = ctk.CTkButton(
    fram_cal, text="sec", border_width=0, width=25, height=25, corner_radius=20, fg_color="black",
)
btn.grid(row=2, column=3, padx=2, pady=2)

btn = ctk.CTkButton(
    fram_cal, text="sqrt", border_width=0, width=25, height=25, corner_radius=20, fg_color="black",
)
btn.grid(row=2, column=4, padx=2, pady=2)

btn = ctk.CTkButton(
    fram_cal, text=",", border_width=0, width=25, height=25, corner_radius=20, fg_color="black",
)
btn.grid(row=2, column=5, padx=2, pady=2)

btn = ctk.CTkButton(
    fram_cal, text="^", border_width=0, width=25, height=25, corner_radius=20, fg_color="black",
)
btn.grid(row=2, column=6, padx=2, pady=2)

# btn : Niveau 3

btn = ctk.CTkButton(
    fram_cal, text="AI", border_width=0, width=25, height=25, corner_radius=20, fg_color="black",
)
btn.grid(row=3, column=0, padx=2, pady=2)

btn = ctk.CTkButton(
    fram_cal, text="(-)", border_width=0, width=25, height=25, corner_radius=20, fg_color="black",
)
btn.grid(row=3, column=1, padx=2, pady=2)

btn = ctk.CTkButton(
    fram_cal, text="π", border_width=0, width=25, height=25, corner_radius=20, fg_color="black",
)
btn.grid(row=3, column=2, padx=2, pady=2)

btn = ctk.CTkButton(
    fram_cal, text="(", border_width=0, width=25, height=25, corner_radius=20, fg_color="black",
)
btn.grid(row=3, column=3, padx=2, pady=2)

btn = ctk.CTkButton(
    fram_cal, text="[", border_width=0, width=25, height=25, corner_radius=20, fg_color="black",
)
btn.grid(row=3, column=4, padx=2, pady=2)

btn = ctk.CTkButton(
    fram_cal, text="]", border_width=0, width=25, height=25, corner_radius=20, fg_color="black",
)
btn.grid(row=3, column=5, padx=2, pady=2)

btn = ctk.CTkButton(
    fram_cal, text=")", border_width=0, width=25, height=25, corner_radius=20, fg_color="black",
)
btn.grid(row=3, column=6, padx=2, pady=2)

# btn : Niveau 4


btn = ctk.CTkButton(
    fram_cal, text="AI", border_width=0, width=35, height=45, corner_radius=0, fg_color="black",
)

btn.grid(row=5, column=0, padx=7, pady=15)

btn = ctk.CTkButton(
    fram_cal, text="AI", border_width=0, width=35, height=45, corner_radius=0, fg_color="black",
)

btn.grid(row=5, column=1, padx=7, pady=15)

btn = ctk.CTkButton(
    fram_cal, text="AI", border_width=0, width=35, height=45, corner_radius=0, fg_color="black",
)

btn.grid(row=5, column=2, padx=7, pady=15)

btn = ctk.CTkButton(
    fram_cal, text="AI", border_width=0, width=35, height=45, corner_radius=0, fg_color="black",
)

btn.grid(row=5, column=3, padx=7, pady=15)

btn = ctk.CTkButton(
    fram_cal, text="AI", border_width=0, width=35, height=45, corner_radius=0, fg_color="black",
)

btn.grid(row=5, column=4, padx=7, pady=15)

btn = ctk.CTkButton(
    fram_cal, text="AI", border_width=0, width=35, height=45, corner_radius=0, fg_color="black",
)

btn.grid(row=5, column=5, padx=7, pady=15)

btn = ctk.CTkButton(
    fram_cal, text="AI", border_width=0, width=35, height=45, corner_radius=0, fg_color="black",
)

btn.grid(row=5, column=6, padx=7, pady=15)

# btn : Niveau 5

btn = ctk.CTkButton(
    fram_cal, text="7", command=lambda: ajout_calcul(7), border_width=0, width=25, height=45, corner_radius=20, fg_color="black",
)

btn.grid(row=6, column=0, padx=7, pady=2)

btn = ctk.CTkButton(
    fram_cal, text="8", command=lambda: ajout_calcul(8), border_width=0, width=25, height=45, corner_radius=20, fg_color="black",
)

btn.grid(row=6, column=1, padx=7, pady=2)

btn = ctk.CTkButton(
    fram_cal, text="9", command=lambda: ajout_calcul(9), border_width=0, width=25, height=45, corner_radius=20, fg_color="black",
)

btn.grid(row=6, column=2, padx=7, pady=2)

btn = ctk.CTkButton(
    fram_cal, text="+", command=lambda: ajout_calcul('+'), border_width=0, width=25, height=45, corner_radius=20, fg_color="black",
)

btn.grid(row=6, column=3, padx=7, pady=2)

btn = ctk.CTkButton(
    fram_cal, text="-", command=lambda: ajout_calcul('-'), border_width=0, width=25, height=45, corner_radius=20, fg_color="black",
)

btn.grid(row=6, column=4, padx=7, pady=2)

btn = ctk.CTkButton(
    fram_cal, text="AI", border_width=0, width=25, height=45, corner_radius=20, fg_color="black",
)

btn.grid(row=6, column=5, padx=7, pady=2)

btn = ctk.CTkButton(
    fram_cal, text="AI", border_width=0, width=25, height=45, corner_radius=20, fg_color="black",
)

btn.grid(row=6, column=6, padx=7, pady=2)

# btn : Niveau 5

btn = ctk.CTkButton(
    fram_cal, text="4", command=lambda: ajout_calcul(4), border_width=0, width=25, height=45, corner_radius=20, fg_color="black",
)

btn.grid(row=7, column=0, padx=7, pady=2)

btn = ctk.CTkButton(
    fram_cal, text="5", command=lambda: ajout_calcul(5), border_width=0, width=25, height=45, corner_radius=20, fg_color="black",
)

btn.grid(row=7, column=1, padx=7, pady=2)

btn = ctk.CTkButton(
    fram_cal, text="6", command=lambda: ajout_calcul(6), border_width=0, width=25, height=45, corner_radius=20, fg_color="black",
)

btn.grid(row=7, column=2, padx=7, pady=2)

btn = ctk.CTkButton(
    fram_cal, text="x", command=lambda: ajout_calcul('*'), border_width=0, width=25, height=45, corner_radius=20, fg_color="black",
)

btn.grid(row=7, column=3, padx=7, pady=2)

btn = ctk.CTkButton(
    fram_cal, text="÷", command=lambda: ajout_calcul('/'), border_width=0, width=25, height=45, corner_radius=20, fg_color="black",
)

btn.grid(row=7, column=4, padx=7, pady=2)

btn = ctk.CTkButton(
    fram_cal, text="AI", border_width=0, width=25, height=45, corner_radius=20, fg_color="black",
)

btn.grid(row=7, column=5, padx=7, pady=2)

btn = ctk.CTkButton(
    fram_cal, text="AI", border_width=0, width=25, height=45, corner_radius=20, fg_color="black",
)

btn.grid(row=7, column=6, padx=7, pady=2)

# btn : Niveau 5

btn = ctk.CTkButton(
    fram_cal, text="1", command=lambda: ajout_calcul(1), border_width=0, width=25, height=45, corner_radius=20, fg_color="black",
)

btn.grid(row=8, column=0, padx=7, pady=2)

btn = ctk.CTkButton(
    fram_cal, text="2", command=lambda: ajout_calcul(2), border_width=0, width=25, height=45, corner_radius=20, fg_color="black",
)

btn.grid(row=8, column=1, padx=7, pady=2)

btn = ctk.CTkButton(
    fram_cal, text="3", command=lambda: ajout_calcul(3), border_width=0, width=25, height=45, corner_radius=20, fg_color="black",
)

btn.grid(row=8, column=2, padx=7, pady=2)

btn = ctk.CTkButton(
    fram_cal, text="0", command=lambda: ajout_calcul(0), border_width=0, width=25, height=45, corner_radius=20, fg_color="black",
)

btn.grid(row=8, column=3, padx=7, pady=2)

btn = ctk.CTkButton(
    fram_cal, text="=", command=lambda: evaluation_de_calcul(), border_width=0, width=25, height=45, corner_radius=20, fg_color="black",
)

btn.grid(row=8, column=4, padx=7, pady=2)

btn = ctk.CTkButton(
    fram_cal, text="AI",  border_width=0, width=25, height=45, corner_radius=20, fg_color="black",
)

btn.grid(row=8, column=5, padx=7, pady=2)

btn = ctk.CTkButton(
    fram_cal, text="AI", border_width=0, width=25, height=45, corner_radius=20, fg_color="black",
)

btn.grid(row=8, column=6, padx=7, pady=2)


ecranai.insert("end", "\n", )


def send_message(event=None):
    try:
        user_message = inputfield.get()
        API_KEY = \
            "AIzaSyBiP7qtGFEX12pwczR6TctrdkfwDKRWJ6w"

        if user_message.strip() != "":
            ecranai.configure(state="normal")
            ecranai.insert("end", f"vous : {user_message}\n", "user")

            # API KEY
            genai.configure(api_key=API_KEY)
            model = genai.GenerativeModel('gemini-2.0-flash')
            chat = model.start_chat()

            response = chat.send_message(user_message)

            ecranai.insert("end", f"Bot : {response.text}", "bot")
            ecranai.update()
            time.sleep(0.05)

            ecranai.configure(state="disabled")
            ecranai.see("end")

            inputfield.delete(0, "end")

    except Exception as e:
        ecranai.insert("end", "Erreur")
        inputfield.delete(0, "end")


ecranai.tag_config("user", foreground="blue")
ecranai.tag_config("bot", foreground="green")


inputfield = ctk.CTkEntry(framefield, border_width=0.5, placeholder_text="Saisir votre message...", corner_radius=2, height=40, width=450,
                          border_color="black")
inputfield.grid(columnspan=9, pady=5, padx=5)

sendbtn = ctk.CTkButton(framefield, text="Envoyer", command=send_message,
                        border_width=0.5, corner_radius=2, height=40, width=450, border_color="black")
sendbtn.grid(columnspan=9, pady=2, padx=5)

Ui.bind("<Return>", send_message)


# Frame
framecran = (ctk.CTkFrame
             (
                 fram_cal, border_width=0.5, corner_radius=2, height=30, width=450, border_color="black",
                 fg_color="black"
             )
             )
framecran.grid(columnspan=9, pady=15, padx=5)


lab = ctk.CTkLabel(framecran, text="AI Gemini 2.0", height=30, width=450)
lab.pack()


Ui.mainloop()
