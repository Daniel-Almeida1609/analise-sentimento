import praw
import configparser


def main():
    config = configparser.ConfigParser()
    config.read("access.ini")

    api_reddit = praw.Reddit(
    client_id=config["API"]["CLIENT_ID"],
    client_secret=config["API"]["CLIENT_SECRET"],
    user_agent="danio/0.1 by Expensive_Spite4841"
    )

    subreddit_name = "fiveguys"
    subreddit = api_reddit.subreddit(subreddit_name)
    for submission in subreddit.new(limit=21):
        print(submission.title)


if __name__ == "__main__":
    main()