
# classe caminhao
class Truck:
    def __init__(self, capacity):
        self.initialCapacity = capacity
        self.capacity = capacity
        self.value = 0
        self.packets = []
    
    def __str__(self):  
        return "Truck totalCapacity: % s; remainCapacity: % s; packetsValue: % s" % (self.initialCapacity, self.capacity, self.value)

    def addPacket(self, packet):
        self.packets.append(packet)
        self.capacity -= packet.weight
        self.value += packet.value

# classe pacote
class Packet:
    def __init__(self, weight, value):
            self.weight = weight
            self.value = value


# abastece os caminhoes
# recebe um array de caminhoes e de pacotes
def fillTrucks(trucks, packets):  
    remainPackets = packets
    for truck in trucks:
        remainPackets = fillTruck(truck, remainPackets)


# funcao que abastece um unico caminhao
# recebe o objeto caminhao e um array de pacotes
# retorna um array de pacotes que ainda nao foram carregados
def fillTruck(truck, packets):

    capacity = truck.capacity
    n = len(packets)

    # inicia a matriz de memoria
    mem = [[-1 for x in range(capacity+1)] for x in range(n+1)]        
    
    for i in range(0, n+1):

        for w in range(0, capacity+1):

            last = i - 1

            if i == 0 or w == 0:

                mem[i][w] = 0

            elif packets[last].weight <= w:

                a = packets[last].value + mem[last][w - packets[last].weight]
                b = mem[last][w]
                mem[i][w] = max(a, b)
            
            else:

                mem[i][w] = mem[last][w]

    # printMemoryMatrix(mem, capacity, n)
    remainPackets = findPackets(truck, packets, mem)

    return remainPackets

# imprime a matriz de memoria
def printMemoryMatrix(mem, capacity, n):
    for y in range(capacity + 1):
        r = '['
        for x in range(n + 1):
            item = mem[x][y]

            r += ' '
            if item < 10:
                r += ' '
            if item < 100:
                r += ' '

            r += str(item) + ', '
        print(r + ']')

# encontra os pacotes e os coloca no caminhao
# recebe o objeto caminhao, um array de pacotes e a matriz de memoria
# retorna os pacotes nao carregados
def findPackets(truck, packets, mem):
    i = len(packets)
    k = truck.capacity
    remainPackets = []

    while i > 0 and k > 0:
        last = i - 1

        if mem[i][k] != mem[last][k]:
            # print(str(i) + ' - ' + str(packets[last].weight) + ' ' + str(packets[last].value) + ' ' + str(k))
            truck.addPacket(packets[last])
            k -= packets[last].weight
        else:
            remainPackets.append(packets[last])
        
        i -= 1

    return remainPackets



def main():

    trucks = [
        Truck(capacity=23),
        Truck(capacity=50),
    ]

    packets = [
        Packet(weight=1, value=1),
        Packet(weight=2, value=6),
        Packet(weight=5, value=18),
        Packet(weight=6, value=22),
        Packet(weight=7, value=28),
        Packet(weight=9, value=40),
        Packet(weight=11, value=60),
    ]

    fillTrucks(trucks, packets)

    for t in trucks:
        print(t)


main()
            
            