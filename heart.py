class Heart:
    def __init__(self,s):
        #s-template's symbol
        self.s=s
        # heart template
        self.template = [
            '  ♥     ♥  ',
            ' ♥♥♥   ♥♥♥ ',
            '♥♥♥♥♥♥♥♥♥♥♥',
            ' ♥♥♥♥♥♥♥♥♥ ',
            '  ♥♥♥♥♥♥♥  ',
            '   ♥♥♥♥♥   ',
            '    ♥♥♥   ',
            '     ♥    '
        ]
    def __generate_template(self):
       new_template=[]
       for line in self.template:
           new_template.append(line.replace('♥',self.s))

       return new_template


        # for i in range(4):
        #     line=''
        #     for j in range(6):
        #         line+=self.s
        #     self.template.append(line)
                

    def print_heart(self):
        if not self.s=='0':
            self.template=self.__generate_template()
        for line in self.template:
            print(line)

if __name__=="__main__":
    # heart=Heart('/')
    # heart.print_heart()
    #
    # heart1=Heart('|')
    # heart1.print_heart()
    #
    # heart2=Heart("\\")
    # heart2.print_heart(2)

    heart2=Heart("\\")
    heart2.print_heart()

    while True:
        inp=input("Введите символ из которого хотите себе сердечко (если хотите выйти напишите Exit): ")
        if inp=='':
            print("Вы ничего не ввели! Повторите снова!")
            continue
        elif inp.lower()=='exit':
            print("Вы выбрали выйти из программы. До свидания, желаю вам всего хорошего и хорошего вам дня!")
            break
        else:
            heart=Heart(inp)
            x=input("Введите значение x (строго больше нуля), это будет множителем сердечек: ")
            heart.print_heart(int(x))
