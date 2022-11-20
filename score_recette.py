import pandas as pd

def score_energy(energy_value):
    if energy_value <= 335:
        return 0
    if energy_value <= 670:
        return 1
    if energy_value <= 1005:
        return 2
    if energy_value <= 1340:
        return 3
    if energy_value <= 1675:
        return 4
    if energy_value <= 2010:
        return 5
    if energy_value <= 2345:
        return 6
    if energy_value <= 2680:
        return 7
    if energy_value <= 3015:
        return 8
    if energy_value <= 3350:
        return 9
    return 10


def score_sucre(sucre_value):
    if sucre_value <= 4.5:
        return 0
    if sucre_value <= 9:
        return 1
    if sucre_value <= 13.5:
        return 2
    if sucre_value <= 18:
        return 3
    if sucre_value <= 22.5:
        return 4
    if sucre_value <= 27:
        return 5
    if sucre_value <= 31:
        return 6
    if sucre_value <= 36:
        return 7
    if sucre_value <= 40:
        return 8
    if sucre_value <= 45:
        return 9
    return 10


def score_acid(acid_value):
    if acid_value <= 1:
        return 0
    if acid_value <= 2:
        return 1
    if acid_value <= 3:
        return 2
    if acid_value <= 4:
        return 3
    if acid_value <= 5:
        return 4
    if acid_value <= 6:
        return 5
    if acid_value <= 7:
        return 6
    if acid_value <= 8:
        return 7
    if acid_value <= 9:
        return 8
    if acid_value <= 10:
        return 9
    return 10

def score_sodium(sodium_value):
    if sodium_value <= 90:
        return 0
    if sodium_value <= 180:
        return 1
    if sodium_value <= 270:
        return 2
    if sodium_value <= 360:
        return 3
    if sodium_value <= 450:
        return 4
    if sodium_value <= 540:
        return 5
    if sodium_value <= 630:
        return 6
    if sodium_value <= 720:
        return 7
    if sodium_value <= 810:
        return 8
    if sodium_value <= 900:
        return 9
    return 10

def score_protein(protein_value):
    if protein_value <= 1.6:
        return 0
    if protein_value <= 3.2:
        return 1
    if protein_value <= 4.8:
        return 2
    if protein_value <= 6.4:
        return 3
    if protein_value <= 8.0:
        return 4
    return 5

def score_fibre(fibre_value):
    if fibre_value <= 0.7:
        return 0
    if fibre_value <= 1.4:
        return 1
    if fibre_value <= 2.1:
        return 2
    if fibre_value <= 2.8:
        return 3
    if fibre_value <= 3.5:
        return 4
    return 5

def score_fruit(percent):
    if percent <= 40:
        return 0
    if percent <= 60:
        return 1
    if percent > 80:
        return 5
    return 2

def get_from_file(ingredient):
    df = pd.read_csv('./data/Table Ciqual 2020_ENG_2020 07 07.csv')
    val = df.loc[df['alim_nom_eng'] ==  ingredient]
    return val.iloc[0]

def score_nutrition(list_composition, percent_fruit):

    point_A = score_energy(list_composition[0]) + score_sucre(list_composition[1])
    point_A += score_acid(list_composition[2]) + score_sodium(list_composition[3])

    fruit_score = score_fruit(percent_fruit)

    point_C = score_fibre(list_composition[4]) + fruit_score

    if fruit_score == 5:
        point_C += score_protein(list_composition[5])

    score_nutri = point_A - point_C

    return score_nutri

    # list de string en args
def score(list_of_ingredients, list_weight):
    index = [9, 18, 17, 60, 26, 14, 3]

    list_composition = [0, 0, 0, 0, 0, 0]
    total_weight_vegetable = 0
    total_weight_other = 0

    for i in range(len(list_of_ingredients)):
        ingredient = get_from_file(list_of_ingredients[i])
        for y in range(len(list_composition)):
            num = 0 if ingredient.iloc[index[y]] == "-" else float(ingredient.iloc[index[y]].replace(',', '.'))
            list_composition[y] += num * list_weight[i] / 100
        if ingredient.iloc[index[-1]] == "fruits, vegetables, legumes and nuts":
            total_weight_vegetable += list_weight[i]
        else:
            total_weight_other += list_weight[i]

    total_weight = total_weight_vegetable + total_weight_other
    percent_of_vegetable = (total_weight_vegetable * 100) / total_weight

    for i in range(len(list_composition)):
        list_composition[i] = (list_composition[i] * 100) / total_weight

    return score_nutrition(list_composition, percent_of_vegetable)


a = score(["Fresh egg pasta, cooked, unsalted", "Cucumber, pulp and peel, raw", "Tomato, raw", "Pine nuts", "Avocado, pulp, raw"], [100, 100, 100, 25, 200])
print(a);

