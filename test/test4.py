import pandas as pd

# csv新規作成
df = pd.DataFrame([],columns=['time', 'value'])
df.to_csv("/home/pi/sample1.csv")

# csv新規作成
df = pd.DataFrame([],columns=['time', 'r','l'])
df.to_csv("/home/pi/sample2.csv")
