import matplotlib
matplotlib.use('agg')

import pandas
from ggplot import *

def plot_weather_data(turnstile_weather):
    ''' 
    Use ggplot to make another data visualization focused on the MTA and weather
    data we used in assignment #3. You should make a type of visualization different
    than you did in exercise #1, and try to use the data in a different way (e.g., if you
    made a lineplot concerning ridership and time of day in exercise #1, maybe look at weather
    and try to make a histogram in exercise #2). 
    
    You should feel free to implement something that we discussed in class
    (e.g., scatterplots, line plots, or histograms) or attempt to implement 
    something more advanced if you'd like.  Here are some suggestions for things
    to investigate and illustrate:
    * Ridership by time of day or day of week
    * How ridership varies based on Subway station
    * Which stations have more exits or entries at different times of day

    If you'd like to learn more about ggplot and its capabilities, take
    a look at the documentation at:
    https://pypi.python.org/pypi/ggplot/
    
    You can check out: 
    https://www.dropbox.com/s/meyki2wl9xfa7yk/turnstile_data_master_with_weather.csv
     
    To see all the columns and data points included in the turnstile_weather 
    dataframe. 
    
    However, due to the limitation of our Amazon EC2 server, we are giving you about 1/3
    of the actual data in the turnstile_weather dataframe
    '''

    df = turnstile_weather
    xvar = df['ENTRIESn_hourly']

    plot = ggplot(aes(xvar), data=diamonds) + geom_histogram(binwidth = 500) + ggtitle("Histogram of Diamond Carats") + labs("Carats", "Freq")

    return plot

if __name__ == "__main__":
    image = "plot.png"
    input_filename = 'turnstile_data_master_with_weather.csv' 
    
    gg =  plot_weather_data(turnstile_weather)
    ggsave(image, gg, width=11, height=8)    
    
