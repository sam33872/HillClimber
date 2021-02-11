import random
import matplotlib.pyplot as plt

# HillClimber Class defines a hillclimber algorithm
class HillClimber:
    def __init__(self, mutation):
        # Mutation rate passed into function by parameter
        self.mutation = mutation
        # Capacity limit set to 20
        self.cap = 20
        # Items are setup, with their name, benefit and volume
        self.items = [["a",5,3],["b",6,2],["c",1,4],["d",9,5],["e",2,8],["f",8,9],["g",4,10],["h",3,1],["i",7,6],["j",10,7]]
        # Genes setup and starting values are randomly generated
        self.genes = [random.randrange(2) for i in range(10)]
    
    # Mutate function deals with mutating a gene
    def mutate(self):
        # Makes a copy of genotype
        child = self.genes.copy()
        # Generate a random number between 0-9
        a = random.randrange(10)
        # If number is less than mutation rate
        # This allows me to control the chance of mutation
        # If mutation is set to 2, then 20% chance
        if(a < self.mutation):
            # Flip selected gene
            if(child[a] == 0):
                child[a] = 1
            else:
                child[a] = 0
            # Check fitness of new genotype compared to old genotype
            if(self.fitness(child) > self.fitness(self.genes)):
                # If new genotype is better, set to be main genotype
                self.genes = child
    
    # Checks how good of a solution a set of genes is
    def fitness(self, genes):
        # Initalise benefit and volume variables
        benefit = 0
        volume = 0
        # Go through all 10 genes
        for i in range(10):
            # Check gene to see if item is in knapsack
            if(genes[i] == 1):
                # Add benefit and volume to variable respectively
                benefit += self.items[i][1]
                volume += self.items[i][2]
        
        # If total volume of items in knapsack doesn't exceeds limit
        if(volume <= self.cap):
            # return total benefit
            return benefit
        # If capacity is exceeded, return 0
        else:
            return 0
    
    # Function used to run the algorithm
    def run(self, loops):
        values = []
        # Runs each generation
        # Runs 'loops' amount of generations 
        for i in range(loops):
            # mutates
            self.mutate()
            # adds fitness value to array
            values.append(self.fitness(self.genes))
        # Returns all fitness values
        return values
