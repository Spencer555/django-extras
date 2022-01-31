from django.db import models
from django.contrib.auth.models import User

class PostQuerySet(models.QuerySet):
    def sorted(self):
        return self.order_by('-created_at')
    
    
    def get_users_posts(self, username):
        return self.filter(author__username=username)
    

class PostManager(models.Manager):
    def sorted(self):
        return self.get_queryset().order_by('-created_at')
    
    #we pass the queryset to the manager so we can use the manager to call methods easily
    #link our queryset to manager
    def get_queryset(self):
        return PostQuerySet(model=self.model, using=self._db, hints=self._hints)
        #means use the current model to search in the database for instance using the current database
        
    def get_matts_posts(self, username):
        return self.get_queryset().get_users_posts(username)






class PostQuerySet(models.QuerySet):
    def get_users_posts(self, username):
        return self.filter(author__username=username)
    

class PostManager(models.Manager):
    def get_queryset(self):
        return PostQuerySet(model=self.model, using=self._db)
        
    def get_matts_posts(self, username):
        return self.get_queryset().get_users_posts(username)


# the queryset handles the logic the manager handles the queryset method

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    objects = PostManager()
    #to make queryset perform as a manager
    objects = PostQuerySet.as_manager()
    
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return f"/posts/{self.slug}/"
    
    def get_update_url(self):
        return f"/posts/{self.slug}/update/"
    
    def get_delete_url(self):
        return f"/posts/{self.slug}/delete/"
    
    
#Post.objects.get_users_posts('username')