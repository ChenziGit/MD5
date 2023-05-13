import tkinter as tk
import hashlib
import tkinter.filedialog as fd
import tkinter.messagebox as mb

class MD5Calculator:

    def __init__(self, master):
        self.master = master
        master.title("MD5计算")
        master.geometry("300x150")

        self.path_label = tk.Label(master, text="文件路径:")
        self.path_label.pack()

        self.filepath_var = tk.StringVar()
        self.path_entry = tk.Entry(master, textvariable=self.filepath_var, width=30)
        self.path_entry.pack()

        self.browse_button = tk.Button(master, text="浏览", command=self.browse_file)
        self.browse_button.pack()

        self.calculate_button = tk.Button(master, text="计算MD5值", command=self.calculate_md5)
        self.calculate_button.pack()

        self.copy_button = tk.Button(master, text="复制MD5", state="disabled", command=self.copy_md5)
        self.copy_button.pack()

        self.md5_label = tk.Label(master, text="")
        self.md5_label.pack()

    def browse_file(self):
        filename = fd.askopenfilename()
        if filename:
            self.filepath_var.set(filename)
            self.copy_button.config(state="disabled")

    def calculate_md5(self):
        filepath = self.path_entry.get()
        if filepath:
            try:
                with open(filepath, 'rb') as file:
                    md5 = hashlib.md5(file.read()).hexdigest()
                    self.md5_label.config(text="MD5: " + md5)
                    self.copy_button.config(state="normal")
            except Exception as e:
                mb.showerror("Error", str(e))
        else:
            mb.showwarning("Warning", "Please select a file.")

    def copy_md5(self):
        md5 = self.md5_label.cget("text").split(" ")[1]
        self.master.clipboard_clear()
        self.master.clipboard_append(md5)
        mb.showinfo("Copied", "MD5 value copied to clipboard")

root = tk.Tk()
MD5Calculator(root)
root.mainloop()
