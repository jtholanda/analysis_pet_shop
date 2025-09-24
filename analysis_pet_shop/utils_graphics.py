import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Função para plotar um gráfico de colunas comparativo com valores de dias da semana e médias passados como parâmetros
def plot_weekday_means(df, group_type, mean_column):
    # Ordena os dias da semana de segunda a domingo
    days_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    mean_values = df.groupby(group_type)[mean_column].mean().reindex(days_order)
    # Plota o gráfico
    plt.figure(figsize=(10, 6))
    sns.barplot(x=mean_values.index, y=mean_values.values, palette='viridis')
    plot_bar_template('Mean Values by Day of the Week', 'Day of the Week', 'Mean Value', 45)

    # Função para plotar um gráfico de colunas comparativo usando 'day_of_week' e 'mean'
def plot_weekday_means(day_of_week, mean, image_path):
    # Ordena os dias da semana de segunda a domingo
    days_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    day_of_week = pd.Categorical(day_of_week, categories=days_order, ordered=True)
    
    # Plota o gráfico
    plt.figure(figsize=(10, 6))
    sns.barplot(x=day_of_week, hue=day_of_week, y=mean, palette='viridis', legend=False)
    plot_bar_template('Mean Values by Day of the Week', 'Day of the Week', 'Mean Value', 45)
    # Salvar a imagem do gráfico
    plt.show()
    plt.savefig(image_path)
    plt.close()  # Fechar o gráfico após salvar

    # Função que configura a estrutura de um gráfico de barras
def plot_bar_template(title, xlabel, ylabel, rotation):
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(rotation=rotation)
    plt.tight_layout()
    plt.show

    # Função para plotar um box plot de um conjunto de dados agrupados por uma coluna específica
def plot_boxplot(data, group_column, value_column):
    plt.figure(figsize=(10, 6))
    sns.boxplot(x=group_column, y=value_column, hue=group_column, data=data, palette='viridis', legend=False)
    plt.title(f'Box Plot of {value_column} grouped by {group_column}')
    plt.xlabel(group_column)
    plt.ylabel(value_column)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    
    # Função para plotar um gráfico de dispersão com linha de tendência e exibir a equação
def plot_scatter_with_trendline(df, date_column, int_column, group_column, group_value):
    # Filtra os dados pelo valor específico na coluna de agrupamento
    filtered_df = df[df[group_column] == group_value].copy()
    
    # Converte a coluna de datas para dias corridos
    filtered_df['days_elapsed'] = (filtered_df[date_column] - filtered_df[date_column].min()).dt.days
    
    # Dados para o gráfico de dispersão
    x = filtered_df['days_elapsed']
    y = filtered_df[int_column]
    
    # Cálculo da linha de tendência
    z = np.polyfit(x, y, 1)
    p = np.poly1d(z)
    
    # Plota o gráfico de dispersão
    plt.figure(figsize=(10, 6))
    plt.scatter(x, y, alpha=0.7, edgecolors='w', s=100, label='Data Points')
    plt.plot(x, p(x), "r--", label=f'Trendline: y = {z[0]:.2f}x + {z[1]:.2f}')  # Adiciona a linha de tendência com a equação
    plt.title(f'Scatter Plot of {int_column} over Time with Trendline\n(Filtered by {group_column}: {group_value})')
    plt.xlabel('Days Elapsed')
    plt.ylabel(int_column)
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()
    
    # Função para gerar um gráfico de Pareto
def plot_pareto(df, category_column, value_column):
    # Agrupa os dados e soma os valores por categoria
    pareto_df = df.groupby(category_column)[value_column].sum().sort_values(ascending=False).reset_index()
    
    # Calcula o percentual acumulado
    pareto_df['cum_percentage'] = pareto_df[value_column].cumsum() / pareto_df[value_column].sum() * 100
    
    # Plota o gráfico de Pareto
    fig, ax1 = plt.subplots(figsize=(12, 6))
    
    # Gráfico de barras
    ax1.bar(pareto_df[category_column], pareto_df[value_column], color='C0')
    ax1.set_xlabel(category_column)
    ax1.set_ylabel(value_column, color='C0')
    ax1.tick_params(axis='y', labelcolor='C0')
    
    # Gráfico de linha para o percentual acumulado
    ax2 = ax1.twinx()
    ax2.plot(pareto_df[category_column], pareto_df['cum_percentage'], color='C1', marker='o', linestyle='-', linewidth=2)
    ax2.set_ylabel('Cumulative Percentage (%)', color='C1')
    ax2.tick_params(axis='y', labelcolor='C1')
    ax2.axhline(80, color='gray', linestyle='--', linewidth=1)  # Linha de referência dos 80%
    
    # Título e layout
    plt.title(f'Pareto Chart of {value_column} by {category_column}')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    
    
    # Função para plotar os valores da média móvel com linha de tendência
def plot_moving_average_with_trendline(values, moving_avg, window_size, x_range, elapsed_days = 365, split_time=False):
    
    
    if split_time:
        # Considera apenas os últimos 365 dias
        if len(values) > elapsed_days:
            values = values[-elapsed_days:]
            moving_avg = moving_avg[-elapsed_days:]
        
    # Cria o eixo x com os índices dos valores
    x = np.arange(1, len(values) + 1)
    
    # Calcula a linha de tendência para a média móvel
    valid_indices = ~np.isnan(moving_avg)  # Exclui valores NaN da média móvel
    z = np.polyfit(x[valid_indices], moving_avg[valid_indices], 1)
    p = np.poly1d(z)
    
    # Plota o gráfico
    plt.figure(figsize=(10, 6))
    plt.scatter(x, values, alpha=0.7, edgecolors='w', s=x_range, label='Original Values')
    plt.plot(x, moving_avg, color='C1', label=f'Moving Average (Window {window_size})')
    plt.plot(x[valid_indices], p(x[valid_indices]), "r--", label=f'Trendline: y = {z[0]:.2f}x + {z[1]:.2f}')
    
    # Ajusta os ticks do eixo x
    ticks = [1] + list(range(x_range, len(values) + 1, x_range))  # Garante que comece em 1 e depois vá para 100, 200, etc.
    plt.xticks(ticks)
    
    plt.xlim(1, len(values))  # Limita o eixo x até o comprimento dos valores

    plt.title(f'Scatter Plot of Moving Average with Trendline {elapsed_days} days')
    plt.xlabel('Days')
    plt.ylabel('Values')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

def plot_moving_average_by_day_of_week(df, data_name, moving_avg_name, day_of_week):
    plt.plot(df[data_name], df[moving_avg_name])
    plt.title(f"Média Móvel de {day_of_week}")
    plt.xlabel("Data")
    plt.ylabel("Média Móvel")
    plt.show()
    
    # Função para plotar um gráfico de colunas com legendas baseadas em uma coluna
def plot_column_chart_with_legend_stacked(df, x_column, y_column, legend_column):
    # Cria um gráfico de colunas
    plt.figure(figsize=(12, 6))
    
    # Plota cada grupo com uma cor diferente
    for key, grp in df.groupby(legend_column):
        plt.bar(grp[x_column], grp[y_column], label=str(key), alpha=0.7)

    # Configurações do gráfico
    plt.title('Gráfico de Colunas')
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    plt.xticks(rotation=45)
    plt.legend(title=legend_column)
    plt.tight_layout()
    plt.show()
    
    # Função para plotar um gráfico de colunas com legendas baseadas em uma coluna
def plot_column_chart_with_legend_side_by_side(df, x_column, y_column, legend_column):
    # Agrupa os dados pela coluna de legenda
    grouped = df.groupby([x_column, legend_column])[y_column].sum().unstack(fill_value=0)

    # Configura a largura das barras
    bar_width = 0.2
    x = np.arange(len(grouped))

    # Cria um gráfico de colunas
    plt.figure(figsize=(12, 6))
    
    # Plota as barras lado a lado
    for i, (key, values) in enumerate(grouped.items()):
        plt.bar(x + i * bar_width, values, width=bar_width, label=str(key), alpha=0.7)

    # Configurações do gráfico
    plt.title('Gráfico de Colunas')
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    plt.xticks(x + bar_width * (len(grouped.columns) - 1) / 2, grouped.index, rotation=45)
    plt.legend(title=legend_column)
    plt.tight_layout()
    plt.show()