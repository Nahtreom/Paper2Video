@echo off
call activate cosyvoice
manim -pqh --output_file 1.mp4 genintro.py Scene1

manim -pqh --output_file 2.mp4 genintro.py Scene2

manim -pqh --output_file 3.mp4 genintro.py Scene3

copy media\videos\genintro\1080p60\1.mp4 ..\automerge\
copy media\videos\genintro\1080p60\2.mp4 ..\automerge\
copy media\videos\genintro\1080p60\3.mp4 ..\automerge\

