from tkinter import simpledialog, messagebox, Tk

# TODO Tell the user a story, but give them options so they can decide the
#  path of the plot.
#  Use pop-ups, if statements, and your imagination to make an interesting
#  story
if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    Begin = simpledialog.askstring(title="Welcome to Among Us!", prompt="You are a crewmate on the renowned Skeld! While in the cafeteria, chowing down on some home made noodles, you hear the captain on the intercom: 'Attention Crew! It appears there is one imposter among us! We can still complete this mission though. Complete your tasks or find and eject this imposter and we will survive!' A loud whispering arises as individuals scatter... What would you like to do? (Call an emergency meeting) (Explore) (Head to tasks)")
    if Begin == "Call an emergency meeting":
        messagebox.showinfo(title="Outcome", message="You called an emergency meeting too early.")
        messagebox.showinfo(title="The end", message="You were ejected.")
    if Begin == "Explore":
        messagebox.showinfo(title="Outcome", message="You find a dead body in Electrical! A stream of blood covers exposed wires and a vent.")
        b1 = simpledialog.askstring(title="Uh-oh", prompt="(Report the body) (Flee)")
        if b1 == "Report the body":
            messagebox.showinfo(title="Outcome", message="You meet everyone in Cafeteria where you inform them of Blue's dead body in Electrical. Green and Brown claim they were together in Reactor.")
            messagebox.showinfo(title="Outcome", message="Pink says they saw red in Security.")
            messagebox.showinfo(title="Outcome", message="There is not enough evidence to eject someone right now.")
            nw1 = simpledialog.askstring(title="Hmmmm", prompt="Now what? (Visit Security) (Tasks)")
            if nw1 == "Tasks":
                messagebox.showinfo(title="Outcome", message="You go to do a task in O2.")
                messagebox.showinfo(title="Outcome", message="There is a dead body in 02!")
                b2 = simpledialog.askstring(title="Uh-oh", prompt="(Report the body) (Flee)")
                if b2 == "Report the body":
                    messagebox.showinfo(title="Outcome", message="You meet everyone in Cafeteria where you inform them of Green's dead body in O2.")
                    messagebox.showinfo(title="ACCUSATION", message="Brown - 'Your killing everyone and reporting their deaths to make yourself look innocent!'")
                    messagebox.showinfo(title="Outcome", message="The crowd agrees with Brown's point.")
                    messagebox.showinfo(title="The end", message="You were ejected.")
                if b2 == "Flee":
                    messagebox.showinfo(title="Outcome", message="You slowly back away from the body...")
                    messagebox.showinfo(title="Outcome", message="A jagged object pierces your spine!")
                    messagebox.showinfo(title="The end", message="YOU DIED")
            if nw1 == "Visit Security":
                messagebox.showinfo(title="Outcome", message="You head to Security to gather evidence via the cameras scattered around the ship...")
                messagebox.showinfo(title="Outcome", message="It seems someone is heading to security. You can't tell much from their quick movement but their suit is a warm color.")
                messagebox.showinfo(title="Outcome", message="A gunshot rings out; you feel a sharp pain...")
                messagebox.showinfo(title="The end", message="YOU DIED")
        if b1 == "Flee":
            messagebox.showinfo(title="Outcome", message="As you attempt to run you trip on the dead body...")
            messagebox.showinfo(title="Outcome", message="A vent shifts and someone approaches you from behind...")
            messagebox.showinfo(title="The end", message="YOU DIED")
    if Begin == "Head to tasks":
        messagebox.showinfo(title="Outcome", message="You head to O2 to do your tasks...")
        messagebox.showinfo(title="Outcome", message="You witness Pink kill Green!")
        messagebox.showinfo(title="Outcome", message="Pink hops in a vent.")
        messagebox.showinfo(title="Outcome", message="You report the body and meet everyone in Cafeteria. You inform them of what you saw. Unfortunately, some of the crowd may take some convincing.")
        m = simpledialog.askstring(title="Be convincing!", prompt="Convince them: (Vote Pink! If Pink is not the imposter vote me!) (I saw it happen though!) (Y'all are stupid) (Pink sus)")
        if m == "Vote pink! If pink is not the imposter vote me!":
            messagebox.showinfo(title="Outcome", message="The crowd considers your offer...")
            messagebox.showinfo(title="Outcome", message="Pink is ejected.")
            messagebox.showinfo(title="Outcome", message="Pink was the imposter!")
            messagebox.showinfo(title="Winner!", message="You win!")
        else:
            messagebox.showinfo(title="Seriously?", message="You were ejected.")
