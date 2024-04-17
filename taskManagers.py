class TaskManager:
    def __init__(self):
        self.commitedTasks = []
        self.uncommittedTasks = []

    def commitTask(self, taskName):
        index = len(self.commitedTasks)
        task = next((task for task in self.uncommittedTasks if task.name == taskName), None) # obtener Task mediante comprension de lista
        task.index = index
        self.commitedTasks.append(task)

    def addUncommitedTask(self, taskName):
        newTask = Task(taskName)
        self.uncommittedTasks.append(newTask)

    def get_tasks(self):
        return self.tasks

    def removeUncommitedTask(self, taskName):
        self.uncommittedTasks = [task for task in self.uncommittedTasks if task.name != taskName] # eliminar task de la lista segun su nombre 

class Task:
    def __init__(self, name):
        self.name = name
        self.status = False # si la tarea no fue realizada
        self.index = None

taskManager = TaskManager()