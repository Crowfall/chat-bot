import openai
import requests
openai.api_key = "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"
from transformers import pipeline, BertTokenizer
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play

class TextProcessor():
    def __init__(self):
        super().__init__()
        self.openai = openai
        self.model_name = "gpt-3.5-turbo"

    def translate_en_to_fr(self, text):
        traduction = pipeline("translation_en_to_fr")
        return traduction(text)[0]['translation_text']
    
    def extract_entities(self, text):
        entities = pipeline("ner")
        return entities(text)
    
    def analyze_sentiment(self, text):
        sentiment = pipeline("sentiment-analysis")
        resultat = sentiment(text)
        return resultat[0]
    
    def extract_embeddings(self, text):
        tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
        return tokenizer.tokenize(text)

    def generate_text(self, prompt=''): 
        text_gen = pipeline("text-generation", model="gpt2")
        return text_gen(prompt)[0]['generated_text']
    
    def openai_translate(self, text):
        return openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
            "role": "system",
            "content": "You will be provided with a sentence in English, and your task is to translate it into French."
            },
            {
            "role": "user",
            "content": "My name is Nicolas. What is yours?"
            },
            {
            "role": "assistant",
            "content": "Mon nom est Nicolas. Quel est le tien?"
            },
            {
            "role": "user",
            "content": text
            }
        ],
        temperature=0,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )['choices'][0]['message']["content"]

        
    def oepenai_text_sumary(self, text): 
        return openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
            "role": "system",
            "content": "Summarize content you are provided with for a second-grade student."
            },
            {
            "role": "user",
            "content": "Jupiter is the fifth planet from the Sun and the largest in the Solar System. It is a gas giant with a mass one-thousandth that of the Sun, but two-and-a-half times that of all the other planets in the Solar System combined. Jupiter is one of the brightest objects visible to the naked eye in the night sky, and has been known to ancient civilizations since before recorded history. It is named after the Roman god Jupiter.[19] When viewed from Earth, Jupiter can be bright enough for its reflected light to cast visible shadows,[20] and is on average the third-brightest natural object in the night sky after the Moon and Venus."
            },
            {
            "role": "assistant",
            "content": "Jupiter is a really big planet in our Solar System. It is the fifth planet from the Sun and it is the largest planet. It is called a gas giant because it is made mostly of gas. Jupiter is much smaller than the Sun, but it is bigger than all the other planets combined. It is very bright and can be seen in the night sky without a telescope. People have known about Jupiter for a very long time, even before they started writing things down. It is named after a god from ancient Rome. When we look at Jupiter from Earth, it can be so bright that it can make shadows. It is usually the third-brightest thing we can see in the night sky, after the Moon and Venus."
            },
            {
            "role": "user",
            "content": text
            }
        ],
        temperature=0,
        max_tokens=1024,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )['choices'][0]['message']["content"]

    def openai_text_generativ(self, text):
        return openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
            "role": "system",
            "content": "Tu vas devoir me générer tu texte en fonction d'une thématique que je vais te donner ou du contenu"
            },
            {
            "role": "user",
            "content": "Thématique: L'esport\nContenu: League fermée"
            },
            {
            "role": "assistant",
            "content": "L'esport, une industrie en pleine expansion, ne cesse de fasciner les amateurs de jeux vidéo du monde entier. Parmi les nombreuses compétitions qui se déroulent chaque année, l'une des formes les plus controversées est celle de la league fermée.\n\nLa league fermée, également connue sous le nom de franchise, consiste à regrouper un nombre limité d'équipes qui participent à une compétition exclusive. Contrairement aux championnats traditionnels, où chaque équipe peut tenter de se qualifier et de montrer ses compétences sur le terrain, la league fermée impose des critères stricts pour rejoindre ses rangs.\n\nCette approche a ses partisans et ses détracteurs. Les partisans soutiennent que la league fermée permet de garantir un niveau de jeu élevé, en réunissant les meilleures équipes du monde dans une compétition féroce. De plus, elle offre aux sponsors et aux investisseurs une plus grande visibilité et une stabilité financière, ce qui peut être bénéfique pour l'ensemble de l'industrie de l'esport.\n\nCependant, les dé"
            },
            {
            "role": "user",
            "content": text
            }
        ],
        temperature=0.8,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )['choices'][0]['message']["content"]

    def openai_codex(self, text):
        return openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k",
        messages=[
            {
            "role": "system",
            "content": "je vais te donner un morceau de code Python et ta tâche consistera à trouver et à corriger les bugs."
            },
            {
            "role": "user",
            "content": "numerator = 10\ndenominator = 0\nresult = numerator / denominator\nprint(\"Result:\", result)"
            },
            {
            "role": "assistant",
            "content": "Le code contient une erreur car on ne peut pas diviser par zéro. Pour corriger cela, nous devons vérifier si le dénominateur est différent de zéro avant de faire la division. Voici le code corrigé :\n\n```python\nnumerator = 10\ndenominator = 0\n\nif denominator != 0:\n    result = numerator / denominator\n    print(\"Result:\", result)\nelse:\n    print(\"Cannot divide by zero.\")\n```\n\nMaintenant, le programme affichera \"Cannot divide by zero.\" au lieu de provoquer une erreur de division par zéro."
            },
            {
            "role": "assistant",
            "content": text
            }
        ],
        temperature=0,
        max_tokens=1024,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )['choices'][0]['message']["content"] 
    
    def openai_create_image(self, prompt):
        response = openai.Image.create(
            prompts=prompt,
            n=1,
            size="1024x1024"
        )
        image_url = response['data'][0]['url']
        return image_url

    def generate_prompt_with_chatgpt(self, user_text):
        prompt = f"Améliorez le texte suivant : '{user_text}'"

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that improves text."},
                {"role": "user", "content": prompt}
            ]
        )

        return response.choices[0].message["content"]
    
    def download_image(self, url_img, img_name='img.png'):
        img = requests.get(url_img).content
        with open(img_name, 'wb') as handler:
            handler.write(img)
    
    def openai_image_creation(self, promt):
        response = openai.Image.create(
        prompt=promt,
        n=1,
        size="1024x1024"
        )
        image_url = response['data'][0]['url']
        return image_url
        
    def openai_create_image_variation(self, bytes_data):
            response = self.openai.Image.create_variation(
                image=bytes_data,
                n=1,
                size="1024x1024"
                )
            image_url = response['data'][0]['url']
            return image_url
    
    def generate_image_description(self, text):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that generates image descriptions."},
                {"role": "user", "content": text}
            ]
        )
        image_description = response.choices[0].message["content"]

        return image_description
    
    def openai_transcribe(self, audio_file_path):
        return openai.Audio.transcribe(model="whisper-1", 
                                     file=open(audio_file_path, "rb"), 
                                     engine="gpt3", 
                                     speaker_labels=True)['text']

    def openai_audio_translate(self, audio_file_path):
        return openai.Audio.translate(model="whisper-1", 
                                    file=open(audio_file_path, "rb"),
                                    engine="davinci",
                                    speaker_labels=True)['text']

    def text_to_speech(self, text, audio_path):
        tts = gTTS(text=text, lang='fr', slow=True)
        tts.save(audio_path)
        return audio_path
    

    def openai_chat_finetune(self, training_data_file):
        response = openai.File.create(
        file=open(training_data_file, "rb"),
        purpose='fine-tune'
        )

        openai.FineTuningJob.create(
            training_file=training_data_file,
            model="gpt-3.5-turbo",
        )
        return response