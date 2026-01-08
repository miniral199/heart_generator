class Heart:
    def __init__(self,s):
        #s-template's symbol
        self.s=s
        # heart template
        self.template=[
            '0   0',
            '00 00',
            '00000',
            ' 000 ',
            '  0  '
        ]

    def __generate_template(self):
       new_template=[]
       for line in self.template:
           new_template.append(line.replace('0',self.s))

       return new_template


        # for i in range(4):
        #     line=''
        #     for j in range(6):
        #         line+=self.s
        #     self.template.append(line)

    def checker(self):
        if not self.s == '♥':
            self.template = self.__generate_template()

    def print_heart(self,x=None):
        self.checker()

        # if x is None:
        #     for line in self.template:
        #         print(line)

        for line in self.template:
            for l in line:
                print(l*x,end='')
            print()

def main():
    # heart=Heart('/')
    # heart.print_heart()
    #
    # heart1=Heart('|')
    # heart1.print_heart()
    #
    # heart2=Heart("\\")
    # heart2.print_heart(2)

    while True:
        inp=input("Введите символ из которого хотите себе сердечко (если хотите выйти напишите Exit): ")
        if inp=='':
            print("Вы ничего не ввели! Повторите снова!")
            continue

        elif inp.lower()=='exit':
            print("Вы выбрали выйти из программы. До свидания, желаю вам всего хорошего и хорошего вам дня!")
            break

        elif len(inp)!=1:
            print("Нужно ввести лишь один символ!")
            continue

        else:
            heart=Heart(inp)
            n_try = 1
            while True:
                multiplier=input("Введите значение x (строго больше нуля), это будет множителем сердечек: ")
                if multiplier.isnumeric():
                    if int(multiplier)>0:
                        heart.print_heart(int(multiplier))
                        break
                    else:
                        n_try+=1
                        print(f"Ошибка! Вы ввели: {multiplier}\nМножитель сердечек строго больше нуля! Попытка: #{n_try}")

                else:
                    n_try+=1
                    print(f"Ошибка! Вы ввели: {multiplier}\nА надо ввести число или цифру! Попытка: #{n_try}")



if __name__ == "__main__":
    main()