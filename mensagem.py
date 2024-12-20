class Mensagem:
    def __init__(self):
        pass
    
class Email(Mensagem):
    def __init__(self):
        super().__init__()
        
    def enviar_mensagem(self):
        print("Mensagem enviada por e-mail")
        
class SMS(Mensagem):
    def __init__(self):
        super().__init__()
        
    def enviar_mensagem(self):
        print("Mensagem enviada por SMS")
        
class NotificacaoPush(Mensagem):
    def __init__(self):
        super().__init__()
        
    def enviar_mensagem(self):
        print("Mensagem enviada por notificação push")