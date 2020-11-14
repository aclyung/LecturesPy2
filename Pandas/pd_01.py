import pandas as pd
from IPython.display import display

dict_a = {"age": [21, 32, 29, 25], "name": ["Jack", "Daniel", "Tomas",
                                            "Gary"], "Career": ["Student", "Doctor", "Teacher", "Developer"]}
df = pd.DataFrame(
    dict_a, index=pd.MultiIndex.from_tuples([("서울", 1), ("서울", 2), ("경기", 1), ("경기", 2)], names=["Resident", "No."]))
display(pd.DataFrame(df))
