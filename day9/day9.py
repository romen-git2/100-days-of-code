import pandas as pd
import json
import os

# generate mock data
def createMockSourceFile(filename):
    data = {
        'sessionId': ['101', '102', '103', '104', '105'],
        'timestamp': ['2023-10-27 10:00:00', '2023-10-27 10:05:00', None, '2023-10-27 10:15:00', '2023-10-27 10:20:00'],
        'userQuery': ['What is ETL?', 'Define Python', 'error log', 'Calculate 5+5', 'Hello'],
        'responseQuality': [0.95, 0.88, 0.0, 0.99, 0.1],
        'status': ['complete', 'complete', 'failed', 'complete', 'timeout']
    }

    df = pd.read_csv('raw_logs.csv') if os.path.exists(
        'raw_logs.csv') else pd.DataFrame(data)
    df.to_csv(filename, index=False)
    print(f"Created source file {filename}")

def extractData(filePath):
    """ Ingest data from a CSV source """
    print(f"Loading data from {filePath}...")
    try:
        df = pd.read_csv(filePath)
        print(f"Loaded {len(df)} rows.")
        return df
    except FileNotFoundError:
        print("Error: File not found.")
        return None

def transformData(df):
    """ Clean and enrich data """
    print("Cleaning data...")

    initialCount = len(df)
    # drop rows with missing critical data(timestamp)
    df = df.dropna(subset=['timestamp'])
    print(f"Dropped {initialCount-len(df)} rows with missing timestamps.")

    # filter out failed or low quality sessions
    df = df[
        (df['status'] == 'complete') &
        (df['responseQuality'] > 0.5)
    ]

    print(f"Filtered down to {len(df)} high quality interactions.")

    df['timestamp'] = pd.to_datetime(df['timestamp'])

    df['processedBy'] = 'ETL Pipeline V1'

    return df


def loadData(df, outputFilepath):
    """ Save processed data to JSON """
    print(f"Saving to {outputFilepath}...")

    df['timestamp'] = df['timestamp'].dt.strftime('%Y-%m-%d %H:%M:%S')

    # convert DataFrame to a list of dictionaries (records format)
    records = df.to_dict(orient='records')

    with open(outputFilepath, 'w') as f:
        json.dump(records, f, indent=4)

    print("Data pipeline completed.")


if __name__ == '__main__':

    sourceFile = 'raw_agent_logs.csv'
    targetFile = 'clean_agent_context.json'

    createMockSourceFile(sourceFile)

    # extract
    rawDf = extractData(sourceFile)

    if rawDf is not None:
        # transform
        cleanDf = transformData(rawDf)
        # load
        loadData(cleanDf, targetFile)
