# from example at http://neuralnetworksanddeeplearning.com/chap1.html
# you want to decide to go to an event
# factor 1: weather
# factor 2: friend is going
# factor 3: close to public transportation
# bias: represents how badly you want to go to the event

class Input:
    def __init__(self, name, value: bool):
        self.name = name
        self.value = value

class Factor:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

class Perceptron: 
    def __init__(self, name, bias, factors):
        self.name = name
        self.bias = bias
        self.factors = factors
    
    def calculate(self, inputs):
        sum = 0
        for input in inputs:
            factor = list(filter(lambda x: x.name == input.name, self.factors))[0]
            #print(f"found input {factor.name} with factor weight of {factor.weight} and value {input.value}")
            sum += (factor.weight * input.value)
            #print(f'sum is {sum}')
        return 1 if sum + self.bias > 0 else 0

run_perceptron = lambda perceptron: print(f'{perceptron.name}: {perceptron.calculate(inputs)}')

# scenario 1: all factors similar, no bias. Bad weather but friend is going and is close to transit
factors = [
    Factor('weather', 2),
    Factor('friend', 2),
    Factor('transit', 2)
]
perceptron = Perceptron('scenario 1', 0, factors)
inputs = [
    Input('weather', 0),
    Input('friend', 1),
    Input('transit', 1)
]
run_perceptron(perceptron)

# scenario 2: all factors similar, bias to not go. Good weather, but friend is not goinig and far from transit
# reuse factors
perceptron = Perceptron('scenario 2', -2, factors)
inputs = [
    Input('weather', 1),
    Input('friend', 0),
    Input('transit', 0)
]
run_perceptron(perceptron)

# scenario 3: you really want to go but hate bad weather. Other factors not important to you
# reuse bad weather inputs from above
factors = [
    Factor('weather', -10),
    Factor('friend', 0),
    Factor('transit', 0)
]
bias = 10 # +10 bias indicating you want to go pretty badly
perceptron = Perceptron('scenario 3', bias, factors)
run_perceptron(perceptron)

