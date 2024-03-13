import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import time

def initialize_plot():
    fig, ax = plt.subplots()
    lines = {
        'temperature1': ax.plot([], [], label='Temperature 1')[0],
        'temperature2': ax.plot([], [], label='Temperature 2')[0],
        'humidity1': ax.plot([], [], label='Humidity 1')[0],
        'humidity2': ax.plot([], [], label='Humidity 2')[0]
    }
    ax.set_xlabel('Timestamp')
    ax.set_ylabel('Value')
    ax.legend()
    return fig, ax, lines

def refresh_data(ax, lines):
    try:
        # change the file path to yor file in place of 'sample_data.csv'
        df = pd.read_csv('sample_data.csv', parse_dates=['Timestamp'])
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return

    if df.empty:
        print("CSV file is empty.")
        return

    for key, line in lines.items():
        line.set_data(df['Timestamp'], df[key])
    
    # Formatting
    ax.set_xticks(df['Timestamp'])
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M:%S'))
    plt.xticks(rotation=45)

    ax.relim()
    ax.autoscale_view()
    plt.draw()
    plt.pause(1)

def main():
    fig, ax, lines = initialize_plot()
    while True:
        refresh_data(ax, lines)
        time.sleep(60)  #1 minute 

if __name__ == "__main__":
    main()
