import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv')
df.set_index("date")
# Clean data
df = df[
    (df['value'] >= df['value'].quantile(0.025))
    & (df['value'] <= df['value'].quantile(0.975))
]


def draw_line_plot():
    # Draw line plot
    figure = df.plot.line(x="date", y='value')
    figure.set(xlabel="Date")
    figure.set(ylabel="Page Views")
    figure.set(title="Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    plt.show()
    fig = figure.get_figure()

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig


def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()

    # print(df_bar.groupby(""))
    # print(df_bar.groupby(df_bar['date'].map(lambda x: x.year)))
    df_bar['date'] = pd.to_datetime(df_bar['date'], format='%Y-%m-%d')
    df_bar['year'] = [d.year for d in df_bar.date]
    df_bar['month'] = [d.month for d in df_bar.date]

    df_bar = df_bar.sort_values("month")
    df_bar['month'] = df_bar.date.dt.month_name()
    # print(df_bar.groupby(df_bar.date.dt.year).head())

    figure = sns.catplot(x="year", y="value", hue="month",
                         data=df_bar, kind="bar", aspect=1.3, ci=None)
    figure.set(xlabel="Years")
    figure.set(ylabel="Average Page Views")
    fig = figure

    ax = fig.axes[0][0]
    print(ax)
    ax.legend()
    for label in ax.get_legend().get_texts():
        # actual.append(label.get_text())
        print(label.get_text())
    plt.show()
    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig


def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box['Date'] = pd.to_datetime(df_box['date'], format='%Y-%m-%d')
    df_box.reset_index(inplace=True)
    df_box['Year'] = [d.year for d in df_box.Date]
    df_box['month'] = [d.month for d in df_box.Date]
    # df_box['Month'] = df_box.sort_values("Month")
    df_box['Month'] = [d.strftime('%b') for d in df_box.Date]
    # Draw box plots (using Seaborn)
    df_box = df_box.sort_values("month")
    # figure = sns.catplot(y="value", data=df_box, kind="box", row="year")
    fig, axs = plt.subplots(1, 2)
    # sns.regplot(x='year', y='value', data=df_box, ax=axs[0])
    # sns.regplot(x='month', y='value', data=df_box, ax=axs[1])
    sns.boxplot(x='Year', y='value', data=df_box, ax=axs[0])
    axs[0].set_title("Year-wise Box Plot (Trend)")
    axs[0].set(ylabel='Page Views')
    sns.boxplot(x='Month', y='value', data=df_box, ax=axs[1])
    axs[1].set_title("Month-wise Box Plot (Seasonality)")
    axs[1].set(ylabel='Page Views')
    fig.tight_layout()
    actual = []
    for label in fig.axes[1].get_xaxis().get_majorticklabels():
        actual.append(label.get_text())

    plt.show()
    print(actual)
    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
