# selenium-fun
Random Selenium scripts created by me to have some fun. 
* link_clicker.py tests a theory I had heard before, that by clicking on the first link on any given Wikipedia page you would eventually end up at the [Philosophy](https://en.wikipedia.org/wiki/Philosophy) page. It turns out this is true and the average random Wikipedia page reaches Philosophy in about 16 jumps.
* cookieclicker.py makes the [Cookie Clicker](http://orteil.dashnet.org/cookieclicker/) game a breeze by automating clicking. The clicking can be toggle on/off by clicking the sell/buy buttons in the game.
* google_form.py provides a template to use Selenium on Google Forms.

In order to run these scripts you must:
  * Install Selenium: pip install selenium
  * [Download](https://chromedriver.storage.googleapis.com/index.html?path=2.27/) the correct Chromedriver for your platform
  * Specify the location of the driver on your local file system in the script
