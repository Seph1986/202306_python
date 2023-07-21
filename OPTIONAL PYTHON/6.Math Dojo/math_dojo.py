class MathDojo:
    
    def __init__(self):
        self.resultado = 0

    def sumar(self, num, *nums):
        self.resultado += num
        if nums:
            for i in nums:
                self.resultado += i
        
        return self
    
    def restar(self, num, *nums):
        self.resultado -= num
        if nums:
            for i in nums:
                self.resultado -= i

        return self

probando = MathDojo()

probando.sumar(2,3,4).restar(2,5,2).sumar(10).restar(10,5,10).sumar(15,15,15)
print(probando.resultado)