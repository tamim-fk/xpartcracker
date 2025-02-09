import json
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext
import asyncio
import os

from flask import Flask, request

# Enable logging
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)

# Embedded course data
COURSES_DATA = {
     "popular": {
        "price": "Join Main Group",
        "notice": "🔥 Limited-time offer! Get 20% off if you enroll today.",
        "courses": [
            [
                {"name": "Data Science and Big Data", "link": "https://t.me/+wnrp0WBf_LA1ZjBl"},
                {"name": "Machine Learning and AI", "link": "https://t.me/+wnrp0WBf_LA1ZjBl"}
            ]

            ]
    },
    "gaming": {
        "price": "Join Main Group",
        "notice": "🔥 Limited-time offer! Get 20% off if you enroll today.",
        "courses": [
            {"name": "Minecraft", "link": "https://t.me/+wnrp0WBf_LA1ZjBl"},
            {"name": "Among Us", "link": "https://t.me/+wnrp0WBf_LA1ZjBl"},
            {"name": "Stardew Valley", "link": "https://t.me/+wnrp0WBf_LA1ZjBl"},
            {"name": "Terraria", "link": "https://t.me/+wnrp0WBf_LA1ZjBl"},
            {"name": "Fortnite", "link": "https://t.me/+wnrp0WBf_LA1ZjBl"}
        ]
    },
    "autocad": {
        "price": "Join Main Group",
        "notice": "💡 Master AutoCAD with hands-on projects!",
        "courses": [
            {"name": "AutoCAD for Beginners", "link": "https://t.me/+wnrp0WBf_LA1ZjBl"},
            {"name": "Advanced AutoCAD", "link": "https://t.me/+wnrp0WBf_LA1ZjBl"}
        ]
    },
    "kali": {
        "price": "Join Main Group",
        "notice": "💡 Learn Kali Linux from scratch!",
        "courses": [
            {"name": "Kali Linux for Beginners", "link": "https://t.me/+wnrp0WBf_LA1ZjBl"},
            {"name": "Advanced Kali Linux", "link": "https://t.me/+wnrp0WBf_LA1ZjBl"}
        ]
    },
    "web": {
        "price": "Join Main Group",
        "notice": "💡 Build modern web applications!",
        "courses": [
            {"name": "Web Development Bootcamp", "link": "https://t.me/+wnrp0WBf_LA1ZjBl"},
            {"name": "Full Stack Development", "link": "https://t.me/+wnrp0WBf_LA1ZjBl"}
        ]
    },
    "hacking": {
        "price": "Join Main Group",
        "notice": "💡 Ethical hacking and cybersecurity fundamentals!",
        "courses": [
            {"name": "Ethical Hacking Basics", "link": "https://t.me/+wnrp0WBf_LA1ZjBl"},
            {"name": "Penetration Testing", "link": "https://t.me/+wnrp0WBf_LA1ZjBl"}
        ]
    },
    "python": {
        "price": "Join Main Group",
        "notice": "💡 Learn Python with real-world projects!",
        "courses": [
            {"name": "Python for Beginners", "link": "https://t.me/+wnrp0WBf_LA1ZjBl"},
            {"name": "Advanced Python", "link": "https://t.me/+wnrp0WBf_LA1ZjBl"}
        ]
    }
}

# Payment link
PAYMENT_LINK = "https://t.me/+wnrp0WBf_LA1ZjBl"

# Bot Token
TELEGRAM_TOKEN = "7941080484:AAFSe6zITZxCjYqFldDLXXN_mm5Y354GCgc"

# Command to start the bot
async def start(update: Update, context: CallbackContext):
    await update.message.reply_text(
        "🎓 **Welcome to the Course Sharing Bot!** 🎓\n\n"
        "💡 Get access to high-quality paid courses.\n"
        "📌 Use /categories to explore available courses."
    )

    # Command to start the bot and pin a notice
async def start(update: Update, context: CallbackContext):
    await update.message.reply_text(
        "📌 **Important Notice:**\n"
        "⚠️ Please read the rules and guidelines before proceeding.\n"
        "💳 Use /payment to make a purchase.\n"
         "🚀 We have all the courses available for you! 🌟\n"
        "Head over to the Admin panel and let us know which course you need, \n"
        "or simply fill out the Google form linked below to tell us your desired course. 📋\n"
        "But hey, if you mention it in the group, we'll be able to respond even faster! ⏱️\n"
        "Thank you! 🙏\n\n"
        "🚀 আমাদের কাছে সকল কোর্চই রয়েছে! 🌟\n"
        "Admin প্যানেল এ গিয়ে আপনার কোন কোর্চ লাগবে তা বলুন, \n"
        "অথবা নিচে দেওয়া গুগল ফর্মে আপনার প্রয়োজনীয় কোর্চটি জানিয়ে দিন। 📋\n"
        "তবে গ্রুপে বললে আমরা আরও দ্রুত রেসপন্স করতে পারবো! ⏱️\n"
        "ধন্যবাদ! 🙏\n\n"
        "Google Form Link: (https://docs.google.com/forms/d/e/1FAIpQLSctZqIbSzpDMBvONo4mCGKfTsUkgUyisAtvPpO0w7nzwpAH7A/viewform?usp=header)\n\n"

        "📂 Explore courses with /categories."
    )
    

    await update.message.reply_text(
        "🎓 **Welcome to the Course Sharing Bot!** 🎓\n\n"
        "💡 Get access to high-quality paid courses.\n"
        "📌 Use /categories to explore available courses."
    )

# Command to show categories
async def categories(update: Update, context: CallbackContext):
    await update.message.reply_text(
        "📂 **Available Categories:**\n"
        "👉 /popular\n"
        "👉 /gaming\n"
        "👉 /autocad\n"
        "👉 /kali\n"
        "👉 /web\n"
        "👉 /hacking\n"
        "👉 /python\n"
        "\n⚡ Choose a category to see course details."
    )

# Command to show payment link
async def payment(update: Update, context: CallbackContext):
    await update.message.reply_text(
        f"💳 **Payment Information:**\n"
        f"👉 [Click here to make a payment]({PAYMENT_LINK})",
        parse_mode="Markdown"
    )

# Function to send course details with price and notice
async def send_courses(update: Update, context: CallbackContext):
    category = update.message.text.lstrip("/").lower()
    
    if category in COURSES_DATA:
        category_data = COURSES_DATA[category]
        message = (
            f"🎯 **{category.capitalize()} Courses** 🎯\n"
            f"💰 **Price:** {category_data['price']}\n"
            f"📢 **Notice:** {category_data['notice']}\n\n\n"
            "⚠️📌**Join The Main Group To Buy Course📌⚠️\n\n\n"
            "📌 **Course List:**\n"
        )
        for course in category_data["courses"]:
            message += f"🔹 [{course['name']}]({course['link']})\n"

        await update.message.reply_text(message, parse_mode="Markdown")
    else:
        await update.message.reply_text("❌ Invalid category. Use /categories to see available options.")

# Main function to run the bot
def main():
    app = Application.builder().token(TELEGRAM_TOKEN).build()

    # Register handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("categories", categories))
    app.add_handler(CommandHandler("payment", payment))
    app.add_handler(CommandHandler("popular", send_courses))
    app.add_handler(CommandHandler("gaming", send_courses))
    app.add_handler(CommandHandler("autocad", send_courses))
    app.add_handler(CommandHandler("kali", send_courses))
    app.add_handler(CommandHandler("web", send_courses))
    app.add_handler(CommandHandler("hacking", send_courses))
    app.add_handler(CommandHandler("python", send_courses))

    # Start the bot
    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    asyncio.run(main())    