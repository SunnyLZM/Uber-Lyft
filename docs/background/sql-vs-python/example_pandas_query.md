```python
import pandas as pd

contributions = pd.DataFrame()
committees = pd.DataFrame()

bush_cmte = committees[committees["Name"] == "Cori Bush for Congress"]

combined = contributions.join(committees, on="MECID", how="left")

totals = combined.groupby("City")[["Amount"]].sum().rename(columns={"sum": "Total"})

final = totals[totals["Total"] > 1000].sort_values(by="Total", ascending=False)
```
