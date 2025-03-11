import os
import pandas as pd

def save_dataframe_to_csv(df, filename, **kwargs):
    # Salva o DataFrame como CSV com os parâmetros fornecidos
    df.to_csv(filename, **kwargs)
    # Retorna o nome do arquivo salvo
    return filename


def merge_csv_files_in_dataframe(directory, output_path):
    """
    Lê todos os arquivos .csv em um diretório e os concatena em um único DataFrame.
    Salva o DataFrame combinado como um arquivo CSV no caminho especificado.

    Parâmetros:
    - directory: Caminho do diretório onde os arquivos .csv estão localizados.
    - output_path: Caminho onde o arquivo .csv combinado será salvo.

    Retorna:
    - O caminho do arquivo CSV combinado.
    """
    # Inicializar uma lista para armazenar os DataFrames
    all_dataframes = []

    # Iterar pelos arquivos na pasta
    for filename in os.listdir(directory):
        # Verificar se o arquivo termina com .csv
        if filename.endswith('.csv'):
            # Ler o arquivo CSV e adicionar à lista
            filepath = os.path.join(directory, filename)
            df = pd.read_csv(filepath)
            all_dataframes.append(df)

    # Concatenar todos os DataFrames em um único DataFrame
    combined_df = pd.concat(all_dataframes, ignore_index=True)

    file_out = save_dataframe_to_csv(combined_df, output_path, index=False)
    
    # Retornar o dataframe
    return combined_df, file_out