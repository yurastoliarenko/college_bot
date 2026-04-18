import logging
import os
from dotenv import load_dotenv
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ContextTypes
import asyncio

# Завантажуємо змінні середовища
load_dotenv()

# Налаштування логування
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    handlers=[
        logging.FileHandler('bot.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# TOKEN з .env (БЕЗПЕЧНІШЕ!)
TOKEN = os.getenv('BOT_TOKEN', '8666785874:AAHUuJCVYGCGpSt7e78KXFLfJEG0YPO6Sj0')

class KorpkBot:
    def __init__(self):
        self.stats = {'users': set(), 'commands': 0}
    
    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Головна команда /start"""
        user_id = update.effective_user.id
        self.stats['users'].add(user_id)
        self.stats['commands'] += 1
        
        keyboard = [
            [InlineKeyboardButton("📅 Розклад", url="http://korpk.org.ua/розклади/")],
            [InlineKeyboardButton("📘 Дисципліни вільного вибору", callback_data="dystiplina")],
            [InlineKeyboardButton("📊 Опитування", callback_data="opituvannya")],
            [InlineKeyboardButton("📈 Моніторинг", callback_data="monitoryng")],
            [InlineKeyboardButton("💻 Віртуальна кімната", url="http://korpk.org.ua/матеріално-технічне-забезпечення/")],
            [InlineKeyboardButton("📑 Графіки та додаткова інформація", callback_data="grafiki")],
            [InlineKeyboardButton("🎓 Абітурієнт", callback_data="abiturient")],
            [InlineKeyboardButton("✍️ Зворотний зв'язок", callback_data="feedback")],
            [InlineKeyboardButton("ℹ️ Статус бота", callback_data="status")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        text = (
            "🎓 *Привіт, я бот @KorpkBot!*\n\n"
            "Я допоможу обрати потрібну категорію інформації:\n\n"
            "👇 Натисни кнопку нижче 👇"
        )
        
        try:
            if update.message:
                await update.message.reply_text(text, reply_markup=reply_markup, parse_mode='Markdown')
            else:
                await update.callback_query.edit_message_text(text, reply_markup=reply_markup, parse_mode='Markdown')
        except Exception as e:
            logger.error(f"Помилка в start: {e}")
    
    async def status(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Статус бота"""
        query = update.callback_query
        await query.answer()
        
        status_text = (
            f"✅ *Статус бота*\n\n"
            f"🟢 Бот **онлайн**\n"
            f"👥 Користувачів: **{len(self.stats['users'])}**\n"
            f"📊 Команд виконано: **{self.stats['commands']}**\n"
            f"🔄 Автономний режим 24/7"
        )
        
        back_keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("⬅️ Назад", callback_data="main_menu")]
        ])
        
        await query.edit_message_text(status_text, reply_markup=back_keyboard, parse_mode='Markdown')
    
    async def back_button(self):
        """Кнопка назад"""
        return InlineKeyboardMarkup([[InlineKeyboardButton("⬅️ Назад до меню", callback_data="main_menu")]])
    
    async def button_handler(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Обробка всіх кнопок"""
        query = update.callback_query
        await query.answer()
        choice = query.data
        
        logger.info(f"Користувач {query.from_user.id} натиснув: {choice}")
        self.stats['commands'] += 1
        
        try:
            if choice == "main_menu":
                await self.start(update, context)
            
            elif choice == "dystiplina":
                keyboard = [
                    [InlineKeyboardButton("Початкова освіта", url="http://korpk.org.ua/вибір-дисциплин-на-2026-2027-навчальний-рік/")],
                    [InlineKeyboardButton("Трудове навчання та технології", url="http://korpk.org.ua/вибір-дисциплин-на-2026-2027-навчальний-рік-2/")],
                    [InlineKeyboardButton("Фізична культура", url="http://korpk.org.ua/вибір-дисциплин-на-2026-2027-навчальний-рік-3/")],
                    [InlineKeyboardButton("⬅️ Назад", callback_data="main_menu")]
                ]
                await query.edit_message_text(
                    "📘 *Дисципліни вільного вибору*\n\nОбери спеціальність:",
                    reply_markup=InlineKeyboardMarkup(keyboard),
                    parse_mode='Markdown'
                )
            
            elif choice == "opituvannya":
                keyboard = [
                    [InlineKeyboardButton("📝 Анкета", url="https://sites.google.com/site/virtualnijmetodicnijkabinet2/опитування")],
                    [InlineKeyboardButton("📊 Результати", url="https://sites.google.com/site/virtualnijmetodicnijkabinet2/опитування/результати-опитування")],
                    [InlineKeyboardButton("⬅️ Назад", callback_data="main_menu")]
                ]
                await query.edit_message_text(
                    "📊 *Опитування*\n\nВибери розділ:",
                    reply_markup=InlineKeyboardMarkup(keyboard),
                    parse_mode='Markdown'
                )
            
            elif choice == "monitoryng":
                keyboard = [
                    [InlineKeyboardButton("📈 Моніторинг якості освіти", url="http://korpk.org.ua/моніторинг-якості-освіти/")],
                    [InlineKeyboardButton("⬅️ Назад", callback_data="main_menu")]
                ]
                await query.edit_message_text(
                    "📈 *Моніторинг*\n\nОбери розділ:",
                    reply_markup=InlineKeyboardMarkup(keyboard),
                    parse_mode='Markdown'
                )
            
            elif choice == "grafiki":
                keyboard = [
                    [InlineKeyboardButton("📋 Графіки освітнього процесу", url="http://korpk.org.ua/grafiki-navchalnogo-procesu/")],
                    [InlineKeyboardButton("🎓 Освітньо-професійні програми", url="http://korpk.org.ua/opp-obgovorennya-proektiv/")],
                    [InlineKeyboardButton("📅 Розклади занять", url="http://korpk.org.ua/розклади/")],
                    [InlineKeyboardButton("🗣️ Графік консультацій", url="http://korpk.org.ua/грфік-консультацій-викладачів/")],
                    [InlineKeyboardButton("📝 Курсова робота", url="http://korpk.org.ua/курсова-робота/")],
                    [InlineKeyboardButton("⬅️ Назад", callback_data="main_menu")]
                ]
                await query.edit_message_text(
                    "📑 *Графіки та додаткова інформація*:",
                    reply_markup=InlineKeyboardMarkup(keyboard),
                    parse_mode='Markdown'
                )
            
            elif choice == "abiturient":
                keyboard = [
                    [InlineKeyboardButton("🏢 Приймальна комісія", url="https://sites.google.com/view/vstypnuk/головна")],
                    [InlineKeyboardButton("📘 Facebook", url="https://www.facebook.com/korpk.official/")],
                    [InlineKeyboardButton("📱 Instagram", url="https://www.instagram.com/_the_college_post/")],
                    [InlineKeyboardButton("🎵 TikTok", url="https://www.tiktok.com/@korcollege.official/")],
                    [InlineKeyboardButton("⬅️ Назад", callback_data="main_menu")]
                ]
                await query.edit_message_text(
                    "🎓 *Інформація для абітурієнтів*:",
                    reply_markup=InlineKeyboardMarkup(keyboard),
                    parse_mode='Markdown'
                )
            
            elif choice == "feedback":
                    await query.edit_message_text(
                        "✍️ *Зворотній зв'язок*\n\n"
                        "Якщо маєш питання або пропозиції — звертайся:\n\n"
                        "📧 Email: lydav.golub@gmail.com",
                        parse_mode="Markdown",
                        reply_markup=back_button()
                    )

            
            elif choice == "status":
                await self.status(update, context)
                
        except Exception as e:
            logger.error(f"Помилка в button_handler ({choice}): {e}")
            await query.edit_message_text(
                "❌ Виникла помилка. Спробуй /start",
                reply_markup=self.back_button()
            )
    
    async def handle_message(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Обробка текстових повідомлень"""
        text = (
            "👆 *Використовуй кнопки меню!*\n\n"
            "Натисни **/start** для виклику головного меню"
        )
        await update.message.reply_text(text, parse_mode='Markdown')
    
    async def error_handler(self, update: object, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Обробка помилок"""
        logger.error(f"Update {update} caused error {context.error}")

def main():
    """Головна функція запуску"""
    if not TOKEN or TOKEN == 'YOUR_TOKEN_HERE':
        logger.error("❌ BOT_TOKEN не налаштовано! Додайте в .env файл")
        return
    
    logger.info("🚀 Запуск KorpkBot...")
    
    # Створюємо додаток
    bot_app = KorpkBot()
    application = Application.builder().token(TOKEN).build()
    
    # Реєструємо обробники
    application.add_handler(CommandHandler("start", bot_app.start))
    application.add_handler(CallbackQueryHandler(bot_app.button_handler))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, bot_app.handle_message))
    application.add_error_handler(bot_app.error_handler)
    
    # Запуск з обробкою помилок
    logger.info("✅ Бот успішно запущено! Готовий до роботи 24/7")
    application.run_polling(drop_pending_updates=True, allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        logger.info("🛑 Бот зупинено користувачем")
    except Exception as e:
        logger.error(f"💥 Критична помилка: {e}")
