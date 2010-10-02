#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  evaluate_paths.py
#  simsearch
# 
#  Created by Lars Yencken on 03-09-2010.
#  Copyright 2010 Lars Yencken. All rights reserved.
#

"""
A script to generate statistics on a set of query traces (i.e. walks through
the kanji graph generated by simulated search).
"""

import os, sys, optparse

from simplestats import basic_stats

from simulate_search import TraceFile

def evaluate_paths(input_file, limit=5):
    print 'Evaluating paths from "%s"' % os.path.basename(input_file)
    traces = TraceFile.load(input_file)

    path_lengths = []
    successes = []
    for (query, target, path) in traces:
        if path and path[-1] == target:
            successes.append(path)
            path_lengths.append(len(path) - 1)
        else:
            path_lengths.append(limit)

    print u'Success rate: %d/%d (%.02f%%)' % (len(successes),
            len(traces), 100.0 * len(successes) / len(traces))

    print u'Mean path length: %.02f (σ = %.02f)' % basic_stats(path_lengths)

#----------------------------------------------------------------------------#

def _create_option_parser():
    usage = \
"""%prog [options] input_file

Generates evaluation statistics on a collection of traces."""

    parser = optparse.OptionParser(usage)

    return parser

def main(argv):
    parser = _create_option_parser()
    (options, args) = parser.parse_args(argv)

    if len(args) != 1:
        parser.print_help()
        sys.exit(1)

    input_file, = args
    evaluate_paths(input_file)

#----------------------------------------------------------------------------#

if __name__ == '__main__':
    main(sys.argv[1:])

# vim: ts=4 sw=4 sts=4 et tw=78: