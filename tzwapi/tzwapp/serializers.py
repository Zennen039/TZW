from rest_framework.serializers import ModelSerializer
from tzwapp.models import Category, Course, Lesson, Tag, User, Comment


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class ItemSerializer(ModelSerializer):
    def to_representation(self, instance):
        data = super().to_representation(instance)

        if instance.image:
            data['image'] = instance.image.url

        return data


class CourseSerializer(ItemSerializer):
    class Meta:
        model = Course
        fields = ['id', 'subject', 'image', 'created_date', 'category_id']


class LessonSerializer(ItemSerializer):
    class Meta:
        model = Lesson
        fields = ['id', 'subject', 'image', 'course_id', 'created_date', 'updated_date']


class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']


class LessonDetailSerializer(LessonSerializer):
    tags = TagSerializer(many=True)

    class Meta:
        model = LessonSerializer.Meta.model
        fields = LessonSerializer.Meta.fields + ['content', 'tags']



class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username', 'password', 'email', 'avatar']
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

    def to_representation(self, instance):
        data = super().to_representation(instance)

        if instance.avatar:
            data['avatar'] = instance.avatar.url

        return data

    def create(self, validated_data):
        data = validated_data.copy()

        u = User(**data)
        u.set_password(u.password)
        u.save()

        return u


class CommentSerializer(ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Comment
        fields = ['id', 'user', 'content', 'created_date', 'updated_date']