from datetime import date
from django.shortcuts import render

posts = [
    {
        "slug": "hike-in-the-mountains",
        "image": "mountain.jpg",
        "author": "Dev",
        "date": date(2024, 6, 25),
        "title": "Mountain Hiking",
        "excerpt": "Iiked to climb in the mountains and I have no complaints!",
        "content": """
            I have always found solace in the mountains. The fresh air, the breathtaking views, and the sense of accomplishment that comes from reaching the summit are unparalleled. Every hike presents a new adventure, a new challenge to overcome. The physical exertion required to navigate the rugged terrain and the mental fortitude needed to keep pushing forward are both demanding and rewarding. It is in these moments of challenge that I find my greatest joy.\nDuring one particular hike, I remember being struck by the sheer beauty of my surroundings. The sun was just beginning to rise, casting a golden hue over the landscape. The distant peaks were shrouded in mist, creating a surreal and almost otherworldly atmosphere. As I climbed higher, the view became even more spectacular, with the valley below stretching out in a patchwork of greens and browns. Each step brought me closer to nature and further from the hustle and bustle of everyday life.\nReaching the summit was a moment of pure elation. The sense of achievement was immense, knowing that I had pushed my limits and succeeded. The view from the top was breathtaking, with mountains stretching as far as the eye could see. It was a reminder of the vastness of the world and my small place within it. Hiking in the mountains is not just a physical activity; it is a journey of self-discovery and a testament to the human spirit's resilience. I have no complaints about my time spent in the mountains – it has been, and continues to be, a source of immense joy and satisfaction.
        """
    }
]

# Create your views here.
def starting_page(request):
    return render(request, "blog/index.html")

def posts(request):
    return render(request, 'blog/all-posts.html')

def post_detail(request, slug):
    return render(request, 'blog/post-detail.html')