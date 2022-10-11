from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework import permissions, status
from rest_framework.decorators import api_view, permission_classes

from apps.profiles.models import Profile
from .models import Rating


User = get_user_model()

@api_view(["POST"])
@permission_classes([permissions.IsAuthenticated])
def create_agent_review(request, profile_id):
    agent_profile = Profile.objects.get(id=profile_id, is_agent=True)
    data = request.data 

    profile_user = User.objects.get(pkid=agent_profile.user.pkid)
    if profile_user.email == request.user.email:
        return Response({"message": "You can't rate yourself"}, status=status.HTTP_403_FORBIDDEN)
    
    already_exists = agent_profile.agent_review.filter(agent__pkid=profile_user.pkid).exists()

    if already_exists:
        return Response({"message": "Profile already reviewed"}, status=status.HTTP_400_BAD_REQUEST)

    elif data.get("rating") == 0:
        return Response({"detail": "Please select a rating"}, status=status.HTTP_400_BAD_REQUEST)

    else: 
        review = Rating.objects.create(rater=request.user, agent=agent_profile, rating=data.get("rating"), comment=data.get("comment")) 

    reviews = agent_profile.agent_review.all()
    agent_profile.num_of_reviews = len(reviews)

    total = 0
    for i in reviews:
        total += i.rating
    

    agent_profile.rating = round(total / len(reviews), 2)
    agent_profile.save()
    return Response("Review Added")


