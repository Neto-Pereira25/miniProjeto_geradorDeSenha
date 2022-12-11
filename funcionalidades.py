from modulos import*

class Funcs():
    def imagem(self, caminho, t1, t2):
        self.app_img = Image.open(caminho)
        self.app_img = self.app_img.resize((t1,t2))
        self.app_img = ImageTk.PhotoImage(self.app_img)
        return self.app_img
    
    # Criando as funções do botão copiar senhas
    def copy_password(self):
        self.info = self.senha
        self.frame_baixo.clipboard_clear()
        self.frame_baixo.clipboard_append(self.info)
        
        messagebox.showinfo("Sucesso", "A senha foi copiada com sucesso")
    
    # Criando as funções do botão gerador de senhas
    def create_password(self):
        self.alfa_maiusculo = string.ascii_uppercase
        self.alfa_minusculo = string.ascii_lowercase
        self.numbers = '1234567890'
        self.simble = '[]{}()@#$%!.,;?/_-'
        
        #global combination
        
        self.combination = ""
        try:
            # Criando a condição para os caracteres maiúsculos
            if self.estado_1.get() == self.alfa_maiusculo:
                self.combination += self.alfa_maiusculo
            else:
                pass
            
            # Criando a condição para os caracteres minúsculo
            if self.estado_2.get() == self.alfa_minusculo:
                self.combination += self.alfa_minusculo
            else:
                pass
            
            # Criando a condição para os caracteres numeéicos
            if self.estado_3.get() == self.numbers:
                self.combination += self.numbers
            else:
                pass
            
            # Criando a condição para os caracteres especiais
            if self.estado_4.get() == self.simble:
                self.combination += self.simble
            else:
                pass
            
            self.comprimento = int(self.spin.get())
            self.senha = "".join(random.sample(self.combination, self.comprimento))
            
            self.lb_senha['text'] = self.senha
                
                # Criando os botão de copiar senhas
            self.bt_copy_password = Button(self.frame_baixo, bd=3, text='Copiar',
                                        font=('verdana', 10, 'bold'), bg=cor6, fg=cor8,
                                        activebackground=cor11, activeforeground=cor1,
                                        command=self.copy_password)
            self.bt_copy_password.place(relx=0.77, rely=0.01, relheight=0.19)
            
        except ValueError as erro:
            msg = "Marque ao menos uma das possibilidades"
            messagebox.showinfo("Não Foi Possível Criar Senha - AVISO!!!", msg)
            self.lb_senha['text'] = '- - - - - - - - - -'