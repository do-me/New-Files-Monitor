# New-Files-Monitor
A simple live monitor to get a new files/s rate in a directory. Working well with 1.000.000+ files. Particularly useful when (chaotically) downloading from multiple threads. A perfect symbiosis with [Fast Instagram Scraper](https://github.com/do-me/fast-instagram-scraper).

## Installation 
I just dicovered [fire](https://github.com/google/python-fire) and found it quite useful as an easy command line parser. 

```pip install fire```

and clone this repo 

```git clone https://github.com/do-me/New-Files-Monitor.git```

or simply copy the source code.

In case you don't want to install fire, either rewrite it yourself with `argparse` or simply use the 'unfired' version with hardcoded params. 

## Usage
```
python new-files-monitor.py 
```
Will give you this information exactly one time for your working directory.

```
 6.62 files/s
 1714195 files total
 2021-01-16 19:23:55.067400 start count
 2021-01-16 19:24:11.363195 end count
 16 seconds delta
 106 files delta
```
## Arguments 
```
 --dir     Default: current working directory. 
           Can be a directory of your choice. 
           
 --wait    Default: 0 
           Wait in between the file counts. Set to a number of your choice.
           Recommendation is some seconds only for a low number of total files
           in a directory (<10.000) or a higher number if you want a 
           better leveled average. 
           When working with large directories (>500.000 files) just use the zero 
           default or a few seconds only as counting itself might take some 
           seconds as well.
           
--repeat   Default: 1
           Repeat the counting process n times. If you are just interested in a 
           one time count/rate leave it to the default. 
           For real-time monitoring set to a high number of your choice and combine
           with a number ≥0 for --wait flag when monitoring small directories. 
           Leave to default for big directories.
           
```

## Logic 
For some reason it is very uncommon on github to explain your code in a few words. I'd appreciated this a lot in the past (and would still do!) so I add this section to all of my future repos. If it helps just one person maybe new to coding it was worth the effort.

Let's sum it up here as pseudocode.

```
Change current working directory if needed
Begin a loop:
  Count all files in dir and get current time #1
  Wait n seconds 
  Count all files in dir and get current time #2
  Calculate deltas and rate 
  Print results and erase previously printed lines
```

