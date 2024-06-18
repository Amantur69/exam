from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    website = models.URLField(blank=True)
    followers= models.ManyToManyField('self', related_name='followed_by', symmetrical=False, blank=True)

    def __str__(self):
        return self.user.username


class Follow(models.Model):
    follow_up= models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='followed')
    following_up = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='followed_up')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.follow_up} follows {self.following_up}'


class Post(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author.user.username


class Comment(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(UserProfile, related_name='liked_by', symmetrical=False, blank=True)

    def __str__(self):
        return self.author.user.username


class Like(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author.user.username


class Story(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    video = models.FileField(upload_to='videos/')
    created = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()

    def __str__(self):
        return self.author.user.username


class Group(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    members = models.ManyToManyField(UserProfile, related_name='group_members', symmetrical=False, blank=True)
    join_key= models.CharField(max_length=50)
    def __str__(self):
        return self.name




