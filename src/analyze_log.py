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
    def find_maria_favorite_food(data_csv):
        find_maria_favorite_food = []
        for line in data_csv:
            if (line.startswith("maria")):
                find_maria_favorite_food.append(line)
        maria_food_counter = Counter(find_maria_favorite_food)
        return maria_food_counter.most_common(1)[0][0].split(',')[1]


# Quantas vezes 'arnaldo' pediu 'hamburguer'?
    def arnaldo_burguer(data_csv):
        find_arnaldo_burguer = []
        for line in data_csv:
            if (line.startswith("arnaldo")):
                find_arnaldo_burguer.append(line.split(',')[1])
        arnaldo_food_counter = Counter(find_arnaldo_burguer)
        return arnaldo_food_counter.most_common()[-1][1] # { hamburguer, 1 }
    
    
# Quais pratos 'joao' nunca pediu?
    def joao_never_ordered(data_csv):
        menu = set()
        for line in data_csv:
                menu.add(line.split(',')[1])
        
        joao_order = set()
        for line in data_csv:
            if (line.startswith("joao")):
                joao_order.add(line.split(',')[1])
        return menu.difference(joao_order)
            
# Quais dias 'joao' nunca foi à lanchonete? Ajuda do Arlisson
    def joao_never_came(data_csv):
        days = set()
        for line in data_csv:
            days.add(line.split(',')[2].replace('\n', ''))
        
        joao_days = set()
        for line in data_csv:
            if (line.startswith("joao")):
                joao_days.add(line.split(',')[2].replace('\n', ''))
        return days.difference(joao_days)
    
    with open('data/mkt_campaign.txt', 'w') as file:
        file.write(
            f"{find_maria_favorite_food(data_csv)}\n"
            f"{arnaldo_burguer(data_csv)}\n"
            f"{joao_never_ordered(data_csv)}\n"
            f"{joao_never_came(data_csv)}\n"
        )