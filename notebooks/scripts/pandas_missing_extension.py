#!../../env/bin/python
import numpy as np
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
        """Returns the total of NAs in the whole Data Frame, or of one variable if is given"""
        if len(var) == 0:
            return self._df.isna().sum().sum()
        elif len(var) > 1:
            raise ValueError(f"Use only one valid variable name of Data Frame")
        else:
            return self._df[var[0]].isna().sum()

    def na_proportion(self, *var):
        """Returns the proportion (from 0 to 1) of NAs in the whole the Data Frame, or of one variable if is given"""
        if len(var) == 0:
            return (self.na_count() / self._df.size)
        elif len(var) > 1:
            raise ValueError(f"Use only one valid variable name of Data Frame")
        else:
            return self.na_count(var[0]) / self._df.shape[0]
    
    def na_percentage(self, *var):
        """Returns the percentage (from 0 to 100) of NAs in the whole Data Frame, or of one variable if is given"""
        if len(var) == 0:
            return (self.na_proportion() * 100)
        elif len(var) > 1:
            raise ValueError(f"Use only one valid variable name of Data Frame")
        else:
            return self.na_proportion(var[0]) * 100

    def not_na_count(self, *var):
        """Returns the total of not NAs in the whole Data Frame, or of one variable if is given"""
        if len(var) == 0:
            return self._df.size - self._df.missing.na_count()
        elif len(var) > 1:
            raise ValueError(f"Use only one valid variable name of Data Frame")
        else:
            return self._df.shape[0] - self.na_count(var[0])
        

    def not_na_proportion(self, *var):
        """Returns the proportion (from 0 to 1) of not NAs in the whole the Data Frame, or of one variable if is given"""
        if len(var) == 0:
            return 1 - self.na_proportion()
        elif len(var) > 1:
            raise ValueError(f"Use only one valid variable name of Data Frame")
        else:
            return 1 - self.na_proportion(var[0])

    def not_na_percentage(self, *var):
        """Returns the percentage (from 0 to 100) of not NAs in the whole Data Frame, or of one variable if is given"""
        

        if len(var) == 0:
            return 100 - self.na_percentage()
        elif len(var) > 1:
            raise ValueError(f"Use only one valid variable name of Data Frame")
        else:
            return 100 - self.na_percentage(var[0])

    def variable_summary(self):
        """Returns a Pandas Data Frame with: variable (Name of each column), n_cases (Number of rows for each variable), n_nas (Number of NAs for each variable), n_not_na (Number of not NAs for each variable), na_proportion (proportion of not NAs for each variable), na_percentage (Percentage of NAs for each variable)"""
        return pd.DataFrame.from_dict({
            "variable": self._df.columns,
            "n_cases": self._df.shape[0],
            "n_na": self._df.isna().sum().to_numpy(),
            "n_not_na": self._df.notna().sum().to_numpy(),
            "na_proportion": (self._df.isna().sum().to_numpy() / self._df.shape[0]),
            "na_percentage": (self._df.isna().sum().to_numpy() / self._df.shape[0]) * 100
        })

    def na_summary(self):
        """Returns a Pandas Data Frame with: n_na (Number of NAs in any variable), n_variables (number of variables with that NAs), prop_of_vars (Proportion of variables with that number of NAs), prc_of_vars (Percentage of variables with that number of NAs)"""
        number_of_nas = np.arange(self.na_count())
        number_of_vars = np.zeros(self.na_count())
        for number in number_of_nas:
            for column in self._df.columns:
                if self._df.missing.na_count(column) == number:
                    number_of_vars[number] += 1
        proportion_of_vars = (number_of_vars / self._df.shape[1])
        percentage_of_vars = proportion_of_vars * 100

        table = pd.DataFrame.from_dict({
            "n_na": number_of_nas,
            "n_variables": number_of_vars,
            "prop_of_vars": proportion_of_vars,
            "prc_of_vars": percentage_of_vars,
        })

        return table[table.n_variables > 0]

    def row_summary(self):
        """Returns a Pandas Data Frame with: case (number of row), n_na (Number of NAs in case), prop_na (Proportion of NAs), prc_na (Percentage of NAs) """
        n_na = np.array([self._df.iloc[i].isna().sum() for i in range(self._df.shape[0]) ])
        n_not_na = np.array([self._df.iloc[i].notna().sum() for i in range(self._df.shape[0]) ])
        prop_na = n_na / (n_na + n_not_na)
        return pd.DataFrame.from_dict({
            "case": np.arange(self._df.shape[0]),
            "n_na": n_na,
            "n_not_na": n_not_na,
            "prop_na": prop_na,
            "prc_na": prop_na * 100
        })
        
        #return n_na
            

    def missing_case_summary(self):
        table = self.row_summary()
        return table[table.n_na > 0]




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
    print(DF_TEST_MISSIGN.missing.row_summary())





