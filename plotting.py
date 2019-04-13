import matplotlib as plt
import pandas as pd

class Plotting():

    def __init__(style = "line"):
        self.style = style


    def CreatePlot(df, filename, x_axis, y_axis):
        """Create a plot from a pandas dataframe and save to disk"""
        plt.plot(df[x_axis], df[y_axis])
        plt.xlabel(x_axis)
        plt.ylabel(y_axis)
        plt.savefig(filename + ".png")
        return df

    def PlotAllAgainst(df, filename, x_axis):
        """Using one column as the x-axis, plot every other column against it"""
        for y in df.columns:
            if y != x_axis:
                CreatePlot(df, filename + y, y, x_axis)
                return df










