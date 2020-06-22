# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 18:53:16 2020

@author: prani
"""
import os


def main():
 # add diredctory to os.listdir('---')
    for count, filename in enumerate(os.listdir("D:/Data/Videos/Anime/Haikyuu!!/Haikyuu!! Season 4")):
        if count < 9:
            dst = "Haikyuu!! S4 0" + str(count+1) + '.mkv'
        else:
            dst = "Haikyuu!! S4 " + str(count+1) + '.mkv'
        src = 'D:/Data/Videos/Anime/Haikyuu!!/Haikyuu!! Season 4/' + filename
        dst = 'D:/Data/Videos/Anime/Haikyuu!!/Haikyuu!! Season 4/' + dst

        # rename() function will
        # rename all the files
        os.rename(src, dst)


# Driver Code
if __name__ == '__main__':

    # Calling main() function
    main()
