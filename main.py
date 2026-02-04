from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, ChatJoinRequestHandler

BOT_TOKEN = "PASTE_YOUR_BOT_TOKEN_HERE"

async def auto_accept(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        await update.chat_join_request.approve()
        print(f"Approved: {update.chat_join_request.from_user.id}")
    except Exception as e:
        print("Error:", e)

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(ChatJoinRequestHandler(auto_accept))

print("🤖 Auto Request Accept Bot is running...")
app.run_polling()
