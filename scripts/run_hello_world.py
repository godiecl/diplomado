#  Copyright (c) 2025. Diplomado en Inteligencia Artificial Aplicada
import logging
import random
import time

from tqdm import tqdm

from benchmark import benchmark
from logger import configure_logging


def main():
    with benchmark("esta es la medicion uno", log):
        time.sleep(1.5)
        log.debug("Hello World 😊")
        time.sleep(0.5)
        log.warning("Hello World 😊")

    with benchmark("esta es la medicion dos", log):
        log.info("Hello World 😊")
        time.sleep(0.5)
        log.error("Hello World 😊")
        log.critical("Hello World 😊")
        log.fatal("Hello World 😊")

    for i in tqdm(range(10_000), ncols=120):
        sleep = random.uniform(0.01, 0.2)
        time.sleep(sleep)


if __name__ == "__main__":
    configure_logging(log_level=logging.DEBUG)

    log = logging.getLogger(__name__)

    with benchmark("main()", log):
        main()
