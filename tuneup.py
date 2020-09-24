#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tuneup assignment

Use the timeit and cProfile libraries to find bad code.
"""

__author__ = """Anie Cross with help from instructor demo recordings,
Group-B discussion topics, Google search, docs.python.org, stackoverflow.com,
Completed with plenty of help from Tutors H.Post, M.Boring"""

import cProfile
import pstats
import functools
import timeit
from collections import Counter


def profile(func):
    """A cProfile decorator function that can be used to
    measure performance.
    """
    def profile_func(*args, **kwargs):
        profiler = cProfile.Profile()
        try:
            profiler.enable()
            result = func(*args, **kwargs)
            profiler.disable()
            return result
        finally:
            ps = pstats.Stats(profiler).sort_stats(pstats.SortKey.CUMULATIVE)
            ps.print_stats()
    return profile_func


def read_movies(src):
    """Returns a list of movie titles."""
    print(f'Reading file: {src}')
    with open(src, 'r') as f:
        return f.read().splitlines()


def is_duplicate(title, movies):
    """Returns True if title is within movies list."""
    for movie in movies:
        if movie == title:
            return True
    return False


@profile
def find_duplicate_movies(src):
    """Returns a list of duplicate movies from a src list."""
    movies = read_movies(src)
    duplicates = Counter()
    for movie in movies:
        duplicates[movie] += 1
    return duplicates


def timeit_helper(func):
    """Part A: Obtain some profiling measurements using timeit."""
    t = timeit.Timer(stmt=func)
    results = t.repeat(repeat=7, number=5)
    min_value = min([result/5 for result in results])
    print("Best time across 7 repeats of 5 runs per repeat: ", min_value)
    pass


def main():
    """Computes a list of duplicate movie entries."""
    dups = []
    result = find_duplicate_movies('movies.txt')
    for k, v in result.items():
        if v > 1:
            dups.append(k)
    print(f'Found {len(dups)} duplicate movies:')
    print('\n'.join(dups))


if __name__ == '__main__':
    timeit_helper(main)
