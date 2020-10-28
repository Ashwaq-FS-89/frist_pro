 #venue = Venue.query.group_by('id','city','state').all()


#  "city": "San Francisco",
#     "state": "CA",
#     "venues": [{
#       "id": 1,
#       "name": "The Musical Hop",
#       "num_upcoming_shows": 0,
  
  # current_date=datetime.now() 
  # num_upcoming_shows=Venue.query.join(Show)..filter(Show.venue_id == i.id)filter(Show.start_time > current_date)
  #db.session.query(Show).filter(Show.venue_id == i.id).filter(Show.start_time >datetime.now()).all()
  # data=[]

  # for i in venue:
  #   if i.city == venue.city:
  #    data.append({"id":i.id,"name":i.name , "city":i.city , 
  #    "state":i.state ,'num_upcoming_shows':db.func.count(num_upcoming_shows)})
  #   else:
  #     data.append({"id":i.id,"name":i.name , "city":i.city , 
  #    "state":i.state ,'num_upcoming_shows':db.func.count(num_upcoming_shows)})