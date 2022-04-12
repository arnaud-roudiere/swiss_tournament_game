# Swiss Tournament Game
An offline Swiss Chess Tournament app to manage the games.

## How it works?
The app will handle the following:
- Creation of the tournament made of 4 rounds each
- Creation of 8 players with all the details (Full name, sex, age, rank, etc.) 
- Generating pairs of players based on their ranking
- Creation of match between each round
- Once all the rounds are done, the app will save the results

The app uses the MVC method for Model, View and Control.

The results are saved in Json with TinyDB.

It includes flake8 to check if the app complies with the PEP8 requirements.

## How to install it?

In order to launch the app, you'll need to::<br><br>

<li>1.Clone the repository</li>
Enter the following in your Terminal to clone the Github repository:
<code class="language-bash" data-lang="bash">git@github.com:arnaud-roudiere/swiss_tournament_game.git</code><br><br>

<li>2.Create a virtual environnement</li>
To install the package, open the Terminal and type the following:
<code class="language-bash" data-lang="bash">pip install virtualenv</code><br>
Create the virtual environnement:
<code class="language-bash" data-lang="bash">virtualenv mypython</code><br>
Once done, you can close it typing:
<code class="language-bash" data-lang="bash">deactivate</code><br><br>

<li>3.Install the requirements</li>
Install the packages with:
<code class="language-bash" data-lang="bash">pip install -r requirements.txt</code><br><br>

<li>4.Run the App</li>
- For unix or macos: <code class="language-bash" data-lang="bash">python3 main.py</code><br>
- For windows: <code class="language-bash" data-lang="bash">py main.py</code><br>

<li>5.Edit a Flake8 report in HTML</li>
- <code class="language-bash" data-lang="bash"flake8 --format=html --htmldir=flake-report</code><br>

## How to use it?
* Launch the App
* You reached the Main menu, you can choose one of the 3 options : 1/Access the previous tournaments data 2/Create a new tournament 3/Quit
  * The nº 1 option will ask you to choose between : 1/Load the previous tournaments 2/Load the rounds 3/Load the matchs 4/ Load the players sorted alphabetically 5/ Load the players sorted by ranking
  * The nº 2 option will bring you to a form where to leave the tournament and players data
  * The nº 3 option will close the App
* After both options, the App will ask you if you want to come back to the main menu or quit the App

### Author:
Arnaud ROUDIERE
