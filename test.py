import bamboo as bm

# Turn asyncronous processing off
bm.set_async(False)

url = 'http://formhub.org/mberg/forms/good_eats/data.csv'
dataset = bm.Dataset.create()
dataset.import_from_url(url, na_values=['n/a'])
dataset.schema

# Resample monthly, 'M', aggregating by mean
date_column = 'submit_date'
monthly = ds.resample(date_column, 'M', 'mean').set_index(date_column)
monthly_amounts = monthly.amount.dropna()

# Plot the amount spent per month
mothly_amounts.plot()