# Total Playback Time from SQL Database exclusively for [ViTune](https://github.com/25huizengek1/ViTune)

**This script is specifically made for ViTune backup database!**
 
For anyone using this script, there's a small catch.

First step is

`python DataFromDb.py <your sql backup>`

This will generate a `DataFromSQL_DB.txt` file. Then you need to do one small change,
open the file and in the start add these `values = `

You can use anything beside 'values' but then respective changes must be made in script.

Finally run `python playback-time.py`

If everything is done correctly, you will see something like `170 hours and 5 minutes played`
