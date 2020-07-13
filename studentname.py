import numpy as np
import pandas as pd
import sqlite3
from sqlalchemy import create_engine

disk_engine = create_engine('sqlite:///db.sqlite3')
df2 = pd.read_sql_table('posts_processedmarks', disk_engine)
processed_id=16
rowsfind = df2.loc[df2['id'] == processed_id]

sname = rowsfind.iat[0, 5]
print(sname)
output_image = rowsfind.iat[0, 4]
attact_file = 'media/' + output_image
print(attact_file)