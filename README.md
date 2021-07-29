# Setup
## Python

    pip install -r req.txt

## CSS/JS/Assets
Download the following into the `static/` directory.

- [bootstrap>=4.3](https://getbootstrap.com/docs/4.3/getting-started/download/)
- [fontawesome-free](https://fontawesome.com) (unpacked directory must be called `fontawesome`)

## Directories

    mkdir -p data/users/

## User-Schema

    {
       name : "name of user",
       accounts : [ "list", "of", "account", "names" ],
       single : "true/false, depending if user has team",
       selectedChampions: ["list of champions", "this user can play"]
       allowedFeatures: ["list of allowed features", "or empty list to allow all"]
    }
