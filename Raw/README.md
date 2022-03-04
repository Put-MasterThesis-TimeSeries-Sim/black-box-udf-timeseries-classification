# spark-udf-characteristics

The structure of the data:
* `filtration` - function type
    * `filterCatalogSalesWhereProfitNegative` - function name
      * `CPU-data-vol-1GB-5nodes`
        * `mean_data.csv` - file with mean data
        * `translated_scaled_smoothed_data.csv` - file with translated and scaled data
        * `mean_CPU.png` - mean CPU plot
        * `source data` - folder with raw, source data
          * `node-11` - folders representing data from specific nodes
            * `08_08_2021_02_00_04.csv` - raw data files date_time.csv
            * `...`
          * `node-12`
          * `...`
      * `CPU-data-vol-1GB-7nodes`
      * `CPU-data-vol-1GB-9nodes`
      * `...`
  