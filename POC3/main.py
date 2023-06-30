import os
import pandas as pd
import warnings
warnings.filterwarnings("ignore")
from dotenv import load_dotenv
load_dotenv()
from pandasai import PandasAI
from pandasai.llm.openai import OpenAI
llm = OpenAI()
pandas_ai = PandasAI(llm, conversational=True)



list_folder = ['Campaign', 'Open Email']

def combine_df(folder_path):
# Define the folder path containing the CSV files

    # Get a list of all CSV files in the folder
    csv_files = [file for file in os.listdir(folder_path) if file.endswith(".csv")]

    # Create an empty dataframe to store the combined data
    combined_df = pd.DataFrame()

    # Iterate over each CSV file and append its data to the combined dataframe
    for file in csv_files:
        file_path = os.path.join(folder_path, file)
        df = pd.read_csv(file_path)
        combined_df = combined_df.append(df, ignore_index=True)

    # Print the combined dataframe
    return combined_df

if __name__ == '__main__':
    df = [combine_df(i) for i in list_folder]
    # while True:
    #     prompt = input('Pasukan pesanmu: ')
    #     print(pandas_ai.run(df, prompt=prompt, show_code=True))

    prompt = """I want you to act as Senior Data Analyst. Based on the provided data, \
    I want you to group which subjects has emoji which one doesn't. \
    After that compare the performance of group that has emoji versus the group that has no emoji. \
    create conclusion whether having emoji on subject can boost performance \
    """
    print(pandas_ai.run(df, prompt=prompt))
