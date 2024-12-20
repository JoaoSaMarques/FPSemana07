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
        return f"Email para {self.destinatario}. Assunto: {self.assunto}. Corpo: {self.corpo}"

        
class SMS(Mensagem):
    def __init__(self, numero, mensagem):
        super().__init__()
        self.numero = numero
        self.mensagem = mensagem
        
    def enviar_mensagem(self):
        return f"SMS para {self.numero}. Mensagem: {self.mensagem}"
        
class NotificacaoPush(Mensagem):
    def __init__(self):
        super().__init__()
        
    def enviar_mensagem(self):
        print("Mensagem enviada por notificação push")