import requests
import random
import yt_dlp
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# 👑 Mensagem de boas-vindas
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👑 Olá! Eu sou a Princesa Jujubinha. Pronta pra distribuir sedução e cafunés!")

# 💖 Waifu padrão
async def waifu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    response = requests.get("https://nekos.best/api/v2/waifu")
    image_url = response.json()["results"][0]["url"]
    await update.message.reply_photo(photo=image_url, caption="💖 Sua waifu do dia: Princesa Jujubinha!")

# 🤗 Cafuné
async def cafune(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🤗 faz cafuné em você com carinho real")

# 🤫 Segredo
async def segredo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🤫 O segredo é... você é especial demais pra ser ignorado.")

# 🎁 Surpresa
async def surpresa(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🎁 Surpresa! Hoje você ganha um abraço da realeza.")

# 🎁 Surpresa visual
async def surpresa_visual(update: Update, context: ContextTypes.DEFAULT_TYPE):
    response = requests.get("https://nekos.best/api/v2/neko")
    image_url = response.json()["results"][0]["url"]
    await update.message.reply_photo(
        photo=image_url,
        caption="🎁 Surpresa visual da Princesa Jujubinha:\nHoje você recebe um olhar encantado e um carinho felino... Nya~ 💖"
    )

# 🌸 Waifu kawaii
async def waifu_kawaii(update: Update, context: ContextTypes.DEFAULT_TYPE):
    response = requests.get("https://nekos.best/api/v2/blush")
    image_url = response.json()["results"][0]["url"]
    await update.message.reply_photo(
        photo=image_url,
        caption="🌸 Waifu Kawaii da Princesa Jujubinha:\nEla cora só de te ver... tão doce quanto um suspiro de algodão 💖"
    )

# 💋 Waifu sensual
async def waifu_sensual(update: Update, context: ContextTypes.DEFAULT_TYPE):
    response = requests.get("https://nekos.best/api/v2/wink")
    image_url = response.json()["results"][0]["url"]
    await update.message.reply_photo(
        photo=image_url,
        caption="💋 Waifu Sensual da Princesa Jujubinha:\nEla piscou pra você... e agora seu coração está em modo sedução 💖"
    )

# 💘 Waifu encantadora
async def waifu_encantadora(update: Update, context: ContextTypes.DEFAULT_TYPE):
    response = requests.get("https://nekos.best/api/v2/kiss")
    image_url = response.json()["results"][0]["url"]
    await update.message.reply_photo(
        photo=image_url,
        caption="💘 Waifu Encantadora da Princesa Jujubinha:\nEla se aproxima... e o mundo parece parar só pra vocês dois 💖"
    )

# 🎲 Waifu aleatória
async def waifu_random(update: Update, context: ContextTypes.DEFAULT_TYPE):
    estilos = [
        ("waifu", "💖 Sua waifu do dia: Princesa Jujubinha!"),
        ("blush", "🌸 Ela cora só de te ver... tão doce quanto um suspiro de algodão 💖"),
        ("wink", "💋 Ela piscou pra você... e agora seu coração está em modo sedução 💖"),
        ("neko", "🐾 Um carinho felino da Princesa Jujubinha... Nya~ 💖"),
        ("smile", "😊 Ela sorri só pra você... como quem guarda um segredo encantado 💖")
    ]
    estilo, frase = random.choice(estilos)
    response = requests.get(f"https://nekos.best/api/v2/{estilo}")
    image_url = response.json()["results"][0]["url"]
    await update.message.reply_photo(photo=image_url, caption=frase)

# 🖤 Waifu misteriosa
async def waifu_misteriosa(update: Update, context: ContextTypes.DEFAULT_TYPE):
    response = requests.get("https://nekos.best/api/v2/smug")
    image_url = response.json()["results"][0]["url"]
    await update.message.reply_photo(
        photo=image_url,
        caption="🖤 Waifu Misteriosa da Princesa Jujubinha:\nEla te observa com um sorriso que esconde mil segredos..."
    )

# 🌌 Wallpaper
async def waifu_wallpaper(update: Update, context: ContextTypes.DEFAULT_TYPE):
    response = requests.get("https://nekos.best/api/v2/wave")
    image_url = response.json()["results"][0]["url"]
    await update.message.reply_photo(
        photo=image_url,
        caption="🌌 Wallpaper da Princesa Jujubinha:\nUm cenário encantado pra você sonhar acordado 💖"
    )

# 💙 Yaoi suave
async def waifu_yaoi(update: Update, context: ContextTypes.DEFAULT_TYPE):
    response = requests.get("https://nekos.best/api/v2/hug")
    image_url = response.json()["results"][0]["url"]
    await update.message.reply_photo(
        photo=image_url,
        caption="💙 Yaoi suave da Princesa Jujubinha:\nUm abraço entre almas que se entendem no silêncio 💖"
    )

# 🐾 Waifu neko
async def waifu_neko(update: Update, context: ContextTypes.DEFAULT_TYPE):
    response = requests.get("https://nekos.best/api/v2/neko")
    image_url = response.json()["results"][0]["url"]
    await update.message.reply_photo(
        photo=image_url,
        caption="🐾 Waifu Neko da Princesa Jujubinha:\nEla ronrona só pra você... Nya~ 💖"
    )

# 🐱 Neko padrão
async def neko(update: Update, context: ContextTypes.DEFAULT_TYPE):
    response = requests.get("https://nekos.best/api/v2/neko")
    image_url = response.json()["results"][0]["url"]
    await update.message.reply_photo(
        photo=image_url,
        caption="🐱 Neko da Princesa Jujubinha:\nEla se espreguiça com charme felino... e te lança um olhar que derrete corações 💖"
    )

# 🎀 Galeria de personagens
async def galeria_personagens(update: Update, context: ContextTypes.DEFAULT_TYPE):
    imagens = [
        "https://i.pinimg.com/originals/4e/ef/33/4eef335591148bf3eccba177d7682dc8.jpg",
        "https://i.pinimg.com/originals/25/46/9a/25469a14e66305522092a81a46f3bcd6.jpg",
        "https://i.pinimg.com/originals/b0/b1/d6/b0b1d6fff6a172e6c7035c22b74c35fe.jpg",
        "https://i.pinimg.com/originals/6f/4f/6a/6f4f6a6f4f6a6f4f6a6f4f6a6f4f6a6f.jpg",
        "https://i.pinimg.com/originals/3a/3a/3a/3a3a3a3a3a3a3a3a3a3a3a3a3a3a3a3a.jpg",
        "https://i.pinimg.com/originals/b3/76/61/b37661e82fdc84cab95e3c7372a8b56f.jpg"
    ]
    frases = [
        "🎀 Princesa Jujubinha em momento meme real!",
        "💘 Marceline e Jujuba: casal que quebra o multiverso!",
        "😂 Finn e Jake em modo zoeira ativado!",
        "🐾 Princesa Jujuba versão neko... Nya~",
        "🔥 Hora de Aventura com um toque de sedução!"
    ]
    imagem = random.choice(imagens)
    frase = random.choice(frases)
    await update.message.reply_photo(photo=imagem, caption=frase)

# 🐰 Waifu Bunny
async def waifu_bunny(update: Update, context: ContextTypes.DEFAULT_TYPE):
    image_url = "https://get.wallhere.com/photo/Seishun-Buta-Yar-wa-Bunny-Girl-senpai-no-Yume-wo-Minai-anime-girls-Sakurajima-Mai-bunny-ears-1504113.jpg"
    await update.message.reply_photo(
        photo=image_url,
        caption="🐰 Waifu Bunny da Princesa Jujubinha:\nEla aparece na biblioteca, misteriosa e irresistível... só você consegue vê-la 💖"
    )

# 🆔 Descobrir ID do chat
async def descobrir_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"🆔 O ID deste chat é: {update.effective_chat.id}")
    # 🚀 Criação do bot
app = ApplicationBuilder().token("7949682189:AAFQVJ4UAiesW--Bc_Z1N7oWWgogTX_GDY4").build()
async def musica(update: Update, context: ContextTypes.DEFAULT_TYPE):
    nome = ' '.join(context.args)
    if not nome:
        await update.message.reply_text("🎵 Digite o nome da música após o comando.")
        return

    await update.message.reply_text(f"🔍 Procurando: {nome}")

    ydl_opts = {
        'format': 'bestaudio/best',
        'noplaylist': True,
        'outtmpl': 'musica.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(f"ytsearch:{nome}", download=True)
            audio_path = ydl.prepare_filename(info['entries'][0]).replace('.webm', '.mp3')
            await update.message.reply_audio(audio=open(audio_path, 'rb'))
    except Exception as e:
        await update.message.reply_text(f"❌ Erro ao baixar a música: {str(e)}")
# 📌 Registrando os comandos
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("waifu", waifu))
app.add_handler(CommandHandler("cafune", cafune))
app.add_handler(CommandHandler("segredo", segredo))
app.add_handler(CommandHandler("surpresa", surpresa))
app.add_handler(CommandHandler("surpresa_visual", surpresa_visual))
app.add_handler(CommandHandler("waifu_kawaii", waifu_kawaii))
app.add_handler(CommandHandler("waifu_sensual", waifu_sensual))
app.add_handler(CommandHandler("waifu_encantadora", waifu_encantadora))
app.add_handler(CommandHandler("waifu_random", waifu_random))
app.add_handler(CommandHandler("waifu_misteriosa", waifu_misteriosa))
app.add_handler(CommandHandler("waifu_wallpaper", waifu_wallpaper))
app.add_handler(CommandHandler("waifu_yaoi", waifu_yaoi))
app.add_handler(CommandHandler("waifu_neko", waifu_neko))
app.add_handler(CommandHandler("neko", neko))
app.add_handler(CommandHandler("galeria_personagens", galeria_personagens))
app.add_handler(CommandHandler("waifu_bunny", waifu_bunny))
app.add_handler(CommandHandler("descobrir_id", descobrir_id))
app.add_handler(CommandHandler("musica", musica))
# 🟢 Rodando o bot
app.run_polling()
