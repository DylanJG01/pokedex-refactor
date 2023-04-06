
# 1 - 1

# class Image(db.Model):
#     __tablename__ = 'image'
#     image_id = db.Column(db.Integer, primary_key = True)
#     name = db.Column(db.String(8))
#     # the one - to - one relation
#     blindmap = relationship("Blindmap", uselist = False, backref = "image")

# class Blindmap(db.Model):
#     __tablename__ = 'blindmap'
#     module_id = db.Column(db.Integer, primary_key = True)
#     image_id = db.Column(db.Integer, ForeignKey('image.image_id'))







# image1 = Image(name = 'image1.png')
# blindmap1 = Blindmap()
# blindmap1.image = image1


