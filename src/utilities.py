import matplotlib.pyplot as plt
# Function to plot the passband and stopband of a filter


def plot_band(ax, start, stop, color, alpha, label=None):
    hatch = None
    if stop < 0:
        neg_start = -start
        start = -stop
        stop = neg_start
        hatch = 'x'

    if start < 0:
        ax.axvspan(-start, stop, color=color, alpha=alpha)
        neg_start = -start
        start = 0
        stop = neg_start
        hatch = 'x'

    ax.axvspan(start, stop, color=color, alpha=alpha, hatch=hatch, label=label)


def plot_filter_response(fpass_low, fpass_high, fstop_low, fstop_high, f_max, title, color_mode='filter'):

    clr = dict()
    match color_mode:
        case 'filter':
            clr['pass'] = 'green'
            clr['trans'] = 'yellow'
            clr['stop'] = 'red'
        case 'image':
            clr['pass'] = 'brown'
            clr['trans'] = 'brown'
            clr['stop'] = 'grey'

    if not (fstop_low <= fpass_low <= fpass_high <= fstop_high):
        plt.text(0.5, 0.5, f"Unable to plot due to non-monotonic frequency spec {fstop_low}, {fpass_low}, {fpass_high}, {fstop_high}",
                 ha='center', va='center', fontsize=12, color='black')
        #raise Exception(f"Frequencies have tp be in correct order, not {fstop_low}, {fpass_low}, {fpass_high}, {fstop_high}")
        return "Error"

    ax = plt.gca()
    ax.axvspan(0, fstop_low, color=clr['stop'], alpha=0.3)
    plot_band(ax, fstop_low, fpass_low, color=clr['trans'], alpha=0.5)
    plot_band(ax, fpass_low, fpass_high, color=clr['pass'], alpha=0.5, label='Passband')
    plot_band(ax, fpass_high, fstop_high, color=clr['trans'], alpha=0.5, label='Transistionband')
    ax.axvspan(max(fstop_high,-fstop_high,-fpass_high,-fpass_low, -fstop_low), f_max, color=clr['stop'], alpha=0.3, label='Stopband')

    # Set labels and title
    ax.set_xlabel('Frequency (MHz)')
    ax.set_title(title)

    # Set limits and grid
    ax.set_xlim(0, f_max)
    ax.grid(True)

    # Add legend
    #ax.legend(loc='best', fontsize='small')

    return "Ok"
