from __future__ import print_function
import csv
import numpy as np
import hashStruct
import sys
##################################
#Author: xiaopeng xu
#Email: charlesxu90@gmail.com
##################################

#csize_file = '../data/Temperature.tsv'


def csize2grate(csize_file):
    """Old version of matching colony size with growth rate! Using
    maximum growth rate of wild type as reference."""
    Cmax = -10
    Cmin = 10
    with open(csize_file, 'rb') as tsvfin:
        tsvfin.next()
        tsvin = csv.reader(tsvfin, delimiter='\t')
        for row in tsvin:
            if len(row) < 1:
                break
            for i in range(1, len(row)):
                if len(row[i]) < 1:
                    row[i] = np.nan

            row_d = [np.float64(value) for value in row[1:len(row)]]
            dmax = 0.0
            dmin = 100.0
            try:
                dmax = np.nanmax(row_d)
                dmin = np.nanmin(row_d)
            except TypeError:
                dmax = 0.0
                dmin = 100
            Cmax = np.fmax(Cmax, dmax)
            Cmin = np.fmin(Cmin, dmin)

    ##Match maximum colony size match with WT opt Growth Rate,
    #Minimum colony size match with Growth Rate 0
    #B * (Xmin + C) = GRmin
    #B * (Xmax + C) = GRwild
    #GRmin = 0
    GRwild = 8.5712968149
    # Parameters for matching: B, C
    C = - Cmin
    B = GRwild / (Cmax + C)
    growth_rates = hashStruct.AutoVivification()
    with open(csize_file, 'rb') as tsvfin:
        tsvin = csv.reader(tsvfin, delimiter='\t')
        next(tsvin, None)  # Jump header
        for row in tsvin:
            if len(row) < 1:
                break
            #print(row[0], file=sys.stdout)

            for i in range(1, len(row)):
                if len(row[i]) < 1:
                    row[i] = np.nan

            # if not nan, set the growth rate, else still nan
            row_d = [B * (np.float64(value) + C)
                     if ~np.isnan(np.float64(value))
                     else np.nan for value in row[1:len(row)]]

            #print(row_d, file=sys.stderr)
            growth_rates[row[0]] = row_d

    return growth_rates


def clnysize(csize_file, cmin):
    """ Read colony size data into hash matrix"""
    clony_size = hashStruct.AutoVivification()
    with open(csize_file, 'rb') as tsvfin:
        tsvfin.next()
        tsvin = csv.reader(tsvfin, delimiter='\t')
        for row in tsvin:
            if len(row) < 1:
                break
            for i in range(1, len(row)):
                if len(row[i]) < 1:
                    row[i] = np.nan
            row_d = [np.float64(value) for value in row[1:len(row)]]
            dmin = 100.0
            try:
                dmin = np.nanmin(row_d)
            except TypeError:
                dmin = 100.0
            cmin[0] = np.fmin(cmin[0], dmin)
            clony_size[row[0]] = row_d
    return clony_size
