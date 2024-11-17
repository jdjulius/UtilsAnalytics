import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def graphBarrPlot(df, varCualitativa):

    variables_numericas = df.select_dtypes(include=['int64', 'float64'])
    numVariables = len(variables_numericas.columns)

    fig, axes = plt.subplots(nrows=numVariables, ncols=1, figsize=(10, 6*numVariables))

    for i, variable in enumerate(variables_numericas.columns):
        sns.barplot(x=varCualitativa, y=variable, ax=axes[i], data=df)
        axes[i].set_title(f'Gráfica de {variable}')
        axes[i].set_xlabel(variable)
        axes[i].set_ylabel('Frecuencia')

    plt.tight_layout()
    plt.show()
    
    
def graphBoxPlot(df, varCualitativa):

    variables_numericas = df.select_dtypes(include=['int64', 'float64'])
    numVariables = len(variables_numericas.columns)

    fig, axes = plt.subplots(nrows=numVariables, ncols=1, figsize=(10, 6*numVariables))

    for i, variable in enumerate(variables_numericas.columns):
        sns.boxplot(x=varCualitativa, y=variable, ax=axes[i], data=df)
        axes[i].set_title(f'Gráfica de {variable}')
        axes[i].set_xlabel(variable)
        axes[i].set_ylabel('Frecuencia')

    plt.tight_layout()
    plt.show()
    
    def graphHistDensity(df, varCualitativa):
        
        variables_numericas = df.select_dtypes(include=['int64', 'float64'])
        numVariables = len(variables_numericas.columns)

        fig, axes = plt.subplots(nrows=numVariables, ncols=1, figsize=(10, 6*numVariables))

        for i, variable in enumerate(variables_numericas.columns):
            sns.histplot(x=variable, hue=varCualitativa, data=df, kde=True, ax=axes[i])
            axes[i].set_title(f'Gráfica de {variable}')
            axes[i].set_xlabel(variable)
            axes[i].set_ylabel('Frecuencia')

        plt.tight_layout()
        plt.show()