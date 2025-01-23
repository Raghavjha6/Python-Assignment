'''Q. In a town, the percentage of men is 52. The percentage of total literacy is 48. If total
percentage of literate men is 35 of the total population, write a program to find the total
number of illiterate men and women if the population of the town is 80,000.'''

population = 80000
percentage_men = 52
percentage_literacy = 48
percentage_literate_men = 35
men_population = (percentage_men / 100) * population
women_population = population - men_population
literate_men = (percentage_literate_men / 100) * population
illiterate_men = men_population - literate_men
illiterate_women = women_population - ((percentage_literacy / 100) * population -literate_men)
print("Illiterate men:",illiterate_men)
print("Illiterate women:",illiterate_women)
