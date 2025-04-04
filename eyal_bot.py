from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
import os
TOKEN = os.getenv("TOKEN")

sessions = {}

def start(update, context):
    user_id = update.message.chat_id
    sessions[user_id] = {"step": 1}
    update.message.reply_text("היי! איזה תפקיד אתה מחפש?\n1. מפתח תוכנה\n2. מפתח תוכנה fullStack\n3. אחר")

def handle_message(update, context):
    user_id = update.message.chat_id
    text = update.message.text.strip()

    if user_id not in sessions:
        update.message.reply_text("שלח /start כדי להתחיל את התהליך")
        return

    step = sessions[user_id]["step"]

    if step == 1:
        if text == "1" or text == "2":
            sessions[user_id]["step"] = 2
            update.message.reply_text("כמה שנות ניסיון אתה מחפש?\n1. 0-1\n2. 1-2\n3. יותר")
        elif text == "3":
            del sessions[user_id]
            update.message.reply_text("תודה רבה, אבל כנראה שזה פחות רלוונטי. בהצלחה! 🙏")
        else:
            update.message.reply_text("אנא בחר 1, 2 או 3 🙏")
    elif step == 2:
        if text == "1" or text == "2":
            sessions[user_id]["step"] = 3
            update.message.reply_text("איזה סוג עובד אתה מחפש?\n1. עצלן\n2. לא חכם במיוחד\n3. לא אוהב לתכנת\n4. חרוץ ובעל מוטיבציה גבוהה")
        elif text == "3":
            del sessions[user_id]
            update.message.reply_text("תודה רבה, אבל נראה שזה פחות יתאים לי. כל טוב! 👋")
        else:
            update.message.reply_text("אנא בחר 1, 2 או 3 🙏")
    elif step == 3:
        if text == "4":
            del sessions[user_id]
            update.message.reply_text("""נשמע שיש התאמה! 🙌
הנה הפרטים שלי:
שם: אייל קובי
📧 eyal4845@gmail.com
📱 0509596599""")
        elif text in ["1", "2", "3"]:
            del sessions[user_id]
            update.message.reply_text("אז כנראה שלא נסתדר 🙂 שיהיה בהצלחה!")
        else:
            update.message.reply_text("אנא בחר 1, 2, 3 או 4 🙏")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    updater.start_polling()
    print("🤖 הבוט מחכה להודעות...")
    updater.idle()

if __name__ == '__main__':
    main()
