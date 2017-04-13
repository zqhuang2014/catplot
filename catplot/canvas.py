#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from matplotlib.spines import Spine

import catplot.descriptors as dc


class Canvas(object):
    """ Canvas abstract base class.

    Parameters:
    -----------
    margin_ratio: float, optional, default is 0.1
        control the white space between energy profile line and axes.

    figsize : tuple of integers, optional, default: None
        width, height in inches. If not provided, defaults to rc figure.figsize.

    dpi : integer, optional, default: None
        resolution of the figure. If not provided, defaults to rc figure.dpi.

    facecolor : str, optional
        the background color. If not provided, defaults to rc figure.facecolor

    edgecolor : str, optional
        the border color. If not provided, defaults to rc figure.edgecolor

    x_ticks : float list
        set the x ticks with a list of ticks.

    y_ticks : float list
        set the y ticks with a list of ticks.

    """
    margin_ratio = dc.MarginRatio("margin_ratio")

    def __init__(self, **kwargs):
        self.margin_ratio = kwargs.pop("margin_ratio", 0.1)
        self.figsize = kwargs.pop("figsize", None)
        self.dpi = kwargs.pop("dpi", None)
        self.facecolor = kwargs.pop("facecolor", None)
        self.edgecolor = kwargs.pop("edgecolor", None)
        self.x_ticks = kwargs.pop("x_ticks", None)
        self.y_ticks = kwargs.pop("y_ticks", None)

        # Create a figure.
        self.figure = plt.figure(figsize=self.figsize,
                                 dpi=self.dpi)

        # Add an axes to figure.
        # NOTE: here we use the canvas facecolor as the axes facecolor.
        self.axes = self.figure.add_subplot(111, facecolor=self.facecolor)

        # Change the spine color of axes.
        if self.edgecolor:
            for child in self.axes.get_children():
                if isinstance(child, Spine):
                    child.set_color(self.edgecolor)

        # Set axe ticks.
        if self.x_ticks is not None:
            self.axes.set_xticks(self.x_ticks)
        if self.y_ticks is not None:
            self.axes.set_yticks(self.y_ticks)

