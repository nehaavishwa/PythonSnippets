import pandas as p

filename = r'C:\PersonalProjects\PythonSnippets\YoungPeople\Files\responses.csv'

df = p.read_csv(filename, usecols={'Daily events', 'Prioritising workload', 'Writing notes', 'Workaholism',
       'Thinking ahead', 'Final judgement', 'Reliability', 'Keeping promises',
       'Loss of interest', 'Friends versus money', 'Funniness', 'Fake',
       'Criminal damage', 'Decision making', 'Elections', 'Self-criticism',
       'Judgment calls', 'Hypochondria', 'Empathy', 'Eating to survive',
       'Giving', 'Compassion to animals', 'Borrowed stuff', 'Loneliness',
       'Cheating in school', 'Health', 'Changing the past', 'God', 'Dreams',
       'Charity', 'Number of friends', 'Punctuality', 'Lying', 'Waiting',
       'New environment', 'Mood swings', 'Appearence and gestures',
       'Socializing', 'Achievements', 'Responding to a serious letter',
       'Children', 'Assertiveness', 'Getting angry',
       'Knowing the right people', 'Public speaking', 'Unpopularity',
       'Life struggles', 'Happiness in life', 'Energy levels',
       'Small - big dogs', 'Personality', 'Finding lost valuables',
       'Getting up', 'Interests or hobbies', r'''Parents' advice''',
       'Questionnaires or polls', 'Internet usage', 'Finances',
       'Shopping centres', 'Branded clothing', 'Entertainment spending','Spending on looks', 'Spending on gadgets',
       'Spending on healthy eating', 'Age', 'Height', 'Weight',
       'Number of siblings', 'Gender', 'Left - right handed', 'Education',
       'Only child', 'Village - town', 'House - block of flats'})
print(type(df))
print(df.shape, df.size, df.columns[:10])

