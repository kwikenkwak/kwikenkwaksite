
from mediamaker import posts
def generate_posts:
    for post in posts:
        d, m, y = post["date"].split("/")
        filename = post["filename"]
        name = filename.split(".")[0]
        if post["is_video"]:
            p = Post(title=post["title"],
                    upload_date=f"{y}-{m}-{d}",
                    img_name_big="images/" + name + "_big.jpg",
                    img_name_small="images/" + name + "_small.jpg",
                    video_name="videos/" + filename,
                    block_dropper=post["blockdropper"])
        else:
            p = Post(title=post["title"],
                    upload_date=f"{y}-{m}-{d}",
                    img_name_big="images/" + name + "_big.jpg",
                    img_name_small="images/" + name + "_small.jpg",
                    video_name="")
        p.save()


