#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-

import pytest


def test_correct_import_statement():
    from singlefile.gist.gist2eafebd9fdcb1e39188aeb1e3627e683.pingpong import main
    assert main() == 'eightnoteight'


def test_wrong_import_statement():
    for _ in range(5):  # loop over to see if
        with pytest.raises(ImportError):  # file not found error
            from singlefile.gist.gist2eafebd9fdcb1e39188aeb1e3627e683.pingpon import main

        with pytest.raises(ImportError):  # gist not found error
            from singlefile.gist.gist2eadasdadsadas.bam import main


def test_non_service_import_statement():
    with pytest.raises(ImportError):
        from singlefile.snippetworld.snip2345 import function
