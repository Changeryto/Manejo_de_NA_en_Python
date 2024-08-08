#!../../env/bin/python
import pandas as pd

# Para borrar en caso de su existencia a .missing
try:
    del pd.DataFrame.missing
except:
    pass



# Extension para manejar numeros no disponibles

@pd.api.extensions.register_dataframe_accessor("missing") # Acceso para los dataframes de pandas
class MissingMethods:
    def __init__(self, pandas_obj):
        self._df = pandas_obj

    def na_full_count(self):
        return self._df.isna().sum().sum()

    def not_na_full_count(self):
        return self._df.size - self._df.missing.na_full_count()

    def na_proportion(self):
        return (self.na_full_count() / self._df.size)


# Para crear un Data Frame que pueda rescatarse

DF_TEST_MISSIGN = pd.DataFrame.from_dict(
    data = {
        "a": list("asdafsdafa"),
        "b": range(0, 10)
    }
    )
DF_TEST_MISSIGN.iloc[2:5, 0] = None
DF_TEST_MISSIGN.iloc[6:7, 1] = None

if __name__ == "__main__":
    print("Probando la extension")
    print(DF_TEST_MISSIGN.missing.na_proportion())





