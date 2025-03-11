import pandas as pd
def drop_repeated_column(df, column):

    # Contar quantos valores estão repetidos na coluna
    num_repeated = df[column].duplicated().sum()
    
    print(f"Há {num_repeated} valores repetidos na coluna '{column}'.")
    
    '''
    subset: Para especificar quais colunas verificar como duplicadas. Exemplo: df.drop_duplicates(subset=['coluna1', 'coluna2'])
    keep: Para definir se deve manter a primeira ou última ocorrência de cada duplicata (padrão é 'first'). 
    Exemplo: df.drop_duplicates(keep='last')
    inplace: Se True, faz a operação no próprio DataFrame sem precisar de reatribuição. Exemplo: df.drop_duplicates(inplace=True)
    '''
    df = df.drop_duplicates(subset=[column])

    # Contar quantos valores estão repetidos na coluna
    num_repeated = df[column].duplicated().sum()

    print(f"Há {num_repeated} valores repetidos na coluna '{column}'.")
    
    return df

def count_occurences(df, column):
    # Contar ocorrências e filtrar valores que aparecem mais de uma vez
    num_repeated = df[column].value_counts()[df[column].value_counts() > 1]
    return num_repeated

