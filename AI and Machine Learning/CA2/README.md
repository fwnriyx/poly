In this project, I aimed to:
- Cluster customers of a shopping mall to understand customers better in order to retain said customers.
- Perform Time Series Forecasting on the Energy Consumption Dataset provided. Using the dataset, we are supposed to build a timeseries model and make predictions of the gas, electricity and water consuption using the test dataset.


I did the traditional method of data preprocessing, visualising, eda, etc and I feel like this project has really given me a good taste of clustering and time series.

Some of the more interesting things I did were genetic algorithm and 3d plots. I tried to implement an artificial bee colony for hyperparameter tuning, but it didnt work too well so I had to abandon the idea (it didnt let me use the package..)

With that, I'll give an example of some of my extra features:

```python
def genetic_algorithm(n_clusters, data, num_generations = 10, population_size = 70, num_selected = 40, mutation_rate = 10, max_selected_features=None):
    num_samples, num_features = data.shape
    population = initialize_population(population_size, num_features, max_selected_features=max_selected_features) 
    
    for generation in range(num_generations):
        fitness_scores = evaluate_fitness(n_clusters, data, population)
        selected_candidates = select_candidates(population, fitness_scores, num_selected)
        new_population = []
        
        for i in range(0, len(selected_candidates), 2):
            parent1 = selected_candidates[i]
            parent2 = selected_candidates[i + 1] if i + 1 < len(selected_candidates) else parent1
            child1, child2 = crossover(parent1, parent2)
            child1 = mutate(child1, mutation_rate)
            child2 = mutate(child2, mutation_rate)
            new_population.append(child1)
            new_population.append(child2)
        
        population = np.array(new_population)
    
    best_fitness_index = np.argmin(fitness_scores)
    best_subset = population[best_fitness_index]
    
    return best_subset
```

This was definitely a highlight of the project as it was quite unique and I feel that the idea was quite out of the box. Some limitations and things I didnt get a chance to implement were:
Exponential Expanding Window which was a way to give each point a weightage before putting them through a time series model. This would ensure that patterns were evenly weighed.
Artificial Bee Colony which was a more efficient way of tuning my hyper parameters.
Upsampling, which I couldnt get to work because of how the interpolation worked. I felt like the values were really too artificial and it didnt benefit the model. Hence, I dropped the idea.

I also learnt new things such as I can't have the same AR and MA in SARIMA.

All in all, this was definitely a beneficial project that let me hone my time series and clustering skills.