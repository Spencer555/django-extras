from django.db import models

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    a = models.CharField(max_length=100)
    b = models.CharField(max_length=100)
    c = models.CharField(max_length=100)
    product_secret_id = models.CharField(max_length=100)
    
    
#products/ fields: title, manufacturer, price 
#products/id/ fields: title, manufacturer, price, a, b, c


# instead of Products.objects.all 

# using list comprehension 
# [product for product in Products.objects.all()]


# u dont need to return all the model only the important ones 

# [(product.title, product.manufacturer, product.price) for product in Product.objects.all()]


#unoptimized query cost u money on servers slow user down etc


#3 functions we can use normally only, values, defer

# product = Product.objects.all().only('title', 'manufacturer', 'price')

# if the field is not specified and u try to get it it would give it to u  
# product.a but this would execute two queries so always inspect it
#beneficial if u dont know ur queries

# product = Product.objects.all().values('title', 'manufacturer', 'price')
#with values u cant make excessive queries which is good
#it is beneficail if u know ur app
# this returns raw python dictionary instead of django orm modules


# to see the raw sql query 
# str(product.query)


#select related is for foriegn keys
# select user and category on the same model
Product.objects.select_related('user ', 'category').all()

# many to many field
# select user and category on the same model
Product.objects.select_related('user', 'category').prefetch_related('name of the many to many field').all()






# class Playlist(Model):
#     user = ForeignKey(User, related_name='playlists')
#     name = CharField( )
#     length = PositiveIntegerField()
    
# class Song(Model):
#     Playlist = ForiegnKey(Playlist)

# #this is the prop that can be used for total shop prod
# @property
# def songs_total_length(self):
#     total_length = 0 
    
#     for song in self.songs.all():
#         total_length += song.length 
        
#         return total_length

# short form

# return sum([song.length for song in self.songs.all()])

# this can make the dbase very slow so we define a queryset to optimize it 

class PlaylistQueryset(QuerySet):
    @classmethod
    def songs_total_length(cls):
        
        queryset = Song.objects.values('playlist_id').filter(playlist__id=OuterRef('id')).values_list(Sum('length'))
        
        
        return Subquery(
            queryset=queryset,
            output_fields=models.IntegerField()
        )
        # the first is the queryset second it the type of value it outputs
        # return Subquery(
        #     query=...,
        #     output_fields=...
        # )
    
    def collect(self):
        return self.annotate(_songs_total_length=self.songs.total_length)
    
    
    
class Playlist(Model):
    def songs_total_length(self):
        if hasattr(self, 'songs_total_length'):
            return self._songs_total_length 
        
        return sum([song.length for song in self.songs.all()]) 
    
    
class UserQuerySet(QuerySet):
    @classmethod
    def playlists_total_length(cls):
        playlist_annotation = PlaylistQueryset.songs_total_length()
        # we have imported the playlist queryset 
        
        queryset = Playlist.objects.values('user__id').filter(user__id=OuterRef('id')).values_list(Sum(playlist_annotation))
        
        return Subquery(
            queryset=queryset, 
            output_field=IntegerField()
        )
        
    def collect(self):
        return self.annotate(_playlists_total_length=self.playlists_total_length())
    
class User(Model):
    objects = UsersQueryset.as_manager()
    
    name = CharField(max_length=255)
    
    @property
    def playlists_total_length(self):
        if hasattr(self, '_playlists_total_length'):
            return self._playlists_total_length
        
        playlists_length = [
            playlist.songs_total_length
            for playlist in self.playlists.all()
        ]
        return sum(p.songs_total_length for p in self.playlists.all())
    
    
    if u have an api which calculate for something but u dont need the obj 
    
u use subquery + outerref 




# problem 3 too many data and too many queries 

class User(Model):
    name = CharField()
    
    @property 
    def playlists_total_length(self):
        return sum([p.songs_total_length for p in self.playlists.all()])
    
class Playlist(model):
    user = fk(user)
    name = charfield()
    
    
    @property 
    def songs_total_length(self):
        return sum([song.real_length for song in self.songs.all()])
    
    
class SongQuerySet(QuerySet):
    @classmethod
    def real_length(cls):
        return ExpressionWrapper(
            expression=...,
            output_field=IntegerField()
        )
        
    def collect(self):
        return self.annotate(_real_length=self.real_length())
    
    
    
class Song(Model):
    playlist = fk(playlist)
    title = charfield()
    length=positiveintegerfield()
    
    
    def real_length(self):
        if hasattr(self, '_real_length'):
            return self._real_length
        return self.length * 0.8
    
    
# writing a testcase 

class SongTests(TestCase):
    def test_song_length(self):
        length = 120 
        real_length = 0.8 * length 
        song = Song.objects.create(title="Europython", length=120)
        self.assertEqual(real_length, song.real_length)
    
    
