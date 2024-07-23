import tkinter as tk
from tkinter import filedialog
import re


class RegexApp:
    def __init__(self, master):
        self.master = master
        master.title("Regex App")

        self.regex_label = tk.Label(master, text="Regex:")
        self.regex_label.pack()

        self.regex_entry = tk.Entry(master)
        self.regex_entry.pack()

        self.text_label = tk.Label(master, text="Text:")
        self.text_label.pack()

        self.text_box = tk.Text(master, height=10, width=50)
        self.text_box.pack()

        self.result_label = tk.Label(master, text="Result:")
        self.result_label.pack()
        self.result_box = tk.Text(master, height=10, width=50)
        self.result_box.pack()

        self.thongbao_label = tk.Label(master, text="")
        self.thongbao_label.pack()

        self.button_frame1 = tk.Frame(root)
        self.button_frame2 = tk.Frame(root)

        self.check_button = tk.Button(
            self.button_frame1, text="Check", command=self.check)

        self.upload_button = tk.Button(
            self.button_frame1, text="Load file", command=self.docfile_txt)

        self.save_button = tk.Button(
            self.button_frame1, text="Write file", command=self.ghifile_txt)

        self.find09_button = tk.Button(
            self.button_frame2, text="Find the digits [0-9]", command=self.find09)

        self.findAZ_button = tk.Button(
            self.button_frame2, text="Find the digits [A-Z]", command=self.findAZ)

        self.findspecialcharacters = tk.Button(
            self.button_frame2, text="Find special characters", command=self.findspecialcharacters
        )

        self.quit_button = tk.Button(
            self.button_frame1, text="Quit", command=master.quit)

        self.check_button.pack(side=tk.LEFT, padx=10)
        self.upload_button.pack(side=tk.LEFT, padx=10)
        self.save_button.pack(side=tk.LEFT, padx=10)
        self.quit_button.pack(side=tk.LEFT, padx=10)
        self.find09_button.pack(side=tk.LEFT, padx=10, pady=10)
        self.findAZ_button.pack(side=tk.LEFT, padx=10)
        self.findspecialcharacters.pack(side=tk.LEFT, padx=10)

        self.button_frame1.pack()
        self.button_frame2.pack()

    def check(self):
        self.text_box.tag_remove("bold", "1.0", tk.END)
        self.text_box.tag_add("normal", "1.0", tk.END)
        # self.text_box.tag_configure("normal", font=("Arial", 10))
        # self.text_box.tag_add("normal", 1.0)
        # self.text_box.tag_configure("normal", font=("Arial", 10))
        regex = self.regex_entry.get()
        # print(regex)
        text = self.text_box.get("1.0", tk.END)
        # print(text)

        def find(regex, text):
            return re.findall(regex, text)

        result = find(regex, text)
        y = 1
        vitri = -1
        mang = ""
        indambatdau = ""
        indamketthuc = ""
        if result:
            for i in result:
                vitri = text.find(i, vitri + 1 if vitri != -1 else 0)
                # vitri = text.find(i)
                if vitri != -1:  # tim thay vi tri
                    indambatdau = "1." + str(vitri)
                    vitri_end = vitri + len(i) - 1
                    indamketthuc = "1." + str(vitri_end+1)
                    self.text_box.tag_add(
                        "bold", indambatdau, indamketthuc)
                    self.text_box.tag_configure(
                        "bold", font=("Arial", 10, "bold"))
                    mang = mang + \
                        "Match {} ({}-{}): {}".format(y,
                                                      vitri, vitri_end + 1, i) + "\n"
                    y = y + 1
                    indam = ''
            self.result_box.delete(1.0, tk.END)
            self.result_box.insert(tk.END, mang)
        else:
            self.result_box.delete(1.0, tk.END)
            self.result_box.insert(tk.END, "Not found!")

    def docfile_txt(self):
        file_path = filedialog.askopenfilename()
        f = open(file_path)
        self.text_box.delete(1.0, tk.END)
        for line in f:
            self.text_box.insert(tk.END, line + ' ')

    def ghifile_txt(self):
        if (len(self.text_box.get("1.0", tk.END)) != 1):
            file_path = filedialog.askopenfilename()
            f = open(file_path, "w")
            text = self.text_box.get("1.0", tk.END)
            f.write(text)
            f.close()
            # self.thongbao_label.config(
            # text="Đã lưu văn bản vào file: " + file_path)
            tk.messagebox.showinfo(
                "Success!", "Saved: " + file_path)
        else:
            # self.thongbao_label.config(
            #     text="Hãy nhập đoạn văn cần lưu vào mục text")
            tk.messagebox.showerror(
                "Error!", "Please enter into textbox!")

    def find09(self):
        self.regex_entry.delete(0, tk.END)
        self.regex_entry.insert(tk.END, "[0-9]+")

    def findAZ(self):
        self.regex_entry.delete(0, tk.END)
        self.regex_entry.insert(tk.END, "[a-zA-Z]+")

    def findspecialcharacters(self):
        self.regex_entry.delete(0, tk.END)
        self.regex_entry.insert(tk.END, "[\W]+")


root = tk.Tk()
app = RegexApp(root)
root.mainloop()
