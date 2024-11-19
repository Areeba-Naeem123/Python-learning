import random

# ==================== Population ==========================
def populate(string_length=8):
    population = []
    for index in range(5):
        string = ''
        for i in range(8):
            random_num = random.randint(1, 100)
            if random_num >= 1 and random_num <= 50:
                string = string + '0'
            else:
                string = string + '1'
        population.append(string)
    return population

# ==================== Fitness Function =======================
def fitness(population):
    fitness = []
    for string in population:
        fitness_count = string.count('1')
        fitness.append((string, fitness_count))
    return fitness

# ==================== Selection Functions =======================
def total_fitness(fitness_list):
    total = 0
    for string, fitness in fitness_list:
        total += fitness
    return total

def ratios(total_fitness, fitness_list):
    selection_probability = []
    for string, fitness in fitness_list:
        probability = fitness / total_fitness
        selection_probability.append(round(probability, 2))
    return selection_probability

def commulative_fitness(selection_probability):
    commulative_fitness = [selection_probability[0]]
    for index in range(1, len(selection_probability)):
        commulative_fitness.append(selection_probability[index] + commulative_fitness[index - 1])
    commulative_fitness = [round(value, 2) for value in commulative_fitness]
    commulative_fitness[-1] = 1.0
    return commulative_fitness

# ==================== Selection =======================
def selection(commulative, population, fitness):
    random_float = round(random.random(), 2)
    selected = []
    if random_float <= commulative[0] and random_float >= 0.0:
        selected.append((population[0], fitness[0]))
    else:
        for index in range(len(commulative) - 1):
            if random_float >= commulative[index] and random_float < commulative[index + 1]:
                selected.append((population[index], fitness[index]))
        if random_float >= commulative[-2] and random_float <= commulative[-1]:
            selected.append((population[-1], fitness[-1]))
    return selected

# ==================== Crossover =======================
def single_crossover(parent1, parent2):
    random_num = random.randint(1, 10)
    child1 = parent1[:random_num] + parent2[random_num:]
    child2 = parent2[:random_num] + parent1[random_num:]
    return child1, child2

# ==================== Mutation =======================
def mutate(population, mutation_rate):
    mutated_population = []
    for individual in population:
        individual_list = list(individual)
        for i in range(len(individual_list)):
            if random.random() <= mutation_rate:
                individual_list[i] = '0' if individual_list[i] == '1' else '1'
        mutated_population.append(''.join(individual_list))
    return mutated_population

# ==================== GA Pipeline =======================
def GA_pipeline(generations):
    population_ = populate()
    for generation in range(generations):
        print(f"\nGeneration {generation + 1}")
        
        fitness_values = fitness(population_)
        total_fitness_value = total_fitness(fitness_values)
        probability = ratios(total_fitness_value, fitness_values)
        
        commulative_values = commulative_fitness(probability)
        parents = selection(commulative_values, population_, fitness_values)
        
        offsprings = []
        if len(parents) <= 1:
            print("No crossover applied.")
        else:
            for i in range(0, len(parents), 2):
                parent1, parent2 = parents[i][0], parents[i + 1][0]
                child1, child2 = single_crossover(parent1, parent2)
                offsprings.append(child1)
                offsprings.append(child2)
            print(f"Parents: {parent1} {parent2}\nOffsprings: {offsprings}")

        print(f"Population: {population_}\nFitness: {fitness_values}\nProbability: {probability}\nCumulative: {commulative_values}")
        mutation_ = mutate(population_, 0.1)
        print(f"Original: {population_}\nMutated: {mutation_}")

        population_ = mutation_

    return population_

final_population = GA_pipeline(5)
print(f"Final population of GA-pipeline: {final_population}")


# ==================== Crop Yield =======================
def Crop_Yield():
    population = populate(4)
    fitness_valuess = fitness(population)
    total_fit_values = total_fitness(fitness_valuess)  # Corrected function call
    probability = ratios(total_fit_values, fitness_valuess)
    commulative_values = commulative_fitness(probability)
    selection_ = selection(commulative_values, population, fitness_valuess)
    
    print("Individual      Fitness(Yield in kg)       Fitness Ratio      Cumulative-Fitness       Selected?")
    
    for individual, fitness_val, prob, commulative in zip(population, fitness_valuess, probability, commulative_values):
        if (individual, fitness_val) in selection_:
            selected = "Yes"
        else:
            selected = "No"
        
        print(f"{individual}        {fitness_val} kg             {prob}                   {commulative}                {selected}")

# Run the Crop Yield function
Crop_Yield()
