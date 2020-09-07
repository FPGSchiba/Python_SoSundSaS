import threading
from Functions.ScanHardware import *
import matplotlib.pyplot as plt
import time

plt.ion()


class DynamicUpdate:
    def close(self):
        self.closing = True

    def on_launch(self):
        # Set up plot
        self.figure, self.ax = plt.subplots()
        self.lines, = self.ax.plot([], [], 'o')
        self.on_TimeUp()
        self.closing = False
        # Other stuff
        ...

    def on_TimeUp(self):
        self.minx = 0
        self.maxx = 60
        self.miny = 0
        self.maxy = DISK_Max()
        # Autoscale on unknown axis and known lims on the other
        self.ax.set_autoscaley_on(False)
        self.ax.set_xlim(self.minx, self.maxx)
        self.ax.set_ylim(self.miny, self.maxy)
        self.ax.grid()

    def on_running(self, xdata, ydata):
        # Update data (with the new _and_ the old points)
        self.lines.set_xdata(xdata)
        self.lines.set_ydata(ydata)
        plt.plot(xdata, ydata, 'b-')
        # Need both of these in order to rescale
        self.ax.relim()
        self.ax.autoscale_view()
        # We need to draw *and* flush
        self.figure.canvas.draw()
        self.figure.canvas.flush_events()

    # Example
    def __call__(self):
        self.on_launch()
        xdata = []
        ydata = []
        while not self.closing:
            t = time.localtime()
            current_time = int(time.strftime("%S", time.localtime()))
            if current_time == 0 or current_time == 1:
                xdata.clear()
                ydata.clear()
                plt.cla()
                self.on_TimeUp()
            xdata.append(current_time)
            ydata.append(DISK_Free())
            self.on_running(xdata, ydata)
            time.sleep(1)


d = DynamicUpdate()


def Init():
    d()


def CloseDashboard():
    d.close()