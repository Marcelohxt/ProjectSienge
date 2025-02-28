# Passo 1: Importar as bibliotecas necessárias
import pandas as pd

# Passo 2: Definir o caminho do arquivo
caminho_arquivo = r'D:\ProgramacaoPhyton\DataScience02\DashboardGestaoObra'  # Substitua pelo caminho do seu arquivo
caminho_arquivo_tratado = r'D:\ProgramacaoPhyton\DataScience02\arquivo_tratado.csv'  # Caminho para salvar o arquivo tratado

# Passo 3: Ler o arquivo com tratamento de codificação e delimitadores
try:
    # Tenta ler o arquivo com codificação UTF-8, delimitador padrão (vírgula) e tratamento de vírgulas mal posicionadas
    df = pd.read_csv(
        caminho_arquivo,
        encoding='utf-8',
        delimiter=',',
        quotechar='"',
        on_bad_lines='skip'
    )
except UnicodeDecodeError:
    try:
        # Se UTF-8 falhar, tenta latin1
        df = pd.read_csv(
            caminho_arquivo,
            encoding='latin1',
            delimiter=',',
            quotechar='"',
            on_bad_lines='skip'
        )
    except UnicodeDecodeError:
        # Se latin1 falhar, tenta ISO-8859-1
        df = pd.read_csv(
            caminho_arquivo,
            encoding='ISO-8859-1',
            delimiter=',',
            quotechar='"',
            on_bad_lines='skip'
        )

# Passo 4: Verificar os dados lidos
print("Primeiras linhas do arquivo original:")
print(df.head())  # Exibe as primeiras 5 linhas do DataFrame

# Passo 5: Limpar os dados
# Remover espaços em branco no início e no fim das strings
df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

# Substituir valores nulos por 'N/A' (ou outro valor desejado)
df = df.fillna('N/A')

# Converter colunas numéricas (se necessário)
# Exemplo: Converter uma coluna chamada 'coluna_numerica' para tipo numérico
try:
    df['coluna_numerica'] = pd.to_numeric(df['coluna_numerica'], errors='coerce')
except KeyError:
    print("Coluna 'coluna_numerica' não existe ou já está no formato correto.")

# Converter colunas de data (se necessário)
# Exemplo: Converter uma coluna chamada 'coluna_data' para tipo datetime
try:
    df['coluna_data'] = pd.to_datetime(df['coluna_data'], errors='coerce')
except KeyError:
    print("Coluna 'coluna_data' não existe ou já está no formato correto.")

# Passo 6: Verificar os dados após a limpeza
print("\nPrimeiras linhas do arquivo tratado:")
print(df.head())

# Passo 7: Salvar o arquivo tratado em um novo CSV
df.to_csv(caminho_arquivo_tratado, index=False, encoding='utf-8')
print(f"\nArquivo tratado salvo em: {caminho_arquivo_tratado}")