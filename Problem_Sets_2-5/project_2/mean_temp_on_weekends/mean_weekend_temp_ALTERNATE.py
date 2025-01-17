import pandas as pd
import pandasql

def avg_min_temperature(filename):
    '''
    This function should run a SQL query on a dataframe of
    weather data.  The SQL query should return one column and
    one row - the average meantempi on days that are a Saturday
    or Sunday (i.e., the the average mean temperature on weekends).
    The dataframe will be titled 'weather_data' and you can access
    the date in the dataframe via the 'date' column.

    You'll need to provide  the SQL query.

    You might also find that interpreting numbers as integers or floats may not
    work initially.  In order to get around this issue, it may be equal to cast
    these numbers as integers.  This can be done by writing cast(column as integer).
    So for example, if we wanted to cast the maxtempi column as an integer, we would actually
    write something like where cast(maxtempi as integer) = 76, as opposed to simply
    where maxtempi = 76.

    Also, you can convert dates to days of the week via the 'strftime' keyword in SQL.
    For example, cast (strftime('%w', date) as integer) will return 0 if the date
    is a Sunday or 6 if the date is a Saturday.

    You can see the weather data that we are passing in below:
    https://www.dropbox.com/s/7sf0yqc9ykpq3w8/weather_underground.csv
    '''
    weather_data = pd.read_csv(filename)

    q = """
    SELECT avg(cast (meantempi as integer))
    FROM weather_data
    WHERE
    cast(strftime('%w', date) as integer) IN (0,6) 
    """
# (0,6) is the list in above statement


    #Execute your SQL command against the pandas frame
    mean_temp_weekends = pandasql.sqldf(q.lower(), locals())
    return mean_temp_weekends

if __name__ == "__main__":
    input_filename = "weather_underground.csv"
    output_filename = "output.csv"
    student_df = avg_min_temperature(input_filename)
    student_df.to_csv(output_filename)