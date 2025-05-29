import openai
import customtkinter
from customtkinter import CTkImage
from PIL import Image
import time

customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

openai.api_key = "OPENAI_API_KEY"


def change_appearance_mode_event(new_appearance_mode: str):
    customtkinter.set_appearance_mode(new_appearance_mode)


def change_scaling_event(new_scaling: str):
    new_scaling_float = int(new_scaling.replace("%", "")) / 100
    customtkinter.set_widget_scaling(new_scaling_float)


def sidebar_button_event():
    print("sidebar_button click")


def chat_bot(prompt):
    company_info = (
        "Turbo is a company that sells new and used cars, offering flexible financing options. Car prices range "
        "from 10,000 to 150,000 LYD depending on model, type, and condition. The company serves both individual "
        "buyers and dealerships, and provides after-sale services like maintenance and insurance. Its system "
        "manages inventory, transactions, and customer records through a centralized database.")
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "assistant",
                       "content": "you are an ai agent help turbo's company , in multiple stuff" + company_info},
                      {"role": "user", "content": prompt}]

        )
    except Exception as e:
        return f"An error occurred: {e}"

    return response.choices[0].message.content.strip()


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("ChatBot")
        self.geometry(f"{1100}x{580}")

        self.midlle_frame = customtkinter.CTkFrame(self, width=700, height=90, corner_radius=15)
        self.midlle_frame.grid(row=0, column=1, padx=10, pady=5, sticky="nsew")

        # create textbox
        self.logo_label = customtkinter.CTkLabel(self.midlle_frame, text="ChatBot v3000",
                                                 font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(padx=20, pady=5)

        self.textbox = customtkinter.CTkTextbox(self, state="normal", wrap="word", font=("tajawal", 22, 'bold'),
                                                width=600, height=500)
        self.textbox.grid(row=0, column=1, padx=20, pady=60, sticky="nsew")
        self.textbox.bindtags(())

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=350, corner_radius=10)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)

        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="ChatBot",
                                                 font=customtkinter.CTkFont(size=40, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=50, pady=(20, 10))

        self.sidebar_button = customtkinter.CTkButton(self.sidebar_frame, text="Press The Button",
                                                      font=("tajawal", 15, 'bold'),
                                                      command=sidebar_button_event, width=300)
        self.sidebar_button.grid(row=2, column=0, padx=20, pady=(100, 10))

        self.sidebar_button2 = customtkinter.CTkButton(self.sidebar_frame, text="Button",
                                                       command=sidebar_button_event, width=300)
        self.sidebar_button2.grid(row=3, column=0, padx=20, pady=10)

        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame,
                                                                       values=["Light", "Dark", "System"],
                                                                       command=change_appearance_mode_event, width=290)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=50, pady=(10, 10))

        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="ChatBot v3000", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))

        # create sidebar frame with widgets
        self.sidebar_frame2 = customtkinter.CTkFrame(self, width=700, height=90, corner_radius=20)
        self.sidebar_frame2.grid(row=3, column=1, padx=(50, 50), pady=(10, 30), sticky="nsew")

        # create main entry and button
        self.entry = customtkinter.CTkEntry(self.sidebar_frame2, justify="left", placeholder_text="Ask The Bot",
                                            width=700,
                                            height=50, font=("tajawal", 16, 'bold'))
        self.entry.place(relx=0.45, rely=0.5, anchor="center")

        chat_img_dark = Image.open("send_dark.png")
        chat_img_light = Image.open("send_light.png")

        self.main_button_1 = customtkinter.CTkButton(master=self.sidebar_frame2, fg_color="transparent", border_width=3,
                                                     text="", corner_radius=25,
                                                     image=CTkImage(dark_image=chat_img_light,
                                                                    light_image=chat_img_light),
                                                     width=30, command=self.send_msg)
        self.main_button_1.place(relx=0.9, rely=0.5, anchor="center")

    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
        print("CTkInputDialog:", dialog.get_input())

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def sidebar_button_event(self):
        print("sidebar_button click")

    def send_msg(self):
        progressbar_1 = customtkinter.CTkProgressBar(self.midlle_frame, width=700)
        progressbar_1.grid(row=1, column=2, padx=(10, 10), pady=(10, 10), sticky="ew")
        progressbar_1.configure(mode="indeterminate")
        progressbar_1.start()
        time.sleep(1)

        entry = self.entry.get()
        # user_input = customtkinter.CTkLabel(self.textbox, text=f"You :\n {entry}")
        # user_input.grid(padx=50, pady=50, sticky="nsew")

        self.textbox.insert("0.0", "You : \n" + entry + "\n\n")
        self.entry.delete(0, customtkinter.END)

        self.textbox.insert("0.0", "Bot : \n" + chat_bot(entry) + "\n\n")
        self.entry.delete(0, customtkinter.END)
        progressbar_1.stop()

        if entry.lower() == '/note':
            self.textbox.insert("0.0", "Bot : \nI will save your note\n\n")
            self.entry.delete(0, customtkinter.END)
            progressbar_1.stop()
            note_name = input(
                "what's the name of your note ( please when you named your note write .txt in the end ): ")
            note = input("write your note:  ")
            file = open(note_name, "w")
            file.write(note)
            file.close()


if __name__ == "__main__":
    app = App()
    app.mainloop()
