# Children Check


Children Check is a workflow for kindergarten employees designed for state processes

  - Upload Children data like name and lastname in to the database 
  - Check all children inside a group
  - trigger the workflow to send the mail to local community/health authority

You can also:
  - restrict employees permissions
  - use it via mobile(mobilefriendly-comming soon)
  - Edit children data

Children Check is a django Application based on simple Web tools.

> The overriding design goal for Children Check
> is to make your work optimized
> as possible. The idea is that
> pedagogues could concentrate more taking
> care about your children and spent less time on 
> clerical activities  


### Tech

DMS uses a number of open source projects to work properly:

* [Python3]
* [django] - great Web-Frameworks for modern web apps
* [env] - environment for faster buildings
* [HTML5] 
* [CSS3] 


### Installation

Download this git repositoy and install and start the server with:

Linux
```sh
$ cd ./Kita-Children-Check
$ source /env/script/activate
$ django manage.py runserver
```

Windows
```sh
$ cd Kita-Children-Check
$  \env\script\activate
$ django manage.py runserver
```