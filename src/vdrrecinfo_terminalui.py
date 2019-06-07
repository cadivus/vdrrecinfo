#!/usr/bin/env python3

import os

import argparse
if __package__ is None or __package__ is "":
  import vdrrecinfo
else:
  from . import vdrrecinfo


parser = argparse.ArgumentParser()
parser.add_argument('--get-channel', action='store_true', help='Prints channel')
parser.add_argument('--get-channel-name', action='store_true', help='Prints name of channel')
parser.add_argument('--get-title', action='store_true', help='Prints title')
parser.add_argument('--get-subheading', action='store_true', help='Prints subheading')
parser.add_argument('--get-description', action='store_true', help='Prints description')
parser.add_argument('--contains-vdr-info', action='store_true', help="Prints whether it's a valid file/directory")
parser.add_argument('vdrfile', help='Recording-directory or recinfo-file')
args = parser.parse_args()

path = os.path.abspath(args.vdrfile)

recinfo = None
def get_recinfo():
  global recinfo
  if recinfo == None:
    recinfo = vdrrecinfo.VdrRecInfo(path)
  return recinfo

if args.contains_vdr_info:
  print(vdrrecinfo.contains_vdr_info(path))

if args.get_channel:
  print(get_recinfo().channel)

if args.get_channel_name:
  print(get_recinfo().channel_name)

if args.get_title:
  print(get_recinfo().title)

if args.get_subheading:
  print(get_recinfo().subheading)

if args.get_description:
  print(get_recinfo().description)