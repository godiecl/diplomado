#  Copyright (c) 2025. Diplomado en Inteligencia Artificial Aplicada
import logging

import pandas as pd
from ydata_profiling import ProfileReport

from benchmark import benchmark
from logger import configure_logging


def main():
    iris_datafile = "../data/iris.csv"
    log.debug(f"Reading file: {iris_datafile} ..")

    with benchmark("reading()", log):
        df = pd.read_csv(iris_datafile)
    log.debug(f"Data readed: {df}.")

    log.debug(f"Head of data:\n{df.head()}")

    log.debug(f"Describe:\n {df.describe()}")

    log.debug("Profiling .. ")
    with benchmark("profiling()", log):
        profile = ProfileReport(df, title="Iris Dataset")
    profile.to_file("../output/iris.html")

    log.debug("Done.")


if __name__ == "__main__":
    configure_logging(log_level=logging.DEBUG)

    log = logging.getLogger(__name__)

    with benchmark("main()", log):
        main()
