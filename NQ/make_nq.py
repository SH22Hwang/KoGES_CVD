import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rc

# 기본 글꼴을 NanumGothic으로 변경
rc("font", family="NanumGothic")

AS1_01_EXAMINEE = pd.read_csv("./AS1_01_EXAMINEE.csv", index_col=0)
AS1_03_DRSM = pd.read_csv("./AS1_03_DRSM.csv", index_col=0)
AS1_17_FFQWEIGHT = pd.read_csv("AS1_17_FFQWEIGHT.csv", index_col=0)

df = pd.DataFrame(index=AS1_01_EXAMINEE.index)

sex_age = AS1_01_EXAMINEE.loc[["AS1_Sex", "AS1_Age"]]
drink = AS1_03_DRSM.loc[["AS1_Drink", "AS1_TotAlc"]]

pd.concat([df, sex_age, drink, AS1_17_FFQWEIGHT])

pd.to_csv(df, "./유")
