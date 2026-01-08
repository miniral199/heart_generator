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
           new_template.append(line.replace('0',self.s))

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
    heart=Heart('/')
    heart.print_heart()

    heart1=Heart('|')
    heart1.print_heart()


 
     