import pandas as pd
import pandas as np

# Função para obter estatísticas descritivas de uma variável específica
def get_descriptive_statistics(df, column):
    stats = {
        'mean': df[column].mean(),
        'std_dev': df[column].std(),
        'variance': df[column].var(),
        'median': df[column].median(),
        'min': df[column].min(),
        'max': df[column].max()
    }
    return pd.DataFrame(stats, index=[0])

# Função para obter estatísticas descritivas agrupadas por outra coluna
def get_grouped_descriptive_statistics(df, group_column, target_column):
    stats = df.groupby(group_column)[target_column].agg(
        mean='mean',
        std_dev='std',
        variance='var',
        median='median',
        min='min',
        max='max'
    ).reset_index()
    
    # Formatar os valores com 2 casas decimais
    stats[['mean', 'std_dev', 'variance', 'median', 'min', 'max']] = stats[['mean', 'std_dev', 'variance', 'median', 'min', 'max']].round(2)

    return stats

# Função para calcular a média móvel
def moving_average(values, window_size):
    return values.rolling(window=window_size).mean()
