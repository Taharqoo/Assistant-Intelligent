import openai

class ChatGPT:
    """
    Une classe pour communiquer avec l'API de OpenAI GPT-3 et obtenir des réponses à partir des messages d'utilisateur.

    Attributes:
        api_key (str): Une clé d'API valide pour accéder à OpenAI GPT-3.
        model (str): Le nom du modèle à utiliser pour générer des réponses (par défaut: "gpt-3.5-turbo").
        messages (list): Une liste de dictionnaires contenant les messages utilisateur et assistant. Chaque dictionnaire a
            deux clés: "role" (qui peut être "user" ou "assistant") et "content" (le message).

    Methods:
        add_message(role, content): Ajoute un message à la liste des messages.
        get_response(user_message): Récupère une réponse à partir de l'API OpenAI GPT-3 en utilisant les messages
            utilisateur et assistant stockés dans la liste des messages.

    """
    def __init__(self, api_key, model="gpt-3.5-turbo"):
        """
        Initialise une instance de la classe ChatGPT.

        Args:
            api_key (str): Une clé d'API valide pour accéder à OpenAI GPT-3.
            model (str): Le nom du modèle à utiliser pour générer des réponses (par défaut: "gpt-3.5-turbo").

        Returns:
            None
        """
        self.model = model
        self.api_key = api_key
        openai.api_key = self.api_key
        self.messages = [
            {"role": "system", "content": "Bonjour ! Je suis votre assistant. Comment puis-je vous aider ?"}]

    def add_message(self, role, content):
        self.messages.append({"role": role, "content": content})
        """
        Ajoute un message à la liste des messages.

        Args:
            role (str): Le rôle du message (peut être "user" ou "assistant").
            content (str): Le contenu du message.

        Returns:
            None
        """
    def get_response(self, user_message):
        """
        Récupère une réponse à partir de l'API OpenAI GPT-3 en utilisant les messages utilisateur et assistant
        stockés dans la liste des messages.

        Args:
            user_message (str): Le message de l'utilisateur.

        Returns:
            La réponse générée par OpenAI GPT-3 sous forme de chaîne de caractères.
        """
        self.add_message("user", user_message)
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=self.messages
        )
        assistant_message = response.choices[0].message['content']
        self.add_message("assistant", assistant_message)
        return assistant_message