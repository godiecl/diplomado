#  Copyright (c) 2025. Diplomado en Inteligencia Artificial Aplicada

import datetime
import logging
import time
from contextlib import contextmanager
from typing import Generator, Optional

import humanize


class Benchmark:
    def __init__(self, name=None):
        self.name = name

    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, ty, val, tb):
        elapsed = time.perf_counter() - self.start
        name = self.name if self.name else "Block"
        log.debug(f"{name} executed in {elapsed:.3f} seconds.")
        return False

    def __call__(self, func):
        def wrapped(*args, **kwargs):
            with self:
                return func(*args, **kwargs)
            return None

        return wrapped


@contextmanager
def benchmark(
    operation_name: Optional[str] = None, log: Optional[logging.Logger] = None
) -> Generator[None, None, None]:
    """Context manager to benchmark a block of code."""

    start: int = time.perf_counter_ns()
    try:
        yield
    finally:
        elapsed: int = time.perf_counter_ns() - start
        elapsed_microseconds = elapsed / 1_000
        delta = datetime.timedelta(microseconds=elapsed_microseconds)

        humanize_time = humanize.precisedelta(
            delta, minimum_unit="microseconds", format="%.2f"
        )

        if not log:
            log = logging.getLogger(__name__)

        if operation_name:
            log.debug(f"* {operation_name} executed in {humanize_time}.")
        else:
            log.debug(f"* executed in {humanize_time}.")
