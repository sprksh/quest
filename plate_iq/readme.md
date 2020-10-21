The app has been built with Flask because it's more lightweight and more suited 
for a small project like this. Django seems a little too heavy for it.

The app is built with an in-memory dictionary based db approach. For a
project like this it seems more logical to use some document store 
and that's why I have taken the dictionary based db approach.

It is meeting all api requirements and will be able to save the data
for as long as the app is running.

The app can be run using the `flask run` command.