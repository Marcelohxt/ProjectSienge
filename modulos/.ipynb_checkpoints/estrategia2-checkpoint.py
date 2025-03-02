# Módulo de conversão de tipos de dados


# Imports
import numpy as np
import pandas as pd


# Converte colunas específicas para o tipo string
def convert_to_string(df, columns):
    for col in columns:
        df[col] = df[col].astype("string")  # Altera o tipo dos dados da coluna para string

# Converte colunas específicas para o tipo inteiro (int64)
def convert_to_int(df, columns):
    for col in columns:
        df[col] = df[col].astype("int64")  # Altera o tipo dos dados da coluna para inteiro

# Converte colunas específicas para o tipo datetime (datas)
def convert_to_datetime(df, columns):
    for col in columns:
        df[col] = pd.to_datetime(df[col])  # Converte os valores da coluna para formato de data

# Multiplica valores de colunas numéricas por um fator específico
def multiply_by_factor(df, columns, factor):
    for col in columns:
        df[col] = df[col] * factor  # Multiplica os valores da coluna pelo fator fornecido





def fill_missing_values(df, columns, strategy="mean", fill_value=None):
    """Preenche valores nulos com média, mediana, moda ou um valor específico."""
    for col in columns:
        if strategy == "mean":
            df[col].fillna(df[col].mean(), inplace=True)
        elif strategy == "median":
            df[col].fillna(df[col].median(), inplace=True)
        elif strategy == "mode":
            df[col].fillna(df[col].mode()[0], inplace=True)
        elif strategy == "constant" and fill_value is not None:
            df[col].fillna(fill_value, inplace=True)


def remove_outliers(df, columns, threshold=1.5):
    """Remove outliers com base no IQR (Intervalo Interquartil)."""
    for col in columns:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - threshold * IQR
        upper_bound = Q3 + threshold * IQR
        df = df[(df[col] >= lower_bound) & (df[col] <= upper_bound)]
    return df


def normalize_columns(df, columns):
    """Normaliza colunas especificadas para o intervalo [0, 1]."""
    scaler = MinMaxScaler()
    df[columns] = scaler.fit_transform(df[columns])


def standardize_columns(df, columns):
    """Padroniza colunas especificadas para média 0 e desvio padrão 1."""
    scaler = StandardScaler()
    df[columns] = scaler.fit_transform(df[columns])


def encode_categorical(df, columns):
    """Aplica label encoding a colunas categóricas especificadas."""
    encoder = LabelEncoder()
    for col in columns:
        df[col] = encoder.fit_transform(df[col])


def one_hot_encode(df, columns):
    """Aplica One-Hot Encoding a colunas categóricas especificadas."""
    df = pd.get_dummies(df, columns=columns, drop_first=True)
    return df
