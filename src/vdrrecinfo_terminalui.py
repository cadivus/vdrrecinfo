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
parser.add_argument('--move-to-subheading', action='store_true', help="Moves recording to a folder named like the subheading")
parser.add_argument('vdrfile', nargs='+', help='Recording-directory or recinfo-file')
args = parser.parse_args()

def get_path(param):
  return os.path.abspath(param)

def make_filename(input):
  input = input.replace(' ', '_')
  input = input.replace('?', '__')
  input = input.replace('/', '__')
  input = input.replace('\\', '__')
  return input

recinfo = {}
def get_recinfo(param):
  if recinfo.get(param) == None:
    recinfo[param] = vdrrecinfo.VdrRecInfo(get_path(param))
  return recinfo.get(param)

if args.contains_vdr_info:
  for param in args.vdrfile:
    print(vdrrecinfo.contains_vdr_info(get_path(param)))

if args.get_channel:
  for param in args.vdrfile:
    print(get_recinfo(param).channel)

if args.get_channel_name:
  for param in args.vdrfile:
    print(get_recinfo(param).channel_name)

if args.get_title:
  for param in args.vdrfile:
    print(get_recinfo(param).title)

if args.get_subheading:
  for param in args.vdrfile:
    print(get_recinfo(param).subheading)

if args.get_description:
  for param in args.vdrfile:
    print(get_recinfo(param).description)

if args.move_to_subheading:
  for param in args.vdrfile:
    path = get_path(param)
    if os.path.isfile(path):
      path = os.path.dirname(path)
    recording = os.path.basename(path)
    recording_new_filename = make_filename(get_recinfo(param).subheading)
    recording_directory = os.path.join(os.path.dirname(path), recording_new_filename)
    if os.path.isdir(recording_directory) == False:
      os.mkdir(recording_directory)
    newpath = os.path.join(recording_directory, recording)
    os.rename(path, newpath)

