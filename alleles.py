import pandas as pd
#надо покопаться с engine, чтобы он кушал xlsx, пока что лучше пересохранить в xls
donors = pd.read_excel ("/home/arus/Загрузки/Telegram Desktop/HLA for AKh.xls", engine = "xlrd", nrows = 19, index_col=0, keep_default_na=False ) 
h = int (input ("Введите то, до какого знака вы собираетесь обрезать аллель, целое число. Например, если вам нужно оставить первые значения (например, HLA-A1*02), введите 2, если вторые (HLA-A1*02*01) - 5, и т.д."))
donors = donors.apply(lambda x: pd.Series(x).str.slice_replace(h, repl=""))
y = str(input ("Введите ген в формате HLA-X1*, например, HLA-A1*"))
x = str(input("Введите аллель в формате XX, например 02"))
donors.index [donors[y]==x]
