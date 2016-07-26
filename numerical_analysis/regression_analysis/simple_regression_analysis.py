#!/usr/bin/env python
# -*- coding: utf-8 -*-#
from __future__ import division

import scipy.stats
import matplotlib.pyplot as plt
import numpy as np

def main():

	'''
	This example concerns the data set from the ordinary least squares article. 
	This data set gives average masses for women as a function of their height 
	in a sample of American women of age 30–39.
	'''

	x = [1.47, 1.50, 1.52, 1.55, 1.57, 1.60, 1.63, 1.65, 1.68, 1.70, 1.73, 1.75, 1.78, 1.80, 1.83]
	y = [52.21, 53.12, 54.48, 55.84, 57.20, 58.57, 59.93, 61.29, 63.11, 64.47, 66.28, 68.10, 69.92, 72.19, 74.46]


	# Step 1: regression analysis
	slope, intercept, r_value, p_value, std_err = scipy.stats.linregress(x,y)

	print "slop\t", slope
	print "intercept\t", intercept
	print "R-squared\t", r_value**2
	print "p-value\t", p_value	
	print "standard error\t", std_err

	# Step 2: plot the graph
	fig, ax = plt.subplots()

	# plot scatter
	ax.plot(x, y, 'bx', markersize=10)

	# plot the straight line
	new_x = np.linspace(min(x), max(x), 1000)
	new_y = slope * new_x + intercept

	ax.plot(new_x, new_y, 'r', linewidth=2)
	ax.set_xlabel('Height (m)')
	ax.set_ylabel('Mass (kg)')
	plt.grid()

	out_file = 'simple_regression_analysis.png'
	plt.savefig(out_file, bbox_inches='tight')

	plt.show()

if __name__ == '__main__':
	main()