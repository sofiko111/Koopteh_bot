import logging
from telegram import Update, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    filters,
    ContextTypes
)

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

TOKEN = 'ZOV'

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["Где находится техникум?", "Какие в техникуме есть специальности?"],
        ["Где находится общежитие техникума?", "Какие документы необходимы для поступления?"],
        ["Ответственное лицо приемной комиссии", "Адрес электронной почты техникума"],
        ["Связь с директором"]
    ]
    
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    
    await update.message.reply_text(
        "Добро пожаловать в официальный бот техникума! Выберите вопрос:",
        reply_markup=reply_markup
    )

async def handle_buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    
    if text == "Где находится техникум?":
           await update.message.reply_text("https://maps.app.goo.gl/JUw5WsySR84jTCVTA ")
    
    elif text == "Какие в техникуме есть специальности?":
        await update.message.reply_text("Информационные системы и программирование, Поварское и кондитерское дело,Туризм и гостеприимство,Право и организация социального обеспечения, Правоохранительная деятельность, Юриспруденция, Коммерция (по отраслям),Финансы, Банковское дело, Торговое дело, Дизайн(по отраслям). ")
    
    elif text == "Где находится общежитие техникума?":
        await update.message.reply_text("https://maps.app.goo.gl/67UjLUJjLuCBSu1T6")

    elif text == "Ответственное лицо приемной комиссии":
        await update.message.reply_text("Марьина Наталья Владимировна, специалист по работе с абитуриентами")

    elif text == "Какие документы необходимы для поступления?":
        await update.message.reply_text(" Заявление, Аттестат или диплом, Копия паспорта, Фото 3*4 4 шт., Копия ИНН, Копия СНИЛС, Копия Полиса, ОМС")

    elif text == "Адрес электронной почты техникума":
        await update.message.reply_text("ikoopteh@mail.ru")

    elif text == "Связь с директором":
        await update.message.reply_text("Белова Елена Ивановна. Приемная директора:(3412)370288")
        
async def handle_inline_buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()


def main():
    application = Application.builder().token(TOKEN).build()
    
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_buttons))
    application.add_handler(CallbackQueryHandler(handle_inline_buttons))
    
    application.run_polling()

if __name__ == '__main__':
    main()
