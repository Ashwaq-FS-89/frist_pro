from app import db



class Venue(db.Model):
    __tablename__ = 'Venue'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    address = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    genres = db.Column(db.ARRAY(db.String(120)))
    image_link = db.Column(db.String(500))
    website_link = db.Column(db.String(120))
    seeking_description =db.Column(db.String(120))
    facebook_link = db.Column(db.String(120))
    shows = db.relationship('Show', backref='venue',lazy=True)
    
    def __repr__(self):
      return f'<Venue ID:{self.id},Venue name:{self.name},Venue city:{self.city},Venue state:{self.state},\
    Venue address:{self.address},Venue phone:{self.phone},Venue genres:{self.genres},Venue seeking_description:{self.seeking_description},\
    Venue image_link:{self.image_link},Venue website_link :{self.website_link },Venue facebook_link:{self.facebook_link}>'

class Artist(db.Model):
    __tablename__ = 'Artist'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    genres = db.Column(db.ARRAY(db.String(120)))
    image_link = db.Column(db.String(500))
    website_link = db.Column(db.String(200))
    seeking_description =db.Column(db.String(200))
    facebook_link = db.Column(db.String(200))
    shows = db.relationship('Show', backref='artist',lazy=True)

    def __repr__(self):
      return f'<Artist ID:{self.id} ,Artist name:{self.name},Artist city:{self.city},Artist state:{self.state}, \
      Artist phone:{self.phone},Artist genres:{self.genres}, \
      Artist image_link:{self.image_link},Artist website_link:{self.website_link},Artist facebook_link:{self.facebook_link}, \
      Artist seeking_description:{self.seeking_description}>'


class Show(db.Model):
  __tablename__ = 'Show'

  show_id=db.Column(db.Integer, primary_key=True)
  artist_id = db.Column(db.Integer,db.ForeignKey('Artist.id', ondelete="CASCADE"))
  venue_id = db.Column(db.Integer,db.ForeignKey('Venue.id', ondelete="CASCADE"))
  start_time = db.Column(db.DateTime)

  def __repr__(self):
      return f'<Show ID:{self.show_id},Artist ID:{self.artist_id} ,Venue ID:{self.venue_id},Show start_time:{self.start_time}>'