import tkinter as tk
import taskManagers
from datetime import datetime

class CurrentDay_GUI:
    def __init__(self, master):
        self.master = master
        self.taskLabelList = []
        self.checkBoxesList = []
        # Creación de los widgets
        self.createWidgets()

    def createWidgets(self):
        """Crea los widgets que se utilizarán en la GUI."""
        self.currentDay_Frame = tk.Frame(self.master)
        self.date_Label = tk.Label(self.currentDay_Frame, text=f"Fecha: {datetime.now().strftime('%Y-%m-%d')}")
        self.daysCompromised_Label = tk.Label(self.currentDay_Frame, text="Días comprometidos: 0")
        self.dayTaskTitle_label = tk.Label(self.currentDay_Frame, text="Tareas del Día:")
        self.taskList_Frame = tk.Frame(self.currentDay_Frame)

    def show(self):
        # Posicionamiento del frame principal
        self.currentDay_Frame.grid(row=0, column=0, padx=10, pady=30, sticky="w")
        self.showTaskList() # gestiona widgets de TaskList
        # Posicionamiento de los labels y frames
        self.date_Label.grid(row=1, column=0, sticky="w")
        self.daysCompromised_Label.grid(row=2, column=0, sticky="w")
        self.dayTaskTitle_label.grid(row=3, column=0, sticky="w")
        self.taskList_Frame.grid(row=4, column=0, sticky="w")  

    def hide(self):
        self.currentDay_Frame.grid_forget()
        self.taskList_Frame.grid_forget()

    def showTaskList(self): # limpia y muestra los widgets de la lista de tareas 
        self.cleanTaskWidgets()
        i = 0
        # Crear un nuevo label para cada tarea y añadirlo al frame de tareas
        for task in taskManagers.taskManager.commitedTasks:
            task_label = tk.Label(self.taskList_Frame, text=f"● {task.name}")
            task_label.grid(row=i, column=0, padx=10, sticky="w")  
            self.taskLabelList.append(task_label)
            self.showCheckBoxes(i, task) # añade un checkBox para cada Label
            i += 1

    def showCheckBoxes(self, row, task): # se llama para cada Task, obtiene la misma y el row de su label
        booleanTk = tk.BooleanVar(value=task.status)  # Estado inicial del Checkbutton
        checkBox = tk.Checkbutton(self.taskList_Frame, variable=booleanTk,
                                 onvalue=True, offvalue=False, command=lambda: self.updateTaskStatus(task, booleanTk))
        checkBox.grid(row=row, column=1, sticky="w")
        self.checkBoxesList.append(checkBox)
        if task.status: # se asegura de que el label se muestre "overstrike" al cambiar de interfaz si fue marcado
            self.taskLabelList[task.index].config(fg="#a3a3a3", font=("Arial", 10, "overstrike"))
        
    def updateTaskStatus(self, task, booleanTk):
        task.status = booleanTk.get()
        # Actualizar label
        if task.status:
            self.taskLabelList[task.index].config(fg="#a3a3a3", font=("Arial", 10, "overstrike"))
        else:
            self.taskLabelList[task.index].config(fg="#000000", font=("Arial", 10, "normal"))

    def cleanTaskWidgets(self): # Limpiar widgets antiguos si existen para evitar duplicados
        for label in self.taskLabelList:
            label.destroy()
        self.taskLabelList.clear()
        for checkBox in self.checkBoxesList:
            checkBox.destroy()
        self.checkBoxesList.clear()


