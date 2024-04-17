from tkinter import messagebox

class AlertManager: 
    def showInfo(self, message):
        messagebox.showinfo("Información", message)

    def showWarning(self, message):
        messagebox.showwarning("Advertencia", message)

    def showError(self, message):
        messagebox.showerror("Error", message)

    def askQuestion(self, message):
        response = messagebox.askquestion("Confirmar", message)
        if response == 'yes':
            return True
        else:
            return False

alertManager = AlertManager()