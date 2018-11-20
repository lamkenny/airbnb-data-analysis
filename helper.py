import seaborn as sns

def lineplot(df, x, y, xlabel=None, ylabel=None, title=None):
    """Creates a line plot from the datafram `df` using columns specified by x and y."""
    ax = df.plot(x, y)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    ax.grid(True)
    return ax

def priceAsFloat(series):
    """Converts dollar values into float values."""
    return series.replace('[\$,]', '', regex=True).astype(float)

def plotCorrelationMatrix(df):
    """Plot correlation matrix"""
    sns.heatmap(df.corr(), annot=True, fmt=".2f")