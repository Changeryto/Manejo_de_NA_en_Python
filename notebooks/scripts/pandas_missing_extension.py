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

    def na_count(self, *var):
        """Returns the total of NAs in the whole Data Frame"""
        if len(var) == 0:
            return self._df.isna().sum().sum()
        elif len(var) > 1:
            raise ValueError(f"Use only one valid variable name of Data Frame")
        else:
            return self._df[var[0]].isna().sum()

    def na_proportion(self):
        """Returns the proportion (from 0 to 1) of NAs in the whole the Data Frame"""
        return (self.na_count() / self._df.size)
    
    def na_percentage(self):
        """Returns the percentage (from 0 to 100) of NAs in the whole Data Frame"""
        return (self.na_proportion() * 100)

    def not_na_count(self):
        """Returns the total of not NAs in the whole Data Frame"""
        return self._df.size - self._df.missing.na_count()

    def not_na_proportion(self):
        """Returns the proportion (from 0 to 1) of not NAs in the whole the Data Frame"""
        return 1 - self.na_proportion()

    def not_na_percentage(self):
        """Returns the percentage (from 0 to 100) of not NAs in the whole Data Frame"""
        return 100 - self.na_percentage()

    def variable_summary(self):
        """Returns a Pandas Data Frame with: variable (Name of each column), n_cases (Number of rows for each variable), n_nas (Number of NAs for each variable), n_availables (Number of not NAs for each variable), na_proportion (proportion of not NAs for each variable), na_percentage (Percentage of NAs for each variable)"""
        return pd.DataFrame.from_dict({
            "variable": self._df.columns,
            "n_cases": self._df.shape[0],
            "n_nas": self._df.isna().sum().to_numpy(),
            "n_availables": self._df.notna().sum().to_numpy(),
            "na_proportion": (self._df.isna().sum().to_numpy() / self._df.shape[0]),
            "na_percentage": (self._df.isna().sum().to_numpy() / self._df.shape[0]) * 100
        })

    def na_summary_table(self):
        """Returns a Pandas Data Frame with: n_na (Number of NAs in any variable), n_variables (number of variables with that NAs), percentage_of_vars (Percentage of variables with that number of NAs)"""





if __name__ == "__main__":
    # Para crear un Data Frame que pueda rescatarse

    DF_TEST_MISSIGN = pd.DataFrame.from_dict(
        data = {
            "a": list("asdafsdafa"),
            "b": range(0, 10)
        }
    )
    DF_TEST_MISSIGN.iloc[2:5, 0] = None
    DF_TEST_MISSIGN.iloc[6:7, 1] = None
    print("Probando la extension")





