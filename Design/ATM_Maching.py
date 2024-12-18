class ATM:

    def __init__(self):
        self.banknotes = [0] * 5
        
    def deposit(self, banknotesCount: List[int]) -> None:

        for i in range(5):
            self.banknotes[i] += banknotesCount[i]
    
    def withdraw(self, amount: int) -> List[int]:
        withdrawn = [0] * 5
        for i in range(4,-1,-1):
            if amount >= [20,50,100,200,500][i]:
                needed = amount //  [20,50,100,200,500][i]
                used = min(needed,self.banknotes[i]) #(1,0)- if there is no banknotes exist else it will take the current banknotes from the ATM

                withdrawn[i] = used
                amount -=  used *[20,50,100,200,500][i]

        if amount > 0:
            return [-1]

        for i in range(5):
            self.banknotes[i] -= withdrawn[i]
        return withdrawn


atm = ATM()
atm.deposit([1,1,1,1,1])
withdrawn  = atm.withdraw(600)
print(withdrawn)
