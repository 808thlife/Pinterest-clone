

def update_view_counter(post):
    post.viewed +=1
    post.save()