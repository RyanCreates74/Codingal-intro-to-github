import numpy as np
import pandas as pd
exam_data = {'name': ['Ryan', 'Reyansh', 'Aaryan'], 
             'score': [8, 6, np.nan], 
             'attempts': [2, 5, 3], 
             'qualify': ['Yes', 'No', 'No']}
labels = ['a', 'b', 'c']
df = pd.DataFrame(exam_data, index = labels)
print(df.info())