import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# title most similar to your current role, 2020:Q5/2021:Q5/2022:Q23
connection = sqlite3.connect('data/kaggle_survey.db')
sql_query = '''
SELECT surveyed_in,
       question_type,
       responses,
       response_count
 FROM aggregated_responses
WHERE (question_index = 'Q5' AND surveyed_in IN (2020,2021)) OR
      (question_index = 'Q23' AND surveyed_in = 2022)
ORDER BY surveyed_in, response_count DESC;      
'''
response_counts = pd.read_sql(sql_query, con=connection)
connection.close()
# print(response_counts)

# activities make up an important part of your role, 2020:Q23/2021:Q24/2022:Q28
connection = sqlite3.connect('data/kaggle_survey.db')
sql_query = '''
SELECT surveyed_in,
       question_type,
       responses,
       response_count
 FROM aggregated_responses
WHERE (question_index = 'Q23' AND surveyed_in = 2020) OR
      (question_index = 'Q24' AND surveyed_in = 2021) OR
      (question_index = 'Q28' AND surveyed_in = 2022)
ORDER BY surveyed_in, response_count DESC;      
'''
response_counts = pd.read_sql(sql_query, con=connection)
connection.close()
# print(response_counts)

# programming language use on regular basis, 2020:Q7/2021:Q7/2022:Q12
connection = sqlite3.connect('data/kaggle_survey.db')
sql_query = '''
SELECT surveyed_in,
       question_type,
       responses,
       response_count
 FROM aggregated_responses
WHERE (question_index = 'Q7' AND surveyed_in IN (2020,2021)) OR
      (question_index = 'Q12' AND surveyed_in = 2022)
ORDER BY surveyed_in, response_count DESC;      
'''
response_counts = pd.read_sql(sql_query, con=connection)
connection.close()
# print(response_counts)

# big data products used most often, 2020:Q29A/2021:Q32A/2022:Q35
connection = sqlite3.connect('data/kaggle_survey.db')
sql_query = '''
SELECT surveyed_in,
       question_type,
       responses,
       response_count
 FROM aggregated_responses
WHERE (question_index = 'Q29A' AND surveyed_in = 2020) OR
      (question_index = 'Q32A' AND surveyed_in = 2021) OR
      (question_index = 'Q35' AND surveyed_in = 2022)
ORDER BY surveyed_in, response_count DESC;      
'''
response_counts = pd.read_sql(sql_query, con=connection)
connection.close()
# print(response_counts)

# visualization libraries/tools used on regular basis, 2020:Q14/2021:Q14/2022:Q15
connection = sqlite3.connect('data/kaggle_survey.db')
sql_query = '''
SELECT surveyed_in,
       question_type,
       responses,
       response_count
 FROM aggregated_responses
WHERE (question_index = 'Q14' AND surveyed_in IN (2020,2021)) OR
      (question_index = 'Q15' AND surveyed_in = 2022)
ORDER BY surveyed_in, response_count DESC;      
'''
response_counts = pd.read_sql(sql_query, con=connection)
connection.close()
# print(response_counts)

# ML algorithms used on regular basis, 2020:Q17/2021:Q17/2022:Q18
connection = sqlite3.connect('data/kaggle_survey.db')
sql_query = '''
SELECT surveyed_in,
       question_type,
       responses,
       response_count
 FROM aggregated_responses
WHERE (question_index = 'Q17' AND surveyed_in IN (2020,2021)) OR
      (question_index = 'Q18' AND surveyed_in = 2022)
ORDER BY surveyed_in, response_count DESC;      
'''
response_counts = pd.read_sql(sql_query, con=connection)
connection.close()
print(response_counts)
