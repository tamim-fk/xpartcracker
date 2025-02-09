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
