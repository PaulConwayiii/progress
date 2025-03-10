# -*- coding: utf-8 -*-

# Copyright (c) 2012 Georgios Verigakis <verigak@gmail.com>
#
# Permission to use, copy, modify, and distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

from __future__ import unicode_literals
from typing import Tuple
from . import Infinite, Progress


class Counter(Infinite):
    def update(self) -> None:
        message = self.message % self
        line = ''.join([message, str(self.index)])
        self.writeln(line)


class Countdown(Progress):
    def update(self) -> None:
        message = self.message % self
        line = ''.join([message, str(self.remaining)])
        self.writeln(line)


class Stack(Progress):
    phases: Tuple[str, ...] = (' ', '▁', '▂', '▃', '▄', '▅', '▆', '▇', '█')

    def update(self) -> None:
        nphases = len(self.phases)
        i = min(nphases - 1, int(self.progress * nphases))
        message = self.message % self
        line = ''.join([message, self.phases[i]])
        self.writeln(line)


class Pie(Stack):
    phases: Tuple[str,...] = ('○', '◔', '◑', '◕', '●')
