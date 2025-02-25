import pandas as pd
from sodapy import Socrata

# Unauthenticated client only works with public data sets. Note 'None'
# in place of application token, and no username or password:
client = Socrata("data.cdc.gov", None)

# First 2000 results, returned as JSON from API / converted to Python list of
# dictionaries by sodapy.
results = client.get("ynw2-4viq", limit=2000)

# Convert to pandas DataFrame
results_df = pd.DataFrame.from_records(results)

# print(list(results_df.columns))
print(results_df.head())