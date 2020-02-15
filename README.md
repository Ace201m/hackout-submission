![](https://imgur.com/hrNlqDm.png)
#  Eatout

Eatout is a  Chat based food recommender webapp. 
Technologies used 

  - Vue.js for frontend
  - Flask for server side RestAPIs
  - Python and BeautifulSoup for the backend algorithm and data obtaining.

### Features provided by Our WebApp!
Due to lot of options and lot of restuarents around us the selection of food that we want is really difficult. In this case Eatout can help you out. Eatout will ask dynamic series of question based on the your responses to recommend you the food you want.

### How to run ?
 - Install flask run the server using command (correct the path for the python interpreter in the first line of ```app.py``` :
    ```sh
    $ chmod +x app.py
    $ ./app.py
    ```
 - Run the Vue Client Side using command:
    ```sh
    $ cd src/front_end/eatout
    $ npm run serve
    ```
Note : If the python server is not running on ```localhost:5000``` then change the base URL in ```eatout/src/components/body.vue``` line no. 41 appropriately.

### Demo Images

![](https://imgur.com/kVX0fOi.png)
![](https://imgur.com/NDqyhAh.png)
