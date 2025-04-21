# cron_worker.py

from app import update_articles_file

if __name__ == "__main__":
    print("Ivy Cron Job: Checking for new articles...")
    updated = update_articles_file()
    if updated:
        print("New article added to articles.txt")
    else:
        print("⏸ No new article found.")
