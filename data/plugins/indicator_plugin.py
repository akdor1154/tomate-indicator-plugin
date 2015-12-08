from __future__ import unicode_literals

import logging

from tomate.constant import State
from tomate.event import Events, on
from tomate.graph import graph
from tomate.plugin import Plugin
from tomate.utils import suppress_errors

logger = logging.getLogger(__name__)


class IndicatorPlugin(Plugin):

    @suppress_errors
    def __init__(self):
        super(IndicatorPlugin, self).__init__()
        self.indicator = graph.get('tomate.indicator')

    @suppress_errors
    def activate(self):
        super(IndicatorPlugin, self).activate()
        self.idle_icon()

    @suppress_errors
    def deactivate(self):
        super(IndicatorPlugin, self).deactivate()
        self.default_icon()

    @suppress_errors
    @on(Events.Session, [State.stopped, State.started, State.reset])
    def default_icon(self, *args, **kwargs):
        self.indicator.set_icon('tomate-indicator')

        logger.debug('set defaul icon')

    def idle_icon(self, *args, **kwargs):
        self.indicator.set_icon('tomate-idle')

        logger.debug('set idle icon')

    @suppress_errors
    @on(Events.Timer, [State.changed])
    def update_icon(self, *args, **kwargs):
        percent = int(kwargs.get('time_ratio', 0) * 100)

        # The icons show 5% steps, so we have to round
        rounded_percent = percent - percent % 5

        # There is no icon for 100%
        if rounded_percent < 99:
            icon_name = 'tomate-{0:02}'.format(rounded_percent)
            self.indicator.set_icon(icon_name)

            logger.debug('set icon %s', icon_name)

    @suppress_errors
    @on(Events.Session, [State.finished])
    def attention_icon(self, *args, **kwargs):
        self.indicator.set_icon('tomate-attention')

        logger.debug('set attention icon')
