from enggames_site import ma


class AdminSchema(ma.Schema):
    class Meta:
        fields = ('id', 'username', 'email', 'imgFile', 'password')

admin_schema = AdminSchema()
admins_schema = AdminSchema(many=True)

class PageSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'name', 'description', 'endpoint')

page_schema = PageSchema()
pages_schema = PageSchema(many=True)


class EventSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'fb_link', 'imgFile', 'description', 'last_updated', 'admin_id')

event_schema = EventSchema()
events_schema = EventSchema(many=True)
