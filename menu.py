#!/usr/bin/python3.8
import sys
import os
dataSourcesDir = os.path.dirname(os.path.realpath(__file__)) + '/dataSources'
sys.path.append(dataSourcesDir)

from stwnodatasource import StwnoDataSource

def main():
    # todo: get the data source as a command line argument
    dataSource = StwnoDataSource()
    menu = dataSource.getMenu()
    print(menu)
    print('main working')


if __name__ == '__main__':
    main()
