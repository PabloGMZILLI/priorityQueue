class MaxHeap:
    def __init__(self):
        self.heap = [0]

    def put(self, item):
        self.heap.append(item)
        self.__floatUp(len(self.heap) - 1)

    def get(self):
        if len(self.heap) > 2:
            self.__swap(1, len(self.heap) - 1)
            max = self.heap.pop()
            self.__bubbleDown(1)
        elif len(self.heap) == 2:
            max = self.heap.pop()
        else:
            max = False
        return max

    def peek(self):
        if self.heap[1]:
            return self.heap[1]
        return False

    def __swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def __floatUp(self, index):
        parent = index//2
        if index <= 1: # nao faz nada se for raiz
            return
        elif self.heap[index] > self.heap[parent]:
            self.__swap(index, parent)
            self.__floatUp(parent)

    def __bubbleDown(self, index):
        left = index * 2
        right = index * 2 + 1
        maior = index
        if len(self.heap) > left and self.heap[maior] < self.heap[left]:
            maior = left
        if len(self.heap) > right and self.heap[maior] < self.heap[right]:
            maior = right

        if maior != index:
            self.__swap(index, maior)
            self.__bubbleDown(maior)

class Pacient:
    def __init__(self, name, bloodType, birthDate):
        self.patient = (name, bloodType, birthDate)
    
    def returnPacient(self):
        return self.patient

h = MaxHeap()
token = 999
patientsAttended = []

while True:
    resp = int(input('\n1 - Adicionar novo paciente;\n2 - Chamar próximo paciente;\n3 - Mostrar próximo paciente;\n4 - Listar os 5 últimos chamados\n5 - Sair\n'))
    if (resp == 1):
        namePacient = input('\nDigite o nome: ')
        bloodPacient = input('\nDigite o tipo sanguíneo: ')
        birthDatePacient = input('\nDigite a data de nascimento: ')
        patient = Pacient(namePacient, bloodPacient, birthDatePacient).returnPacient()
        (name, blood, birthDate) = patient
        urgency = int(input('\nDigite a urgência do caso (1 a 10): '))
        h.put((urgency, token, name, blood, birthDate))
        token -= 1
    elif (resp == 2):
        try:
            patient = h.get()
            print('Nome: '+patient[2]+'\nSangue: '+patient[3]+'\nData de Nascimento: '+patient[4]+'\nUrgência: '+str(patient[0])+'\nFicha: '+str(patient[1])+'\n\n')
            patientsAttended.append(patient)
        except:
            print('Sem pacientes a ser chamados')
    elif (resp == 3):
        try:
            patient = h.peek()
            print('Nome: '+patient[2]+'\nSangue: '+patient[3]+'\nData de Nascimento: '+patient[4]+'\nUrgência: '+str(patient[0])+'\nFicha: '+str(patient[1])+'\n\n')
        except:
            print('Nenhum paciente a ser mostrados')
    elif (resp == 4):
        print('\n=== Total de Pacientes Atendidos ({}) ==='.format(len(patientsAttended)))
        if (len(patientsAttended)>5):
            for item in range(len(patientsAttended)-1,len(patientsAttended)-5,-1):
                print(item)
                patient = patientsAttended[item]
                print('Nome: '+patient[2]+'\nSangue: '+patient[3]+'\nData de Nascimento: '+patient[4]+'\nUrgência: '+str(patient[0])+'\nFicha: '+str(patient[1])+'\n\n')
        else:
            for patient in patientsAttended:
                print('Nome: '+patient[2]+'\nSangue: '+patient[3]+'\nData de Nascimento: '+patient[4]+'\nUrgência: '+str(patient[0])+'\nFicha: '+str(patient[1])+'\n\n')
    elif (resp == 5):
        break
    else:
        print()
