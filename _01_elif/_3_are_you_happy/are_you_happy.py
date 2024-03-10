from tkinter import Tk, simpledialog, messagebox


if __name__ == '__main__':
    # TODO: Look at the AreYouHappy.png image
    #       Use pop-ups to recreate the chart using if and elif statements
    window = Tk()
    window.withdraw()
    happy1 = simpledialog.askstring(title="Answer in all Caps", prompt="ARE YOU HAPPY?")
    if happy1 == "NO":
        happy2 = simpledialog.askstring(title="Answer in all Caps", prompt="DO YOU WANT TO BE HAPPY?")
        if happy2 == "YES":
            messagebox.showinfo(title="My advice",message="CHANGE SOMETHING.")
        else:
            messagebox.showinfo(title="My advice",message="KEEP DOING WHATEVER YOU'RE DOING.")
    else:
        messagebox.showinfo(title="My advice",message="KEEP DOING WHATEVER YOU'RE DOING.")
