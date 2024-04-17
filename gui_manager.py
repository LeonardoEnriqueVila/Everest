import tkinter as tk
import gui_currentDay
import gui_addTask

class GUIManager:
    def __init__(self, master):
        self.master = master
        self.currentDayGUI = gui_currentDay.CurrentDay_GUI(master)
        self.addTaskGUI = gui_addTask.AddTask_GUI(master)
        self.createButtons()
        self.showCurrentDay() # Muestra la vista del día actual al iniciar
    
    def showCurrentDay(self):
        self.currentDayGUI.show()
        self.addTaskGUI.hide()
        self.currentDay_button.grid_forget()
        self.addTasks_button.grid(row=0, column=0, sticky="nw")

    def showAddTask(self):
        self.addTaskGUI.show()
        self.currentDayGUI.hide()
        self.addTasks_button.grid_forget()
        self.currentDay_button.grid(row=0, column=0, sticky="nw")

    def createButtons(self):
        self.addTasks_button = tk.Button(self.master, text="Añadir tareas", command=lambda: self.showAddTask())
        self.currentDay_button = tk.Button(self.master, text="Dia actual", command=lambda: self.showCurrentDay())

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Everest")
    manager = GUIManager(root)
    root.mainloop()
