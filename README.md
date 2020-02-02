### Age Of Empires 2 : Definitive Edition Random Map Script Extract



The repository contains extracted information from `GeneratingObjects.inc` file, using constants from it. The generated
 files can be found under `generated/<map size>/<map resources>/<game type>/<map name>.rms`
 
 If you ever wonder, for example,_"how objects are generated when I play Arena on Tiny map, on regicide ?"_ 
Then you can navigate to `generated/TINY_MAP/OTHER_RESOURCES/REGICIDE/` and open `Arena.rms` !


Because GeneratingObjects.inc doesn't use all the constants of the game _(like DEFAULT_RESOURCES)_, if you don't find a constant, then use the `OTHER_` folder as it will be what the game use _(like `OTHER_RESOURCES` in the example above)_



**If a MAP is missing**, please let me know by either:
* Opening an issue
* Reaching me by message 

You must provide the map name, but don't bother with the constants.
