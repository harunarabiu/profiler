from profiler import ma

class ProfileSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        fields = ('id', 'title','first_name', 'last_name', 'gender', 'dob', 'phone', 'email', 'nationality')
        

profile_schema = ProfileSchema()
profiles_schema = ProfileSchema(many=True)
