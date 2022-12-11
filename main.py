from modulos import*
from funcionalidades import Funcs

class GenerationPassword(Funcs):
    def __init__(self):
        self.root = Tk()
        self.screen_root()
        self.frames_screen()
        self.widgets_screen()
        
        self.root.mainloop()
    
    def screen_root(self):
        self.root.title("")
        self.root.geometry('300x350+200+200')
        self.root.configure(bg=cor1)
        self.root.resizable(width=True, height=True)
        self.root.maxsize(width=500, height=400)
        self.root.minsize(width=200, height=250)
        
        self.eslito = ttk.Style(self.root)
        self.eslito.theme_use('clam')
        
    def frames_screen(self):
        self.frame_cima = Frame(self.root, bd=4, bg=cor2, highlightbackground=cor6, highlightthickness=3)
        self.frame_cima.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.15)

        self.frame_baixo = Frame(self.root, bd=4, bg=cor2, highlightbackground=cor6, highlightthickness=3)
        self.frame_baixo.place(relx=0.02, rely=0.19, relwidth=0.96, relheight=0.79)

        self.frame_options = Frame(self.frame_baixo, bd=4, bg=cor2, highlightbackground=cor6)
        self.frame_options.place(relx=0, rely=0.4, relwidth=1, relheight=0.6)
        
    def widgets_screen(self):
        img_frame_cima = self.imagem('senha.png', 30, 30)

        self.lb_logo = Label(self.frame_cima, image=img_frame_cima, compound=LEFT, anchor=NW, bg=cor2)
        self.lb_logo.place(relx=0, rely=0.02)

        self.lb_logo = Label(self.frame_cima, text='GERADOR DE SENHA', font=('Ivy 16 bold'),
                        compound=LEFT, anchor=CENTER, bg=cor2)
        self.lb_logo.place(relx=0.13, rely=0.1)

        # Configurações do frame de baixo
        self.lb_senha = Label(self.frame_baixo, bd=4,  text='- - - - - - - - - -', font=('Ivy 12 bold'),
                        highlightbackground=cor6, highlightthickness=3,
                        compound=LEFT, anchor=CENTER, bg=cor2, fg=cor7)
        self.lb_senha.place(relx=0.01, rely=0.01, relwidth=0.75, relheight=0.2)

        self.lb_info = Label(self.frame_baixo, bd=4,  text='Número total de caracteres', font=('Ivy 10 bold'),
                        compound=LEFT, anchor=CENTER, bg=cor2, fg=cor7)
        self.lb_info.place(relx=0.01, rely=0.24)
        
                # Criando as variáveis para a lógica do sistema
        self.alfa_maiusculo = string.ascii_uppercase
        self.alfa_minusculo = string.ascii_lowercase
        self.numbers = '1234567890'
        self.simble = '[]{}()@#$%!.,;?/_-'

        # Criando spinBox do número de senhas
        self.var = IntVar()
        self.var.set(8)
        self.spin = Spinbox(self.frame_baixo, from_=0, to=20, textvariable=self.var)
        self.spin.place(relx=0.03, rely=0.33, relwidth=0.15)


        # Criando os checks buttons da senhas
            # Caracteres maiúsculas
        self.estado_1 = StringVar()
        self.estado_1.set(False)

        self.check_1 = Checkbutton(self.frame_options, var=self.estado_1, onvalue=self.alfa_maiusculo, offvalue='off', bg=cor2)
        self.check_1.place(relx=0, rely=0.03, relwidth=0.15)

        self.lb_info_check_1 = Label(self.frame_options, bd=4,  text='ABC letras maiúsculas', font=('Ivy 10 bold'),
                        compound=LEFT, anchor=CENTER, bg=cor2, fg=cor7)
        self.lb_info_check_1.place(relx=0.2, rely=0.03)

        # Caracteres maiúsculas
        self.estado_2 = StringVar()
        self.estado_2.set(False)

        self.check_2 = Checkbutton(self.frame_options, var=self.estado_2, onvalue=self.alfa_minusculo, offvalue='off', bg=cor2)
        self.check_2.place(relx=0, rely=0.23, relwidth=0.15)

        self.lb_info_check_2 = Label(self.frame_options, bd=4,  text='abc letras minúsculas', font=('Ivy 10 bold'),
                        compound=LEFT, anchor=CENTER, bg=cor2, fg=cor7)
        self.lb_info_check_2.place(relx=0.2, rely=0.23)

        # Caracteres números
        self.estado_3 = StringVar()
        self.estado_3.set(False)

        self.check_3 = Checkbutton(self.frame_options, var=self.estado_3, onvalue=self.numbers, offvalue='off', bg=cor2)
        self.check_3.place(relx=0, rely=0.43, relwidth=0.15)

        self.lb_info_check_3 = Label(self.frame_options, bd=4,  text='123 Números', font=('Ivy 10 bold'),
                        compound=LEFT, anchor=CENTER, bg=cor2, fg=cor7)
        self.lb_info_check_3.place(relx=0.2, rely=0.43)

        # Caracteres especiais
        self.estado_4 = StringVar()
        self.estado_4.set(False)

        self.check_4 = Checkbutton(self.frame_options, var=self.estado_4, onvalue=self.simble, offvalue='off', bg=cor2)
        self.check_4.place(relx=0, rely=0.63, relwidth=0.15)

        self.lb_info_check_4 = Label(self.frame_options, bd=4,  text=' !@# caracteres especiais', font=('Ivy 10 bold'),
                        compound=LEFT, anchor=CENTER, bg=cor2, fg=cor7)
        self.lb_info_check_4.place(relx=0.2, rely=0.63)


        # Criando os botão de gerar senhas
        self.bt_generation_password = Button(self.frame_options, bd=3, text='Gerar Senha',
                                    font=('verdana', 10, 'bold'), bg=cor6, fg=cor8,
                                    activebackground=cor11, activeforeground=cor1,
                                    command=self.create_password)
        self.bt_generation_password.place(relx=0.04, rely=0.83, relwidth=0.9)

GenerationPassword()
