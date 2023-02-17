import csv
from collections import Counter
from pathlib import Path

def analyze_log(path_to_file):
    # if not path_to_file.endswith('.csv'):
    #     raise FileNotFoundError(f"Extensão inválida: '{path_to_file}'")
    path = Path(path_to_file)
    if path.suffix != '.csv':
        raise FileNotFoundError(f"Extensão inválida: '{path_to_file}'")
    
    try:
        with open(path_to_file, "r") as log_file:
            data_csv = log_file.readlines()
            
    except FileNotFoundError:
        # raise FileNotFoundError("Arquivo inexistente: '{}'".format(path_to_file))
        raise FileNotFoundError(f"Arquivo inexistente: '{path_to_file}'")
    
# Qual o prato mais pedido por 'maria'?
    # def find_maria_favorite_food():
    find_maria_favorite_food = []
    for line in data_csv:
        if (line.startswith("maria")):
            find_maria_favorite_food.append(line)
            # print(line)
   
    maria_food_counter = Counter(find_maria_favorite_food) # all maria's foods
    # print(maria_food_counter)
    maria_hamburguer = maria_food_counter.most_common(1)[0][0].split(',')[1] # hamburguer
    # print(maria_hamburguer)

    with open('data/mkt_campaign.txt', 'w') as maria:
        maria.write(maria_hamburguer)
    # print(maria_favorite_food)

# Quantas vezes 'arnaldo' pediu 'hamburguer'?
    # arnaldo_hamburguer = []
    # for line in data_csv:
    #     if (line.startswith("arnaldo")):
    #         arnaldo_hamburguer.append(line)
    # # print(arnaldo_hamburguer)
    # arnaldo_count = Counter(arnaldo_hamburguer) # all arnaldo's foods
    # arnaldo_order_hamburguer = arnaldo_count.most_common(1)[0][0].split(',')[1] # misto-quente mais comum
    



# Quais pratos 'joao' nunca pediu?





# Quais dias 'joao' nunca foi à lanchonete?
