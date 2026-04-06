from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ContextTypes

import os
TOKEN = os.getenv("BOT_TOKEN")

# --- Головне меню ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📅 Розклад", url="http://korpk.org.ua/%d1%80%d0%be%d0%b7%d0%ba%d0%bb%d0%b0%d0%b4%d0%b8/")],
        [InlineKeyboardButton("📘 Дисципліна вільного вибору", callback_data="dystiplina")],
        [InlineKeyboardButton("📊 Опитування", callback_data="opituvannya")],
        [InlineKeyboardButton("📈 Моніторинг", callback_data="monitoryng")],
        [InlineKeyboardButton("💻 Віртуальна кімната", url="http://korpk.org.ua/%d0%bc%d0%b0%d1%82%d0%b5%d1%80%d1%96%d0%b0%d0%bb%d1%8c%d0%bd%d0%be-%d1%82%d0%b5%d1%85%d0%bd%d1%96%d1%87%d0%bd%d0%b5-%d0%b7%d0%b0%d0%b1%d0%b5%d0%b7%d0%bf%d0%b5%d1%87%d0%b5%d0%bd%d0%bd%d1%8f/")],
        [InlineKeyboardButton("📑 Графіки та додаткова інформація", callback_data="grafiki")],
        [InlineKeyboardButton("🎓 Абітурієнт", callback_data="abiturient")],
        [InlineKeyboardButton("✍️ Зворотний зв'язок", callback_data="feedback")],
        [InlineKeyboardButton("⬅️ Вихід", callback_data="exit")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    text = "Привіт, я бот @KorpkBot, який хоче допомогти обрати потрібну категорію:"

    if update.message:
        await update.message.reply_text(text, reply_markup=reply_markup)
    else:
        await update.callback_query.edit_message_text(text, reply_markup=reply_markup)


# --- Кнопка назад ---
def back_button():
    return InlineKeyboardMarkup([[InlineKeyboardButton("⬅️ Назад", callback_data="main_menu")]])


# --- Обробка кнопок ---
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    choice = query.data

    if choice == "dystiplina":
        keyboard = [
            [InlineKeyboardButton("Початкова освіта", url="http://korpk.org.ua/%d0%ba%d0%b0%d1%82%d0%b0%d0%bb%d0%be%d0%b3-%d0%b2%d0%b8%d0%b1%d1%96%d1%80%d0%ba%d0%be%d0%b2%d0%b8%d1%85-%d0%b4%d0%b8%d1%81%d1%86%d0%b8%d0%bf%d0%bb%d1%96%d0%bd-%d0%bd%d0%b0-2026-2027-%d0%bd%d0%b0%d0%b2/")],
            [InlineKeyboardButton("Трудове навчання та технології", url="http://korpk.org.ua/%d0%ba%d0%b0%d1%82%d0%b0%d0%bb%d0%be%d0%b3-%d0%b2%d0%b8%d0%b1%d1%96%d1%80%d0%ba%d0%be%d0%b2%d0%b8%d1%85-%d0%b4%d0%b8%d1%81%d1%86%d0%b8%d0%bf%d0%bb%d1%96%d0%bd-%d0%bd%d0%b0-2026-2027-%d0%bd%d0%b0%d0%b2/")],
            [InlineKeyboardButton("Фізична культура", url="http://korpk.org.ua/%d0%ba%d0%b0%d1%82%d0%b0%d0%bb%d0%be%d0%b3-%d0%b2%d0%b8%d0%b1%d1%96%d1%80%d0%ba%d0%be%d0%b2%d0%b8%d1%85-%d0%b4%d0%b8%d1%81%d1%86%d0%b8%d0%bf%d0%bb%d1%96%d0%bd/")],
            [InlineKeyboardButton("⬅️ Назад", callback_data="main_menu")]
        ]
        await query.edit_message_text("📘 Обери дисципліну:", reply_markup=InlineKeyboardMarkup(keyboard))

    elif choice == "opituvannya":
        keyboard = [
            [InlineKeyboardButton("📝 Анкета", url="https://sites.google.com/site/virtualnijmetodicnijkabinet2/%D0%BE%D0%BF%D0%B8%D1%82%D1%83%D0%B2%D0%B0%D0%BD%D0%BD%D1%8F")],
            [InlineKeyboardButton("📊 Результати", url="https://sites.google.com/site/virtualnijmetodicnijkabinet2/%D0%BE%D0%BF%D0%B8%D1%82%D1%83%D0%B2%D0%B0%D0%BD%D0%BD%D1%8F/%D1%80%D0%B5%D0%B7%D1%83%D0%BB%D1%8C%D1%82%D0%B0%D1%82%D0%B8-%D0%BE%D0%BF%D0%B8%D1%82%D1%83%D0%B2%D0%B0%D0%BD%D0%BD%D1%8F")],
            [InlineKeyboardButton("⬅️ Назад", callback_data="main_menu")]
        ]
        await query.edit_message_text("📊 Опитування:", reply_markup=InlineKeyboardMarkup(keyboard))

    elif choice == "monitoryng":
        keyboard = [
            [InlineKeyboardButton("📈 Моніторинг якості освіти", url="http://korpk.org.ua/%d0%bc%d0%be%d0%bd%d1%96%d1%82%d0%be%d1%80%d0%b8%d0%bd%d0%b3-%d1%8f%d0%ba%d0%be%d1%81%d1%82%d1%96-%d0%be%d1%81%d0%b2%d1%96%d1%82%d0%b8/")],
            [InlineKeyboardButton("⬅️ Назад", callback_data="main_menu")]
        ]
        await query.edit_message_text("📈 Обери розділ моніторингу:", reply_markup=InlineKeyboardMarkup(keyboard))

    elif choice == "grafiki":
        keyboard = [
            [InlineKeyboardButton("Графіки освітнього процесу", url="http://korpk.org.ua/grafiki-navchalnogo-procesu/")],
            [InlineKeyboardButton("Освітньо-професійні програми", url="http://korpk.org.ua/opp-obgovorennya-proektiv/")],
            [InlineKeyboardButton("Розклади та графіки занять", url="http://korpk.org.ua/%d1%80%d0%be%d0%b7%d0%ba%d0%bb%d0%b0%d0%b4%d0%b8/")],
            [InlineKeyboardButton("Графік консультацій", url="http://korpk.org.ua/%d0%b3%d1%80%d0%a4%d1%96%d0%ba-%d0%ba%d0%be%d0%bd%d1%81%d1%83%d0%bb%d1%8c%d1%82%d0%b0%d1%86%d1%96%d0%b9-%d0%b2%d0%b8%d0%ba%d0%bb%d0%b0%d0%b4%d0%b0%d1%87%d1%96%d0%b2/")],
            [InlineKeyboardButton("Курсова робота", url="http://korpk.org.ua/%d0%ba%d1%83%d1%80%d1%81%d0%be%d0%b2%d0%b0-%d1%80%d0%be%d0%b1%d0%be%d1%82%d0%b0/")],
            [InlineKeyboardButton("⬅️ Назад", callback_data="main_menu")]
        ]
        await query.edit_message_text("📑 Графіки та додаткова інформація:", reply_markup=InlineKeyboardMarkup(keyboard))

    elif choice == "abiturient":
        keyboard = [
            [InlineKeyboardButton("Приймальна комісія", url="https://sites.google.com/view/vstypnuk/%D0%B3%D0%BE%D0%BB%D0%BE%D0%B2%D0%BD%D0%B0")],
            [InlineKeyboardButton("Facebook", url="https://www.facebook.com/korpk.official/")],
            [InlineKeyboardButton("Instagram", url="https://www.instagram.com/_the_college_post/")],
            [InlineKeyboardButton("Tik-Tok", url="https://www.tiktok.com/@korcollege.official/")],
            [InlineKeyboardButton("⬅️ Назад", callback_data="main_menu")]
        ]
        await query.edit_message_text("🎓 Інформація для абітурієнтів:", reply_markup=InlineKeyboardMarkup(keyboard))

    elif choice == "feedback":
        await query.edit_message_text(
            "✍️ *Зворотній зв'язок*\n\n"
            "Якщо маєш питання або пропозиції — звертайся:\n\n"
            "📧 Email: lydav.golub@gmail.com",
            parse_mode="Markdown",
            reply_markup=back_button()
        )

    elif choice == "main_menu":
        await start(update, context)

    elif choice == "exit":
        await query.edit_message_text("Бувай! Якщо знадоблюся — пиши /start 👋")


# --- Обробка текстових повідомлень ---
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Я реагую лише на кнопки меню. Натисни /start для виклику меню.")


# --- Запуск ---
if __name__ == '__main__':
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Бот запущений...")
    app.run_polling()