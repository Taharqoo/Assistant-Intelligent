# Assistant Pascal

## Description du projet
L'Assistant Pascal est une application qui utilise l'API OpenAI pour permettre à un utilisateur de discuter avec un assistant virtuel. L'application utilise la technologie de génération de texte GPT-3 pour comprendre les demandes de l'utilisateur et y répondre de manière appropriée. L'assistant peut répondre à une variété de questions et peut également ouvrir des applications sur l'ordinateur de l'utilisateur.

## Installation
1.	Clonez le dépôt sur votre machine : 

```
git clone https://github.com/Taharqoo/Assistant-Pascal.git

```
2.	Installez Pipenv : 

```
pip install pipenv

```
3.	Naviguez dans le répertoire du projet et installez les dépendances :

```
pipenv install

```
4.	Activez l'environnement virtuel : 

```
pipenv shell

```
5.	Ensuite, vous pouvez installer les différentes bibliothèques en tapant les commandes suivantes :

```
	openai : pipenv install openai
	dotenv : pipenv install python-dotenv
	speech_recognition : pipenv install speech_recognition
	pygame : pipenv install pygame
	gtts : pipenv install gtts

```
6.	Créez le fichier *.env* à la racine du projet et ajoutez votre clé API OpenAI : **CHATGPT_API_KEY=<votre_clé>**

## Utilisation
1.	Exécutez le programme en exécutant la commande suivante :

```
 pipenv run python nom_de_votre_fichier.py

```
2.	L'assistant vocal est en attente et écoute pour les commandes de l'utilisateur.Lorsque vous êtes invité à parler, dites **Hey Pascal** pour réveiller l'assistant.
3.	Lorsque l'assistant est réveillé, posez des questions ou donnez des commandes à l'aide de la voix. L'assistant comprendra et répondra en conséquence. Pour quitter, dites simplement **au revoir**.

## Configuration
1.	Pour configurer l'application, vous pouvez modifier les paramètres dans le fichier *.env*. Les seuls paramètres qui doivent être configurés sont **CHATGPT_API_KEY=<votre_clé>**, qui est la clé d'API OpenAI utilisée par l'assistant.
2.	Vous pouvez obtenir une clé en créant un compte sur [OpenAI](https://beta.openai.com/signup/).

## Licence
Le projet est sous la **LICENSE** [MIT](https://opensource.org/license/mit/).
