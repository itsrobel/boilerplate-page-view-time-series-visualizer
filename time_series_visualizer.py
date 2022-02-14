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
    (df['value']>= df['value'].quantile(0.025))
    &(df['value'] <= df['value'].quantile(0.975))
    ]


def draw_line_plot():
    plt.clf()
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
    plt.clf()
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()

    #print(df_bar.groupby(""))
    # print(df_bar.groupby(df_bar['date'].map(lambda x: x.year)))
    df_bar['date'] = pd.to_datetime(df_bar['date'], format='%Y-%m-%d')
    df_bar['year'] = [d.year for d in df_bar.date]
    df_bar['month'] = [d.month for d in df_bar.date]
    # print(df_bar.groupby(df_bar.date.dt.year).head())
    print(df_bar.head())
    # Draw bar plot





    # Save image and return fig (don't change this part)
    # fig.savefig('bar_plot.png')
    # return fig

def draw_box_plot():
    plt.clf()
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)





    # Save image and return fig (don't change this part)
    # fig.savefig('box_plot.png')
    # return fig
