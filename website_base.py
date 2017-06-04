import movie_collector
import urllib
tile_content=''' <a href="#" class="responsive-picture picture-link-11"><picture data-open="{modal_number}">
                <img alt="Placeholder Picture" src="{poster_image}"></picture></a>
                '''
modal_content='''<div id="{modal_number}" class="reveal" data-reveal data-close aria-labelledby="modalTitle" aria-hidden="true" role="dialog">
    	            <iframe width="560" height="315" src="{trailer_url}" frameborder="0" allowfullscreen></iframe>
    	        </div>
    	    '''

head_content='''<!DOCTYPE html>
<html>

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <meta name="generator" content="Responsive Foundation Framer 2.0.358">
  <title>Movie Trailers Website</title>
  <link rel="stylesheet" href="css/foundation.min.css">
  <link rel="stylesheet" href="css/wireframe-theme.min.css">
  <script>document.createElement( "picture" );</script>
  <script src="js/picturefill.min.js" class="picturefill" async="async"></script>
  <link rel="stylesheet" href="css/main.css">
  <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Titillium+Web:b">
</head>
'''


body_content='''<body class="no-js">
  <div class="row row-1">
    <div class="columns small-12 medium-12 custom-319-small-12 column-2">
      <h1 class="heading-1">Trailer Website</h1>
    </div>
  </div>
  <div class="row">
    <div class="columns small-12 column-1">
      {movie_tiles_holder}
    </div>
  </div>
  <script src="js/jquery.min.js"></script>
  <script src="js/what-input.min.js"></script>
  <script src="js/foundation.min.js"></script>
  <script>$(document).foundation();</script>
</body>

</html>'''

index=0
movie_index="modal_number_"
def tiles(movie):
    global index
    updated_modal=modal_content.format(
        modal_number=movie_index+str(index),
        trailer_url=movie.youtube_trailer_url

    )
    updated_tile_content=tile_content.format(
        poster_image=movie.poster_url,
        modal_number=movie_index+str(index)
    )
    index+=1
    tile=updated_tile_content+updated_modal
    return tile

movie_tiles=""
def update_page_content(movies):
    for movie in movies:
        global movie_tiles
        movie_tiles += tiles(movie)
    new_body_content=body_content.format(
        movie_tiles_holder=movie_tiles
    )
    total_content=head_content+new_body_content
    output_file=open('output.html','w')
    output_file.write(total_content)

class Movie():
    def __init__(self,movie_name, youtube_trailer_url, poster_url):
        self.name=movie_name
        self.youtube_trailer_url=youtube_trailer_url
        self.poster_url=poster_url

movies_list=list()
movie_name="picture.jpg"
f_name=0
name_list,poster_list,url_list=movie_collector.return_info()
for i in range(0,len(poster_list)):
    urllib.urlretrieve(poster_list[i], str(f_name) + movie_name)
    movie_obj = Movie(name_list[i], url_list[i], str(f_name) + movie_name)
    f_name=f_name+1
    movies_list.append(movie_obj)

update_page_content(movies_list)