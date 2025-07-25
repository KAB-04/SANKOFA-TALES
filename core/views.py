from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Story

def index(request):
    return render(request, 'sankofa.html')

@csrf_exempt
def generate_story(request):
    if request.method == "POST":
        data = json.loads(request.body)
        good = data.get("good_moral", "").strip()
        bad = data.get("bad_moral", "").strip()

        # Simple story generator
        story_text = (
            f"Once in a Ghanaian village, a child learned that {good or 'virtue'} is powerful "
            f"and that {bad or 'vice'} can lead to trouble. The tale ends with wisdom and legacy."
        )

        # Save to DB
        Story.objects.create(
            good_moral=good,
            bad_moral=bad,
            story_text=story_text
        )

        return JsonResponse({"story": story_text})
    return JsonResponse({"error": "Invalid request"}, status=400)

def get_all_stories(request):
    stories = Story.objects.order_by('-created_at')[:50]  # Limit to latest 50
    story_list = [
        {
            "id": story.id,
            "label": f"{story.good_moral} vs {story.bad_moral}".strip(" vs "),
            "text": story.story_text
        }
        for story in stories
    ]
    return JsonResponse({"stories": story_list})


