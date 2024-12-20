class Mensagem:
    def __init__(self):
        pass
    
    def enviar_mensagem(self):
        raise NotImplementedError("Este método deve ser implementado por subclasses.")

    
class Email(Mensagem):
    def __init__(self, destinatario, assunto, corpo):
        super().__init__()
        self.destinatario = destinatario
        self.assunto = assunto
        self.corpo = corpo
        
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