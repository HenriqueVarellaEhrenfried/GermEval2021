import pandas as pd
import os

TEST = './Datasets/GermEval21_TestData.csv'
TRAIN = './Datasets/GermEval21_TrainData.csv'

FILES = [TRAIN, TEST]

def get_file_content():
    all_data = []
    for f in FILES:
        all_data.append(pd.read_csv(f, sep=',', quotechar='"'))
    return all_data

def save_file(file_name, content):
    with open(file_name, 'w', encoding="utf-8") as f:
        f.write(content)

def build_dataset(starting_id, df):
    
    # Make sure there is the target dir
    os.system("mkdir -p 'Datasets/Toxic'")
    os.system("mkdir -p 'Datasets/Engaging'")
    os.system("mkdir -p 'Datasets/FactClamming'")

    DATASETS_NAME = ["Sub1_Toxic","Sub2_Engaging","Sub3_FactClaiming"]
    for dn in DATASETS_NAME:
        if dn == DATASETS_NAME[0]:
            path = './Datasets/Toxic/'
        elif dn == DATASETS_NAME[1]:
            path = './Datasets/Engaging/'
        elif dn == DATASETS_NAME[2]:
            path = './Datasets/FactClamming/'
        
        data = df[["comment_text", dn]].to_dict('records')
        i = starting_id
        for d in data:
            # id_class.txt
            name = "%s%04d_%s.txt" % (path, i, d[dn])
            save_file(name, d["comment_text"])
            i += 1
    return i


def main():

    all_data = get_file_content()
    i = 0
    for df in all_data:
        i = build_dataset(i, df)



if __name__ == "__main__":
    print(">> Starting to separe dataset into three distinct datasets. The pattern will be <id>_<class>.txt. We deal with test set after the train set, so the last 944 files are from the test set")
    main()
    print(">> Evertything Done!")

# comment_id,comment_text,Sub1_Toxic,Sub2_Engaging,Sub3_FactClaiming
# 3244 Train
# 944  Test