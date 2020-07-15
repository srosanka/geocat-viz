def add_lat_lon_ticklabels(ax, zero_direction_label=False, dateline_direction_label=False):
    """
    Utility function to make plots look like NCL plots by using latitude, longitude tick labels

    Args:

        ax (:class:`matplotlib.axes._subplots.AxesSubplot` or :class:`cartopy.mpl.geoaxes.GeoAxesSubplot`):
            Current axes to the current figure

        zero_direction_label (:class:`bool`):
            Set True to get 0 E / O W or False to get 0 only.

        dateline_direction_label (:class:`bool`):
            Set True to get 180 E / 180 W or False to get 180 only.
    """
    from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter

    lon_formatter = LongitudeFormatter(zero_direction_label=zero_direction_label,
                                       dateline_direction_label=dateline_direction_label)
    lat_formatter = LatitudeFormatter()
    ax.xaxis.set_major_formatter(lon_formatter)
    ax.yaxis.set_major_formatter(lat_formatter)


def add_major_minor_ticks(ax, x_minor_per_major=3, y_minor_per_major=3, labelsize="small"):
    """
    Utility function to make plots look like NCL plots by adding minor and major tick lines

    Args:

        ax (:class:`matplotlib.axes._subplots.AxesSubplot` or :class:`cartopy.mpl.geoaxes.GeoAxesSubplot`):
            Current axes to the current figure

        x_minor_per_major (:class:`int`):
            Number of minor ticks between adjacent major ticks on x-axis

        y_minor_per_major (:class:`int`):
            Number of minor ticks between adjacent major ticks on y-axis
    """
    import matplotlib.ticker as tic

    ax.tick_params(labelsize=labelsize)
    ax.minorticks_on()
    ax.xaxis.set_minor_locator(tic.AutoMinorLocator(n=x_minor_per_major))
    ax.yaxis.set_minor_locator(tic.AutoMinorLocator(n=y_minor_per_major))

    # length and width are in points and may need to change depending on figure size etc.
    ax.tick_params(
        "both",
        length=8,
        width=0.9,
        which="major",
        bottom=True,
        top=True,
        left=True,
        right=True,
    )
    ax.tick_params(
        "both",
        length=4,
        width=0.4,
        which="minor",
        bottom=True,
        top=True,
        left=True,
        right=True,
    )


def set_titles_and_labels(ax, maintitle=None, maintitlefontsize=18, lefttitle=None, lefttitlefontsize=18, righttitle=None, righttitlefontsize=18,
                          xlabel=None, ylabel=None, labelfontsize=16):
    """
    Utility function to handle axis titles, left/right aligned titles, and labels as they appear in NCL plots.

    The intent of this function is to help make the plot look like an NCL plot as well as to help developers use only
    this convenience function instead of multiple matplotlib.axes.Axes functions, when applicable.

    (1) If no lefttitle and righttitle is set, maintitle is placed just top to the axes as follows:

                     maintitle
     ___________________________________________
    |                   Axes                    |
    |                                           |

    (2) If any of lefttitle or righttitle is set, lefttitle and righttitle are placed into a row that is just top to the axes, and maintitle is placed to top of
    the row of lefttitle/righttitle as follows:

                     maintitle
     lefttitle                        righttitle
     ___________________________________________
    |                   Axes                    |
    |                                           |

    Args:

        ax (:class:`matplotlib.axes._subplots.AxesSubplot` or :class:`cartopy.mpl.geoaxes.GeoAxesSubplot`):
            Current axes to the current figure

        maintitle (:class:`str`):
            Text to use for the maintitle.

        maintitlefontsize (:class:`int`):
            Text font size for maintitle. A default value of 18 is used if nothing is set.

        lefttitle (:class:`str`):
            Text to use for an optional left-aligned title, if any. For most plots, only a maintitle is enough,
            but for some plot types, a lefttitle likely with a right-aligned title, righttitle, can be used together.

        lefttitlefontsize (:class:`int`):
            Text font size for lefttitle. A default value of 18 is used if nothing is set.

        righttitle (:class:`str`):
            Text to use for an optional right-aligned title, if any. For most plots, only a maintitle is enough,
            but for some plot types, a righttitle likely with a left-aligned title, lefttitle, can be used together.

        righttitlefontsize (:class:`int`):
            Text font size for righttitle. A default value of 18 is used if nothing is set.

        xlabel (:class:`str`):
            Text for the x-axis label.

        ylabel (:class:`str`):
            Text for the y-axis label.

        labelfontsize (:class:`int`):
            Text font size for x- and y-axes. A default value of 16 is used if nothing is set.
    """

    if maintitle is not None:
        if lefttitle is not None or righttitle is not None:
            ax.set_title(maintitle, fontsize=maintitlefontsize + 2, y=1.12)
        else:
            ax.set_title(maintitle, fontsize=maintitlefontsize, y=1.04)

    if lefttitle is not None:
        ax.set_title(lefttitle, fontsize=lefttitlefontsize, y=1.04, loc='left')

    if righttitle is not None:
        ax.set_title(righttitle, fontsize=righttitlefontsize, y=1.04, loc='right')

    if xlabel is not None:
        ax.set_xlabel(xlabel, fontsize=labelfontsize)

    if ylabel is not None:
        ax.set_ylabel(ylabel, fontsize=labelfontsize)


def set_axes_limits_and_ticks(ax, xlim=None, ylim=None, xticks=None, yticks=None, xticklabels=None, yticklabels=None):
    """
    Utility function to determine axis limits, tick values and labels

    The intent of this function is to help developers use only this convenience function instead of multiple
    matplotlib.axes.Axes functions, when applicable.

    Args:

        ax (:class:`matplotlib.axes._subplots.AxesSubplot` or :class:`cartopy.mpl.geoaxes.GeoAxesSubplot`):
            Current axes to the current figure

        xlim (:class:`tuple`):
            Should be given as a tuple of numeric values (left, right), where left and right are the left and right
            x-axis limits in data coordinates. Passing None for any of them leaves the limit unchanged. See Matplotlib
            documentation for further information.

        ylim (:class:`tuple`):
            Should be given as a tuple of numeric values (left, right), where left and right are the left and right
            y-axis limits in data coordinates. Passing None for any of them leaves the limit unchanged. See Matplotlib
            documentation for further information.

        xticks (:class:`list`):
            List of x-axis tick locations. See Matplotlib documentation for further information.

        yticks (:class:`list`):
            List of y-axis tick locations. See Matplotlib documentation for further information.

        xticklabels (:class:`list[str]`):
            List of string labels for x-axis ticks. See Matplotlib documentation for further information.

        yticklabels (:class:`list[str]`):
            List of string labels for y-axis ticks. See Matplotlib documentation for further information.
    """

    if xticks is not None:
        ax.set_xticks(xticks)

    if yticks is not None:
        ax.set_yticks(yticks)

    if xticklabels is not None:
        ax.set_xticklabels(xticklabels)

    if yticklabels is not None:
        ax.set_yticklabels(yticklabels)

    if xlim is not None:
        ax.set_xlim(xlim)

    if ylim is not None:
        ax.set_ylim(ylim)


def truncate_colormap(cmap, minval=0.0, maxval=1.0, n=100, name=None):
    """
    Utility function that truncates a colormap.
    Registers the new colormap by name in plt.cm, and also returns the updated map.

    Copied from  https://stackoverflow.com/questions/18926031/how-to-extract-a-subset-of-a-colormap-as-a-new-colormap-in-matplotlib

    Args:

        cmap (:class:`matplotlib.colors.Colormap`):
            Colormap to be truncated.

        minval (:class:`int` or :class:`float`):
            Minimum value to be used for truncation of the color map.

        maxval (:class:`int` or :class:`float`):
            Maximum value to be used for truncation of the color map.

        n (:class:`int`):
            Number of color values in the new color map.

        name (:class:`str`):
            Optional name of the new color map. If not set, a new name is generated by using the name of the input
            colormap as well as min and max values.
    """
    import numpy as np
    import matplotlib as mpl
    from matplotlib import cm

    if not name:
        name = "trunc({n},{a:.2f},{b:.2f})".format(n=cmap.name, a=minval, b=maxval)
    new_cmap = mpl.colors.LinearSegmentedColormap.from_list(
        name=name,
        colors=cmap(np.linspace(minval, maxval, n)),
    )
    cm.register_cmap(name, new_cmap)
    return new_cmap


def xr_add_cyclic_longitudes(da, coord):
    """
    Utility function to handle the no-shown-data artifact of 0 and 360-degree longitudes

    Args:

        da (:class:`xarray.core.dataarray.DataArray`):
            Data array that contains one or more coordinates, strictly including the coordinate with the name
            given with the "coord" parameter.

        coord (:class:`str`):
            Name of the longitude coordinate within "da" data array.
    """

    import xarray as xr
    import cartopy.util as cutil

    cyclic_data, cyclic_coord = cutil.add_cyclic_point(da.values, coord=da[coord])

    coords = da.coords.to_dataset()
    coords[coord] = cyclic_coord

    new_da = xr.DataArray(cyclic_data, dims=da.dims, coords=coords.coords, attrs=da.attrs)
    new_da.encoding = da.encoding

    return new_da


def plotCLabels(da, contours, transform, ax, proj, Clevels=[], lowClevels=[], highClevels=[], rfs=14, efs=22, whitebbox=False,
                rHorizontal=False, eHorizontal=True):

    """
    Utility function to plot contour labels. Regular contour labels will be plotted using the built-in matplotlib
    clabel function. High/Low contour labels will be plotted using text boxes for more accurate label values 
    and placement.

    Args:

        da: (:class:`xarray.DataArray`):
            Xarray data array containing the lat, lon, and field variable data values.

        contours (:class:`cartopy.mpl.contour.GeoContourSet`):
            Contour set that is being labeled.

        transform (:class:`cartopy._crs`):
            Instance of CRS that represents the source coordinate system of coordinates.
            (ex. ccrs.Geodetic()).

        ax (:class:`matplotlib.pyplot.axis`):
            Axis containing the contour set.

        proj (:class:`cartopy.crs`):
            Projection 'ax' is defined by.
            This is the instaance of CRS that the coordinates will be transformed to.

        Clevels (:class:`list`):
            List of coordinate tuples in GPS form (lon in degrees, lat in degrees)
            that specify where the contours with regular field variable values should be plotted.

        lowClevels (:class:`list`):
            List of coordinate tuples in GPS form (lon in degrees, lat in degrees)
            that specify where the contours with low field variable values should be plotted.

        highClevels (:class:`list`):
            List of coordinate tuples in GPS form (lon in degrees, lat in degrees)
            that specify where the contours with high field variable values should be plotted.

        rfs (:class:`int`):
            Font size of regular contour labels.

        efs (:class:`int`):
            Font size of extrema contour labels.

        rHorizontal (:class:`bool`):
            Setting this to "True" will cause the regular contour labels to be horizontal.

        eHorizontal (:class:`bool`):
            Setting this to "True" will cause the extrema contour labels to be horizontal.
        
        whitebbox (:class:`bool`):
            Setting this to "True" will cause all labels to be plotted with white backgrounds

    Returns:

        allLabels (:class:`list`):
            List of text instances of all contour labels

    """

    import numpy as np
    import matplotlib.pyplot as plt

    # Create array of coordinates in the same shape as field variable data
    # so each coordinate can be easily mapped to its data value.
    coordarr = []
    for y in np.array(da.lat):
        temparr = []
        for x in np.array(da.lon):
            temparr.append((x, y))
        coordarr.append(temparr)
    coordarr = np.array(coordarr)

    # Initialize empty array that will be filled with contour label text objects and returned
    allLabels = []

    # Plot any regular contour levels
    if Clevels != []:
        clevelpoints = proj.transform_points(transform,
                                             np.array([x[0] for x in Clevels]),
                                             np.array([x[1] for x in Clevels]))
        transformedClevels = [(x[0], x[1]) for x in clevelpoints]
        ax.clabel(contours, manual=transformedClevels, inline=True, fontsize=rfs, colors='k', fmt="%.0f")
        [allLabels.append(txt) for txt in contours.labelTexts]
        if rHorizontal == True:
            [allLabels.set_rotation('horizontal') for txt in contours.labelTexts]

    # Plot any low contour levels
    if lowClevels != []:
        clevelpoints = proj.transform_points(transform,
                                             np.array([x[0] for x in lowClevels]),
                                             np.array([x[1] for x in lowClevels]))
        transformedLowClevels = [(x[0], x[1]) for x in clevelpoints]
        for x in range(len(transformedLowClevels)):
            try:
                # Find field variable data at that coordinate
                coord = lowClevels[x]
                for z in range(len(coordarr)):
                    for y in range(len(coordarr[z])):
                        if coordarr[z][y][0] == coord[0] and coordarr[z][y][1] == coord[1]:
                            p = int(round(da.data[z][y]))

                lab = plt.text(transformedLowClevels[x][0], transformedLowClevels[x][1], "L$_{" + str(p) + "}$", fontsize=efs,
                         horizontalalignment='center', verticalalignment='center')
                if eHorizontal == True:
                    lab.set_rotation('horizontal')
                allLabels.append(lab)
            except:
                continue

    # Plot any high contour levels
    if highClevels != []:
        clevelpoints = proj.transform_points(transform,
                                             np.array([x[0] for x in highClevels]),
                                             np.array([x[1] for x in highClevels]))
        transformedHighClevels = [(x[0], x[1]) for x in clevelpoints]
        for x in range(len(transformedHighClevels)):
            try:
                # Find field variable data at that coordinate
                coord = highClevels[x]
                for z in range(len(coordarr)):
                    for y in range(len(coordarr[z])):
                        if coordarr[z][y][0] == coord[0] and coordarr[z][y][1] == coord[1]:
                            p = int(round(da.data[z][y]))

                lab = plt.text(transformedHighClevels[x][0], transformedHighClevels[x][1], "H$_{" + str(p) + "}$", fontsize=efs,
                         horizontalalignment='center', verticalalignment='center')
                if eHorizontal == True:
                    lab.set_rotation('horizontal')
                allLabels.append(lab)
            except:
                continue

    if whitebbox == True:
        [txt.set_bbox(dict(facecolor='w', edgecolor='none', pad=2)) for txt in allLabels]

    return allLabels

###############################################################################
#
# The following functions are deprecated and should eventually be removed
#
###############################################################################


def nclize_axis(ax, minor_per_major=3):
    """
    Utility function to make plots look like NCL plots

    Deprecated, use `add_major_minor_ticks` instead
    """
    import warnings
    warnings.simplefilter('always', DeprecationWarning)
    warnings.warn('geocat.viz.util.nclize_axis: This function has been '
                  'deprecated, please use geocat.viz.util.add_major_minor_ticks'
                  ' instead.', DeprecationWarning, stacklevel=2)
    warnings.filters.pop(0)

    add_major_minor_ticks(ax, x_minor_per_major=minor_per_major, y_minor_per_major=minor_per_major)


def make_byr_cmap():
    """
    Define the byr colormap
    Note: this will be replaced with cmaps.BlueYellowRed
    """
    from . import cmaps

    import warnings
    warnings.simplefilter('always', DeprecationWarning)
    warnings.warn('geocat.viz.util.make_byr_cmap: This function has been '
                  'deprecated, please use geocat.viz.cmaps.BlueYellowRed '
                  'instead.', DeprecationWarning, stacklevel=2)
    warnings.filters.pop(0)

    return cmaps.BlueYellowRed
