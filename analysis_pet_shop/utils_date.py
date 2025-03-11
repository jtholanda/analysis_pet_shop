# Função para extrair o dia do mês
def get_day_of_month(df, column_date):
    df['day'] = df[column_date].dt.day
    return df

# Função para extrair o mês
def get_month(df, column_date):
    df['month'] = df[column_date].dt.month
    return df

# Função para extrair o ano
def get_year(df, column_date):
    df['year'] = df[column_date].dt.year
    return df

# Função para extrair o dia da semana como string
def get_day_of_week_str(df, column_date):
    df['day_of_week'] = df[column_date].dt.day_name()
    return df

# Função para extrair a semana do mês
def get_week_of_month(df, column_date):
    df['week_of_month'] = (df[column_date].dt.day - 1) // 7 + 1
    return df

# Função para extrair a semana do ano
def get_week_of_year(df, column_date):
    df['week_of_year'] = df[column_date].dt.isocalendar().week
    return df

# Função para extrair o ano e o nome do mês
def get_year_month_name(df, column_date):
    df['year_month'] = df[column_date].dt.strftime('%Y-%B')
    return df

def get_all_columns(df, column_date):
    """
    Adiciona várias colunas derivadas de uma coluna de datas ao DataFrame.

    Parâmetros:
    df (pd.DataFrame): DataFrame original.
    column_date (str): Nome da coluna que contém os dados de datas.

    Retorna:
    pd.DataFrame: DataFrame atualizado com novas colunas.
    """
    # Extrai o dia da data e adiciona como uma nova coluna 'day'
    df['day'] = df[column_date].dt.day
    
    # Extrai o mês da data e adiciona como uma nova coluna 'month'
    df['month'] = df[column_date].dt.month
    
    # Extrai o ano da data e adiciona como uma nova coluna 'year'
    df['year'] = df[column_date].dt.year
    
    # Extrai o nome do dia da semana e adiciona como uma nova coluna 'day_of_week'
    df['day_of_week'] = df[column_date].dt.day_name()
    
    # Calcula a semana do mês e adiciona como uma nova coluna 'week_of_month'
    df['week_of_month'] = (df[column_date].dt.day - 1) // 7 + 1
    
    # Extrai a semana do ano e adiciona como uma nova coluna 'week_of_year'
    df['week_of_year'] = df[column_date].dt.isocalendar().week
    
    # Formata a data como 'ano-mês' e adiciona como uma nova coluna 'year_month'
    df['year_month'] = df[column_date].dt.strftime('%Y-%B')
    
    # Retorna o DataFrame com as novas colunas
    return df



