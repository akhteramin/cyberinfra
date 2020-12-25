import os
import json
import csv
import pandas as pd

# This finds our json files
path_to_json = (r"./responses_new") # Path to folder where json files are located
json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]


jsons_data = pd.DataFrame(columns=['ID', 'useful_question_1', 'enjoy_question_1', 'easy_to_follow_question_1', 'comment_1', 'useful_question_2', 'enjoy_question_2', 'easy_to_follow_question_2', 'comment_2',
'useful_question_3', 'enjoy_question_3', 'easy_to_follow_question_3', 'comment_3','useful_question_4', 'enjoy_question_4', 'easy_to_follow_question_4', 'comment_4',
'useful_question_5', 'enjoy_question_5', 'easy_to_follow_question_5', 'comment_5','useful_question_6', 'enjoy_question_6', 'easy_to_follow_question_6', 'comment_6',
'useful_question_7', 'enjoy_question_7', 'easy_to_follow_question_7', 'comment_7','useful_question_8', 'enjoy_question_8', 'easy_to_follow_question_8', 'comment_8',
'useful_question_9', 'enjoy_question_9', 'easy_to_follow_question_9', 'comment_9','useful_question_10', 'enjoy_question_10', 'easy_to_follow_question_10', 'comment_10',
'useful_question_11', 'enjoy_question_11', 'easy_to_follow_question_11', 'comment_11','useful_question_12', 'enjoy_question_12', 'easy_to_follow_question_12', 'comment_12'])


#Code to clean JSON Files
# for index, js in enumerate(json_files):
#     with open(os.path.join(path_to_json, js)) as json_file:
#         content = json.loads(json_file)
#         clean = content.replace('"{', '{').replace('}"', '}').replace('\\', '').replace('likert', 'enjoy_question')
#         json_files = json.loads(clean)



#Need both the json and an index number to use enumerate()
for index, js in enumerate(json_files):
    with open(os.path.join(path_to_json, js)) as json_file:
        json_text = json.load(json_file)
        print(json_text)
        # Here I need to know the layout of the json file and each json file has to have the same structure

        value = json.dumps(json_text[0]['responses'])
        pre_output = json.loads(value)
        output = json.loads(pre_output)
        ID = output['ID']

        value = json.dumps(json_text[1]['responses'])
        pre_output = json.loads(value)
        output = json.loads(pre_output)
        useful_question_1 = output['useful_question']
        enjoy_question_1 = output['enjoy_question']
        easy_to_follow_question_1 = output['easy_to_follow_question']
        comment_1 = output['comment']

        value = json.dumps(json_text[2]['responses'])
        pre_output = json.loads(value)
        output = json.loads(pre_output)
        useful_question_2 = output['useful_question']
        enjoy_question_2 = output['enjoy_question']
        easy_to_follow_question_2 = output['easy_to_follow_question']
        comment_2 = output['comment']

        value = json.dumps(json_text[3]['responses'])
        pre_output = json.loads(value)
        output = json.loads(pre_output)
        useful_question_3 = output['useful_question']
        enjoy_question_3 = output['enjoy_question']
        easy_to_follow_question_3 = output['easy_to_follow_question']
        comment_3 = output['comment']

        value = json.dumps(json_text[4]['responses'])
        pre_output = json.loads(value)
        output = json.loads(pre_output)
        useful_question_4 = output['useful_question']
        enjoy_question_4 = output['enjoy_question']
        easy_to_follow_question_4 = output['easy_to_follow_question']
        comment_4 = output['comment']

        value = json.dumps(json_text[5]['responses'])
        pre_output = json.loads(value)
        output = json.loads(pre_output)
        useful_question_5 = output['useful_question']
        enjoy_question_5 = output['enjoy_question']
        easy_to_follow_question_5 = output['easy_to_follow_question']
        comment_5 = output['comment']

        value = json.dumps(json_text[6]['responses'])
        pre_output = json.loads(value)
        output = json.loads(pre_output)
        useful_question_6 = output['useful_question']
        enjoy_question_6 = output['enjoy_question']
        easy_to_follow_question_6 = output['easy_to_follow_question']
        comment_6 = output['comment']

        value = json.dumps(json_text[7]['responses'])
        pre_output = json.loads(value)
        output = json.loads(pre_output)
        useful_question_7 = output['useful_question']
        enjoy_question_7 = output['enjoy_question']
        easy_to_follow_question_7 = output['easy_to_follow_question']
        comment_7 = output['comment']

        value = json.dumps(json_text[8]['responses'])
        pre_output = json.loads(value)
        output = json.loads(pre_output)
        useful_question_8 = output['useful_question']
        enjoy_question_8 = output['enjoy_question']
        easy_to_follow_question_8 = output['easy_to_follow_question']
        comment_8 = output['comment']

        value = json.dumps(json_text[9]['responses'])
        pre_output = json.loads(value)
        output = json.loads(pre_output)
        useful_question_9 = output['useful_question']
        enjoy_question_9 = output['enjoy_question']
        easy_to_follow_question_9 = output['easy_to_follow_question']
        comment_9 = output['comment']

        value = json.dumps(json_text[10]['responses'])
        pre_output = json.loads(value)
        output = json.loads(pre_output)
        useful_question_10 = output['useful_question']
        enjoy_question_10 = output['enjoy_question']
        easy_to_follow_question_10 = output['easy_to_follow_question']
        comment_10 = output['comment']

        value = json.dumps(json_text[11]['responses'])
        pre_output = json.loads(value)
        output = json.loads(pre_output)
        useful_question_11 = output['useful_question']
        enjoy_question_11 = output['enjoy_question']
        easy_to_follow_question_11 = output['easy_to_follow_question']
        comment_11 = output['comment']

        value = json.dumps(json_text[12]['responses'])
        pre_output = json.loads(value)
        output = json.loads(pre_output)
        useful_question_12 = output['useful_question']
        enjoy_question_12 = output['enjoy_question']
        easy_to_follow_question_12 = output['easy_to_follow_question']
        comment_12 = output['comment']


        # push a list of data into a pandas DataFrame at row given by 'index'
        jsons_data.loc[index] = [ID.encode('utf-8'), useful_question_1.encode('utf-8'), enjoy_question_1.encode('utf-8'), easy_to_follow_question_1.encode('utf-8'), comment_1.encode('utf-8'),
        useful_question_2.encode('utf-8'), enjoy_question_2.encode('utf-8'), easy_to_follow_question_2.encode('utf-8'), comment_2.encode('utf-8'),
        useful_question_3.encode('utf-8'), enjoy_question_3.encode('utf-8'), easy_to_follow_question_3.encode('utf-8'), comment_3.encode('utf-8'), useful_question_4.encode('utf-8'), enjoy_question_4.encode('utf-8'), easy_to_follow_question_4.encode('utf-8'), comment_4.encode('utf-8'),
        useful_question_5.encode('utf-8'), enjoy_question_5.encode('utf-8'), easy_to_follow_question_5.encode('utf-8'), comment_5.encode('utf-8'), useful_question_6.encode('utf-8'), enjoy_question_6.encode('utf-8'), easy_to_follow_question_6.encode('utf-8'), comment_6.encode('utf-8'),
        useful_question_7.encode('utf-8'), enjoy_question_7.encode('utf-8'), easy_to_follow_question_7.encode('utf-8'), comment_7.encode('utf-8'), useful_question_8.encode('utf-8'), enjoy_question_8.encode('utf-8'), easy_to_follow_question_8.encode('utf-8'), comment_8.encode('utf-8'),
        useful_question_9.encode('utf-8'), enjoy_question_9.encode('utf-8'), easy_to_follow_question_9.encode('utf-8'), comment_9.encode('utf-8'), useful_question_10.encode('utf-8'), enjoy_question_10.encode('utf-8'), easy_to_follow_question_10.encode('utf-8'), comment_10.encode('utf-8'),
        useful_question_11.encode('utf-8'), enjoy_question_11.encode('utf-8'), easy_to_follow_question_11.encode('utf-8'), comment_11.encode('utf-8'), useful_question_12.encode('utf-8'), enjoy_question_12.encode('utf-8'), easy_to_follow_question_12.encode('utf-8'), comment_12.encode('utf-8')]

# now json data is in DataFrame, let's see it.
# print(jsons_data)

#Convert DataFrame to a csv file.
jsons_data.to_csv('Experiment_OutputData.csv', index=False)
