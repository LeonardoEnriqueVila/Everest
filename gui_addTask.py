import tkinter as tk
import taskManagers
import alertManagers
import uncommited_DATA

class AddTask_GUI:
    def __init__(self, master):
        self.master = master
        self.UncommittedTaskList_LABELS = []
        self.deleteButtonList = []
        self.compromiseButtonList = []
        # Creación de los widgets
        self.createWidgets()
        self.row = 0
        self.startWithData()

    def startWithData(self): # inicializa el manager llamando a la base de datos y actuando en consecuencia
        data = uncommited_DATA.uncommittedTask_DATA.get_tasks() # obtiene una lista de tuplas con los datos
        taskAmount = len(data)
        if taskAmount != 0:
            for i in range(0, taskAmount):
                self.addUncommittedTask_FROM_DATA(data[i][1]) # el indice 1 de las tuplas contienen el campo de "name"
                # entonces, usando el name, luego se pueden crear las instancias y widgets necesarios para la Task en cuestion

    def addUncommittedTask_FROM_DATA(self, taskName): # Settear las tareas Uncommited desde la base de datos
        self.row += 1 # se le suma 1 para evitar superponer sobre label anterior
        task_label = tk.Label(self.taskList_Frame, text=f"● {taskName}")
        task_label.grid(row=self.row, column=0, padx=10, sticky="w")
        self.UncommittedTaskList_LABELS.append(task_label)

        compromise_Button = tk.Button(self.taskList_Frame, text="Comprometer", command=lambda: self.commitTask(task_label, compromise_Button, delete_Button))
        compromise_Button.grid(row=self.row, column=2, sticky="w")
        self.compromiseButtonList.append(compromise_Button)

        delete_Button = tk.Button(self.taskList_Frame, text="Borrar", command=lambda: self.deleteTask(task_label, compromise_Button, delete_Button))
        delete_Button.grid(row=self.row, column=1, sticky="w")
        self.deleteButtonList.append(delete_Button)
            
        taskManagers.taskManager.addUncommitedTask(taskName)

    def createWidgets(self):
        """Crea los widgets que se utilizarán en la GUI para añadir tareas."""
        self.addTask_Frame = tk.Frame(self.master)
        self.taskInput_Label = tk.Label(self.addTask_Frame, text="Ingresar tarea:")
        self.taskInput_Entry = tk.Entry(self.addTask_Frame)  # Campo de entrada para la nueva tarea
        self.addTask_button = tk.Button(self.addTask_Frame, text="Añadir tarea", command=lambda: self.addUncommittedTask())
        self.spacer_Label1 = tk.Label(self.addTask_Frame, height=2)  # Ajusta la 'height' para el espacio deseado

        self.taskList_Frame = tk.Frame(self.master)
        self.uncompromisedTask_Label = tk.Label(self.taskList_Frame, text="Tareas sin comprometer:")

    def show(self):
        """Posiciona los widgets en el grid."""
        self.addTask_Frame.grid(row=0, column=0, padx=10, sticky="nsew")
        self.spacer_Label1.grid(row=0, column=0, sticky="ew")
        self.taskInput_Label.grid(row=1, column=0, sticky="w")
        self.taskInput_Entry.grid(row=2, column=0, sticky="ew")  # Asegura que el input se expanda horizontalmente
        self.addTask_button.grid(row=2, column=1)

        self.taskList_Frame.grid(row=1, column=0, padx=10, sticky="nsew")
        self.uncompromisedTask_Label.grid(row=0, column=0, sticky="w")

    def hide(self):
        self.addTask_Frame.grid_forget()
        self.taskList_Frame.grid_forget()

    def addUncommittedTask(self): # añadir widgets de tarea provisoria 
        taskName = self.taskInput_Entry.get()
        taskName_Compare = next((task for task in taskManagers.taskManager.uncommittedTasks if task.name == taskName), None) # verificar si el nombre de task ya está en uso
        # asegurarse de que el nombre de task no fue utilizado y el input no es ""
        if taskName != "" and taskName_Compare == None:
            self.row += 1 # se le suma 1 para evitar superponer sobre label anterior
            self.taskInput_Entry.delete(0, tk.END)
            task_label = tk.Label(self.taskList_Frame, text=f"● {taskName}")
            task_label.grid(row=self.row, column=0, padx=10, sticky="w")
            self.UncommittedTaskList_LABELS.append(task_label)

            compromise_Button = tk.Button(self.taskList_Frame, text="Comprometer", command=lambda: self.commitTask(task_label, compromise_Button, delete_Button))
            compromise_Button.grid(row=self.row, column=2, sticky="w")
            self.compromiseButtonList.append(compromise_Button)

            delete_Button = tk.Button(self.taskList_Frame, text="Borrar", command=lambda: self.deleteTask(task_label, compromise_Button, delete_Button))
            delete_Button.grid(row=self.row, column=1, sticky="w")
            self.deleteButtonList.append(delete_Button)
            
            taskManagers.taskManager.addUncommitedTask(taskName)
            uncommited_DATA.uncommittedTask_DATA.addTask(taskName)
        else: 
            alertManagers.alertManager.showError("Entrada duplicada o vacía.")
            self.taskInput_Entry.delete(0, tk.END)


    def deleteTask(self, label, compromiseButton, deleteButton):
        # Eliminar las referencias en las listas
        self.UncommittedTaskList_LABELS.remove(label)
        self.deleteButtonList.remove(deleteButton)
        self.compromiseButtonList.remove(compromiseButton)

        if len(self.UncommittedTaskList_LABELS) == 0: # resetear contador de row a 0 si no hay labels
            self.row = 0

        taskManagers.taskManager.removeUncommitedTask(label.cget("text").replace("● ", ""))
        uncommited_DATA.uncommittedTask_DATA.deleteTask(label.cget("text").replace("● ", ""))

        label.destroy()
        compromiseButton.destroy()
        deleteButton.destroy()

    def commitTask(self, label, compromiseButton, deleteButton): # comprometer Task (se borra de esta interfaz y se agrega a CurrentDay)
        taskManagers.taskManager.commitTask(label.cget("text").replace("● ", ""))
        self.deleteTask(label, compromiseButton, deleteButton)


