
def custom_data_generator(split):
    assert split in ["test", "train", "valid"]

    examples = [
        {
            "id": "t3_o08yr",
            "subreddit": "AskReddit",
            "title": "How do you get someone out of your head?",
            "post": "Hi,\nI'm 22, and I have been with my girlfriend for 5 years now. We recently moved together. We've always loved each other intensely.\n\nProblem, I recently started to have feelings for an other person (a friend). This person has had a boyfriend for now 3 years, and has absolutely no ideas. Those feelings were so strong, it was hard to hide them. After 2 months of me being distant and really sad, my girlfriend forced me to say what was bothering me. I'm not a good liar, and now she knows.\n\nWe decided to give us a week alone, I went to my parents. \n\nNow, I'm completely lost. I keep on thinking about this person, and I hate that. I would like for those feelings to go away, to leave me alone. But I can't.  \n\nWhat do I do? It's been 3 months now, and I'm just desperate.",
            "summary": "long relationship; fell in love with an other person; admitted it; would like it to disappear, though it doesn't."
        },
        {
            "id": "t3_o08y2",
            "subreddit": "AskReddit",
            "title": "How do you get someone out of your head?",
            "post": "Hi,\nI'm 22, and I have been with my girlfriend for 5 years now. We recently moved together. We've always loved each other intensely.\n\nProblem, I recently started to have feelings for an other person (a friend). This person has had a boyfriend for now 3 years, and has absolutely no ideas. Those feelings were so strong, it was hard to hide them. After 2 months of me being distant and really sad, my girlfriend forced me to say what was bothering me. I'm not a good liar, and now she knows.\n\nWe decided to give us a week alone, I went to my parents. \n\nNow, I'm completely lost. I keep on thinking about this person, and I hate that. I would like for those feelings to go away, to leave me alone. But I can't.  \n\nWhat do I do? It's been 3 months now, and I'm just desperate.",
            "summary": "long relationship; fell in love with an other person; admitted it; would like it to disappear, though it doesn't."
        },
    ]

    datas = examples
    for data in datas:
        yield dict(reference=data["summary"], **{k: v for (k, v) in data.items() if k != "summary"})