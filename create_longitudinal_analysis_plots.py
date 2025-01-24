import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

def plot_horizontal_bars(sql_query: str, fig_name: str, shareyaxis: bool = False):
    connection = sqlite3.connect('data/kaggle_survey.db')
    response_counts = pd.read_sql(sql_query, con=connection)
    connection.close()
    plt.style.use('seaborn-v0_8-darkgrid')
    fig, axes = plt.subplots(ncols=3, figsize=(32,8),sharey=shareyaxis)
    
    survey_years = [2020, 2021, 2022]
    for i in range(len(survey_years)):
        survey_year = survey_years[i]
        response_counts_year = response_counts[response_counts['surveyed_in'] == survey_year]
        y = response_counts_year['responses'].values
        width = response_counts_year['response_count'].values
        for j in range(len(y)):
            axes[i].barh(y=y[j], width=width[j], color=plt.cm.YlGnBu(width[j] / max(width)))
            axes[i].set_title(f'{survey_year}')
    plt.tight_layout()
    fig.savefig(f'{fig_name}.png')


# which title most similar to your current role, 2020:Q5/2021:Q5/2022:Q23
sql_query = '''
SELECT surveyed_in,
       question_type,
       responses,
       response_count
  FROM aggregated_responses
 WHERE (question_index = 'Q5' AND surveyed_in IN (2020,2021)) OR
       (question_index = 'Q23' AND surveyed_in = 2022)
ORDER BY surveyed_in, response_count;
'''
plot_horizontal_bars(sql_query, fig_name='plot1_data_science_job_titles')

# activities make up an important part of your role, 2020:Q23/2021:Q24/2022:Q28
sql_query = '''
SELECT surveyed_in,
       question_type,
       responses,
       response_count
  FROM aggregated_responses
 WHERE (question_index = 'Q23' AND surveyed_in = 2020) OR
       (question_index = 'Q24' AND surveyed_in = 2021) OR
       (question_index = 'Q28' AND surveyed_in = 2022)
ORDER BY surveyed_in, response_count;
'''
plot_horizontal_bars(sql_query, fig_name='plot2_data_science_job_tasks',shareyaxis=True)

# programming language use on regular basis, 2020:Q7/2021:Q7/2022:Q12
sql_query = '''
SELECT surveyed_in,
       question_type,
       responses,
       response_count
  FROM aggregated_responses
 WHERE (question_index = 'Q7' AND surveyed_in IN (2020,2021)) OR
       (question_index = 'Q12' AND surveyed_in = 2022)
ORDER BY surveyed_in, response_count;
'''
plot_horizontal_bars(sql_query, fig_name='plot3_data_science_job_programming_languages')

# big data products used most often, 2020:Q29A/2021:Q32A/2022:Q35
sql_query = '''
SELECT surveyed_in,
       question_type,
       responses,
       response_count
  FROM aggregated_responses
 WHERE (question_index = 'Q29A' AND surveyed_in = 2020) OR
       (question_index = 'Q32A' AND surveyed_in = 2021) OR
       (question_index = 'Q35' AND surveyed_in = 2022)
ORDER BY surveyed_in, response_count;
'''
# print(response_counts)
plot_horizontal_bars(sql_query, fig_name='plot4_data_science_job_databasees')

# visualization libraries/tools used on regular basis, 2020:Q14/2021:Q14/2022:Q15
sql_query = '''
SELECT surveyed_in,
       question_type,
       responses,
       response_count
  FROM aggregated_responses
 WHERE (question_index = 'Q14' AND surveyed_in IN (2020,2021)) OR
       (question_index = 'Q15' AND surveyed_in = 2022)
ORDER BY surveyed_in, response_count;
'''
plot_horizontal_bars(sql_query, fig_name='plot5_data_science_job_visualizations')

# ML algorithms used on regular basis, 2020:Q17/2021:Q17/2022:Q18
sql_query = '''
SELECT surveyed_in,
       question_type,
       responses,
       response_count
  FROM aggregated_responses
 WHERE (question_index = 'Q17' AND surveyed_in IN (2020,2021)) OR
       (question_index = 'Q18' AND surveyed_in = 2022)
ORDER BY surveyed_in, response_count;
'''
plot_horizontal_bars(sql_query, fig_name='plot6_data_science_job_machine_learnings')